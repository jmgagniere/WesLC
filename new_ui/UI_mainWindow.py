# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateTimeEdit, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QToolBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1128, 791)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionConfig_Legende = QAction(MainWindow)
        self.actionConfig_Legende.setObjectName(u"actionConfig_Legende")
        self.actionactionBase = QAction(MainWindow)
        self.actionactionBase.setObjectName(u"actionactionBase")
        self.actionactionBase.setMenuRole(QAction.MenuRole.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.main_gridLayout = QGridLayout()
        self.main_gridLayout.setObjectName(u"main_gridLayout")
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMinimumSize(QSize(120, 140))
        self.groupBox_3.setMaximumSize(QSize(120, 140))
        self.verticalLayout = QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_ftp = QPushButton(self.groupBox_3)
        self.btn_ftp.setObjectName(u"btn_ftp")

        self.verticalLayout.addWidget(self.btn_ftp)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btn_plot = QPushButton(self.groupBox_3)
        self.btn_plot.setObjectName(u"btn_plot")

        self.verticalLayout.addWidget(self.btn_plot)


        self.main_gridLayout.addWidget(self.groupBox_3, 0, 3, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QSize(750, 150))
        self.groupBox.setMaximumSize(QSize(750, 150))
        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 22, 761, 132))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.le_val_1w3 = QLineEdit(self.layoutWidget)
        self.le_val_1w3.setObjectName(u"le_val_1w3")
        self.le_val_1w3.setReadOnly(True)

        self.gridLayout.addWidget(self.le_val_1w3, 1, 5, 1, 1)

        self.le_val_pince2 = QLineEdit(self.layoutWidget)
        self.le_val_pince2.setObjectName(u"le_val_pince2")
        self.le_val_pince2.setReadOnly(True)

        self.gridLayout.addWidget(self.le_val_pince2, 3, 5, 1, 1)

        self.le_val_pulse1 = QLineEdit(self.layoutWidget)
        self.le_val_pulse1.setObjectName(u"le_val_pulse1")
        self.le_val_pulse1.setReadOnly(True)

        self.gridLayout.addWidget(self.le_val_pulse1, 3, 0, 1, 1)

        self.cb_pince1 = QCheckBox(self.layoutWidget)
        self.cb_pince1.setObjectName(u"cb_pince1")

        self.gridLayout.addWidget(self.cb_pince1, 2, 3, 1, 1)

        self.le_val_pince1 = QLineEdit(self.layoutWidget)
        self.le_val_pince1.setObjectName(u"le_val_pince1")
        self.le_val_pince1.setReadOnly(True)

        self.gridLayout.addWidget(self.le_val_pince1, 3, 3, 1, 1)

        self.le_pince1 = QLineEdit(self.layoutWidget)
        self.le_pince1.setObjectName(u"le_pince1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.le_pince1.sizePolicy().hasHeightForWidth())
        self.le_pince1.setSizePolicy(sizePolicy1)
        self.le_pince1.setMaximumSize(QSize(15, 15))
        self.le_pince1.setReadOnly(True)

        self.gridLayout.addWidget(self.le_pince1, 3, 4, 1, 1)

        self.le_ph3 = QLineEdit(self.layoutWidget)
        self.le_ph3.setObjectName(u"le_ph3")
        sizePolicy1.setHeightForWidth(self.le_ph3.sizePolicy().hasHeightForWidth())
        self.le_ph3.setSizePolicy(sizePolicy1)
        self.le_ph3.setMaximumSize(QSize(15, 15))
        self.le_ph3.setReadOnly(True)

        self.gridLayout.addWidget(self.le_ph3, 3, 15, 1, 1)

        self.cb_pince2 = QCheckBox(self.layoutWidget)
        self.cb_pince2.setObjectName(u"cb_pince2")

        self.gridLayout.addWidget(self.cb_pince2, 2, 5, 1, 1)

        self.cb_ph3 = QCheckBox(self.layoutWidget)
        self.cb_ph3.setObjectName(u"cb_ph3")

        self.gridLayout.addWidget(self.cb_ph3, 2, 14, 1, 1)

        self.le_1w2 = QLineEdit(self.layoutWidget)
        self.le_1w2.setObjectName(u"le_1w2")
        sizePolicy1.setHeightForWidth(self.le_1w2.sizePolicy().hasHeightForWidth())
        self.le_1w2.setSizePolicy(sizePolicy1)
        self.le_1w2.setMaximumSize(QSize(15, 15))
        self.le_1w2.setReadOnly(True)

        self.gridLayout.addWidget(self.le_1w2, 1, 4, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 1, 10, 1, 1)

        self.le_ph1 = QLineEdit(self.layoutWidget)
        self.le_ph1.setObjectName(u"le_ph1")
        sizePolicy1.setHeightForWidth(self.le_ph1.sizePolicy().hasHeightForWidth())
        self.le_ph1.setSizePolicy(sizePolicy1)
        self.le_ph1.setMaximumSize(QSize(15, 15))
        self.le_ph1.setReadOnly(True)

        self.gridLayout.addWidget(self.le_ph1, 3, 11, 1, 1)

        self.cb_pulse1 = QCheckBox(self.layoutWidget)
        self.cb_pulse1.setObjectName(u"cb_pulse1")

        self.gridLayout.addWidget(self.cb_pulse1, 2, 0, 1, 1)

        self.cb_ph2 = QCheckBox(self.layoutWidget)
        self.cb_ph2.setObjectName(u"cb_ph2")

        self.gridLayout.addWidget(self.cb_ph2, 2, 12, 1, 1)

        self.cb_pa = QCheckBox(self.layoutWidget)
        self.cb_pa.setObjectName(u"cb_pa")

        self.gridLayout.addWidget(self.cb_pa, 2, 8, 1, 1)

        self.cb_base = QCheckBox(self.layoutWidget)
        self.cb_base.setObjectName(u"cb_base")

        self.gridLayout.addWidget(self.cb_base, 0, 8, 1, 1)

        self.cb_1w3 = QCheckBox(self.layoutWidget)
        self.cb_1w3.setObjectName(u"cb_1w3")

        self.gridLayout.addWidget(self.cb_1w3, 0, 5, 1, 1)

        self.le_val_ph3 = QLineEdit(self.layoutWidget)
        self.le_val_ph3.setObjectName(u"le_val_ph3")
        self.le_val_ph3.setReadOnly(True)

        self.gridLayout.addWidget(self.le_val_ph3, 3, 14, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 7, 1, 1)

        self.cb_1w2 = QCheckBox(self.layoutWidget)
        self.cb_1w2.setObjectName(u"cb_1w2")

        self.gridLayout.addWidget(self.cb_1w2, 0, 3, 1, 1)

        self.le_1w1 = QLineEdit(self.layoutWidget)
        self.le_1w1.setObjectName(u"le_1w1")
        sizePolicy1.setHeightForWidth(self.le_1w1.sizePolicy().hasHeightForWidth())
        self.le_1w1.setSizePolicy(sizePolicy1)
        self.le_1w1.setMaximumSize(QSize(15, 15))
        self.le_1w1.setReadOnly(True)

        self.gridLayout.addWidget(self.le_1w1, 1, 1, 1, 1)

        self.le_ph2 = QLineEdit(self.layoutWidget)
        self.le_ph2.setObjectName(u"le_ph2")
        sizePolicy1.setHeightForWidth(self.le_ph2.sizePolicy().hasHeightForWidth())
        self.le_ph2.setSizePolicy(sizePolicy1)
        self.le_ph2.setMaximumSize(QSize(15, 15))
        self.le_ph2.setReadOnly(True)

        self.gridLayout.addWidget(self.le_ph2, 3, 13, 1, 1)

        self.le_val_1w1 = QLineEdit(self.layoutWidget)
        self.le_val_1w1.setObjectName(u"le_val_1w1")
        self.le_val_1w1.setReadOnly(True)

        self.gridLayout.addWidget(self.le_val_1w1, 1, 0, 1, 1)

        self.le_conso = QLineEdit(self.layoutWidget)
        self.le_conso.setObjectName(u"le_conso")
        self.le_conso.setReadOnly(True)

        self.gridLayout.addWidget(self.le_conso, 1, 12, 1, 3)

        self.le_1w3 = QLineEdit(self.layoutWidget)
        self.le_1w3.setObjectName(u"le_1w3")
        sizePolicy1.setHeightForWidth(self.le_1w3.sizePolicy().hasHeightForWidth())
        self.le_1w3.setSizePolicy(sizePolicy1)
        self.le_1w3.setMaximumSize(QSize(15, 15))
        self.le_1w3.setReadOnly(True)

        self.gridLayout.addWidget(self.le_1w3, 1, 6, 1, 1)

        self.cb_ph1 = QCheckBox(self.layoutWidget)
        self.cb_ph1.setObjectName(u"cb_ph1")

        self.gridLayout.addWidget(self.cb_ph1, 2, 10, 1, 1)

        self.le_val_ph2 = QLineEdit(self.layoutWidget)
        self.le_val_ph2.setObjectName(u"le_val_ph2")
        self.le_val_ph2.setReadOnly(True)

        self.gridLayout.addWidget(self.le_val_ph2, 3, 12, 1, 1)

        self.le_val_ph1 = QLineEdit(self.layoutWidget)
        self.le_val_ph1.setObjectName(u"le_val_ph1")
        self.le_val_ph1.setReadOnly(True)

        self.gridLayout.addWidget(self.le_val_ph1, 3, 10, 1, 1)

        self.le_val_pa = QLineEdit(self.layoutWidget)
        self.le_val_pa.setObjectName(u"le_val_pa")
        self.le_val_pa.setReadOnly(True)

        self.gridLayout.addWidget(self.le_val_pa, 3, 8, 1, 1)

        self.le_pa = QLineEdit(self.layoutWidget)
        self.le_pa.setObjectName(u"le_pa")
        sizePolicy1.setHeightForWidth(self.le_pa.sizePolicy().hasHeightForWidth())
        self.le_pa.setSizePolicy(sizePolicy1)
        self.le_pa.setMaximumSize(QSize(15, 15))
        self.le_pa.setReadOnly(True)

        self.gridLayout.addWidget(self.le_pa, 3, 9, 1, 1)

        self.le_pulse1 = QLineEdit(self.layoutWidget)
        self.le_pulse1.setObjectName(u"le_pulse1")
        sizePolicy1.setHeightForWidth(self.le_pulse1.sizePolicy().hasHeightForWidth())
        self.le_pulse1.setSizePolicy(sizePolicy1)
        self.le_pulse1.setMaximumSize(QSize(15, 15))
        self.le_pulse1.setReadOnly(True)

        self.gridLayout.addWidget(self.le_pulse1, 3, 1, 1, 1)

        self.cb_1w1 = QCheckBox(self.layoutWidget)
        self.cb_1w1.setObjectName(u"cb_1w1")

        self.gridLayout.addWidget(self.cb_1w1, 0, 0, 1, 1)

        self.le_val_1w2 = QLineEdit(self.layoutWidget)
        self.le_val_1w2.setObjectName(u"le_val_1w2")
        self.le_val_1w2.setReadOnly(True)

        self.gridLayout.addWidget(self.le_val_1w2, 1, 3, 1, 1)

        self.le_pince2 = QLineEdit(self.layoutWidget)
        self.le_pince2.setObjectName(u"le_pince2")
        sizePolicy1.setHeightForWidth(self.le_pince2.sizePolicy().hasHeightForWidth())
        self.le_pince2.setSizePolicy(sizePolicy1)
        self.le_pince2.setMaximumSize(QSize(15, 15))
        self.le_pince2.setReadOnly(True)

        self.gridLayout.addWidget(self.le_pince2, 3, 6, 1, 1)


        self.main_gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.main_gridLayout.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QSize(200, 140))
        self.groupBox_2.setMaximumSize(QSize(200, 140))
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.dt_fin = QDateTimeEdit(self.groupBox_2)
        self.dt_fin.setObjectName(u"dt_fin")

        self.gridLayout_2.addWidget(self.dt_fin, 2, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)

        self.le_base = QLineEdit(self.groupBox_2)
        self.le_base.setObjectName(u"le_base")

        self.gridLayout_2.addWidget(self.le_base, 3, 1, 1, 1)

        self.dt_deb = QDateTimeEdit(self.groupBox_2)
        self.dt_deb.setObjectName(u"dt_deb")

        self.gridLayout_2.addWidget(self.dt_deb, 1, 1, 1, 1)

        self.cb_calendrier = QCheckBox(self.groupBox_2)
        self.cb_calendrier.setObjectName(u"cb_calendrier")

        self.gridLayout_2.addWidget(self.cb_calendrier, 0, 1, 1, 1)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)


        self.main_gridLayout.addWidget(self.groupBox_2, 0, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.main_gridLayout.addItem(self.verticalSpacer_2, 1, 0, 1, 1)


        self.gridLayout_4.addLayout(self.main_gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.actionQuit)
        self.toolBar.addAction(self.actionConfig_Legende)
        self.toolBar.addAction(self.actionactionBase)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
#if QT_CONFIG(shortcut)
        self.actionQuit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionConfig_Legende.setText(QCoreApplication.translate("MainWindow", u"Config L\u00e9gende", None))
#if QT_CONFIG(tooltip)
        self.actionConfig_Legende.setToolTip(QCoreApplication.translate("MainWindow", u"Config Legende", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionConfig_Legende.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+L", None))
#endif // QT_CONFIG(shortcut)
        self.actionactionBase.setText(QCoreApplication.translate("MainWindow", u"Base", None))
#if QT_CONFIG(shortcut)
        self.actionactionBase.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+B", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Commandes", None))
        self.btn_ftp.setText(QCoreApplication.translate("MainWindow", u"FTP-Data", None))
        self.btn_plot.setText(QCoreApplication.translate("MainWindow", u"Plot", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"L\u00e9gende Data et choix affichage", None))
        self.le_val_1w3.setText("")
        self.cb_pince1.setText(QCoreApplication.translate("MainWindow", u"VMC", None))
        self.cb_pince2.setText(QCoreApplication.translate("MainWindow", u"ECS", None))
        self.cb_ph3.setText(QCoreApplication.translate("MainWindow", u"Ph3", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"KW:", None))
        self.cb_pulse1.setText(QCoreApplication.translate("MainWindow", u"Gialix", None))
        self.cb_ph2.setText(QCoreApplication.translate("MainWindow", u"Ph2", None))
        self.cb_pa.setText(QCoreApplication.translate("MainWindow", u"Pa", None))
        self.cb_base.setText(QCoreApplication.translate("MainWindow", u"T_Infos", None))
        self.cb_1w3.setText(QCoreApplication.translate("MainWindow", u"T\u00b0 Ext", None))
        self.cb_1w2.setText(QCoreApplication.translate("MainWindow", u"T\u00b0 RdC", None))
        self.cb_ph1.setText(QCoreApplication.translate("MainWindow", u"Ph1", None))
        self.cb_1w1.setText(QCoreApplication.translate("MainWindow", u"T\u00b0 Cave", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"P\u00e9riode", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"fin:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.cb_calendrier.setText(QCoreApplication.translate("MainWindow", u"Calendrier On", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"deb:", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

