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
    QFrame, QGridLayout, QGroupBox, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QTextEdit,
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
        self.layoutWidget.setGeometry(QRect(-2, 32, 232, 367))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(11, 0, 0, 0)
        self.lab_base_courante = QLabel(self.layoutWidget)
        self.lab_base_courante.setObjectName(u"lab_base_courante")
        sizePolicy.setHeightForWidth(self.lab_base_courante.sizePolicy().hasHeightForWidth())
        self.lab_base_courante.setSizePolicy(sizePolicy)
        self.lab_base_courante.setMinimumSize(QSize(190, 29))
        self.lab_base_courante.setMaximumSize(QSize(190, 30))
        font = QFont()
        font.setBold(True)
        self.lab_base_courante.setFont(font)

        self.verticalLayout.addWidget(self.lab_base_courante)

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
        self.label = QLabel(self.gb_splitBase)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(17, 33, 81, 16))
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.lab_firstRec = QLabel(self.gb_splitBase)
        self.lab_firstRec.setObjectName(u"lab_firstRec")
        self.lab_firstRec.setGeometry(QRect(145, 33, 90, 21))
        sizePolicy.setHeightForWidth(self.lab_firstRec.sizePolicy().hasHeightForWidth())
        self.lab_firstRec.setSizePolicy(sizePolicy)
        self.lab_firstRec.setMinimumSize(QSize(90, 21))
        self.lab_firstRec.setMaximumSize(QSize(90, 21))
        self.label_2 = QLabel(self.gb_splitBase)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(427, 33, 78, 16))
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.lab_lastRec = QLabel(self.gb_splitBase)
        self.lab_lastRec.setObjectName(u"lab_lastRec")
        self.lab_lastRec.setGeometry(QRect(521, 33, 90, 21))
        self.lab_lastRec.setMinimumSize(QSize(90, 21))
        self.lab_lastRec.setMaximumSize(QSize(90, 21))
        self.label_3 = QLabel(self.gb_splitBase)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(17, 60, 95, 16))
        self.dt_firstRecord = QDateEdit(self.gb_splitBase)
        self.dt_firstRecord.setObjectName(u"dt_firstRecord")
        self.dt_firstRecord.setGeometry(QRect(145, 60, 94, 20))
        sizePolicy.setHeightForWidth(self.dt_firstRecord.sizePolicy().hasHeightForWidth())
        self.dt_firstRecord.setSizePolicy(sizePolicy)
        self.dt_firstRecord.setMinimumSize(QSize(90, 0))
        self.label_4 = QLabel(self.gb_splitBase)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(427, 60, 82, 16))
        self.dt_lastRecord = QDateEdit(self.gb_splitBase)
        self.dt_lastRecord.setObjectName(u"dt_lastRecord")
        self.dt_lastRecord.setGeometry(QRect(521, 60, 94, 20))
        sizePolicy.setHeightForWidth(self.dt_lastRecord.sizePolicy().hasHeightForWidth())
        self.dt_lastRecord.setSizePolicy(sizePolicy)
        self.dt_lastRecord.setMinimumSize(QSize(90, 0))
        self.cb_autoriseSplit = QCheckBox(self.gb_splitBase)
        self.cb_autoriseSplit.setObjectName(u"cb_autoriseSplit")
        self.cb_autoriseSplit.setGeometry(QRect(15, 97, 106, 20))
        self.cb_autoriseSplit.setMaximumSize(QSize(16777215, 30))
        self.btn_splitBase = QPushButton(self.gb_splitBase)
        self.btn_splitBase.setObjectName(u"btn_splitBase")
        self.btn_splitBase.setEnabled(False)
        self.btn_splitBase.setGeometry(QRect(427, 96, 183, 27))
        sizePolicy.setHeightForWidth(self.btn_splitBase.sizePolicy().hasHeightForWidth())
        self.btn_splitBase.setSizePolicy(sizePolicy)
        self.btn_splitBase.setMinimumSize(QSize(183, 0))
        self.btn_splitBase.setMaximumSize(QSize(16777215, 30))
        self.lineH = QFrame(self.gb_splitBase)
        self.lineH.setObjectName(u"lineH")
        self.lineH.setGeometry(QRect(138, 86, 479, 3))
        sizePolicy.setHeightForWidth(self.lineH.sizePolicy().hasHeightForWidth())
        self.lineH.setSizePolicy(sizePolicy)
        self.lineH.setMinimumSize(QSize(478, 0))
        self.lineH.setBaseSize(QSize(0, 0))
        self.lineH.setStyleSheet(u"background-color: rgb(0, 0, 255);")
        self.lineH.setLineWidth(3)
        self.lineH.setFrameShape(QFrame.Shape.HLine)
        self.lineH.setFrameShadow(QFrame.Shadow.Sunken)
        self.lineV1 = QFrame(self.gb_splitBase)
        self.lineV1.setObjectName(u"lineV1")
        self.lineV1.setGeometry(QRect(138, 57, 3, 30))
        sizePolicy.setHeightForWidth(self.lineV1.sizePolicy().hasHeightForWidth())
        self.lineV1.setSizePolicy(sizePolicy)
        self.lineV1.setMinimumSize(QSize(0, 30))
        self.lineV1.setStyleSheet(u"background-color: rgb(0, 0, 255);")
        self.lineV1.setLineWidth(3)
        self.lineV1.setFrameShape(QFrame.Shape.VLine)
        self.lineV1.setFrameShadow(QFrame.Shadow.Sunken)
        self.lineV2 = QFrame(self.gb_splitBase)
        self.lineV2.setObjectName(u"lineV2")
        self.lineV2.setGeometry(QRect(616, 58, 3, 30))
        self.lineV2.setMinimumSize(QSize(0, 30))
        self.lineV2.setStyleSheet(u"background-color: rgb(0, 0, 255);")
        self.lineV2.setLineWidth(3)
        self.lineV2.setFrameShape(QFrame.Shape.VLine)
        self.lineV2.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_5 = QLabel(self.gb_splitBase)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(294, 71, 95, 16))
        font1 = QFont()
        font1.setPointSize(11)
        self.label_5.setFont(font1)
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
        self.gb_baseCourante.setTitle(QCoreApplication.translate("Dialog", u"Base Courante:", None))
        self.lab_base_courante.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.btn_infosBase.setText(QCoreApplication.translate("Dialog", u"Infos Base", None))
        self.btn_optimiseBase.setText(QCoreApplication.translate("Dialog", u"Optimise", None))
        self.btn_base_OK.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.gb_splitBase.setTitle(QCoreApplication.translate("Dialog", u"Split Base", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Date 1er Rec:", None))
        self.lab_firstRec.setText(QCoreApplication.translate("Dialog", u"YYYY-MM-DD", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Date fin Rec:", None))
        self.lab_lastRec.setText(QCoreApplication.translate("Dialog", u"YYYY-MM-DD", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("Dialog", u"date non incluse dans la suppression", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Supprime <:", None))
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip(QCoreApplication.translate("Dialog", u"date non incluse dans la suppression", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Supprime >:", None))
        self.cb_autoriseSplit.setText(QCoreApplication.translate("Dialog", u"Autorise Split", None))
        self.btn_splitBase.setText(QCoreApplication.translate("Dialog", u"Split Base", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Portion incluse", None))
        self.gb_bases.setTitle(QCoreApplication.translate("Dialog", u"Bases:", None))
        self.btn_loadBase.setText(QCoreApplication.translate("Dialog", u"Charge autre base", None))
        self.btn_kill_base.setText(QCoreApplication.translate("Dialog", u"Supprime", None))
    # retranslateUi

