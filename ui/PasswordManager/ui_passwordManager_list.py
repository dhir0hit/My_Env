# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PasswordManager_List.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_accounts_list(object):
    def setupUi(self, parent):
        self.accounts_list = QWidget()
        if not self.accounts_list.objectName():
            self.accounts_list.setObjectName(u"accounts_list")
        self.accounts_list.resize(769, 439)
        self.accounts_list.setStyleSheet(u"background-color: rgb(36, 36, 35);")
        self.verticalLayout = QVBoxLayout(self.accounts_list)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.accounts_list_scroll = QScrollArea(self.accounts_list)
        self.accounts_list_scroll.setObjectName(u"accounts_list_scroll")
        self.accounts_list_scroll.setWidgetResizable(True)
        self.account_list_contaienr = QWidget()
        self.account_list_contaienr.setObjectName(u"account_list_contaienr")
        self.account_list_contaienr.setGeometry(QRect(0, 0, 753, 423))
        self.verticalLayout_2 = QVBoxLayout(self.account_list_contaienr)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.trash = QLabel(self.account_list_contaienr)
        self.trash.setObjectName(u"trash")

        self.verticalLayout_2.addWidget(self.trash)

        self.accounts_list_scroll.setWidget(self.account_list_contaienr)

        self.verticalLayout.addWidget(self.accounts_list_scroll)


        self.retranslateUi(self.accounts_list)

        QMetaObject.connectSlotsByName(self.accounts_list)
    # setupUi

    def retranslateUi(self, accounts_list):
        accounts_list.setWindowTitle(QCoreApplication.translate("accounts_list", u"Form", None))
        self.trash.setText(QCoreApplication.translate("accounts_list", u"TextLabel", None))
    # retranslateUi

