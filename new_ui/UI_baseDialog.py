# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_baseDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateEdit, QDialog,
    QGridLayout, QGroupBox, QHeaderView, QLabel,
    QLayout, QPushButton, QSizePolicy, QTextEdit,
    QTreeView, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1046, 445)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(650, 440))
        Dialog.setMaximumSize(QSize(1500, 800))
        self.gb_baseCourante = QGroupBox(Dialog)
        self.gb_baseCourante.setObjectName(u"gb_baseCourante")
        self.gb_baseCourante.setGeometry(QRect(790, 12, 364, 411))
        self.gb_baseCourante.setFlat(False)
        self.layoutWidget = QWidget(self.gb_baseCourante)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(-2, 32, 232, 384))
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
        self.te_infosBase.setMinimumSize(QSize(220, 226))
        self.te_infosBase.setMaximumSize(QSize(220, 220))

        self.verticalLayout.addWidget(self.te_infosBase)

        self.btn_base_OK = QPushButton(self.layoutWidget)
        self.btn_base_OK.setObjectName(u"btn_base_OK")
        sizePolicy.setHeightForWidth(self.btn_base_OK.sizePolicy().hasHeightForWidth())
        self.btn_base_OK.setSizePolicy(sizePolicy)
        self.btn_base_OK.setMinimumSize(QSize(93, 32))

        self.verticalLayout.addWidget(self.btn_base_OK)

        self.gb_splitBase = QGroupBox(Dialog)
        self.gb_splitBase.setObjectName(u"gb_splitBase")
        self.gb_splitBase.setGeometry(QRect(24, 18, 744, 411))
        self.gb_splitBase.setMinimumSize(QSize(350, 120))
        self.gb_splitBase.setFlat(False)
        self.layoutWidget_2 = QWidget(self.gb_splitBase)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(0, 28, 349, 95))
        self.gridLayout_2 = QGridLayout(self.layoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget_2)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.layoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 0, 1, 1, 2)

        self.label_2 = QLabel(self.layoutWidget_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 3, 1, 1)

        self.dt_firstRecord = QDateEdit(self.layoutWidget_2)
        self.dt_firstRecord.setObjectName(u"dt_firstRecord")
        self.dt_firstRecord.setMinimumSize(QSize(106, 0))

        self.gridLayout_2.addWidget(self.dt_firstRecord, 1, 0, 1, 1)

        self.dt_splitRecord = QDateEdit(self.layoutWidget_2)
        self.dt_splitRecord.setObjectName(u"dt_splitRecord")
        self.dt_splitRecord.setMinimumSize(QSize(106, 0))
        self.dt_splitRecord.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.dt_splitRecord, 1, 1, 1, 2)

        self.dt_lastRecord = QDateEdit(self.layoutWidget_2)
        self.dt_lastRecord.setObjectName(u"dt_lastRecord")
        self.dt_lastRecord.setMinimumSize(QSize(106, 0))

        self.gridLayout_2.addWidget(self.dt_lastRecord, 1, 3, 1, 1)

        self.cb_autoriseSplit = QCheckBox(self.layoutWidget_2)
        self.cb_autoriseSplit.setObjectName(u"cb_autoriseSplit")

        self.gridLayout_2.addWidget(self.cb_autoriseSplit, 2, 0, 1, 2)

        self.btn_splitBase = QPushButton(self.layoutWidget_2)
        self.btn_splitBase.setObjectName(u"btn_splitBase")
        self.btn_splitBase.setEnabled(False)

        self.gridLayout_2.addWidget(self.btn_splitBase, 2, 2, 1, 2)

        self.btn_loadBase = QPushButton(self.gb_splitBase)
        self.btn_loadBase.setObjectName(u"btn_loadBase")
        self.btn_loadBase.setGeometry(QRect(20, 132, 141, 32))
        sizePolicy.setHeightForWidth(self.btn_loadBase.sizePolicy().hasHeightForWidth())
        self.btn_loadBase.setSizePolicy(sizePolicy)
        self.tree_view = QTreeView(self.gb_splitBase)
        self.tree_view.setObjectName(u"tree_view")
        self.tree_view.setGeometry(QRect(20, 168, 687, 213))

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
        self.label.setText(QCoreApplication.translate("Dialog", u"Date 1er Rec", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Date Split Rec", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Date fin Rec", None))
        self.cb_autoriseSplit.setText(QCoreApplication.translate("Dialog", u"Autorise Split", None))
        self.btn_splitBase.setText(QCoreApplication.translate("Dialog", u"Split Base", None))
        self.btn_loadBase.setText(QCoreApplication.translate("Dialog", u"Charge autre base", None))
    # retranslateUi

