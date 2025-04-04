# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_InfosBaseDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QPushButton,
    QSizePolicy, QSpacerItem, QTextEdit, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(500, 400)
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.te_infos = QTextEdit(Dialog)
        self.te_infos.setObjectName(u"te_infos")
        self.te_infos.setReadOnly(True)

        self.gridLayout_2.addWidget(self.te_infos, 0, 0, 4, 1)

        self.btn_infos = QPushButton(Dialog)
        self.btn_infos.setObjectName(u"btn_infos")

        self.gridLayout_2.addWidget(self.btn_infos, 0, 1, 1, 1)

        self.btn_optimise = QPushButton(Dialog)
        self.btn_optimise.setObjectName(u"btn_optimise")

        self.gridLayout_2.addWidget(self.btn_optimise, 1, 1, 1, 1)

        self.btn_purge_ftp = QPushButton(Dialog)
        self.btn_purge_ftp.setObjectName(u"btn_purge_ftp")

        self.gridLayout_2.addWidget(self.btn_purge_ftp, 2, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 234, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 3, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(341, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 4, 0, 1, 1)

        self.btn_OK = QPushButton(Dialog)
        self.btn_OK.setObjectName(u"btn_OK")

        self.gridLayout_2.addWidget(self.btn_OK, 4, 1, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Infos Base", None))
        self.btn_infos.setText(QCoreApplication.translate("Dialog", u"Infos Base", None))
        self.btn_optimise.setText(QCoreApplication.translate("Dialog", u"Optimise Base", None))
        self.btn_purge_ftp.setText(QCoreApplication.translate("Dialog", u"Purge FTP", None))
        self.btn_OK.setText(QCoreApplication.translate("Dialog", u"OK", None))
    # retranslateUi

