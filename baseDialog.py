#import datetime from datetime
import os, glob, time, sys, tarfile
import datetime as dt

from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QFileSystemModel, QInputDialog, QLineEdit
from PySide6.QtCore import QDir, Qt
from PySide6.QtSql import QSqlDatabase

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
        db = QSqlDatabase.database("conn_base", True)
        ##print("connection names = ", QSqlDatabase.connectionNames())
        name = QSqlDatabase.databaseName(db).split("/")[-1:][0]
        print("database name =", name)
        self.gb_baseCourante.setTitle(name)
        self.dt_splitRecord.setCalendarPopup(True)
        self.dt_firstRecord.setCalendarPopup(True)
        self.dt_lastRecord.setCalendarPopup(True)

        self.btn_infosBase_clicked()
        self.btn_loadBase.setEnabled(False)
        self.get_list_of_existing_base()
        self.rb_garde_apres_date_split.setChecked(True)

        self.update_split_gb()

    def setup_connections(self):
        print("baseDialog.setup_connections")
        self.cb_autoriseSplit.stateChanged.connect(self.cb_autoriseSplit_stateChanged)
        self.btn_infosBase.clicked.connect(self.btn_infosBase_clicked)
        self.btn_optimiseBase.clicked.connect(self.btn_optimiseBase_clicked)
        self.btn_base_OK.clicked.connect(self.btn_base_OK_clicked)
        self.btn_loadBase.clicked.connect(self.btn_loadBase_clicked)
        self.btn_splitBase.clicked.connect(self.btn_splitBase_clicked)
        self.tree_view.clicked.connect(self.tree_view_clicked)
        self.rb_garde_apres_date_split.toggled.connect(lambda :self.rb_garde_toggled(self.rb_garde_apres_date_split))
        self.rb_garde_avant_date_split.toggled.connect(lambda: self.rb_garde_toggled(self.rb_garde_avant_date_split))
        print("baseDialog.setup_connections OUT")

    def update_split_gb(self):
        print("baseDialog.update_split_gb")
        date_deb, date_fin = Database.base_periode(self)
        print("date1er=", date_deb, " date_last=", date_fin)
        last_record_date = QtCore.QDate.fromString(date_fin, ("yyyy-MM-dd"))
        self.dt_lastRecord.setDate(last_record_date)
        self.dt_splitRecord.setDate(last_record_date)
        first_record_date = QtCore.QDate.fromString(date_deb, ("yyyy-MM-dd"))
        self.dt_firstRecord.setDate(first_record_date)
        print("baseDialog.update_split_gb OUT")

    def btn_infosBase_clicked(self):
        print("baseDialog.btn_infosBase_clicked")
        db = QSqlDatabase.database("conn_base", True)
        print("connection names = ", QSqlDatabase.connectionNames())
        name = QSqlDatabase.databaseName(db)
        print("database name =", name)

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
        db = QSqlDatabase.database("conn_base", True)
        print("connection names = ", QSqlDatabase.connectionNames())
        name = QSqlDatabase.databaseName(db)

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
        #print("Old Connection_name=", QSqlDatabase.database())
        #QSqlDatabase.database().close()

        # ouverture nouvelle base current
        db = QSqlDatabase.database("conn_base", True)
        db.setDatabaseName(path_base_to_load)
        flag = db.open()
        print("flagncbaseopen=",flag)

        self.gb_baseCourante.setTitle(path_base_to_load[9:]) ###
        self.te_infosBase.clear()
        self.update_split_gb()
        self.btn_infosBase_clicked()


        print("baseDialog.btn_loadBase_clicked OUT")
        #win.setWindowTitle(f"WES - LC base:{self.new_base_to_load}")

    def rb_garde_toggled(self,rbtn):
        print("rb_garde_toggled")

        print("rb_garde_toggled OUT")

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
        self.te_infosBase.append("\nArchivage en cours...")
        # Compression de la base pour une sauvegarde avant destruction des records
        ## recupère nom de la base qui va être splitter
        db = QSqlDatabase.database("conn_base", True)
        ##print("connection names = ", QSqlDatabase.connectionNames())
        name = QSqlDatabase.databaseName(db)
        ##print("database name =", name)
        self.te_infosBase.append("\nArchivage fini...\n")
        self.btn_splitBase.setEnabled(False)
        self.cb_autoriseSplit.setChecked(False)

        with tarfile.open(name + '.bz', "w:bz2") as tar:
            tar.add(name, name)

        # determine si on garde les enregistrements avant ou après date de split
        if self.rb_garde_apres_date_split.isChecked():
            save_after = True
        else:
            save_after = False

        # récupere la date du split
        dt_split = self.dt_splitRecord.dateTime()
        ##print("dt_split=",dt_split)
        Database.split_base(self, dt_split, save_after)

        basename, ok = QInputDialog.getText(self,"Nouveau nom :",
                                            "Nouveau nom pour la base:", QLineEdit.Normal)
        if ok and basename:
            print("base_name=", basename)
            if basename[-3:] != ".db":
                basename = basename + ".db"
            Database.change_current_database_in_base(self, basename)
            os.rename(name, "./database/" + basename)

            QSqlDatabase.close(db)
            # Ouverture connection à la nouvelle base
            db = QSqlDatabase.addDatabase("QSQLITE", "conn_base")
            db.setDatabaseName("./database/" + basename)
            # Mise à jour des widgets
            self.gb_baseCourante.setTitle(basename)
            self.btn_infosBase_clicked()
            self.update_split_gb()

        print("baseDialog.btn_splitBase_clicked OUT")



