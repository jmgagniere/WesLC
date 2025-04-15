# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_baseDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateEdit, QDialog,
    QGridLayout, QGroupBox, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTextEdit,
    QTreeView, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(950, 440)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(950, 440))
        Dialog.setMaximumSize(QSize(950, 440))
        self.gb_baseCourante = QGroupBox(Dialog)
        self.gb_baseCourante.setObjectName(u"gb_baseCourante")
        self.gb_baseCourante.setGeometry(QRect(692, 14, 240, 407))
        sizePolicy.setHeightForWidth(self.gb_baseCourante.sizePolicy().hasHeightForWidth())
        self.gb_baseCourante.setSizePolicy(sizePolicy)
        self.gb_baseCourante.setFlat(False)
        self.layoutWidget = QWidget(self.gb_baseCourante)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(-2, 32, 232, 359))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(11, 0, 0, 0)
        self.btn_infosBase = QPushButton(self.layoutWidget)
        self.btn_infosBase.setObjectName(u"btn_infosBase")
        sizePolicy.setHeightForWidth(self.btn_infosBase.sizePolicy().hasHeightForWidth())
        self.btn_infosBase.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.btn_infosBase)

        self.btn_optimiseBase = QPushButton(self.layoutWidget)
        self.btn_optimiseBase.setObjectName(u"btn_optimiseBase")
        sizePolicy.setHeightForWidth(self.btn_optimiseBase.sizePolicy().hasHeightForWidth())
        self.btn_optimiseBase.setSizePolicy(sizePolicy)
        self.btn_optimiseBase.setMinimumSize(QSize(93, 0))

        self.verticalLayout.addWidget(self.btn_optimiseBase)

        self.te_infosBase = QTextEdit(self.layoutWidget)
        self.te_infosBase.setObjectName(u"te_infosBase")
        sizePolicy.setHeightForWidth(self.te_infosBase.sizePolicy().hasHeightForWidth())
        self.te_infosBase.setSizePolicy(sizePolicy)
        self.te_infosBase.setMinimumSize(QSize(220, 200))
        self.te_infosBase.setMaximumSize(QSize(220, 200))

        self.verticalLayout.addWidget(self.te_infosBase)

        self.btn_base_OK = QPushButton(self.layoutWidget)
        self.btn_base_OK.setObjectName(u"btn_base_OK")
        sizePolicy.setHeightForWidth(self.btn_base_OK.sizePolicy().hasHeightForWidth())
        self.btn_base_OK.setSizePolicy(sizePolicy)
        self.btn_base_OK.setMinimumSize(QSize(93, 32))

        self.verticalLayout.addWidget(self.btn_base_OK)

        self.gb_splitBase = QGroupBox(Dialog)
        self.gb_splitBase.setObjectName(u"gb_splitBase")
        self.gb_splitBase.setGeometry(QRect(16, 10, 649, 131))
        sizePolicy.setHeightForWidth(self.gb_splitBase.sizePolicy().hasHeightForWidth())
        self.gb_splitBase.setSizePolicy(sizePolicy)
        self.gb_splitBase.setMinimumSize(QSize(350, 120))
        self.gb_splitBase.setFlat(False)
        self.gridLayout_2 = QGridLayout(self.gb_splitBase)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.gb_splitBase)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.lab_firstRec = QLabel(self.gb_splitBase)
        self.lab_firstRec.setObjectName(u"lab_firstRec")
        sizePolicy.setHeightForWidth(self.lab_firstRec.sizePolicy().hasHeightForWidth())
        self.lab_firstRec.setSizePolicy(sizePolicy)
        self.lab_firstRec.setMinimumSize(QSize(90, 21))
        self.lab_firstRec.setMaximumSize(QSize(90, 21))

        self.gridLayout_2.addWidget(self.lab_firstRec, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(164, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.label_2 = QLabel(self.gb_splitBase)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.label_2, 0, 3, 1, 1)

        self.lab_lastRec = QLabel(self.gb_splitBase)
        self.lab_lastRec.setObjectName(u"lab_lastRec")
        self.lab_lastRec.setMinimumSize(QSize(90, 21))
        self.lab_lastRec.setMaximumSize(QSize(90, 21))

        self.gridLayout_2.addWidget(self.lab_lastRec, 0, 4, 1, 1)

        self.label_3 = QLabel(self.gb_splitBase)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.dt_firstRecord = QDateEdit(self.gb_splitBase)
        self.dt_firstRecord.setObjectName(u"dt_firstRecord")
        sizePolicy.setHeightForWidth(self.dt_firstRecord.sizePolicy().hasHeightForWidth())
        self.dt_firstRecord.setSizePolicy(sizePolicy)
        self.dt_firstRecord.setMinimumSize(QSize(90, 0))

        self.gridLayout_2.addWidget(self.dt_firstRecord, 1, 1, 1, 1)

        self.label_4 = QLabel(self.gb_splitBase)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 1, 3, 1, 1)

        self.dt_lastRecord = QDateEdit(self.gb_splitBase)
        self.dt_lastRecord.setObjectName(u"dt_lastRecord")
        sizePolicy.setHeightForWidth(self.dt_lastRecord.sizePolicy().hasHeightForWidth())
        self.dt_lastRecord.setSizePolicy(sizePolicy)
        self.dt_lastRecord.setMinimumSize(QSize(90, 0))

        self.gridLayout_2.addWidget(self.dt_lastRecord, 1, 4, 1, 1)

        self.cb_autoriseSplit = QCheckBox(self.gb_splitBase)
        self.cb_autoriseSplit.setObjectName(u"cb_autoriseSplit")
        self.cb_autoriseSplit.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_2.addWidget(self.cb_autoriseSplit, 2, 0, 1, 1)

        self.btn_splitBase = QPushButton(self.gb_splitBase)
        self.btn_splitBase.setObjectName(u"btn_splitBase")
        self.btn_splitBase.setEnabled(False)
        sizePolicy.setHeightForWidth(self.btn_splitBase.sizePolicy().hasHeightForWidth())
        self.btn_splitBase.setSizePolicy(sizePolicy)
        self.btn_splitBase.setMinimumSize(QSize(183, 0))
        self.btn_splitBase.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_2.addWidget(self.btn_splitBase, 2, 3, 1, 2)

        self.gb_bases = QGroupBox(Dialog)
        self.gb_bases.setObjectName(u"gb_bases")
        self.gb_bases.setGeometry(QRect(16, 154, 649, 271))
        self.gridLayout = QGridLayout(self.gb_bases)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_loadBase = QPushButton(self.gb_bases)
        self.btn_loadBase.setObjectName(u"btn_loadBase")
        sizePolicy.setHeightForWidth(self.btn_loadBase.sizePolicy().hasHeightForWidth())
        self.btn_loadBase.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_loadBase, 0, 0, 1, 1)

        self.tree_view = QTreeView(self.gb_bases)
        self.tree_view.setObjectName(u"tree_view")
        sizePolicy.setHeightForWidth(self.tree_view.sizePolicy().hasHeightForWidth())
        self.tree_view.setSizePolicy(sizePolicy)
        self.tree_view.setMinimumSize(QSize(600, 0))

        self.gridLayout.addWidget(self.tree_view, 1, 0, 1, 3)

        self.btn_kill_base = QPushButton(self.gb_bases)
        self.btn_kill_base.setObjectName(u"btn_kill_base")
        sizePolicy.setHeightForWidth(self.btn_kill_base.sizePolicy().hasHeightForWidth())
        self.btn_kill_base.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_kill_base, 0, 1, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.gb_baseCourante.setTitle(QCoreApplication.translate("Dialog", u"Base Courante", None))
        self.btn_infosBase.setText(QCoreApplication.translate("Dialog", u"Infos Base", None))
        self.btn_optimiseBase.setText(QCoreApplication.translate("Dialog", u"Optimise", None))
        self.btn_base_OK.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.gb_splitBase.setTitle(QCoreApplication.translate("Dialog", u"Split Base", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Date 1er Rec:", None))
        self.lab_firstRec.setText(QCoreApplication.translate("Dialog", u"YYYY-MM-DD", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Date fin Rec:", None))
        self.lab_lastRec.setText(QCoreApplication.translate("Dialog", u"YYYY-MM-DD", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Split avant:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Split apr\u00e8s", None))
        self.cb_autoriseSplit.setText(QCoreApplication.translate("Dialog", u"Autorise Split", None))
        self.btn_splitBase.setText(QCoreApplication.translate("Dialog", u"Split Base", None))
        self.gb_bases.setTitle(QCoreApplication.translate("Dialog", u"Bases:", None))
        self.btn_loadBase.setText(QCoreApplication.translate("Dialog", u"Charge autre base", None))
        self.btn_kill_base.setText(QCoreApplication.translate("Dialog", u"Supprime", None))
    # retranslateUi

