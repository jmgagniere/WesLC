from functools import partial

from PySide6 import QtWidgets, QtCore

from package.api.database import Database

class BlocWidget(QtWidgets.QWidget):
    def __init__(self, id="Id", cb_check=False, cb_label="name", color="#303030", width=0):
        super().__init__()

        self.cb_check = cb_check
        self.cb_label = cb_label
        self.id = id
        self.color = color
        self.width = width

        self.setup_ui()

    def setup_ui(self):
        self.create_widget()
        self.modify_widget()
        self.create_layout()
        self.add_widgets_to_layout()


    def create_widget(self):
        self.cb = QtWidgets.QCheckBox(self.cb_label)
        self.le = QtWidgets.QLineEdit(str(self.id))
        self.btn = QtWidgets.QPushButton()
        self.spin = QtWidgets.QSpinBox()

    def modify_widget(self):
        self.cb.setCheckState(QtCore.Qt.CheckState(self.cb_check))
        #self.le.setReadOnly(True)
        self.btn.setFixedHeight(16)
        self.spin.setRange(1, 5)

    def create_layout(self):
        self.layout = QtWidgets.QHBoxLayout()
        self.layout.setSpacing(0)
        self.setLayout(self.layout)

    def add_widgets_to_layout(self):
        self.layout.addWidget(self.cb)
        self.layout.addWidget(self.le)
        self.layout.addWidget(self.btn)
        self.layout.addWidget(self.spin)


class ConfigDialog(QtWidgets.QDialog):
    def __init__(self):
        super(ConfigDialog, self).__init__()
        self.setWindowTitle("Configuration")
        self.db = Database()

        self.create_layout()
        self.create_widget()
        self.modify_widget()
        self.add_widgets_to_layout()
        self.setup_connections()

    def create_widget(self):
        # - Récuperation des parametres en base
        bloc_param = self.db.get_plot_param()
        # query_string = "SELECT id, name, color, state, width FROM plot_param"
        bloc_position = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (0, 2), (1, 2), (2, 2), (3, 2), (0, 1)]

        self.blocs_data_dict = {}
        for i, blo in enumerate(bloc_param):
            bloc = BlocWidget(id=blo[0], cb_label=blo[0], color=blo[2], cb_check=blo[3],  width=blo[4])
            bloc.le.setText(blo[1])
            bloc.btn.setStyleSheet('QPushButton {background-color:' + blo[2] + '; border:  none}')
            bloc.spin.setValue(blo[4])
            # Add to Layout
            self.grid_layout.addWidget(bloc, bloc_position[i][0], bloc_position[i][1], 1, 1)
            # Signal
            bloc.cb.stateChanged.connect(partial(self.module_changed, bloc.id))
            bloc.btn.clicked.connect(partial(self.choix_couleur, bloc.id))

            self.blocs_data_dict[bloc.id] = bloc

        self.gb_param = QtWidgets.QGroupBox("Paramètres Serveur Wes")

        self.btn_abandon = QtWidgets.QPushButton("Abandonner")
        self.btn_save = QtWidgets.QPushButton("Enregistrer")

    def modify_widget(self):

        self.blocs_data_dict["base"].cb.setText("T_Infos")
        self.blocs_data_dict["base"].btn.setVisible(False)
        self.blocs_data_dict["base"].spin.setVisible(False)

        for key in ["ph1", "ph2", "ph3", "pa", "base"]:
            self.blocs_data_dict[key].le.setVisible(False)



    def create_layout(self):
        self.grid_layout = QtWidgets.QGridLayout()
        self.group_layout =QtWidgets.QGridLayout()


    def add_widgets_to_layout(self):
        self.gb_param.setLayout(self.grid_layout)
        self.group_layout.addWidget(self.gb_param, 0, 0, 1, 3)
        self.group_layout.addWidget(self.btn_abandon, 1, 1, 1, 1)
        self.group_layout.addWidget(self.btn_save, 1, 2, 1, 1)
        self.setLayout(self.group_layout)
        pass

    def setup_connections(self):
        self.btn_abandon.clicked.connect(self.btn_abandon_clicked)
        self.btn_save.clicked.connect(self.btn_save_clicked)

    def btn_abandon_clicked(self):
        print("btn_abandon clicked")
        self.hide()

    def btn_save_clicked(self):
        print("btn_save clicked")
        #cb_Check = []
        for key in self.blocs_data_dict:
            # CheckBoxes
            if str(self.blocs_data_dict[key].cb.checkState()) == 'CheckState.Checked':
                print(key," is checked" )
                self.blocs_data_dict[key].cb_check = 2
                #cb_Check.append(2)
            else:
                print(key, " is unchecked")
                self.blocs_data_dict[key].cb_check = 0
                #cb_Check.append(0)

            # LineEdits
            self.blocs_data_dict[key].cb_label = self.blocs_data_dict[key].le.text()

            # PushButton Color => traiter dans choix_couleur

            # SpinBoxes
            self.blocs_data_dict[key].width = self.blocs_data_dict[key].spin.value()

        self.db.save_plot_param(**self.blocs_data_dict)
        self.done(QtWidgets.QDialog.DialogCode.Accepted)

    def choix_couleur(self, id):
        print('Choix couleur pour ', id)
        couleur = QtWidgets.QColorDialog.getColor().name()
        print('couleur =', couleur)
        # Change la couleur du bouton
        self.blocs_data_dict[id].btn.setStyleSheet('QPushButton {background-color:' + couleur + '; border:  none}')
        self.blocs_data_dict[id].color = couleur




    def module_changed(self, id, state):
        print("Widget state changed", id, state)
        self.blocs_data_dict[id].cb_check = state

    def le_text_changed(self, id, text):
        print("text changed", id, text)




    """   self.db = Database()

        self.cb_list = [self.ui.cb_1w1, self.ui.cb_1w2, self.ui.cb_1w3,
                                self.ui.cb_pulse1,
                                self.ui.cb_pince1, self.ui.cb_pince2,
                                self.ui.cb_ph1, self.ui.cb_ph2, self.ui.cb_ph3,
                                self.ui.cb_pa, self.ui.cb_base]

        self.b_color_list = [self.ui.b_c1w1, self.ui.b_c1w2, self.ui.b_c1w3,
                             self.ui.b_pulse1,
                             self.ui.b_cpince1, self.ui.b_cpince2,
                             self.ui.b_cph1, self.ui.b_cph2, self.ui.b_cph3, self.ui.b_cpa]

        self.options_list = ['1w1', 'col_1w1', '1w2', 'col_1w2', '1w3', 'col_1w3', '1w4', 'col_1w4',
                             '1w5', 'col_1w5', '1w6', 'col_1w6',
                             'pulse1', 'col_pulse1', 'pulse2', 'col_pulse2', 'pulse3', 'col_pulse3', 'pulse4',
                             'col_pulse4',
                             'pince 1', 'col_pince 1', 'pince 2', 'col_pince 2', 'pince 3', 'col_pince 3', 'pince 4',
                             'col_pince 4',
                             'base', 'col_base', 'ph1', 'col_ph1', 'ph2', 'col_ph2', 'ph3', 'col_ph3', 'pa', 'col_pa']

        self.le_list = [self.ui.le_1w1, self.ui.le_1w2, self.ui.le_1w3,
                        self.ui.le_pulse1,
                        self.ui.le_pince1, self.ui.le_pince2]

        self.read_conf_from_base()
        self.updateUI()


        self.ui.b_cancel.clicked.connect(self.b_cancel_clicked)
        self.ui.b_save.clicked.connect(self.b_save_clicked)
        self.ui.b_c1w1.clicked.connect(lambda state, x=0: self.choix_couleur(x))
        self.ui.b_c1w2.clicked.connect(lambda state, x=1: self.choix_couleur(x))
        self.ui.b_c1w3.clicked.connect(lambda state, x=2: self.choix_couleur(x))
        self.ui.b_pulse1.clicked.connect(lambda state, x=3: self.choix_couleur(x))
        self.ui.b_cpince1.clicked.connect(lambda state, x=4: self.choix_couleur(x))
        self.ui.b_cpince2.clicked.connect(lambda state, x=5: self.choix_couleur(x))
        self.ui.b_cph1.clicked.connect(lambda state, x=6: self.choix_couleur(x))
        self.ui.b_cph2.clicked.connect(lambda state, x=7: self.choix_couleur(x))
        self.ui.b_cph3.clicked.connect(lambda state, x=8: self.choix_couleur(x))
        self.ui.b_cpa.clicked.connect(lambda state, x=9: self.choix_couleur(x))

    def b_cancel_clicked(self):
        self.hide()

    def b_save_clicked(self):
        cb_Check = []
        for cb in self.cb_list:
            if str(cb.checkState()) == 'CheckState.Checked':
                cb_Check.append(1)
            else:
                cb_Check.append(0)

        print("cb_Check=",cb_Check)

        plot_param = PlotParam(d1_name = self.ui.le_1w1.text(),
                               d1_color = self.ui.b_c1w1.palette().button().color().name(),
                               d1_show = cb_Check[0],
                               d1_width = int(self.ui.spBox_1w1.text()),
                               d2_name = self.ui.le_1w2.text(),
                               d2_color = self.ui.b_c1w2.palette().button().color().name(),
                               d2_show = cb_Check[1],
                               d2_width = int(self.ui.spBox_1w2.text()),
                               d3_name = self.ui.le_1w3.text(),
                               d3_color = self.ui.b_c1w3.palette().button().color().name(),
                               d3_show = cb_Check[2],
                               d3_width = int(self.ui.spBox_1w3.text()),
                               pulse1_name = self.ui.le_pulse1.text(),
                               pulse1_color = self.ui.b_pulse1.palette().button().color().name(),
                               pulse1_show = cb_Check[3],
                               pulse1_width = int(self.ui.spBox_pulse1.text()),
                               pince1_name = self.ui.le_pince1.text(),
                               pince1_color = self.ui.b_cpince1.palette().button().color().name(),
                               pince1_show = cb_Check[4],
                               pince1_width = int(self.ui.spBox_pince1.text()),
                               pince2_name = self.ui.le_pince2.text(),
                               pince2_color = self.ui.b_cpince2.palette().button().color().name(),
                               pince2_show = cb_Check[5],
                               pince2_width = int(self.ui.spBox_pince2.text()),
                               ph1_name = 'ph1',
                               ph1_color = self.ui.b_cph1.palette().button().color().name(),
                               ph1_show = cb_Check[6],
                               ph1_width = int(self.ui.spBox_ph1.text()),
                               ph2_name = 'ph2',
                               ph2_color = self.ui.b_cph2.palette().button().color().name(),
                               ph2_show = cb_Check[7],
                               ph2_width = int(self.ui.spBox_ph2.text()),
                               ph3_name = 'ph3',
                               ph3_color = self.ui.b_cph3.palette().button().color().name(),
                               ph3_show = cb_Check[8],
                               ph3_width = int(self.ui.spBox_ph3.text()),
                               pa_name = 'pa',
                               pa_color = self.ui.b_cpa.palette().button().color().name(),
                               pa_show = cb_Check[9],
                               pa_width = int(self.ui.spBox_pa.text()),
                               base_name = "base",
                               base_color = "#000000",
                               base_show = cb_Check[10],
                               base_width = 0)

        self.db.save_plot_param(plot_param)
        self.done(QtWidgets.QDialog.DialogCode.Accepted)

    def choix_couleur(self, num):
        print('Choix couleur pour ', num)
        couleur = QColorDialog.getColor().name()
        print('couleur =', couleur)
        # Change la couleur du bouton
        self.b_color_list[num].setStyleSheet('QPushButton {background-color:' + couleur + '; border:  none}')

    def read_conf_from_base(self):
        print("read_conf_from_base")
        self.plot_param = self.db.get_plot_param()
        #print("plot_param=", plot_param)

    def updateUI(self):
        self.ui.cb_1w1.setCheckState(self.setValue(self.plot_param.d1_show))
        self.ui.cb_1w2.setCheckState(self.setValue(self.plot_param.d2_show))
        self.ui.cb_1w3.setCheckState(self.setValue(self.plot_param.d3_show))
        self.ui.cb_1w2.setCheckState(self.setValue(self.plot_param.d2_show))
        self.ui.cb_pulse1.setCheckState(self.setValue(self.plot_param.pulse1_show))
        self.ui.cb_pince1.setCheckState(self.setValue(self.plot_param.pince1_show))
        self.ui.cb_pince2.setCheckState(self.setValue(self.plot_param.pince2_show))
        self.ui.cb_base.setCheckState(self.setValue(self.plot_param.base_show))
        self.ui.cb_ph1.setCheckState(self.setValue(self.plot_param.ph1_show))
        self.ui.cb_ph2.setCheckState(self.setValue(self.plot_param.ph2_show))
        self.ui.cb_ph3.setCheckState(self.setValue(self.plot_param.ph3_show))
        self.ui.cb_pa.setCheckState(self.setValue(self.plot_param.pa_show))

        self.ui.le_1w1.setText(self.plot_param.d1_name)
        self.ui.le_1w2.setText(self.plot_param.d2_name)
        self.ui.le_1w3.setText(self.plot_param.d3_name)
        self.ui.le_pulse1.setText(self.plot_param.pulse1_name)
        self.ui.le_pince1.setText(self.plot_param.pince1_name)
        self.ui.le_pince2.setText(self.plot_param.pince2_name)

        self.ui.b_c1w1.setStyleSheet('QPushButton {background-color:' + self.plot_param.d1_color + '; border:  none}')
        self.ui.b_c1w2.setStyleSheet('QPushButton {background-color:' + self.plot_param.d2_color + '; border:  none}')
        self.ui.b_c1w3.setStyleSheet('QPushButton {background-color:' + self.plot_param.d3_color + '; border:  none}')
        self.ui.b_pulse1.setStyleSheet('QPushButton {background-color:' + self.plot_param.pulse1_color + '; border:  none}')
        self.ui.b_cpince1.setStyleSheet('QPushButton {background-color:' + self.plot_param.pince1_color + '; border:  none}')
        self.ui.b_cpince2.setStyleSheet('QPushButton {background-color:' + self.plot_param.pince2_color + '; border:  none}')
        self.ui.b_cph1.setStyleSheet('QPushButton {background-color:' + self.plot_param.ph1_color + '; border:  none}')
        self.ui.b_cph2.setStyleSheet('QPushButton {background-color:' + self.plot_param.ph2_color + '; border:  none}')
        self.ui.b_cph3.setStyleSheet('QPushButton {background-color:' + self.plot_param.ph3_color + '; border:  none}')
        self.ui.b_cpa.setStyleSheet('QPushButton {background-color:' + self.plot_param.pa_color + '; border:  none}')

        self.ui.spBox_1w1.setValue(self.plot_param.d1_width)
        self.ui.spBox_1w2.setValue(self.plot_param.d2_width)
        self.ui.spBox_1w3.setValue(self.plot_param.d3_width)
        self.ui.spBox_pulse1.setValue(self.plot_param.pulse1_width)
        self.ui.spBox_pince1.setValue(self.plot_param.pince1_width)
        self.ui.spBox_pince2.setValue(self.plot_param.pince2_width)
        self.ui.spBox_ph1.setValue(self.plot_param.ph1_width)
        self.ui.spBox_ph2.setValue(self.plot_param.ph2_width)
        self.ui.spBox_ph3.setValue(self.plot_param.ph3_width)
        self.ui.spBox_pa.setValue(self.plot_param.pa_width)

    def setValue(self,vi):
        val = QtCore.Qt.CheckState.Checked if vi == 1 else QtCore.Qt.CheckState.Unchecked
        return val
        
        """

