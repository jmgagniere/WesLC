from PySide6 import QtWidgets
from PySide6.QtSql import QSqlQuery, QSqlDatabase

import os

class Database:
    is_instantiated = False

    def __init__(self):
        if not Database.is_instantiated:
            # Verification de l'exixtence de la base
            # Get the current working directory
            ##print("The current working directory is:", current_directory)
            file_path = "database/baseWes.db"
            if os.path.exists(file_path):
                print("The file exists.")
                # création de la connexion
                self.db = QSqlDatabase.addDatabase("QSQLITE")
                self.db.setDatabaseName("database/baseWes.db")

                self.db.open()
                Database.is_instantiated = True
                print("database has been instantiated")
            else:
                print("The file does not exist.")
                # création de la connexion
                self.db = QSqlDatabase.addDatabase("QSQLITE")
                self.db.setDatabaseName("database/baseWes.db")

                self.db.open()
                Database.is_instantiated = True
                print("database has been instantiated")
                # Creation des tables si elles n'existent pas
                query = QSqlQuery()
                query.prepare("""   CREATE TABLE IF NOT EXISTS 'ftp_param' (
                                "host" TEXT NOT NULL,
                                "login" TEXT NOT NULL,
                                "passwd" TEXT NOT NULL)
                             """)
                query.exec()

                query.prepare("""   CREATE TABLE IF NOT EXISTS 'plot_param' (
	                            "id"	TEXT,
	                            "name"	TEXT,
	                            "color"	TEXT,
	                            "state"	INTEGER,
	                            "width"	INTEGER)
                             """)
                query.exec()

                query.prepare("""
                                INSERT INTO 'plot_param' VALUES ('1w1','T° Cave','#0000ff',2,3),
                                ('1w2','T° RdC','#fc0107',2,3),
                                ('1w3','T° Ext','#408002',2,3),
                                ('pulse1','Gialix','#fd8008',2,2),
                                ('pince1','VMC','#1eb612',2,1),
                                ('pince2','ECS','#996633',2,2),
                                ('ph1','ph1','#9e533c',0,1),
                                ('ph2','ph2','#d94f36',0,1),
                                ('ph3','ph3','#ffaa00',0,1),
                                ('pa','pa','#00aaff',0,4),
                                ('base','T_Infos','#000000',0,1)
                               """)
                query.exec()

                query.prepare("""   CREATE TABLE IF NOT EXISTS 'weslc_new' (
	                            "Id"	INTEGER,
	                            "Time"	TEXT,
	                            "time_utc"	TEXT UNIQUE,
	                            "w1"	REAL,
	                            "w2"	REAL,
	                            "w3"	REAL,
	                            "pulse_1"	REAL,
	                            "pince_1"	REAL,
	                            "pince_2"	REAL,
	                            "base"	REAL,
	                            "ph1"	REAL,
	                            "ph2"	REAL,
	                            "ph3"	REAL,
	                            "pa"	REAL)
                              """)
                query.exec()

                query.prepare("""   INSERT INTO "weslc_new" 
                                    VALUES (1,'2019-01-01 00:00','2019-01-01 00:00',0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0) 
                            """)
                query.exec()

        else:
            print("database has already been created")

    # ************** Transfert FTP *****************

    def init_transfert_param(self):
        print("init_transfert_param")
        query = QSqlQuery()

        query.exec("DROP TABLE IF EXISTS 'ftp_param' ")

        query.prepare(""" CREATE TABLE "ftp_param" (
                          "host" TEXT NOT NULL,
                          "login" TEXT NOT NULL,
                          "passwd" TEXT NOT NULL) """)
        query.exec()

        query.prepare("""INSERT INTO ftp_param (host, login, passwd)VALUES ('82.64.197.53', 'jmg-ftp', 'jmg-wes@lc') """)

        flag = query.exec()
        self.test_result(flag)
        return ['82.64.197.53', 'jmg-ftp', 'jmg-wes@lc']

    def get_transfert_param(self):
        print("get_transfert_param")

        query = QSqlQuery()
        query_string = "SELECT host, login, passwd FROM ftp_param"
        flag = query.exec(query_string)
        self.test_result(flag)

        record = query.record()
        nbr_col = record.count()

        list = []
        while query.next():

            for i in range(nbr_col):
                list.append(query.value(i))

        if nbr_col == 0 or  not list :
            QtWidgets.QMessageBox.critical(
                None,
                "Erreur!",
                "Paramétres FTP absents"
            )
            list = self.init_transfert_param()
        return list

    def save_transfert_param(self, param_list):
        print("save_transfert_param")

        query = QSqlQuery()
        query.exec("DELETE FROM ftp_param")

        query.prepare("""INSERT INTO ftp_param (host, login, passwd)
                         VALUES (:host, :login, :passwd) """)

        query.bindValue(":host", param_list[0])
        query.bindValue(":login", param_list[1])
        query.bindValue(":passwd", param_list[2])

        flag = query.exec()
        #self.test_result(flag)

    # *************** Plot Param ******************

    def get_plot_param(self):
        query =  QSqlQuery()
        query_string = "SELECT id, name, color, state, width FROM plot_param"
        flag = query.exec(query_string)

        record = query.record()
        nbr_col = record.count()
        list = []
        while query.next():
            sub_list = []
            for i in range(nbr_col):
                sub_list.append(query.value(i))
            list.append(sub_list)
        #print("list_param=", list)
        return list

    def save_plot_param(self, **b_dict):
        query = QSqlQuery()
        query.exec("DELETE FROM plot_param")

        for key in b_dict:
            #print("key:",key, " cb_label=", b_dict[key].cb_label, " color=",b_dict[key].color, "show=", b_dict[key].cb_check, " width=", b_dict[key].width)
            query.prepare("""INSERT INTO plot_param (id, name, color, state, width)
                            VALUES (:id1, :d1_name, :d1_color, :d1_show, :d1_width)""")

            query.bindValue(":id1", key)
            query.bindValue(":d1_name", b_dict[key].cb_label)
            query.bindValue(":d1_color", b_dict[key].color)
            query.bindValue(":d1_show", b_dict[key].cb_check)
            query.bindValue(":d1_width", b_dict[key].width)

            flag = query.exec()
            #self.test_result(flag)

    # ****************** Datas WES ********************

    def add_record(self, recordBase):
        #print("add_recordBase")
        # Id, Time, time_utc, w1, w2, w3, pulse_1, pince_1, pince_2, base, ph1, ph2, ph3, pa):

        query = QSqlQuery()

        flag = query.prepare("""INSERT INTO weslc_new (Id, Time, time_utc, w1, w2, w3,
                             pulse_1,
                             pince_1, pince_2,
                             base, ph1, ph2, ph3, pa)
                             VALUES (:Id, :Time, :time_utc, :w1, :w2, :w3,
                             :pulse_1,
                             :pince_1, :pince_2,
                             :base, :ph1, :ph2, :ph3, :pa)""")

        #self.test_result(flag)
        query.bindValue(":Id", recordBase[0])
        query.bindValue(":Time", recordBase[1])
        query.bindValue(":time_utc", recordBase[2])
        query.bindValue(":w1", recordBase[3])
        query.bindValue(":w2", recordBase[4])
        query.bindValue(":w3", recordBase[5])
        query.bindValue(":pulse_1", recordBase[6])
        query.bindValue(":pince_1", recordBase[7])
        query.bindValue(":pince_2", recordBase[8])
        query.bindValue(":base", recordBase[9])
        query.bindValue(":ph1", recordBase[10])
        query.bindValue(":ph2", recordBase[11])
        query.bindValue(":ph3", recordBase[12])
        query.bindValue(":pa", recordBase[13])

        flag = query.exec()
        #print("queryexe=",query.executedQuery())
        #self.test_result(flag)

        return flag

    def get_datas_from_base(self, deb, fin):
        print("get_datas_from_base", deb, " ", fin)

        self.deb = deb
        self.fin = fin
        data = []

        query = QSqlQuery()

        flag = query.prepare("""SELECT Time, w1, w2, w3, pulse_1, pince_1, pince_2, ph1, ph2, ph3, pa, base FROM weslc_new
                                WHERE Time BETWEEN :deb AND :fin ORDER BY Time ASC
                               """)

        query.bindValue(":deb", self.deb)
        query.bindValue(":fin", self.fin)

        flag = query.exec()
        #print("queryexe=",query.executedQuery())

        while query.next():
            data.append([query.value('Time'), query.value('w1'), query.value('w2'), query.value('w3'),
                         query.value('pulse_1'), query.value('pince_1'), query.value('pince_2'),
                         query.value('ph1'), query.value('ph2'), query.value('ph3'), query.value('pa'),
                         query.value('base')])
        return data

    def get_lastRecordDate(self):
        print("get_lastRecordDate")
        query = QSqlQuery()
        query_str = """SELECT time FROM weslc_new ORDER by time DESC LIMIT 1"""
        flag = query.exec(query_str)
        #self.test_result(flag)
        while query.next():
            date = query.value(0)
        date = date[0:10]
        #print("date=", date)
        return date

    def get_nbr_records(self):
        print("get_nbr_records")
        query = QSqlQuery()
        flag = query.exec("select count(*) from weslc_new")
        self.test_result(flag)
        while query.next():
            nb_record = query.value(0)
        return nb_record

    #----------------- Infos Base -----------------

    def base_periode(self):
        query = QSqlQuery()
        query_str = """SELECT time_utc FROM weslc_new ORDER by time DESC LIMIT 1"""
        flag = query.exec(query_str)
        self.test_result(flag)
        while query.next():
            date = query.value(0)
        last = date[0:10]

        query_str = """SELECT time_utc FROM weslc_new ORDER by time ASC LIMIT 1"""
        flag = query.exec(query_str)
        self.test_result(flag)
        while query.next():
            date = query.value(0)
        deb = date[0:10]

        return (deb, last)

    def base_optimise(self):
        query = QSqlQuery()
        flag = query.exec("VACUUM")
        self.test_result(flag)

    def test_result(self, flag):
        if flag:
            print("query OK !")
        else:
            print("query. ECHEC")


