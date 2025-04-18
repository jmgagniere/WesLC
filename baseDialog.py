
import os, glob, bz2
import datetime as dt

from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QFileSystemModel, QInputDialog, QLineEdit, QMessageBox
from PySide6.QtCore import QDir, Qt
from PySide6.QtSql import QSqlDatabase

from new_ui.UI_baseDialog import Ui_Dialog
from package.api.database import Database


class BaseDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        #print("baseDialog.__init  IN")
        super().__init__()
        self.setupUi(self)

        self.init_widgets()
        self.setup_connections()
        #print("baseDialog.__init OUT")

    def init_widgets(self):
        #print("baseDialog.init_widgets  IN")
        # change le nom de la base dans le groupBox
        db = QSqlDatabase.database("conn_base", True)
        ###print("connection names = ", QSqlDatabase.connectionNames())
        name = QSqlDatabase.databaseName(db).split("/")[-1:][0]
        #print("database name =", name)
        self.lab_base_courante.setText(name)
        self.dt_firstRecord.setCalendarPopup(True)
        self.dt_lastRecord.setCalendarPopup(True)
        self.btn_loadBase.setEnabled(False)
        self.btn_kill_base.setEnabled(False)

        self.btn_infosBase_clicked()
        self.get_list_of_existing_base()
        self.update_split_gb()

    def setup_connections(self):
        #print("baseDialog.setup_connections  IN")
        self.cb_autoriseSplit.stateChanged.connect(self.cb_autoriseSplit_stateChanged)
        self.btn_infosBase.clicked.connect(self.btn_infosBase_clicked)
        self.btn_optimiseBase.clicked.connect(self.btn_optimiseBase_clicked)
        self.btn_base_OK.clicked.connect(self.btn_base_OK_clicked)
        self.btn_loadBase.clicked.connect(self.btn_loadBase_clicked)
        self.btn_splitBase.clicked.connect(self.btn_splitBase_clicked)
        self.tree_view.clicked.connect(self.tree_view_clicked)
        self.btn_kill_base.clicked.connect(self.btn_kill_base_clicked)
        #print("baseDialog.setup_connections OUT")

    def update_split_gb(self):
        #print("baseDialog.update_split_gb IN")
        date_deb, date_fin = Database.base_periode(self, False)
        #print("date1er=", date_deb, " date_last=", date_fin)
        last_record_date = QtCore.QDate.fromString(date_fin, ("yyyy-MM-dd"))
        self.dt_lastRecord.setDate(last_record_date)
        self.lab_lastRec.setText(date_fin)
        first_record_date = QtCore.QDate.fromString(date_deb, ("yyyy-MM-dd"))
        self.dt_firstRecord.setDate(first_record_date)
        self.lab_firstRec.setText(date_deb)
        #print("baseDialog.update_split_gb OUT")

    def btn_infosBase_clicked(self):
        #print("baseDialog.btn_infosBase_clicked  IN")
        db = QSqlDatabase.database("conn_base", True)
        ###print("connection names = ", QSqlDatabase.connectionNames())
        name = QSqlDatabase.databaseName(db)
        #print("database name =", name)

        taille = os.path.getsize(name)
        nbr_row = Database.get_nbr_records(self)
        nbr_jour = nbr_row / 1440
        first, last = Database.base_periode(self)
        self.te_infosBase.append('Taille du fichier = ' + str(taille) + ' octets')
        self.te_infosBase.append('Nbre enreg en base = ' + str(nbr_row))
        self.te_infosBase.append('Nbre de jours en base = ' + str(nbr_jour))
        self.te_infosBase.append('Période du:\n' + first + '   au:\n' + last + '\n')
        #print("baseDialog.btn_infosBase_clicked OUT")

    def cb_autoriseSplit_stateChanged(self):
        #print("baseDialog.cb_autoriseSplit_stateChanged  IN")
        self.btn_splitBase.setEnabled(True)
        #print("baseDialog.cb_autoriseSplit_stateChanged OUT")

    def btn_optimiseBase_clicked(self):
        #print("baseDialog.btn_optimiseBase_clicked  IN")
        Database.base_optimise(self)
        db = QSqlDatabase.database("conn_base", True)
        #print("connection names = ", QSqlDatabase.connectionNames())
        name = QSqlDatabase.databaseName(db)

        taille = os.path.getsize(name)
        self.te_infosBase.append('Nouvelle Taille du fichier = ' + str(taille) + ' octets')
        #print("baseDialog.btn_optimiseBase_clicked OUT")

    def btn_base_OK_clicked(self):
        #print("baseDialog.btn_base_OK_clicked  IN")
        self.done(QtWidgets.QDialog.DialogCode.Accepted)
        #print("baseDialog.btn_base_OK_clicked OUT")

    def tree_view_clicked(self):
        #print("baseDialog.tree_view_clicked IN")
        # #print item from first column
        index = self.tree_view.currentIndex().siblingAtColumn(0)

        self.selected_file = self.tree_view.model().data(index)
        #print("item",self.selected_file)
        self.btn_loadBase.setEnabled(True)
        self.btn_kill_base.setEnabled(True)
        #print("baseDialog.tree_view_clicked OUT")

    def btn_loadBase_clicked(self):
        #print("baseDialog.btn_loadBase_clicked IN")
        #print("selected_file=", self.selected_file)
        # écrit nouvelle base courante en base
        Database.change_current_database_in_base(self, self.selected_file)
        path_base_to_load = f"database/{self.selected_file}"

        # ouverture nouvelle base current
        db = QSqlDatabase.database("conn_base", True)
        db.setDatabaseName(path_base_to_load)
        db.open()

        self.lab_base_courante.setText(path_base_to_load[9:])
        self.te_infosBase.clear()
        self.update_split_gb()
        self.btn_infosBase_clicked()
        #print("baseDialog.btn_loadBase_clicked OUT")

    def btn_kill_base_clicked(self):
        #print("baseDialog.btn_kill_base_clicked IN")
        self.btn_kill_base.setEnabled(False)
        # Vérif fichier n'est pas la base courante
        f_to_kill = self.selected_file
        cur_base = Database.get_current_base_name_in_base(self)
        #print("cur_base=",cur_base, "selected_file=",self.selected_file)
        if cur_base != self.selected_file:
            bt = QMessageBox.question(self,"ATTENTION !",
                                                "Etes-vous sûr de bien vouloir détruire cette base?",
                                                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                                defaultButton=QMessageBox.StandardButton.No)
            if bt == QMessageBox.StandardButton.Yes:
                os.remove("./database/" + self.selected_file)
        else:
            bt = QMessageBox.critical(self,"ATTENTION !", "La base courante ne peut pas être détruite")

        self.get_list_of_existing_base()
        #print("baseDialog.btn_kill_base_clicked OUT")

    def get_list_of_existing_base(self):
        #print("baseDialog.get_list_of_existing_base  IN")
        path = "database/*.db"

        list_files = []
        for file in glob.glob(path,recursive=True):
            file_time = dt.datetime.fromtimestamp(os.path.getmtime(file))
            ##print("file_time=", file_time.strftime("%d/%m/%Y, %H:%M"))
            list_files.append([file, file_time.strftime("%d/%m/%Y %H:%M"),  os.path.getsize(file)])
        #print("list_files", list_files)
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
        #print("baseDialog.get_list_of_existing_base OUT")

    def btn_splitBase_clicked(self):
        """ But:
        scinder la base pour que les manipulations sur la base soient plus rapides
        on récupère la date à laquelle on veut scinder la base en cours,
        on jette  la partie avant la date du 1er record et la partie après la date du dernier"""

        #print("baseDialog.btn_splitBase_clicked  IN")
        self.te_infosBase.append("\nArchivage en cours...")
        # Compression de la base pour une sauvegarde avant destruction des records
        ## recupère nom de la base qui va être splitter
        db = QSqlDatabase.database("conn_base", True)
        name = QSqlDatabase.databaseName(db)
        self.te_infosBase.append("\nArchivage fini...\n")
        self.btn_splitBase.setEnabled(False)
        self.cb_autoriseSplit.setChecked(False)
        name_path_list = name.split('/')
        #print("name_path_list=",name_path_list)
        name_arch = "./" + name_path_list[0] + "/archives/" + name_path_list[1]
        #print("name_arch=", name_arch)

        with open(name, 'rb') as f1:
            data = f1.read()
        # test si archive existe déja
        if os.path.exists(name_arch + '.bz2'):
            bt = QMessageBox.question(self,'ATTENTION !', "L'archive existe déjà, voulez-vous l'écraser ?",
                                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                        defaultButton = QMessageBox.StandardButton.No )
            if bt == QMessageBox.StandardButton.No:
                name_arch = name_arch + 'new'
        f = bz2.open(name_arch + '.bz2', "wb")
        f.write(data)
        f.close()

        # récupere la periode du split
        dt_deb_split = self.dt_firstRecord.dateTime()
        dt_fin_split = self.dt_lastRecord.dateTime().addDays(1)
        Database.split_base(self, dt_deb_split, dt_fin_split )

        basename, ok = QInputDialog.getText(self,"Nouveau nom :",
                                            "Nouveau nom pour la base:", QLineEdit.Normal)
        if ok and basename:
            #print("base_name=", basename)
            if basename[-3:] != ".db":
                basename = basename + ".db"
            Database.change_current_database_in_base(self, basename)
            os.rename(name, "./database/" + basename)

            QSqlDatabase.close(db)
            # Ouverture connection à la nouvelle base
            db = QSqlDatabase.addDatabase("QSQLITE", "conn_base")
            db.setDatabaseName("./database/" + basename)
            # Mise à jour des widgets
            #self.gb_baseCourante.setTitle(basename)
            self.lab_base_courante.setText(basename)
            self.btn_infosBase_clicked()
            self.update_split_gb()
            # Decompresse l'archive
            #with bz2.open(name + '.bz2', 'rb' ) as f:
            #    data = f.read()
            with open(name, 'wb') as f:
                f.write(data)

        #print("baseDialog.btn_splitBase_clicked OUT")


