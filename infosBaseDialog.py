import os

from PySide6 import QtWidgets, QtCore

from new_ui.UI_InfosBaseDialog import Ui_Dialog
from package.api.database import Database

class InfosBaseDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Infos Base")

        self.db = Database()

        self.setupUi(self)

        self.btn_infos_clicked()

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

