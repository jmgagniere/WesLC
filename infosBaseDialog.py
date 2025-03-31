import os

from PySide6 import QtWidgets, QtCore

from package.api.database import Database

class InfosBaseDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Infos Base")

        self.db = Database()

        self.setup_ui()
        self.btn_infos_clicked()

    def setup_ui(self):
        self.create_layout()
        self.create_widgets()
        self.modify_widgets()
        self.add_widgets_to_layout()
        self.setup_connections()

    def create_layout(self):
        self.grid_layout = QtWidgets.QGridLayout()
        pass

    def create_widgets(self):
        self.btn_infos = QtWidgets.QPushButton("Infos Base")
        self.btn_optimise = QtWidgets.QPushButton("Optimise Base")
        self.btn_OK = QtWidgets.QPushButton("OK")
        self.btn_purge_ftp = QtWidgets.QPushButton("Purge FTP")
        self.te_infos = QtWidgets.QTextEdit()


    def modify_widgets(self):
        self.te_infos.setReadOnly(True)

    def add_widgets_to_layout(self):
        self.grid_layout.addWidget(self.te_infos, 0, 0, 5, 2)
        self.grid_layout.addWidget(self.btn_infos, 0, 4, 1, 1)
        self.grid_layout.addWidget(self.btn_optimise, 1, 4, 1, 1)
        self.grid_layout.addWidget(self.btn_purge_ftp, 3, 4, 1, 1)
        self.grid_layout.addWidget(self.btn_OK, 5, 4, 1, 1 )

        self.setLayout(self.grid_layout)

    def setup_connections(self):
        self.btn_infos.clicked.connect(self.btn_infos_clicked)
        self.btn_optimise.clicked.connect(self.btn_optimise_clicked)
        self.btn_OK.clicked.connect(self.btn_OK_clicked)
        self.btn_purge_ftp.clicked.connect(self.btn_purge_ftp_clicked)


    def btn_infos_clicked(self):
        print("btn_infos_base clicked")
        taille = os.path.getsize("database/baseWes.db")
        nbr_row = self.db.get_nbr_records()
        nbr_jour = nbr_row / 1440
        first, last = self.db.base_periode()
        self.te_infos.append('Taille du fichier = ' + str(taille) + ' octets')
        self.te_infos.append('Nbre enreg en base = ' + str(nbr_row))
        self.te_infos.append('Nbre de jours en base = ' + str(nbr_jour))
        self.te_infos.append('Période du:\n' + first + '   au:\n' + last + '\n')

    def btn_optimise_clicked(self):
        print("btn_optimise clicked")
        self.db.base_optimise()
        taille = os.path.getsize("database/baseWes.db")
        self.te_infos.append('Nouvelle Taille du fichier = ' + str(taille) + ' octets')

    def btn_OK_clicked(self):
        print("btn_Ok clicked")
        self.done(QtWidgets.QDialog.DialogCode.Accepted)

    def btn_purge_ftp_clicked(self):
        print("btn_purge_ftp_clicked")
        list = os.listdir('./ftp_temp')

        for f in list:
            os.remove(f"./ftp_temp/{f}")

