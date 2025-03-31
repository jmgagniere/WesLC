"""
Construction de l'interface graphique, gestion des boutons
"""



import sys
from functools import partial

from PySide6 import QtWidgets, QtCore
from pyqtgraph import PlotWidget
import pyqtgraph as pg

from package.api.database import Database
from package.api.PlotData import PlotData
from configDialog import ConfigDialog
from ftpDialog import FtpDialog
from infosBaseDialog import InfosBaseDialog

"""
Bloc_Info est un bloc graphique regroupant:
- une checkBox pour afficher sur le graph la courbe définie par le bloc
- un label pour le nom du bloc
- un lineEdit pour afficher la sonde ou le capteur utilisé
- un bouton pour indiquer la couleur utilisée par la courbe sur le graphe
"""
class Bloc_Info(QtWidgets.QWidget):
    def __init__(self, id="Id", cb_check=False, cb_label="name", color="#303030", width=0):
        super().__init__()

        self.cb_check = cb_check
        self.cb_label = cb_label
        self.id = id
        self.color = color

        self.setup_ui()

    def setup_ui(self):
        self.create_widget()
        self.modify_widget()
        self.create_layout()
        self.add_widgets_to_layout()

    def create_widget(self):
        self.cb = QtWidgets.QCheckBox(self.cb_label)
        self.le = QtWidgets.QLineEdit(self.id)
        self.btn = QtWidgets.QPushButton()

    def modify_widget(self):
        self.cb.setCheckState(QtCore.Qt.CheckState(self.cb_check))
        self.le.setReadOnly(True)
        self.btn.setFixedHeight(10)

    def create_layout(self):
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setSpacing(0)
        self.setLayout(self.layout)


    def add_widgets_to_layout(self):
        self.layout.addWidget(self.cb)
        self.layout.addWidget(self.le)
        self.layout.addWidget(self.btn)

#----------------------------------------------------------

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        self.setWindowTitle("WES - LC")

        self.db = Database()
        self.setup_ui()

        self.flag_firstPlot = True
        self.flag_fin_ajout_data_in_base = False
        self.xdict = []

        self.init_plot()

    def setup_ui(self):
        self.create_layouts()
        self.create_widgets()
        self.modify_widgets()
        self.add_widgets_to_layouts()
        self.setup_connections()

    def create_layouts(self):
        # GroupBox Data
        self.grid_data = QtWidgets.QGridLayout()
        
        # GroupBox Periode
        self.grid_periode = QtWidgets.QGridLayout()

        # GroupBox Commande
        self.grid_command = QtWidgets.QGridLayout()

        # Bandeau regroupant les groupbox
        self.bandeau = QtWidgets.QHBoxLayout()

        self.grid_main_layout = QtWidgets.QGridLayout()

        self.window = QtWidgets.QWidget()
        self.setCentralWidget(self.window)

    def create_widgets(self):
        # GroupBox Data
        self.gb_data = QtWidgets.QGroupBox("Data:")
        self.gb_data.setContentsMargins(2, 2, 2, 2)

        # - Récuperation des parametres en base
        bloc_param = self.db.get_plot_param()
        bloc_position = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (1, 4), (1, 5), (1, 6), (1, 3), (0, 3)]

        self.blocs_data_dict = {}
        for i, blo in enumerate(bloc_param):
            bloc = Bloc_Info(id=blo[0], cb_check=blo[3], cb_label=blo[1], color=blo[2], width=blo[4])
            bloc.btn.setStyleSheet('QPushButton {background-color:' + blo[2] + '; border:  none}')
            # Add to Layout
            self.grid_data.addWidget(bloc, bloc_position[i][0], bloc_position[i][1], 1, 1)
            # Signal
            bloc.cb.stateChanged.connect(partial(self.checkBox_changed, bloc.id))

            self.blocs_data_dict[bloc.id] = bloc

        self.lab_conso = QtWidgets.QLabel("           KW:")
        self.le_conso = QtWidgets.QLineEdit("6754")

        # GroupBox Periode
        self.gb_periode = QtWidgets.QGroupBox("Periode")
        self.gb_periode.setContentsMargins(2, 2, 2, 2)
        self.lab_deb = QtWidgets.QLabel("deb:")
        self.dt_deb = QtWidgets.QDateTimeEdit()
        self.lab_fin = QtWidgets.QLabel("fin:")
        self.dt_fin = QtWidgets.QDateTimeEdit()
        self.cb_calendrier = QtWidgets.QCheckBox("Calendrier On")
        self.lab_base = QtWidgets.QLabel("X =")
        self.le_base = QtWidgets.QLineEdit("30/04/2022 21:53")

        # GroupBox Commande
        self.gb_command = QtWidgets.QGroupBox("Commandes")

        self.btn_ftp = QtWidgets.QPushButton("FTP - Data")
        self.btn_plot = QtWidgets.QPushButton("Plot")
        self.btn_infos_base = QtWidgets.QPushButton("Infos Base")
        self.btn_config = QtWidgets.QPushButton("Config")

        # Plot widget
        pg.setConfigOptions(antialias=True)
        pg.setConfigOption('background', '#c7c7c7')
        pg.setConfigOption('foreground', '#000000')

        self.p1 = PlotWidget()
        self.p2 = pg.ViewBox()

    def modify_widgets(self):
        # GroupBox Data
        #self.blocs_data[10].le.setVisible(False)
        self.blocs_data_dict["base"].le.setVisible(False)
        self.blocs_data_dict["base"].btn.setVisible(False)
        #self.blocs_data[10].btn.setVisible(False)
        self.le_conso.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        self.cb_base_clicked()

        # GroupBox Periode
        self.cb_calendrier.setCheckState(QtCore.Qt.CheckState.Checked)
        self.cb_calendrier_stateChanged(2)
        # Mise à jour Periode
        self.get_date_last_record()
        # Efface position curseur
        self.le_base.setText("")

        # GroupBox Commande
        self.p1.setMinimumSize(QtCore.QSize(830, 400))
        #self.p1.setMinimumHeight(700)
        #self.p1.setMinimumWidth(1200)

    def add_widgets_to_layouts(self):
        # GroupBox Data
        self.grid_data.addWidget(self.lab_conso, 0, 4, 1, 1)
        self.grid_data.addWidget(self.le_conso, 0, 5, 1, 1)
        self.gb_data.setLayout(self.grid_data)
        
        # GroupBox Periode
        self.grid_periode.addWidget(self.cb_calendrier, 0, 1)
        self.grid_periode.addWidget(self.lab_deb, 1, 0)
        self.grid_periode.addWidget(self.dt_deb, 1, 1)
        self.grid_periode.addWidget(self.lab_fin, 2, 0)
        self.grid_periode.addWidget(self.dt_fin, 2, 1)
        self.grid_periode.addWidget(self.lab_base, 3, 0)
        self.grid_periode.addWidget(self.le_base, 3, 1)
        self.gb_periode.setLayout(self.grid_periode)

        # GroupBox Commande
        self.grid_command.setContentsMargins(5,0,5,0)
        self.grid_command.addWidget(self.btn_ftp, 0, 0)
        self.grid_command.addWidget(self.btn_plot, 3, 0)
        self.grid_command.addWidget(self.btn_config, 1, 0)
        self.grid_command.addWidget(self.btn_infos_base, 2, 0)
        self.gb_command.setLayout(self.grid_command)


        self.bandeau.addWidget(self.gb_data)
        self.bandeau.addWidget(self.gb_periode)
        self.bandeau.addWidget(self.gb_command)
        self.bandeau.setContentsMargins(0, 0, 0, 0)



        self.grid_main_layout.addLayout(self.bandeau, 0, 0, 1, 1)

        self.grid_main_layout.addWidget(self.p1, 1,0,1,1)
        self.window.setLayout(self.grid_main_layout)

    def setup_connections(self):
        self.cb_calendrier.stateChanged.connect(self.cb_calendrier_stateChanged)
        self.dt_deb.dateTimeChanged.connect(self.dt_deb_changed)
        self.dt_fin.dateTimeChanged.connect(self.dt_fin_changed)

        self.btn_ftp.clicked.connect(self.btn_ftp_clicked)
        self.btn_config.clicked.connect(self.btn_config_clicked)
        self.btn_plot.clicked.connect(self.plot)
        self.btn_infos_base.clicked.connect(self.btn_infos_base_clicked)




    def btn_config_clicked(self):
        print("btn_config clicked")
        configDialog =  ConfigDialog()
        result = configDialog.exec()
        if result == QtWidgets.QDialog.DialogCode.Accepted:
            print("OKOK")


    def btn_ftp_clicked(self):
        print("btn_ftp clicked")
        ftpDialog = FtpDialog()
        result = ftpDialog.exec()
        if result == QtWidgets.QDialog.DialogCode.Accepted:
            print("OKOK")
            self.flag_fin_ajout_data_in_base = True

    def btn_infos_base_clicked(self):
        print("btn_infos_base clicked")
        print("info_base_button clicked")
        infosBaseDialog =  InfosBaseDialog()
        result = infosBaseDialog.exec()
        if result == QtWidgets.QDialog.DialogCode.Accepted:
            print("OKOK")


    def btn_plot_clicked(self):
        print("btn_plot clicked")
        self.plot()

    def cb_base_clicked(self):
        print("cb_base_StateChanged", self.blocs_data_dict['base'].cb.isChecked())
        if self.blocs_data_dict['base'].cb.isChecked() == True:
            self.blocs_data_dict['ph1'].cb.setCheckState(QtCore.Qt.CheckState.Checked)
            self.blocs_data_dict['ph2'].cb.setCheckState(QtCore.Qt.CheckState.Checked)
            self.blocs_data_dict['ph3'].cb.setCheckState(QtCore.Qt.CheckState.Checked)
            self.blocs_data_dict['pa'].cb.setCheckState(QtCore.Qt.CheckState.Checked)
        else:
            self.blocs_data_dict['ph1'].cb.setCheckState(QtCore.Qt.CheckState.Unchecked)
            self.blocs_data_dict['ph2'].cb.setCheckState(QtCore.Qt.CheckState.Unchecked)
            self.blocs_data_dict['ph3'].cb.setCheckState(QtCore.Qt.CheckState.Unchecked)
            self.blocs_data_dict['pa'].cb.setCheckState(QtCore.Qt.CheckState.Unchecked)


    def cb_calendrier_stateChanged(self, state):
        print("calendrier on=", state)
        if self.cb_calendrier.isChecked() == True:
            self.dt_deb.setCalendarPopup(True)
            self.dt_fin.setCalendarPopup(True)
        else:
            self.dt_deb.setCalendarPopup(False)
            self.dt_fin.setCalendarPopup(False)

    def checkBox_changed(self, id, state):
        print(f"checkBox {id} state changed to {state}")
        if id == "base":
            self.cb_base_clicked()
        self.plot()

    def dt_deb_changed(self):
        print("deb_date_changed")
        self.deb_dateTime = self.dt_deb.dateTime()
        print("deb_dateTime=", self.deb_dateTime.toString("yyyy-MM-dd hh:mm"))
        periode = self.periode(self.deb_dateTime, self.fin_dateTime)

        if self.deb_dateTime > self.fin_dateTime:
            QtWidgets.QMessageBox.critical(
                None,
                "Erreur!",
                "Date début > Date fin"
            )
        # si écart supérieur à 31 jour on bloque la mise à jour jusqu'à nouvel date de fin
        # le graphe sera mis à jour soit nouvelle fin ou bouton plot
        if periode < 32:
            self.plot()

    def dt_fin_changed(self):
        print("fin_date_changed")
        self.fin_dateTime = self.dt_fin.dateTime()
        print("fin_dateTime=", self.fin_dateTime.toString("yyyy-MM-dd hh:mm"))
        if self.deb_dateTime > self.fin_dateTime:
            QtWidgets.QMessageBox.critical(
                None,
                "Erreur!",
                "Date début > Date fin"
            )
        self.plot()

    def get_date_last_record(self):
        # Mise à jour des LineEdit à la date du dernier enregistrement en base
        print("get_date_last_record")
        datedeb = self.db.get_lastRecordDate()
        print(datedeb)
        self.deb_dateTime = QtCore.QDateTime.fromString(datedeb, ("yyyy-MM-dd"))
        datefin = self.deb_dateTime.toString("yyyy-MM-dd")
        self.fin_dateTime = QtCore.QDateTime.fromString(datefin, "yyyy-MM-dd").addSecs(86340)
        self.dt_deb.setDateTime(self.deb_dateTime)
        self.dt_fin.setDateTime(self.fin_dateTime)

    def periode(self, deb, fin):
        #print(" periode ")
        periode = deb.daysTo(fin)
        print("periode=", periode)
        return periode


    def plot(self):
        print("PLOT !")
        print(" plot button clicked")
        # Mise à jour des LineEdit au dernier jour d'enregistrement en base
        if self.flag_fin_ajout_data_in_base:
            #self.get_date_last_record()
            self.flag_fin_ajout_data_in_base = False

        deb = self.deb_dateTime.toString("yyyy-MM-dd hh:mm")
        fin = self.fin_dateTime.toString("yyyy-MM-dd hh:mm")

        # Lecture en base données recues sous forme de liste
        data = self.db.get_datas_from_base(deb, fin)
        plotData = PlotData(data)

        # Calcul de la consommation sur la période donnée
        delta_base = plotData.d_base[-1] - plotData.d_base[0]
        delta_base = "%.0f" %delta_base
        #print("delta_base =", delta_base)
        self.le_conso.setText(str(delta_base))

        # Axe des X
        self.xdict = dict(enumerate(plotData.date_time))
        x = list(self.xdict.keys())

        self.w1_dict = dict(enumerate(plotData.d_w1))
        self.w2_dict = dict(enumerate(plotData.d_w2))
        self.w3_dict = dict(enumerate(plotData.d_w3))
        self.pulse1_dict = dict(enumerate(plotData.d_pulse_1))
        self.pince1_dict = dict(enumerate(plotData.d_pince_1))
        self.pince2_dict = dict(enumerate(plotData.d_pince_2))
        self.ph1_dict = dict(enumerate(plotData.d_ph1))
        self.ph2_dict = dict(enumerate(plotData.d_ph2))
        self.ph3_dict = dict(enumerate(plotData.d_ph3))
        self.pa_dict = dict(enumerate(plotData.d_pa))

        if self.flag_firstPlot:
            print("First plot")
            #self.init_plot()
        else:
            print("Plot update")
            if self.blocs_data_dict['1w1'].cb.isChecked():
                self.line_d1.setData(x, plotData.d_w1)
            else:
                self.line_d1.clear()

            if self.blocs_data_dict['1w2'].cb.isChecked():
                self.line_d2.setData(x, plotData.d_w2)
            else:
                self.line_d2.clear()

            if self.blocs_data_dict['1w3'].cb.isChecked():
                self.line_d3.setData(x, plotData.d_w3)
            else:
                self.line_d3.clear()

            if self.blocs_data_dict['pulse1'].cb.isChecked():
                self.line_pulse1.setData(x,  plotData.d_pulse_1)
            else:
                self.line_pulse1.clear()

            if self.blocs_data_dict['pince1'].cb.isChecked():
                self.line_pince1.setData(x,  plotData.d_pince_1)
            else:
                self.line_pince1.clear()

            if self.blocs_data_dict['pince2'].cb.isChecked():
                self.line_pince2.setData(x,  plotData.d_pince_2)
            else:
                self.line_pince2.clear()

            if self.blocs_data_dict['ph1'].cb.isChecked():
                self.line_ph1.setData(x,  plotData.d_ph1)
            else:
                self.line_ph1.clear()

            if self.blocs_data_dict['ph2'].cb.isChecked():
                self.line_ph2.setData(x,  plotData.d_ph2)
            else:
                self.line_ph2.clear()

            if self.blocs_data_dict['ph3'].cb.isChecked():
                self.line_ph3.setData(x,  plotData.d_ph3)
            else:
                self.line_ph3.clear()

            if self.blocs_data_dict['pa'].cb.isChecked():
                self.line_pa.setData(x,  plotData.d_pa)
            else:
                self.line_pa.clear()

            self.updateViews(self.p2, self.p1)


    def init_plot(self):
        print("init_plot")
        # récupération des parametres graphe en base
        plot_param = self.db.get_plot_param()
        #print("plot_param=",plot_param)

        # mise en place graph_Widget
        self.p1.getPlotItem().scene().addItem(self.p2)
        self.p1.getPlotItem().getAxis('right').linkToView(self.p2)
        self.p2.setXLink(self.p1.getPlotItem())
        #self.p2.setYRange(0,10)

        self.proxy = pg.SignalProxy(self.p1.scene().sigMouseMoved, rateLimit=60, slot=self.update_crosshair)

        ##self.p1.getPlotItem().showGrid(True, True,255)
        self.p1.getPlotItem().setLabel('left', "T°", units='C')
        self.p1.getPlotItem().setLabel('right', "P", units='Kw')

        # Add crosshair lines.
        self.crosshair_v = pg.InfiniteLine(angle=90, movable=False, pen=pg.mkPen(color='black', width=0))
        #self.crosshair_h = pg.InfiniteLine(angle=0, movable=False, pen=pg.mkPen(color='black', width=0))
        self.p1.addItem(self.crosshair_v, ignoreBounds=True)
        #self.p1.addItem(self.crosshair_h, ignoreBounds=True)

        # Ajout des courbes
        self.line_d1 = pg.PlotCurveItem(pen=pg.mkPen(color=plot_param[0][2], width=plot_param[0][4]))
        self.line_d2 = pg.PlotCurveItem(pen=pg.mkPen(color=plot_param[1][2], width=plot_param[1][4]))
        self.line_d3 = pg.PlotCurveItem(pen=pg.mkPen(color=plot_param[2][2], width=plot_param[2][4]))
        self.line_pulse1 = pg.PlotCurveItem(pen=pg.mkPen(color=plot_param[3][2], width=plot_param[3][4]))
        self.line_pince1 = pg.PlotCurveItem(pen=pg.mkPen(color=plot_param[4][2], width=plot_param[4][4]))
        self.line_pince2 = pg.PlotCurveItem(pen=pg.mkPen(color=plot_param[5][2], width=plot_param[5][4]))
        self.line_ph1 = pg.PlotCurveItem(pen=pg.mkPen(color=plot_param[6][2], width=plot_param[6][4]))
        self.line_ph2 = pg.PlotCurveItem(pen=pg.mkPen(color=plot_param[7][2], width=plot_param[7][4]))
        self.line_ph3 = pg.PlotCurveItem(pen=pg.mkPen(color=plot_param[8][2], width=plot_param[8][4]))
        self.line_pa = pg.PlotCurveItem(pen=pg.mkPen(color=plot_param[9][2], width=plot_param[9][4]))

        self.p1.addItem(self.line_d1)
        self.p1.addItem(self.line_d2)
        self.p1.addItem(self.line_d3)
        self.p2.addItem(self.line_pulse1)
        self.p2.addItem(self.line_pince1)
        self.p2.addItem(self.line_pince2)
        self.p2.addItem(self.line_ph1)
        self.p2.addItem(self.line_ph2)
        self.p2.addItem(self.line_ph3)
        self.p2.addItem(self.line_pa)

        self.updateViews(self.p2, self.p1)
        self.flag_firstPlot = False

    def update_crosshair(self, e):
            pos = e[0]
            if self.p1.sceneBoundingRect().contains(pos):
                #print("update_crosshair")
                mousePoint = self.p1.getPlotItem().vb.mapSceneToView(pos)
                self.crosshair_v.setPos(mousePoint.x())
                #self.crosshair_h.setPos(mousePoint.y())
                pos_x = int(mousePoint.x())
                #print("pos=", pos_x)
                if pos_x in self.xdict:
                    self.le_base.setText(self.xdict[pos_x])
                    self.blocs_data_dict['1w1'].le.setText(str(self.w1_dict[pos_x]))
                    self.blocs_data_dict['1w2'].le.setText(str(self.w2_dict[pos_x]))
                    self.blocs_data_dict['1w3'].le.setText(str(self.w3_dict[pos_x]))

                    self.blocs_data_dict['pulse1'].le.setText(str(int(self.pulse1_dict[pos_x] * 1000)))
                    self.blocs_data_dict['pince1'].le.setText(str(int(self.pince1_dict[pos_x] * 1000)))
                    self.blocs_data_dict['pince2'].le.setText(str(int(self.pince2_dict[pos_x] * 1000)))
                    self.blocs_data_dict['ph1'].le.setText(str(self.ph1_dict[pos_x]))
                    self.blocs_data_dict['ph2'].le.setText(str(self.ph2_dict[pos_x]))
                    self.blocs_data_dict['ph3'].le.setText(str(self.ph3_dict[pos_x]))
                    self.blocs_data_dict['pa'].le.setText(str(self.pa_dict[pos_x] * 1000))

    def updateViews(self, p2, p1):
        print("updateViews")
        p2.setGeometry(p1.getViewBox().sceneBoundingRect())
        p2.linkedViewChanged(p1.getViewBox(), p2.XAxis)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    win = MainWindow()
    #win.resize(50, 50)
    win.show()
    sys.exit(app.exec())
