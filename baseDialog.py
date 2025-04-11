#import datetime from datetime
import os, glob, time, sys, tarfile
import datetime as dt
from itertools import compress

from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QFileSystemModel
from PySide6.QtCore import QDir, Qt
from PySide6.QtSql import QSqlQuery, QSqlDatabase

from new_ui.UI_baseDialog import Ui_Dialog
from package.api.database import Database


class BaseDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        print("baseDialog.__init")
        super().__init__()
        self.setupUi(self)

        self.init_widgets()
        self.setup_connections()
        print("baseDialog.__init OUT")

    def init_widgets(self):
        print("baseDialog.init_widgets")
        # change le nom de la base dans le groupBox
        dbx = QSqlDatabase.database()
        name = QSqlDatabase.databaseName(dbx)
        self.gb_baseCourante.setTitle(name[9:])

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
        print("baseDialog.init_widgets OUT")


    def setup_connections(self):
        print("baseDialog.setup_connections")
        self.cb_autoriseSplit.stateChanged.connect(self.cb_autoriseSplit_stateChanged)
        self.btn_infosBase.clicked.connect(self.btn_infosBase_clicked)
        self.btn_optimiseBase.clicked.connect(self.btn_optimiseBase_clicked)
        self.btn_base_OK.clicked.connect(self.btn_base_OK_clicked)
        self.btn_loadBase.clicked.connect(self.btn_loadBase_clicked)
        self.btn_splitBase.clicked.connect(self.btn_splitBase_clicked)
        self.tree_view.clicked.connect(self.tree_view_clicked)
        print("baseDialog.setup_connections OUT")

    def btn_infosBase_clicked(self):
        print("baseDialog.btn_infosBase_clicked")
        #name = Database.get_current_base_name_in_base(self)
        dbx = QSqlDatabase.database()
        name = QSqlDatabase.databaseName(dbx)
        #print("name=",name)
        taille = os.path.getsize(name)
        nbr_row = Database.get_nbr_records(self)
        nbr_jour = nbr_row / 1440
        first, last = Database.base_periode(self)
        self.te_infosBase.append('Taille du fichier = ' + str(taille) + ' octets')
        self.te_infosBase.append('Nbre enreg en base = ' + str(nbr_row))
        self.te_infosBase.append('Nbre de jours en base = ' + str(nbr_jour))
        self.te_infosBase.append('Période du:\n' + first + '   au:\n' + last + '\n')
        print("baseDialog.btn_infosBase_clicked OUT")

    def cb_autoriseSplit_stateChanged(self):
        print("baseDialog.cb_autoriseSplit_stateChanged")
        self.btn_splitBase.setEnabled(True)
        print("baseDialog.cb_autoriseSplit_stateChanged OUT")

    def btn_optimiseBase_clicked(self):
        print("baseDialog.btn_optimiseBase_clicked")
        Database.base_optimise(self)
        dbx = QSqlDatabase.database()
        name = QSqlDatabase.databaseName(dbx)
        taille = os.path.getsize(name)
        self.te_infosBase.append('Nouvelle Taille du fichier = ' + str(taille) + ' octets')
        print("baseDialog.btn_optimiseBase_clicked OUT")

    def btn_base_OK_clicked(self):
        print("baseDialog.btn_base_OK_clicked")
        self.done(QtWidgets.QDialog.DialogCode.Accepted)
        print("baseDialog.btn_base_OK_clicked OUT")

    def tree_view_clicked(self):
        print("baseDialog.tree_view_clicked")
        # print item from first column
        #index = self.tree_view.selectedIndexes()[0]
        index = self.tree_view.currentIndex()
        self.new_base_to_load = self.tree_view.model().data(index)
        #print("item",self.new_base_to_load)
        self.btn_loadBase.setEnabled(True)
        print("baseDialog.tree_view_clicked OUT")


    def btn_loadBase_clicked(self):
        print("baseDialog.btn_loadBase_clicked")
        print("new_base_to_load=", self.new_base_to_load)
        # écrit nouvelle base courante en base
        Database.change_current_database_in_base(self, self.new_base_to_load)
        path_base_to_load = f"database/{self.new_base_to_load}"
        # cloture ancienne base
        #Database.close(self)
        print("Old Connection_name=", QSqlDatabase.database())
        QSqlDatabase.database().close()
        # ouverture nouvelle base current
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName(path_base_to_load)
        db.open()
        Database.is_instantiated = True

        # change le nom de la base dans le groupBox
        dbx = QSqlDatabase.database()
        name = QSqlDatabase.databaseName(dbx)
        self.gb_baseCourante.setTitle(name[9:])

        print("New Connection_name=", QSqlDatabase.database())
        print("baseDialog.btn_loadBase_clicked OUT")
        #win.setWindowTitle(f"WES - LC base:{self.new_base_to_load}")

    def get_list_of_existing_base(self):
        print("baseDialog.get_list_of_existing_base")
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
        print("baseDialog.get_list_of_existing_base OUT")

    def btn_splitBase_clicked(self):
        """ But:
        scinder la base pour que les manipulations sur la base soient plus rapides
        on récupère la date à laquelle on veut scinder la base en cours,
        on jette  la partie plus ancienne"""

        print("baseDialog.btn_splitBase_clicked")
        self.te_infosBase.append("\nArchivage en cours...\n")
        # Compression de la base pour une sauvegarde avant destruction des records
        ## recupère nom de la base
        dbx = QSqlDatabase.database()
        name = QSqlDatabase.databaseName(dbx)
        #print("time_start=", dt.datetime.now())
        self.te_infosBase.append("\nArchivage fini...\n")
        self.btn_splitBase.setEnabled(False)
        self.cb_autoriseSplit.setChecked(False)

        with tarfile.open(name + '.bz', "w:bz2") as tar:
            tar.add(name, 'baseWes_full.db')
        #print("time_stop=", dt.datetime.now())



        """# récupere la date du split
        dt_split = self.dt_splitRecord.dateTime()
        #date = QtCore.QDateTime.toString(dt_split, "yyyy-MM-dd")
        print("dt_split=",dt_split)
        Database.split_base(self, dt_split)"""

        print("baseDialog.btn_splitBase_clicked OUT")



