import os
from PySide6 import QtWidgets, QtCore

from new_ui.UI_baseDialog import Ui_Dialog
from package.api.database import Database

class BaseDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.db = Database()

        self.init_widgets()
        self.setup_connections()

    def init_widgets(self):
        print("init_widgets")
        self.current_base_name = self.db.get_current_base_name()
        print("current base=", self.current_base_name)
        self.gb_baseCourante.setTitle(self.current_base_name)
        self.btn_infosBase_clicked()
        date = self.db.get_lastRecordDate()[0:10]
        self.deb_last_record_date = QtCore.QDate.fromString(date, ("yyyy-MM-dd"))
        self.dt_lastRecord.setDate(self.deb_last_record_date)
        self.dt_splitReccord.setDate(self.deb_last_record_date)
        date = self.db.get_firstRecordDate()[0:10]
        self.firstRecord_date = QtCore.QDate.fromString(date, ("yyyy-MM-dd"))
        self.dt_firstRecord.setDate(self.firstRecord_date)



    def setup_connections(self):
        self.btn_infosBase.clicked.connect(self.btn_infosBase_clicked)
        self.btn_optimiseBase.clicked.connect(self.btn_optimiseBase_clicked)

    def btn_infosBase_clicked(self):
        print("infosBase btn clicked")
        path = "database/"  + self.current_base_name
        taille = os.path.getsize(path)
        nbr_row = self.db.get_nbr_records()
        nbr_jour = nbr_row / 1440
        first, last = self.db.base_periode()
        self.te_infosBase.append('Taille du fichier = ' + str(taille) + ' octets')
        self.te_infosBase.append('Nbre enreg en base = ' + str(nbr_row))
        self.te_infosBase.append('Nbre de jours en base = ' + str(nbr_jour))
        self.te_infosBase.append('Période du:\n' + first + '   au:\n' + last + '\n')

    def btn_optimiseBase_clicked(self):
        print("btn_optimiseBase clicked")
        self.db.base_optimise()
        taille = os.path.getsize("database/baseWes.db")
        self.te_infosBase.append('Nouvelle Taille du fichier = ' + str(taille) + ' octets')
