import sys
from functools import partial

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtCore, QtWidgets
from pyqtgraph import PlotWidget
import pyqtgraph as pg

from new_ui.UI_mainWindow import Ui_MainWindow
from package.api.database import Database
from package.api.PlotData import PlotData
from configDialog import ConfigDialog
from ftpDialog import FtpDialog
from infosBaseDialog import InfosBaseDialog
from baseDialog import BaseDialog

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle("WES - LC")
        self.db = Database()
        self.flag_firstPlot = True
        self.flag_fin_ajout_data_in_base = False


        self.init_widget()
        self.setup_connections()
        self.init_plot()

    def init_widget(self):
        # Widgets Légende
        self.key_list = []
        self.cb_val = []
        # self.cb_label = []
        self.le_color = []
        # liste des widgets utilisé dans le groupbox Légende par categorie
        self.list_cb_widget = [self.cb_1w1, self.cb_1w2, self.cb_1w3, self.cb_pulse1, self.cb_pince1, self.cb_pince2,
                               self.cb_ph1, self.cb_ph2, self.cb_ph3, self.cb_pa, self.cb_base]
        # le_widget affiche la couleur
        self.list_le_widget = [self.le_1w1, self.le_1w2, self.le_1w3, self.le_pulse1, self.le_pince1, self.le_pince2,
                               self.le_ph1, self.le_ph2, self.le_ph3, self.le_pa ]
        # le_val_widget affiche la valeur à la position du curseur
        self.list_le_val_widget = [self.le_val_1w1, self.le_val_1w2, self.le_val_1w3,
                                   self.le_val_pulse1, self.le_val_pince1, self.le_val_pince2,
                                    self.le_val_ph1, self.le_val_ph2, self.le_val_ph3, self.le_val_pa ]

        # Widgets Période
        self.cb_calendrier.setCheckState(QtCore.Qt.CheckState.Checked)
        self.dt_deb.setCalendarPopup(True)
        self.dt_fin.setCalendarPopup(True)

        # Mise à jour Periode
        self.get_date_last_record()
        # Efface position curseur
        self.le_base.setText("")

        # PlotWidgets
        pg.setConfigOptions(antialias=True)
        pg.setConfigOption('background', '#c7c7c7')
        pg.setConfigOption('foreground', '#000000')

        self.p1 = PlotWidget()
        self.p2 = pg.ViewBox()

        self.p1.setMinimumSize(QtCore.QSize(1000, 400))
        self.main_gridLayout.addWidget(self.p1, 1, 0, -1, -1)

    def setup_connections(self):
        self.cb_calendrier.stateChanged.connect(self.cb_calendrier_stateChanged)
        self.dt_deb.dateTimeChanged.connect(self.dt_deb_changed)
        self.dt_fin.dateTimeChanged.connect(self.dt_fin_changed)

        self.btn_plot.clicked.connect(self.plot)
        self.btn_ftp.clicked.connect(self.btn_ftp_clicked)

        self.actionQuit.triggered.connect(self.close)
        self.actionConfig_Legende.triggered.connect(self.btn_config_clicked)
        self.actionactionBase.triggered.connect(self.actionBase_triggered)

    def init_plot(self):
        print("init_plot")

        # récupération des parametres graphe en base
        plot_param = self.db.get_plot_param()
        print("plot_param=",plot_param)

        for i, blo in enumerate(plot_param):
            #      Id       name    color   cb etat width
            #bloc = Bloc_Info(id=blo[0], cb_check=blo[3], cb_label=blo[1], color=blo[2], width=blo[4])

            self.key_list.append(blo[0])
            self.cb_val.append([blo[3], blo[1], self.list_cb_widget[i]])
            #self.cb_label.append(blo[1])
            if i < 10:
                self.le_color.append([blo[2], self.list_le_widget[i]])

        self.dict_cb = dict(zip(self.key_list, self.cb_val))
        print("dict_cb=",self.dict_cb)

        self.dict_le = dict(zip(self.key_list, self.le_color))
        print("dict_le", self.dict_le)

        # Affichage valeurs checkBox et lineEdit
        for key, val in self.dict_cb.items():
            # checkBox state
            val[2].setCheckState(QtCore.Qt.CheckState(val[0]))
            # checkBox name
            val[2].setText(val[1])
            # Signal
            val[2].stateChanged.connect(partial(self.checkBox_changed, key))

        for key, val in self.dict_le.items():
            str = "QLineEdit { background:" + val[0] +";}"
            val[1].setStyleSheet(str)

        # mise en place graph_Widget
        self.p1.getPlotItem().scene().addItem(self.p2)
        self.p1.getPlotItem().getAxis('right').linkToView(self.p2)
        self.p2.setXLink(self.p1.getPlotItem())
        #self.p2.setYRange(0,10)

        self.proxy = pg.SignalProxy(self.p1.scene().sigMouseMoved, rateLimit=60, slot=self.update_crosshair)

        #self.p1.getPlotItem().showGrid(True, True,255)
        self.p1.getPlotItem().setLabel('left', "T°", units='C')
        self.p1.getPlotItem().setLabel('right', "P", units='Kw')

        # Add crosshair lines.
        self.crosshair_v = pg.InfiniteLine(angle=90, movable=False, pen=pg.mkPen(color='black', width=0))
        # self.crosshair_h = pg.InfiniteLine(angle=0, movable=False, pen=pg.mkPen(color='black', width=0))
        self.p1.addItem(self.crosshair_v, ignoreBounds=True)
        # self.p1.addItem(self.crosshair_h, ignoreBounds=True)

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

    def plot(self):
        print("plot ")
        print(" plot button clicked")
        # Mise à jour des LineEdit au dernier jour d'enregistrement en base
        if self.flag_fin_ajout_data_in_base:
            # self.get_date_last_record()
            self.flag_fin_ajout_data_in_base = False

        deb = self.deb_dateTime.toString("yyyy-MM-dd hh:mm")
        fin = self.fin_dateTime.toString("yyyy-MM-dd hh:mm")

        # Lecture en base données recues sous forme de liste
        data = self.db.get_datas_from_base(deb, fin)
        plotData = PlotData(data)

        # Calcul de la consommation sur la période donnée
        delta_base = plotData.d_base[-1] - plotData.d_base[0]
        delta_base = "%.0f" % delta_base
        # print("delta_base =", delta_base)
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
            # self.init_plot()
        else:
            print("Plot update")
            if self.dict_cb['1w1'][2].isChecked():
                self.line_d1.setData(x, plotData.d_w1)
            else:
                self.line_d1.clear()

            if self.dict_cb['1w2'][2].isChecked():
                self.line_d2.setData(x, plotData.d_w2)
            else:
                self.line_d2.clear()

            if self.dict_cb['1w3'][2].isChecked():
                self.line_d3.setData(x, plotData.d_w3)
            else:
                self.line_d3.clear()

            if self.dict_cb['pulse1'][2].isChecked():
                self.line_pulse1.setData(x, plotData.d_pulse_1)
            else:
                self.line_pulse1.clear()

            if self.dict_cb['pince1'][2].isChecked():
                self.line_pince1.setData(x, plotData.d_pince_1)
            else:
                self.line_pince1.clear()

            if self.dict_cb['pince2'][2].isChecked():
                self.line_pince2.setData(x, plotData.d_pince_2)
            else:
                self.line_pince2.clear()

            if self.dict_cb['ph1'][2].isChecked():
                self.line_ph1.setData(x, plotData.d_ph1)
            else:
                self.line_ph1.clear()

            if self.dict_cb['ph2'][2].isChecked():
                self.line_ph2.setData(x, plotData.d_ph2)
            else:
                self.line_ph2.clear()

            if self.dict_cb['ph3'][2].isChecked():
                self.line_ph3.setData(x, plotData.d_ph3)
            else:
                self.line_ph3.clear()

            if self.dict_cb['pa'][2].isChecked():
                self.line_pa.setData(x, plotData.d_pa)
            else:
                self.line_pa.clear()

            self.updateViews(self.p2, self.p1)

    def update_crosshair(self, e):
        print("update_crosshair")
        pos = e[0]
        if self.p1.sceneBoundingRect().contains(pos):
            # print("update_crosshair")
            mousePoint = self.p1.getPlotItem().vb.mapSceneToView(pos)
            self.crosshair_v.setPos(mousePoint.x())
            # self.crosshair_h.setPos(mousePoint.y())
            pos_x = int(mousePoint.x())
            # print("pos=", pos_x)
            if pos_x in self.xdict:
                self.le_base.setText(self.xdict[pos_x])
                self.le_val_1w1.setText(str(self.w1_dict[pos_x]))
                self.le_val_1w2.setText(str(self.w2_dict[pos_x]))
                self.le_val_1w3.setText(str(self.w3_dict[pos_x]))

                self.le_val_pulse1.setText(str(int(self.pulse1_dict[pos_x] * 1000)))
                self.le_val_pince1.setText(str(int(self.pince1_dict[pos_x] * 1000)))
                self.le_val_pince2.setText(str(int(self.pince2_dict[pos_x] * 1000)))
                self.le_val_ph1.setText(str(self.ph1_dict[pos_x]))
                self.le_val_ph2.setText(str(self.ph2_dict[pos_x]))
                self.le_val_ph3.setText(str(self.ph3_dict[pos_x]))
                self.le_val_pa.setText(str(self.pa_dict[pos_x] * 1000))

    def updateViews(self, p2, p1):
        print("updateViews")
        p2.setGeometry(p1.getViewBox().sceneBoundingRect())
        p2.linkedViewChanged(p1.getViewBox(), p2.XAxis)

    def checkBox_changed(self, id, state):
        print(f"checkBox {id} state changed to {state}")
        if id == "base":
            self.cb_base_clicked()
        self.plot()

    def cb_calendrier_stateChanged(self, state):
        print("calendrier on=", state)
        if self.cb_calendrier.isChecked() == True:
            self.dt_deb.setCalendarPopup(True)
            self.dt_fin.setCalendarPopup(True)
        else:
            self.dt_deb.setCalendarPopup(False)
            self.dt_fin.setCalendarPopup(False)

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

    def actionBase_triggered(self):
        print("actionBase triggered")
        baseDialog = BaseDialog()
        result = baseDialog.exec()
        if result == QtWidgets.QDialog.DialogCode.Accepted:
            print("okok")


    def cb_base_clicked(self):
        print("cb_base_StateChanged", self.cb_base.isChecked())
        if self.cb_base.isChecked() == True:
            self.cb_ph1.setCheckState(QtCore.Qt.CheckState.Checked)
            self.cb_ph2.setCheckState(QtCore.Qt.CheckState.Checked)
            self.cb_ph3.setCheckState(QtCore.Qt.CheckState.Checked)
            self.cb_pa.setCheckState(QtCore.Qt.CheckState.Checked)
        else:
            self.cb_ph1.setCheckState(QtCore.Qt.CheckState.Unchecked)
            self.cb_ph2.setCheckState(QtCore.Qt.CheckState.Unchecked)
            self.cb_ph3.setCheckState(QtCore.Qt.CheckState.Unchecked)
            self.cb_pa.setCheckState(QtCore.Qt.CheckState.Unchecked)


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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    win = MainWindow()
    #win.resize(50, 50)
    win.show()
    sys.exit(app.exec())
