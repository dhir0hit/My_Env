# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PasswordManager_Create.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)


class Ui_password_manager_create(object):
    def setupUi(self, parent):
        self.account_create_container = QWidget(parent)
        if not self.account_create_container.objectName():
            self.account_create_container.setObjectName(u"account_create_container")
        self.account_create_container.resize(751, 505)
        self.account_create_container.setStyleSheet(u"background-color: rgb(36, 36, 35);")
        self.verticalLayout_2 = QVBoxLayout(self.account_create_container)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 15, 15, 15)
        self.username_container = QWidget(self.account_create_container)
        self.username_container.setObjectName(u"username_container")
        self.username_container.setMaximumSize(QSize(600, 16777215))
        self.verticalLayout_6 = QVBoxLayout(self.username_container)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(6, -1, -1, -1)
        self.user_label = QLabel(self.username_container)
        self.user_label.setObjectName(u"user_label")
        font = QFont()
        font.setPointSize(15)
        self.user_label.setFont(font)

        self.verticalLayout_6.addWidget(self.user_label)

        self.user_input = QLineEdit(self.username_container)
        self.user_input.setObjectName(u"user_input")
        self.user_input.setStyleSheet(u"border: 'none';\n"
"background-color: rgb(51, 53, 51);\n"
"padding: 5;")

        self.verticalLayout_6.addWidget(self.user_input)


        self.verticalLayout_2.addWidget(self.username_container)

        self.line_1 = QFrame(self.account_create_container)
        self.line_1.setObjectName(u"line_1")
        self.line_1.setFrameShape(QFrame.HLine)
        self.line_1.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_1)

        self.password_container = QWidget(self.account_create_container)
        self.password_container.setObjectName(u"password_container")
        self.password_container.setMaximumSize(QSize(600, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.password_container)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(7, -1, -1, -1)
        self.password_label = QLabel(self.password_container)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setFont(font)

        self.verticalLayout_5.addWidget(self.password_label)

        self.password_input = QLineEdit(self.password_container)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setStyleSheet(u"border: 'none';\n"
"background-color: rgb(51, 53, 51);\n"
"padding: 5;")

        self.verticalLayout_5.addWidget(self.password_input)


        self.verticalLayout_2.addWidget(self.password_container)

        self.line_2 = QFrame(self.account_create_container)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.platform_container = QWidget(self.account_create_container)
        self.platform_container.setObjectName(u"platform_container")
        self.platform_container.setMaximumSize(QSize(600, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.platform_container)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(6, -1, -1, -1)
        self.platform_label = QLabel(self.platform_container)
        self.platform_label.setObjectName(u"platform_label")
        self.platform_label.setFont(font)

        self.verticalLayout_4.addWidget(self.platform_label)

        self.platform_input = QLineEdit(self.platform_container)
        self.platform_input.setObjectName(u"platform_input")
        self.platform_input.setStyleSheet(u"border: 'none';\n"
"background-color: rgb(51, 53, 51);\n"
"padding: 5;")

        self.verticalLayout_4.addWidget(self.platform_input)


        self.verticalLayout_2.addWidget(self.platform_container)

        self.line_3 = QFrame(self.account_create_container)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_3)

        self.website_container = QWidget(self.account_create_container)
        self.website_container.setObjectName(u"website_container")
        self.website_container.setMaximumSize(QSize(600, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.website_container)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(6, -1, -1, -1)
        self.website_label = QLabel(self.website_container)
        self.website_label.setObjectName(u"website_label")
        self.website_label.setFont(font)

        self.verticalLayout_3.addWidget(self.website_label)

        self.website_input = QLineEdit(self.website_container)
        self.website_input.setObjectName(u"website_input")
        self.website_input.setStyleSheet(u"border: 'none';\n"
"background-color: rgb(51, 53, 51);\n"
"padding: 5;")

        self.verticalLayout_3.addWidget(self.website_input)


        self.verticalLayout_2.addWidget(self.website_container)

        self.create_container = QWidget(self.account_create_container)
        self.create_container.setObjectName(u"create_container")
        self.verticalLayout = QVBoxLayout(self.create_container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, 15, -1)
        self.Create_Button = QPushButton(self.create_container)
        self.Create_Button.setObjectName(u"Create_Button")
        self.Create_Button.setStyleSheet(u"background-color: rgb(245, 203, 92);\n"
"color: rgb(36, 36, 35);\n"
"border: 'none';\n"
"padding: 5;\n"
"padding-right: 15;\n"
"padding-left: 15;")

        self.verticalLayout.addWidget(self.Create_Button, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.create_container)


        self.retranslateUi(self.account_create_container)

        QMetaObject.connectSlotsByName(self.account_create_container)
    # setupUi

    def retranslateUi(self, account_create_container):
        account_create_container.setWindowTitle(QCoreApplication.translate("account_create_container", u"Form", None))
        self.user_label.setText(QCoreApplication.translate("account_create_container", u"User Name / Email", None))
        self.password_label.setText(QCoreApplication.translate("account_create_container", u"Password", None))
        self.platform_label.setText(QCoreApplication.translate("account_create_container", u"Platform", None))
        self.website_label.setText(QCoreApplication.translate("account_create_container", u"Website", None))
        self.Create_Button.setText(QCoreApplication.translate("account_create_container", u"Create", None))
