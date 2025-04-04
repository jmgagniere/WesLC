# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_configDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGridLayout,
    QGroupBox, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(673, 384)
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.le_1w3 = QLineEdit(self.groupBox)
        self.le_1w3.setObjectName(u"le_1w3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_1w3.sizePolicy().hasHeightForWidth())
        self.le_1w3.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.le_1w3, 2, 1, 1, 1)

        self.cb_1w1 = QCheckBox(self.groupBox)
        self.cb_1w1.setObjectName(u"cb_1w1")

        self.gridLayout.addWidget(self.cb_1w1, 0, 0, 1, 1)

        self.spBox_1w3 = QSpinBox(self.groupBox)
        self.spBox_1w3.setObjectName(u"spBox_1w3")

        self.gridLayout.addWidget(self.spBox_1w3, 2, 3, 1, 1)

        self.cb_pince1 = QCheckBox(self.groupBox)
        self.cb_pince1.setObjectName(u"cb_pince1")

        self.gridLayout.addWidget(self.cb_pince1, 4, 0, 1, 1)

        self.cb_ph1 = QCheckBox(self.groupBox)
        self.cb_ph1.setObjectName(u"cb_ph1")

        self.gridLayout.addWidget(self.cb_ph1, 0, 8, 1, 1)

        self.cb_base = QCheckBox(self.groupBox)
        self.cb_base.setObjectName(u"cb_base")

        self.gridLayout.addWidget(self.cb_base, 0, 6, 1, 1)

        self.spBox_pince1 = QSpinBox(self.groupBox)
        self.spBox_pince1.setObjectName(u"spBox_pince1")

        self.gridLayout.addWidget(self.spBox_pince1, 4, 3, 1, 1)

        self.cb_1w3 = QCheckBox(self.groupBox)
        self.cb_1w3.setObjectName(u"cb_1w3")

        self.gridLayout.addWidget(self.cb_1w3, 2, 0, 1, 1)

        self.spBox_1w2 = QSpinBox(self.groupBox)
        self.spBox_1w2.setObjectName(u"spBox_1w2")

        self.gridLayout.addWidget(self.spBox_1w2, 1, 3, 1, 1)

        self.b_c1w3 = QPushButton(self.groupBox)
        self.b_c1w3.setObjectName(u"b_c1w3")

        self.gridLayout.addWidget(self.b_c1w3, 2, 2, 1, 1)

        self.cb_ph3 = QCheckBox(self.groupBox)
        self.cb_ph3.setObjectName(u"cb_ph3")

        self.gridLayout.addWidget(self.cb_ph3, 2, 8, 1, 1)

        self.b_cph2 = QPushButton(self.groupBox)
        self.b_cph2.setObjectName(u"b_cph2")

        self.gridLayout.addWidget(self.b_cph2, 1, 9, 1, 1)

        self.cb_pulse1 = QCheckBox(self.groupBox)
        self.cb_pulse1.setObjectName(u"cb_pulse1")

        self.gridLayout.addWidget(self.cb_pulse1, 3, 0, 1, 1)

        self.b_cph3 = QPushButton(self.groupBox)
        self.b_cph3.setObjectName(u"b_cph3")

        self.gridLayout.addWidget(self.b_cph3, 2, 9, 1, 1)

        self.le_1w1 = QLineEdit(self.groupBox)
        self.le_1w1.setObjectName(u"le_1w1")
        sizePolicy.setHeightForWidth(self.le_1w1.sizePolicy().hasHeightForWidth())
        self.le_1w1.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.le_1w1, 0, 1, 1, 1)

        self.b_cph1 = QPushButton(self.groupBox)
        self.b_cph1.setObjectName(u"b_cph1")

        self.gridLayout.addWidget(self.b_cph1, 0, 9, 1, 1)

        self.cb_ph2 = QCheckBox(self.groupBox)
        self.cb_ph2.setObjectName(u"cb_ph2")

        self.gridLayout.addWidget(self.cb_ph2, 1, 8, 1, 1)

        self.b_c1w2 = QPushButton(self.groupBox)
        self.b_c1w2.setObjectName(u"b_c1w2")

        self.gridLayout.addWidget(self.b_c1w2, 1, 2, 1, 1)

        self.spBox_pa = QSpinBox(self.groupBox)
        self.spBox_pa.setObjectName(u"spBox_pa")

        self.gridLayout.addWidget(self.spBox_pa, 3, 10, 1, 1)

        self.le_1w2 = QLineEdit(self.groupBox)
        self.le_1w2.setObjectName(u"le_1w2")
        sizePolicy.setHeightForWidth(self.le_1w2.sizePolicy().hasHeightForWidth())
        self.le_1w2.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.le_1w2, 1, 1, 1, 1)

        self.le_pulse1 = QLineEdit(self.groupBox)
        self.le_pulse1.setObjectName(u"le_pulse1")
        sizePolicy.setHeightForWidth(self.le_pulse1.sizePolicy().hasHeightForWidth())
        self.le_pulse1.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.le_pulse1, 3, 1, 1, 1)

        self.spBox_pince2 = QSpinBox(self.groupBox)
        self.spBox_pince2.setObjectName(u"spBox_pince2")

        self.gridLayout.addWidget(self.spBox_pince2, 5, 3, 1, 1)

        self.b_c1w1 = QPushButton(self.groupBox)
        self.b_c1w1.setObjectName(u"b_c1w1")

        self.gridLayout.addWidget(self.b_c1w1, 0, 2, 1, 1)

        self.b_cpa = QPushButton(self.groupBox)
        self.b_cpa.setObjectName(u"b_cpa")

        self.gridLayout.addWidget(self.b_cpa, 3, 9, 1, 1)

        self.b_cpince1 = QPushButton(self.groupBox)
        self.b_cpince1.setObjectName(u"b_cpince1")

        self.gridLayout.addWidget(self.b_cpince1, 4, 2, 1, 1)

        self.cb_pa = QCheckBox(self.groupBox)
        self.cb_pa.setObjectName(u"cb_pa")

        self.gridLayout.addWidget(self.cb_pa, 3, 8, 1, 1)

        self.le_pince1 = QLineEdit(self.groupBox)
        self.le_pince1.setObjectName(u"le_pince1")
        sizePolicy.setHeightForWidth(self.le_pince1.sizePolicy().hasHeightForWidth())
        self.le_pince1.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.le_pince1, 4, 1, 1, 1)

        self.spBox_ph3 = QSpinBox(self.groupBox)
        self.spBox_ph3.setObjectName(u"spBox_ph3")

        self.gridLayout.addWidget(self.spBox_ph3, 2, 10, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 5, 1, 1)

        self.b_cpince2 = QPushButton(self.groupBox)
        self.b_cpince2.setObjectName(u"b_cpince2")

        self.gridLayout.addWidget(self.b_cpince2, 5, 2, 1, 1)

        self.spBox_ph1 = QSpinBox(self.groupBox)
        self.spBox_ph1.setObjectName(u"spBox_ph1")

        self.gridLayout.addWidget(self.spBox_ph1, 0, 10, 1, 1)

        self.cb_1w2 = QCheckBox(self.groupBox)
        self.cb_1w2.setObjectName(u"cb_1w2")

        self.gridLayout.addWidget(self.cb_1w2, 1, 0, 1, 1)

        self.b_cpulse1 = QPushButton(self.groupBox)
        self.b_cpulse1.setObjectName(u"b_cpulse1")

        self.gridLayout.addWidget(self.b_cpulse1, 3, 2, 1, 1)

        self.cb_pince2 = QCheckBox(self.groupBox)
        self.cb_pince2.setObjectName(u"cb_pince2")

        self.gridLayout.addWidget(self.cb_pince2, 5, 0, 1, 1)

        self.spBox_1w1 = QSpinBox(self.groupBox)
        self.spBox_1w1.setObjectName(u"spBox_1w1")

        self.gridLayout.addWidget(self.spBox_1w1, 0, 3, 1, 1)

        self.spBox_ph2 = QSpinBox(self.groupBox)
        self.spBox_ph2.setObjectName(u"spBox_ph2")

        self.gridLayout.addWidget(self.spBox_ph2, 1, 10, 1, 1)

        self.le_pince2 = QLineEdit(self.groupBox)
        self.le_pince2.setObjectName(u"le_pince2")
        sizePolicy.setHeightForWidth(self.le_pince2.sizePolicy().hasHeightForWidth())
        self.le_pince2.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.le_pince2, 5, 1, 1, 1)

        self.spBox_pulse1 = QSpinBox(self.groupBox)
        self.spBox_pulse1.setObjectName(u"spBox_pulse1")

        self.gridLayout.addWidget(self.spBox_pulse1, 3, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 7, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 3)

        self.horizontalSpacer = QSpacerItem(417, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.btn_abandon = QPushButton(Dialog)
        self.btn_abandon.setObjectName(u"btn_abandon")

        self.gridLayout_2.addWidget(self.btn_abandon, 1, 1, 1, 1)

        self.btn_save = QPushButton(Dialog)
        self.btn_save.setObjectName(u"btn_save")

        self.gridLayout_2.addWidget(self.btn_save, 1, 2, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Param\u00e8tres Serveur Wes", None))
        self.cb_1w1.setText(QCoreApplication.translate("Dialog", u"1w1", None))
        self.cb_pince1.setText(QCoreApplication.translate("Dialog", u"pince1", None))
        self.cb_ph1.setText(QCoreApplication.translate("Dialog", u"ph1", None))
        self.cb_base.setText(QCoreApplication.translate("Dialog", u"T_Infos", None))
        self.cb_1w3.setText(QCoreApplication.translate("Dialog", u"1w3", None))
        self.b_c1w3.setText("")
        self.cb_ph3.setText(QCoreApplication.translate("Dialog", u"ph3", None))
        self.b_cph2.setText("")
        self.cb_pulse1.setText(QCoreApplication.translate("Dialog", u"pulse1", None))
        self.b_cph3.setText("")
        self.b_cph1.setText("")
        self.cb_ph2.setText(QCoreApplication.translate("Dialog", u"ph2", None))
        self.b_c1w2.setText("")
        self.b_c1w1.setText("")
        self.b_cpa.setText("")
        self.b_cpince1.setText("")
        self.cb_pa.setText(QCoreApplication.translate("Dialog", u"pa", None))
        self.b_cpince2.setText("")
        self.cb_1w2.setText(QCoreApplication.translate("Dialog", u"1w2", None))
        self.b_cpulse1.setText("")
        self.cb_pince2.setText(QCoreApplication.translate("Dialog", u"pince2", None))
        self.btn_abandon.setText(QCoreApplication.translate("Dialog", u"Abandonner", None))
        self.btn_save.setText(QCoreApplication.translate("Dialog", u"Enregistrer", None))
    # retranslateUi

