import ftplib

from PySide6 import QtWidgets, QtCore
from new_ui.UI_FTP_Dialog import Ui_Dialog
from package.api.database import Database
from package.api.CsvTraitement import CsvTraitement


class FtpDialog(QtWidgets.QDialog, Ui_Dialog):

    path_base = "ftp_temp" + '/'
    para_nom_fic = ('TP-', 'PL-', 'PC-', 'TI-')
    para_nom_rep = ('TEMP', 'PLS', 'PCE', 'TELEINFO')

    def __init__(self):
        print("ftpDialog.__init__ IN")
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("FTP-Data")
        self.modify_widget()
        self.setup_connections()

        self.retrieve_ftp_param()
        date = Database.get_lastRecordDate(self)
        self.dateImport = QtCore.QDate.fromString(date, "yyyy-MM-dd").addDays(1)
        self.date_import.setDate(self.dateImport)
        self.te_infos_transfer.clear()
        print("ftpDialog.__init__ OUT")

    def modify_widget(self):
        print("ftpDialog.modify_widget IN")

        self.le_passwd.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.date_import.setCalendarPopup(True)
        self.btn_ajout_base.setEnabled(True)
        print("ftpDialog.modify_widget OUT")

    def setup_connections(self):
        print("ftpDialog.setup_connections  IN")
        self.cb_passVisible.stateChanged.connect(self.cb_passVisible_stateChanged)
        self.btn_abandon.clicked.connect(self.hide)
        self.btn_save_param.clicked.connect(self.btn_save_param_clicked)
        self.date_import.dateChanged.connect(self.date_import_dateChanged)
        self.btn_test.clicked.connect(self.btn_test_clicked)
        self.btn_transfer.clicked.connect(self.btn_transfer_clicked)
        self.btn_ajout_base.clicked.connect(self.btn_ajout_base_clicked)
        print("ftpDialog.setup_connections OUT")


    def cb_passVisible_stateChanged(self):
        print("ftpDialog.cb_passVisible_stateChanged  IN")
        if self.cb_passVisible.isChecked():
            self.le_passwd.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        else:
            self.le_passwd.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
            print("ftpDialog.cb_passVisible_stateChanged OUT")

    def date_import_dateChanged(self):
        print("ftpDialog.date_import_dateChanged IN")
        self.dateImport =  self.date_import.date()
        print("nvelle date=",self.dateImport.toString("yyyy-MM-dd"))
        print("ftpDialog.date_import_dateChanged OUT")

    def retrieve_ftp_param(self):
        print("ftpDialog.retrieve_ftp_param IN")
        param_list = Database.get_transfert_param(self)
        host = param_list[0]
        login = param_list[1]
        passwd = param_list[2]

        self.le_host.setText(host)
        self.le_login.setText(login)
        self.le_passwd.setText(passwd)
        print("ftpDialog.retrieve_ftp_param OUT")

    def btn_ajout_base_clicked(self):
        print("ftpDialog.btn_ajout_base_clicked  IN")
        self.te_infos_transfer.append("Ajout en base en cours.")
        CsvTraitement(self.dateImport.toString("yyyy-MM-dd"))
        self.hide()
        self.btn_ajout_base.setEnabled(False)
        self.done(QtWidgets.QDialog.DialogCode.Accepted)
        print("ftpDialog.btn_ajout_base_clicked OUT")

    def btn_save_param_clicked(self):
        print("ftpDialog.btn_save_param_clicked  IN")
        list_param = [self.le_host.text(), self.le_login.text(), self.le_passwd.text()]
        Database.save_transfert_param(self, list_param)
        print("ftpDialog.btn_save_param_clicked OUT")

    def btn_test_clicked(self):
        print("ftpDialog.btn_test_clicked  IN")
        self.te_infos_transfer.append("Bouton Ajout Base Enabled")
        self.btn_ajout_base.setEnabled(True)
        host = self.le_host.text()
        login = self.le_login.text()
        passwd = self.le_passwd.text()

        try:
            ftp = ftplib.FTP(host, login, passwd)
            etat = ftp.getwelcome()
            self.te_infos_transfer.append(etat)
            self.te_infos_transfer.append('Test OK !')
            ftp.quit()
        except ftplib.all_errors as e:
            self.te_infos_transfer.append("Erreur:" + str(e))

        QtWidgets.QApplication.processEvents()
        print("ftpDialog.btn_test_clicked OUT")

    def btn_transfer_clicked(self):
        print("ftpDialog.btn_transfer_clicked  IN")

        dateImport_str =  self.dateImport.toString("yyyy-MM-dd")

        an = dateImport_str[0:4]
        date = dateImport_str[5:10]
        print('an=', an, 'date=', date)

        host = self.le_host.text()
        login = self.le_login.text()
        passwd = self.le_passwd.text()

        # Connexion (à try except)
        try:
            ftp = ftplib.FTP(host, login, passwd)
        except ftplib.all_errors as e:
            self.te_infos_transfer.append("Erreursize:" + str(e))
            QtWidgets.QApplication.processEvents()
            return

        etat = ftp.getwelcome()
        parent_dir = ftp.pwd()
        self.te_infos_transfer.append(etat)
        QtWidgets.QApplication.processEvents()  # Pour forcer la mise à jour

        # Changement de répertoire
        for index, par in enumerate(self.para_nom_rep):
            ftp.cwd(par + '/' + an)
            filename = self.para_nom_fic[index] + date + '.csv'
            self.te_infos_transfer.append('Fichier:' + ftp.pwd() + '/' + filename)
            QtWidgets.QApplication.processEvents()

            try:
                size = ftp.size(filename)
            except ftplib.all_errors as e:
                self.te_infos_transfer.append("Erreursize:" + str(e))
                QtWidgets.QApplication.processEvents()
                size = 0

            if size != 0:
                self.te_infos_transfer.append("Téléchargement en cours.")
                QtWidgets.QApplication.processEvents()
                try:
                    with open(self.path_base + filename, 'wb') as my_file:
                        ftp.retrbinary('RETR ' + filename, my_file.write, 1024)
                except ftplib.all_errors as e:
                    self.te_infos_transfer.append("Erreur:" + str(e))
                    QtWidgets.QApplication.processEvents()

            ftp.cwd(parent_dir)

        # Fermeture de la connexion
        ftp.quit()

        if size == 0:
            self.te_infos_transfer.append('Echec de l\'import')
        else:
            self.te_infos_transfer.append('Fini - Prêt à importer en base')
            # Activation bouton Ajout_base
            self.btn_ajout_base.setEnabled(True)

        print('Fertig')
        print("ftpDialog.btn_transfer_clicked OUT")

