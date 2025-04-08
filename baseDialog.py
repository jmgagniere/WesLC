import os, glob, time
import datetime as dt
from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QFileSystemModel
from PySide6.QtCore import QDir, Qt
from PySide6.QtSql import QSqlQuery, QSqlDatabase

from new_ui.UI_baseDialog import Ui_Dialog
from package.api.database import Database


class BaseDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        pass
        self.db = Database()

        self.init_widgets()
        self.setup_connections()

    def init_widgets(self):
        print("init_widgets")
        self.current_base_name = Database.get_current_base_name(self)
        print("current base=", self.current_base_name)
        self.gb_baseCourante.setTitle(self.current_base_name)
        self.btn_infosBase_clicked()
        self.btn_loadBase.setEnabled(False)
        self.get_list_of_existing_base()

        date = Database.get_lastRecordDate(self)[0:10]
        self.deb_last_record_date = QtCore.QDate.fromString(date, ("yyyy-MM-dd"))
        self.dt_lastRecord.setDate(self.deb_last_record_date)
        self.dt_splitRecord.setDate(self.deb_last_record_date)
        date = Database.get_firstRecordDate(self)[0:10]
        self.firstRecord_date = QtCore.QDate.fromString(date, ("yyyy-MM-dd"))
        self.dt_firstRecord.setDate(self.firstRecord_date)


    def setup_connections(self):
        self.btn_infosBase.clicked.connect(self.btn_infosBase_clicked)
        self.btn_optimiseBase.clicked.connect(self.btn_optimiseBase_clicked)
        self.btn_base_OK.clicked.connect(self.btn_base_OK_clicked)
        self.btn_loadBase.clicked.connect(self.btn_loadBase_clicked)
        self.tree_view.clicked.connect(self.tree_view_clicked)

    def btn_infosBase_clicked(self):
        print("infosBase btn clicked")
        path = "database/"  + self.current_base_name
        taille = os.path.getsize(path)
        nbr_row = Database.get_nbr_records(self)
        nbr_jour = nbr_row / 1440
        first, last = Database.base_periode(self)
        self.te_infosBase.append('Taille du fichier = ' + str(taille) + ' octets')
        self.te_infosBase.append('Nbre enreg en base = ' + str(nbr_row))
        self.te_infosBase.append('Nbre de jours en base = ' + str(nbr_jour))
        self.te_infosBase.append('Période du:\n' + first + '   au:\n' + last + '\n')

    def btn_optimiseBase_clicked(self):
        print("btn_optimiseBase clicked")
        Database.base_optimise(self)
        taille = os.path.getsize("database/baseWes.db")
        self.te_infosBase.append('Nouvelle Taille du fichier = ' + str(taille) + ' octets')

    def btn_base_OK_clicked(self):
        print("btn_base_OK_clicked")
        self.done(QtWidgets.QDialog.DialogCode.Accepted)

    def tree_view_clicked(self):
        print("tree_view_clicked")
        # print item from first column
        #index = self.tree_view.selectedIndexes()[0]
        index = self.tree_view.currentIndex()
        self.new_base_to_load = self.tree_view.model().data(index)
        print("item",self.new_base_to_load)
        self.btn_loadBase.setEnabled(True)


    def btn_loadBase_clicked(self):
        print("btn_loadBase_clicked")
        print("new_base_to_load=", self.new_base_to_load)
        # écrit nouvelle base courante en base
        Database.change_current_database(self, self.new_base_to_load)
        # cloture ancienne base
        #Database.close(self)
        print("Connection_name=", QSqlDatabase.database())
        QSqlDatabase.database().close()



    def get_list_of_existing_base(self):
        print("get_list_of_existing_base")
        path = "database/*.db"

        list_files = []
        for file in glob.glob(path,recursive=True):
            file_time = dt.datetime.fromtimestamp(os.path.getmtime(file))
            #print("file_time=", file_time.strftime("%d/%m/%Y, %H:%M"))
            list_files.append([file, file_time.strftime("%d/%m/%Y %H:%M"),  os.path.getsize(file)])
            #item = QtGui.QStandardItem(file)
            #model.appendRow(item)
        print("list_files", list_files)
        model = QFileSystemModel()
        path = "database"
        model.setRootPath(path)
        filter = ["*.db"]
        model.setFilter(QDir.NoDot | QDir.Files )
        #model.setFilter(QDir.NoDot | QDir.Files | QDir.AllDirs)
        model.setNameFilters(filter)
        model.setNameFilterDisables(False)
        model.sort(0, Qt.SortOrder.AscendingOrder)
        model.removeColumn(2)

        self.tree_view.setModel(model)
        self.tree_view.setRootIndex(model.index(path))
        self.tree_view.header().setSortIndicator(0, Qt.AscendingOrder)
        self.tree_view.setSortingEnabled(True)
        self.tree_view.setColumnHidden(2, True)
        self.tree_view.setColumnWidth(0,200)
        self.tree_view.setColumnWidth(1, 100)
        self.tree_view.setColumnWidth(3, 100)



