# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_FTP_Dialog.ui'
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
    QGridLayout, QGroupBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(483, 504)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMaximumSize(QSize(490, 505))
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btn_transfer = QPushButton(Dialog)
        self.btn_transfer.setObjectName(u"btn_transfer")
        sizePolicy.setHeightForWidth(self.btn_transfer.sizePolicy().hasHeightForWidth())
        self.btn_transfer.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.btn_transfer, 1, 3, 1, 1)

        self.date_import = QDateEdit(Dialog)
        self.date_import.setObjectName(u"date_import")

        self.gridLayout_2.addWidget(self.date_import, 1, 1, 1, 1)

        self.te_infos_transfer = QTextEdit(Dialog)
        self.te_infos_transfer.setObjectName(u"te_infos_transfer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.te_infos_transfer.sizePolicy().hasHeightForWidth())
        self.te_infos_transfer.setSizePolicy(sizePolicy1)
        self.te_infos_transfer.setMinimumSize(QSize(350, 300))

        self.gridLayout_2.addWidget(self.te_infos_transfer, 2, 0, 4, 4)

        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QSize(445, 136))
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.le_host = QLineEdit(self.groupBox)
        self.le_host.setObjectName(u"le_host")

        self.gridLayout.addWidget(self.le_host, 0, 1, 1, 1)

        self.btn_save_param = QPushButton(self.groupBox)
        self.btn_save_param.setObjectName(u"btn_save_param")

        self.gridLayout.addWidget(self.btn_save_param, 0, 2, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.le_login = QLineEdit(self.groupBox)
        self.le_login.setObjectName(u"le_login")

        self.gridLayout.addWidget(self.le_login, 1, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.le_passwd = QLineEdit(self.groupBox)
        self.le_passwd.setObjectName(u"le_passwd")

        self.gridLayout.addWidget(self.le_passwd, 2, 1, 1, 1)

        self.cb_passVisible = QCheckBox(self.groupBox)
        self.cb_passVisible.setObjectName(u"cb_passVisible")

        self.gridLayout.addWidget(self.cb_passVisible, 2, 2, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 5)

        self.btn_test = QPushButton(Dialog)
        self.btn_test.setObjectName(u"btn_test")

        self.gridLayout_2.addWidget(self.btn_test, 1, 2, 1, 1)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)

        self.btn_ajout_base = QPushButton(Dialog)
        self.btn_ajout_base.setObjectName(u"btn_ajout_base")

        self.gridLayout_2.addWidget(self.btn_ajout_base, 3, 4, 1, 1)

        self.btn_abandon = QPushButton(Dialog)
        self.btn_abandon.setObjectName(u"btn_abandon")

        self.gridLayout_2.addWidget(self.btn_abandon, 2, 4, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.btn_transfer.setText(QCoreApplication.translate("Dialog", u"Transfert", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Param\u00e8tres de connexion", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"host:", None))
        self.btn_save_param.setText(QCoreApplication.translate("Dialog", u"Enregistre param", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Login:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Password:", None))
        self.cb_passVisible.setText(QCoreApplication.translate("Dialog", u"Visible", None))
        self.btn_test.setText(QCoreApplication.translate("Dialog", u"Test", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Date Import:", None))
        self.btn_ajout_base.setText(QCoreApplication.translate("Dialog", u"Ajout Base", None))
        self.btn_abandon.setText(QCoreApplication.translate("Dialog", u"Abandon", None))
    # retranslateUi

