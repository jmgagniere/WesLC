import ftplib

from PySide6 import QtWidgets, QtCore

from package.api.database import Database
from package.api.CsvTraitement import CsvTraitement


class FtpDialog(QtWidgets.QDialog):

    path_base = "ftp_temp" + '/'
    para_nom_fic = ('TP-', 'PL-', 'PC-', 'TI-')
    para_nom_rep = ('TEMP', 'PLS', 'PCE', 'TELEINFO')

    def __init__(self):
        super().__init__()

        self.setWindowTitle("FTP-Data")
        self.resize(470,470)

        self.create_layout()
        self.create_widget()
        self.modify_widget()
        self.add_widgets_to_layout()
        self.setup_connections()

        self.db = Database()
        self.retrieve_ftp_param()
        date = self.db.get_lastRecordDate()
        self.dateImport = QtCore.QDate.fromString(date, ("yyyy-MM-dd")).addDays(1)
        self.date_import.setDate(self.dateImport)
        self.te_infos_transfer.clear()

    def create_layout(self):
        self.param_grid_layout = QtWidgets.QGridLayout()
        self.transfert_h_layout =  QtWidgets.QHBoxLayout()
        self.vertical_layout = QtWidgets.QVBoxLayout()
        self.btns_grid_layout = QtWidgets.QGridLayout()

    def create_widget(self):
        self.gb_ftp = QtWidgets.QGroupBox("Paramétres de connexion")
        self.lab_host = QtWidgets.QLabel("host:")
        self.lab_login = QtWidgets.QLabel("Login:")
        self.lab_passwd = QtWidgets.QLabel("Password:")
        self.le_host = QtWidgets.QLineEdit()
        self.le_login = QtWidgets.QLineEdit()
        self.le_passwd = QtWidgets.QLineEdit()
        self.cb_passVisible = QtWidgets.QCheckBox("Visible")
        self.btn_save_param = QtWidgets.QPushButton("Enregistre param")

        self.lab_date = QtWidgets.QLabel("Date Import:")
        self.date_import = QtWidgets.QDateEdit()
        self.btn_test = QtWidgets.QPushButton("Test")
        self.btn_transfer = QtWidgets.QPushButton("Transfer")

        self.te_infos_transfer = QtWidgets.QTextEdit()
        self.btn_abandon = QtWidgets.QPushButton("Abandon")
        self.btn_ajout_base = QtWidgets.QPushButton("Ajout Base")

    def modify_widget(self):
        self.lab_date.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        self.lab_date.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.le_passwd.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.te_infos_transfer.setMinimumHeight(300)
        #self.date_import.setCalendarPopup(True)
        self.btn_ajout_base.setEnabled(True)

    def add_widgets_to_layout(self):
        self.param_grid_layout.addWidget(self.lab_host, 0, 0, 1, 1)
        self.param_grid_layout.addWidget(self.le_host, 0, 1, 1, 1)
        self.param_grid_layout.addWidget(self.lab_login, 1,0, 1,1)
        self.param_grid_layout.addWidget(self.le_login, 1, 1, 1, 1)
        self.param_grid_layout.addWidget(self.lab_passwd, 2, 0, 1, 1)
        self.param_grid_layout.addWidget(self.le_passwd, 2, 1, 1, 1)
        self.param_grid_layout.addWidget(self.btn_save_param, 0, 2, 1, 1 )
        self.param_grid_layout.addWidget(self.cb_passVisible, 2, 2, 1, 1)
        self.gb_ftp.setLayout(self.param_grid_layout)

        self.transfert_h_layout.addWidget(self.lab_date)
        self.transfert_h_layout.addWidget(self.date_import)
        self.transfert_h_layout.addWidget(self.btn_test)
        self.transfert_h_layout.addWidget(self.btn_transfer)

        self.btns_grid_layout.addLayout(self.transfert_h_layout, 0, 0, 1, 4)
        self.btns_grid_layout.addWidget(self.te_infos_transfer, 1, 0, 5, 4)
        self.btns_grid_layout.addWidget(self.btn_abandon, 1, 5, 1, 1)
        self.btns_grid_layout.addWidget(self.btn_ajout_base, 2, 5, 1, 1)

        self.vertical_layout.addWidget(self.gb_ftp)
        self.vertical_layout.addLayout(self.transfert_h_layout)
        self.vertical_layout.addLayout(self.btns_grid_layout)

        self.setLayout(self.vertical_layout)

    def setup_connections(self):
        self.cb_passVisible.stateChanged.connect(self.cb_passVisible_stateChanged)
        self.btn_abandon.clicked.connect(self.hide)
        self.btn_save_param.clicked.connect(self.btn_save_param_clicked)
        self.date_import.dateChanged.connect(self.date_import_dateChanged)
        self.btn_test.clicked.connect(self.btn_test_clicked)
        self.btn_transfer.clicked.connect(self.btn_transfer_clicked)
        self.btn_ajout_base.clicked.connect(self.btn_ajout_base_clicked)


    def cb_passVisible_stateChanged(self):
        if self.cb_passVisible.isChecked():
            self.le_passwd.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        else:
            self.le_passwd.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

    def date_import_dateChanged(self):
        print("date import changed")
        self.dateImport =  self.date_import.date()
        print("nvelle date=",self.dateImport.toString("yyyy-MM-dd"))


    def retrieve_ftp_param(self):
        print("retrieve Ftp_param")
        self.db = Database()
        param_list = self.db.get_transfert_param()
        self.host = param_list[0]
        self.login = param_list[1]
        self.passwd = param_list[2]

        self.le_host.setText(self.host)
        self.le_login.setText(self.login)
        self.le_passwd.setText(self.passwd)

    def btn_ajout_base_clicked(self):
        print("Ajout Base button clicked")
        self.te_infos_transfer.append("Ajout en base en cours.")
        csv_traitement = CsvTraitement(self.dateImport.toString("yyyy-MM-dd"))
        self.hide()
        self.btn_ajout_base.setEnabled(False)
        self.done(QtWidgets.QDialog.DialogCode.Accepted)

    def btn_save_param_clicked(self):
        print("Save Param transfert button clicked")
        list_param = [self.le_host.text(), self.le_login.text(), self.le_passwd.text()]
        self.db.save_transfert_param(list_param)

    def btn_test_clicked(self):
        print("Transfert button clicked")
        self.te_infos_transfer.append("Bouton Ajout Base Enabled")
        self.btn_ajout_base.setEnabled(True)
        try:
            ftp = ftplib.FTP(self.host, self.login, self.passwd)
            etat = ftp.getwelcome()
            self.te_infos_transfer.append(etat)
            self.te_infos_transfer.append('Test OK !')
            ftp.quit()
        except ftplib.all_errors as e:
            self.te_infos_transfer.append("Erreur:" + str(e))

        QtWidgets.QApplication.processEvents()

    def btn_transfer_clicked(self):
        print("Transfert button clicked")

        self.dateImport_str =  self.dateImport.toString("yyyy-MM-dd")

        an = self.dateImport_str[0:4]
        date = self.dateImport_str[5:10]
        print('an=', an, 'date=', date)

        # Connexion (à try except)
        try:
            ftp = ftplib.FTP(self.host, self.login, self.passwd)
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
            result = ftp.cwd(par + '/' + an)
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



