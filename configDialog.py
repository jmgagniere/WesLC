from functools import partial
from PySide6 import QtWidgets, QtCore

from new_ui.UI_configDialog import Ui_Dialog
from package.api.database import Database

class ConfigDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super(ConfigDialog, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Configuration")

        #self.db = Database()
        self.init_widget()

        # Signaux
        self.btn_abandon.clicked.connect(self.btn_abandon_clicked)
        self.btn_save.clicked.connect(self.btn_save_clicked)

    def init_widget(self):
        # listes des widgets de l'interface graphique par catégories
        self.list_cb_widget = [self.cb_1w1, self.cb_1w2, self.cb_1w3, self.cb_pulse1, self.cb_pince1, self.cb_pince2,
                        self.cb_ph1, self.cb_ph2, self.cb_ph3, self.cb_pa, self.cb_base]

        self.list_le_widget = [self.le_1w1, self.le_1w2, self.le_1w3, self.le_pulse1, self.le_pince1, self.le_pince2]

        self.list_color_widget = [self.b_c1w1, self.b_c1w2, self.b_c1w3, self.b_cpulse1, self.b_cpince1, self.b_cpince2,
                           self.b_cph1, self.b_cph2, self.b_cph3, self.b_cpa]

        self.list_width_widget = [self.spBox_1w1, self.spBox_1w2, self.spBox_1w3,
                           self.spBox_pulse1, self.spBox_pince1, self.spBox_pince2,
                           self.spBox_ph1, self.spBox_ph2, self.spBox_ph3, self.spBox_pa]

        # - Récuperation des parametres en base
        self.bloc_param = Database.get_plot_param(self)
        #print("bloc_param", self.bloc_param)
        # query_string = "SELECT id, name, color, state, width FROM plot_param"
        # self.bloc_param est une liste de liste, chaque sous liste contient les 5 éléments issus de query_string
        # on va récuperer une liste  key_list qui servira de clés pour des dictionnaires
        # on récupere une liste qui servira de valeur pour les lineEdit
        # on récupere une liste qui servira de valeur pour les couleurs
        # on récuoere une liste qui servira de valeur pour l'etat des checkBox (O pas coché, 2 coché)
        # on récupère une liste qui servira de valeur pour le nombre de chiffre à afficher
        self.key_list = []
        le_val = []
        color_val = []
        cbox_val = []
        spbox_val = []
        for i, blo in enumerate(self.bloc_param):
            self.key_list.append(blo[0])
            le_val.append(blo[1])
            color_val.append(blo[2])
            cbox_val.append(blo[3])
            spbox_val.append(blo[4])

        """print("key_list", self.key_list)
        print("le_val", le_val)
        print("color_val", color_val)
        print("cbox_val", cbox_val)
        print("spbox_val", spbox_val)"""

        # creation des dictionnaires
        self.dict_cbox_val = dict(zip(self.key_list, cbox_val))
        self.dict_le_val = dict(zip(self.key_list, le_val))
        self.dict_color_val = dict(zip(self.key_list, color_val))
        self.dict_spbox_val = dict(zip(self.key_list, spbox_val))

        self.dict_cbox_widget = dict(zip(self.key_list, self.list_cb_widget))
        self.dict_le_widget = dict(zip(self.key_list, self.list_le_widget))
        self.dict_color_widget = dict(zip(self.key_list, self.list_color_widget))
        self.dict_spbox_widget = dict(zip(self.key_list, self.list_width_widget))

        # Mise à jour affichage des checkBox
        for key, val in self.dict_cbox_val.items():
            self.dict_cbox_widget[key].setCheckState(QtCore.Qt.CheckState(val))
        # Mise à jour affichage des lineEdit
        for key in self.dict_le_widget:
            self.dict_le_widget[key].setText(self.dict_le_val[key])
        # Mise à jour affichage des color
        for key in self.dict_color_widget:
            val = self.dict_color_val[key]
            self.dict_color_widget[key].setStyleSheet('QPushButton {background-color:' + val + '; border:  none}')
            # Signal
            self.dict_color_widget[key].clicked.connect(partial(self.choix_couleur, key))
        # Mise à jour affichage des spinBox
        for key in self.dict_spbox_widget:
            self.dict_spbox_widget[key].setValue(self.dict_spbox_val[key])

    def btn_abandon_clicked(self):
        print("btn_abandon clicked")
        self.hide()

    def btn_save_clicked(self):
        print("btn_save clicked")
        #cb_Check = []
        # Mise à jour de bloc_param
        #   checkBoxs
        for i, cb in enumerate(self.list_cb_widget):
            if str(self.list_cb_widget[i].checkState()) == 'CheckState.Checked':
                self.bloc_param[i][3] = 2
            else:
                self.bloc_param[i][3] = 0
        #   LineEdits
        for i, le in enumerate(self.list_le_widget):
            self.bloc_param[i][1] = self.list_le_widget[i].text()
        #   bouton colors
        for i, col in enumerate(self.list_color_widget):
            self.bloc_param[i][2] = self.list_color_widget[i].palette().button().color().name()
        #   spinBoxs
        for i, val in enumerate(self.list_width_widget):
            #print("i=", i, "val=",val)
            self.bloc_param[i][4] = val.value()

        #print("bloc_param_s", self.bloc_param)
        blocs_data = dict(zip(self.key_list, self.bloc_param))
        #print("blocs_data", blocs_data)

        Database.save_plot_param(self,**blocs_data)
        self.done(QtWidgets.QDialog.DialogCode.Accepted)

    def choix_couleur(self, key):
        print('Choix couleur pour ', key)
        couleur = QtWidgets.QColorDialog.getColor().name()
        print('couleur =', couleur)
        # Change la couleur du bouton
        #print("dict_color.get(id)", self.dict_color_widget[key])
        self.dict_color_widget[key].setStyleSheet('QPushButton {background-color:' + couleur + '; border:  none}')


    """def module_changed(self, id, state):
        print("Widget state changed", id, state)
        self.blocs_data_dict[id].cb_check = state

    def le_text_changed(self, id, text):
        print("text changed", id, text)"""
