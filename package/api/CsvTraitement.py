import os

from PySide6.QtCore import QDateTime
from PySide6.QtWidgets import QMessageBox

from package.api.database import Database
from infosBaseDialog import InfosBaseDialog

class CsvTraitement:
    def __init__(self, dateImport):
        self.db = Database()
        self.dateImport = dateImport

        print("dateImport=", self.dateImport)
        self.readCsvFiles()

    def readCsvFiles(self):
        date = self.dateImport[5:10]
        path_base = "ftp_temp" + '/'

        path_to_file_temp = f"ftp_temp/TP-{date}.csv"
        path_to_file_pulse = f"ftp_temp/PL-{date}.csv"
        path_to_file_pince = f"ftp_temp/PC-{date}.csv"
        path_to_file_teleinfo = f"ftp_temp/TI-{date}.csv"

        temp_data = []
        pulse_data =[]
        pince_data = []
        teleinfo_data = []
        file_path_list = [path_to_file_temp, path_to_file_pulse, path_to_file_pince, path_to_file_teleinfo]
        file_data_list = [temp_data, pulse_data, pince_data, teleinfo_data]
        data_list = ["Temp", "Pulse", "Pince", "TéléInfo"]
        self.nb_row_attendu_list = [1442, 1441, 1441, 1442]

        for i in range(4):
            # Test existence fichiers à importer
            print("Traitement en cours:", data_list[i])
            if not os.path.isfile(file_path_list[i]):
                QMessageBox.critical(None, "Erreur:", f" Fichier {file_path_list[i][12:]} absent !")
                return
            f = open(file_path_list[i], 'r', encoding='UTF-8')
            data = f.read()
            rows = data.split('\n')
            nb_row = len(rows)
            delta_row =  self.nb_row_attendu_list[i] - nb_row
            print("nombre de lignes=",len(rows), "pour ", data_list[i])

            index = 0
            for row in rows:
                split_row =  row.split(',')
                # suppression des colonnes inutiles
                if i == 0:  # fichier temp
                    del split_row[4:31]

                elif i == 1:  # fichier pulse
                    del split_row[2:]

                elif i == 2: # fichier pince
                    del split_row[3:9]
                file_data_list[i].append(split_row)
            #suppression header
            file_data_list[i] = (file_data_list[i])[1:]
            #suppression dernière ligne vide
            file_data_list[i] = file_data_list[i][0:-1]
            #print("temp_data=", (file_data_list[i])[0:5])
            #print("temp_data=", (file_data_list[i])[-5:])

            # Ajout de la ligne manquante pulses
            if i == 1:
                dp = file_data_list[i][0]
                print("dp=", dp)
                #dp0 = ['00:00', str(float(dp[1])/2), str(float(dp[2])/2), str(float(dp[3])/2), str(float(dp[4])/2)]
                #dp1 = ['00:01', str(float(dp[1])/2), str(float(dp[2])/2), str(float(dp[3])/2), str(float(dp[4])/2)]
                dp0 = ['00:00', str(float(dp[1])/2)]
                dp1 = ['00:01', str(float(dp[1])/2)]

                print("dp0=",dp0)
                file_data_list[1].insert(0,dp0)
                file_data_list[1][1] = dp1

            # Ajout de la ligne manquante pinces
            if i == 2:
                dp = file_data_list[i][0]
                print("dp=", dp)
                #dp0 = ['00:00', dp[1], dp[2], dp[3], dp[4]]
                #dp1 = ['00:01', dp[1], dp[2], dp[3], dp[4]]
                dp0 = ['00:00', dp[1], dp[2]]
                dp1 = ['00:01', dp[1], dp[2]]

                print("dp0=",dp0)
                file_data_list[i].insert(0,dp0)
                file_data_list[i][1] = dp1

            nb_row = len(file_data_list[i])
            print("nb_row verif de i=",i,":", nb_row)
            # Si pas de probleme nb_row = 1440
            delta_row = 1440 - nb_row

            # Test fichier intègre
            if delta_row == 60:
                QMessageBox.critical(None, " Info", "Passage à l'heure d'été ?")
            elif delta_row == -60:
                QMessageBox.critical(None, " Info", "Passage à l'heure d'hiver ?")
            elif delta_row > 0:
                pos_trou = self.find_trous(i, nb_row, file_data_list)
                if pos_trou == "NOK":
                    QMessageBox.critical(None, "Problème", "Journée incomplète !")
                else:
                    QMessageBox.critical(None, "Problème:", f" Manque {delta_row} Data pour {data_list[i]} en {pos_trou}")
                self.fill_trous(i, delta_row)


        # fin du for

        # Fusion des listes pour injection dans la base
        #self.final_list = []
        index = 1 # car header déjà supprimé
        nb_row = len(file_data_list[0])
        for i in range(nb_row):
            #sublist=[]
            sublist1 = file_data_list[0][i] + file_data_list[1][i] + file_data_list[2][i] + file_data_list[3][i]
            #sublist.append(file_data_list[0][i] + file_data_list[1][i] + file_data_list[2][i] + file_data_list[3][i])
            #sublist1 = [item for sublist in sublist for item in sublist]

            sublist1.insert(0, str(index))
            index += 1

            # structure de la sublist1 =
            # Id, Time, 1w1, 1w2, 1w3, Time, pulse_1, Time, pince1, pince2, Time, base, ph1, ph2, ph3, pa

            # suppression des colonnes time inutiles
            del sublist1[10]
            del sublist1[7]
            del sublist1[5]

            # nouvelle structure de la sublist1 =
            # Id, Time, 1w1, 1w2, 1w3, pulse_1, pince1, pince2, base, ph1, ph2, ph3, pa

            # conversion time en datetime
            sublist1[1] = self.dateImport + " " + sublist1[1]

            # Insertion de time_utc
            datelocal =  QDateTime.fromString(sublist1[1], ("yyyy-MM-dd hh:mm"))
            dateutc =  datelocal.toUTC().toString("yyyy-MM-dd hh:mm")
            sublist1.insert(2, dateutc)

            ##print("sublist1=",sublist1)
            # Id, Time, time_utc, w1, w2, w3, pulse_1, pince_1, pince_2, base, ph1, ph2, ph3, pa):

            recordBase = [int(sublist1[0]), sublist1[1],(sublist1[2]),
                              float(sublist1[3]), float(sublist1[4]), float(sublist1[5]),
                              float(sublist1[6]),
                              float(sublist1[7]), float(sublist1[8]),
                              float(sublist1[9]), float(sublist1[10]), float(sublist1[11]), float(sublist1[12]), float(sublist1[13])]


            flag = self.db.add_record(recordBase)
        if not flag:
            QMessageBox.critical(
                None,
                "App Name - Error!",
                #"Database Error: %s" % self.db.lastError().databaseText(),
                "Echec ecriture en base"
            )

        print("Fin ajout base")

        # Vidage def ftp_temp
        list = os.listdir('./ftp_temp')

        for f in list:
            os.remove(f"./ftp_temp/{f}")



    def convert_index_to_time_string(self,index):
        h, m = divmod(index, 60)
        str_h = str(h)
        str_m = str(m)
        if h < 10:
            str_h = "0" + str_h
        if m < 10:
            str_m = "0" + str_m
        return str_h + ":" + str_m

    def fill_trous(self, i, nb_trous):
        print("fill_trous")
        # Recherche de la position des trous
        #list_trous = []

        # Copie de la ligne avant le trou
        return

    def find_trous(self, i, nb_row, data_list):
        print("find_trous")
        for j in range(len(data_list[i])):

            i_time = self.convert_index_to_time_string(j)
            print("i_time=", i_time," datalist=", (data_list[i])[j][0])
            if i_time != (data_list[i])[j][0]:
                print("itime=",i_time)
                return i_time

        return "NOK"