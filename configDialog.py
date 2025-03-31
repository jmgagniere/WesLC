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
