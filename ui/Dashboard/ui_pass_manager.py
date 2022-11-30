# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PasswordManager.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QMetaObject, QSize, Qt)
from PySide6.QtGui import (QFont, QIcon)
from PySide6.QtWidgets import (QLabel, QPushButton, QSizePolicy,
                               QVBoxLayout, QHBoxLayout, QLineEdit, QWidget, QLCDNumber)

from src.PasswordManager import PasswordManager


class Ui_password_manager_container(object):
    def __init__(self):
        self.manager_name = QLabel()
        self.lineEdit = QLineEdit()
        self.manager_name = QLabel()

    def setupUi(self, parent):
        password_manager = PasswordManager()
        self.parent = parent

        # self.__unlocking__(self.parent)
        if password_manager.AccessPass:
            self.__unlocking__(self.parent)
        else:
            self.__locked__(self.parent)

    def __unlocking__(self, parent):
        self.password_manager_container = QWidget(parent)
        if not self.password_manager_container.objectName():
            self.password_manager_container.setObjectName(u"password_manager_container")
        self.password_manager_container.resize(400, 300)
        self.password_manager_container.setStyleSheet(u"background-color: rgb(36, 36, 35);")
        self.horizontalLayout = QHBoxLayout(self.password_manager_container)
        self.horizontalLayout.setObjectName(u"password_manager_container")
        self.unlock_manager_container_3 = QWidget(self.password_manager_container)
        self.unlock_manager_container_3.setObjectName(u"unlock_manager_container_3")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.unlock_manager_container_3.sizePolicy().hasHeightForWidth())
        self.unlock_manager_container_3.setSizePolicy(sizePolicy)
        self.verticalLayout_21 = QVBoxLayout(self.unlock_manager_container_3)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.manager_name = QLabel(self.unlock_manager_container_3)
        self.manager_name.setObjectName(u"manager_name_3")
        self.manager_name.setText("Write Down Your Password")

        self.verticalLayout_21.addWidget(self.manager_name, 0, Qt.AlignHCenter)

        self.horizontalWidget = QWidget(self.unlock_manager_container_3)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalWidget.setStyleSheet(u"border: 1 solid  rgb(245, 203, 92);")
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(6, 1, 6, 1)
        self.lineEdit = QLineEdit(self.horizontalWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        font = QFont()
        font.setPointSize(15)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(u"color: rgb(245, 203, 92);\n"
                                    "border:none;")
        self.lineEdit.setEchoMode(QLineEdit.Password)
        self.lineEdit.setCursorPosition(0)

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.horizontalWidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setStyleSheet(u"border: none;\n"
                                      "padding: 7;")
        icon = QIcon()
        icon.addFile(u":/resources/subdirectory_arrow_left_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal,
                     QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.verticalLayout_21.addWidget(self.horizontalWidget)

        self.horizontalLayout.addWidget(self.unlock_manager_container_3)

        QMetaObject.connectSlotsByName(self.password_manager_container)
    # setupUi

    def __locked__(self, parent):
        self.password_manager_container = QWidget(parent)
        if not self.password_manager_container.objectName():
            self.password_manager_container.setObjectName(u"password_manager_container")
        self.password_manager_container.resize(416, 238)
        self.password_manager_container.setStyleSheet(u"background-color: rgb(36, 36, 35);")

        self.verticalLayout = QVBoxLayout(self.password_manager_container)
        self.verticalLayout.setObjectName(u"password_manager_container")
        
        self.unlock_manager_container = QWidget(self.password_manager_container)
        self.unlock_manager_container.setObjectName(u"unlock_manager_container_3")
        
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.unlock_manager_container.sizePolicy().hasHeightForWidth())
        
        self.unlock_manager_container.setSizePolicy(sizePolicy)
        self.verticalLayout_21 = QVBoxLayout(self.unlock_manager_container)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.manager_name = QLabel(self.unlock_manager_container)
        self.manager_name.setObjectName(u"manager_name_3")
        self.manager_name.setText("Password Manager")
        self.manager_name.setStyleSheet("color: rgb(232, 237, 223);")

        self.verticalLayout_21.addWidget(self.manager_name)

        self.unlock_button = QPushButton(self.unlock_manager_container)
        self.unlock_button.setText("Unlock...")
        self.unlock_button.setObjectName(u"unlock_button_3")
        self.unlock_button.setStyleSheet(u"border: none;\n"
"padding-top: 5;\n"
"padding-right: 10;\n"
"padding-bottom:  5;\n"
"padding-left: 10;\n"
"background-color: rgb(245, 203, 92);\n"
"color: rgb(51, 53, 51);")

        self.verticalLayout_21.addWidget(self.unlock_button)

        self.verticalLayout.addWidget(self.unlock_manager_container, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        QMetaObject.connectSlotsByName(self.password_manager_container)
        # self.unlock_button.connect(self.try_unlock())
    # setupUi

    def __unlocked__(self, parent):
        self.password_manager_container = QWidget(parent)
        if not self.password_manager_container.objectName():
            self.password_manager_container.setObjectName(u"password_manager_container")
        self.password_manager_container.resize(734, 171)
        font = QFont()
        font.setPointSize(4)
        self.password_manager_container.setFont(font)
        self.password_manager_container.setWindowTitle("password_manager_container")
        self.password_manager_container.setStyleSheet(u"background-color: rgb(36, 36, 35);")
        self.horizontalLayout = QHBoxLayout(self.password_manager_container)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.total_accounts_container = QWidget(self.password_manager_container)
        self.total_accounts_container.setObjectName(u"total_accounts_container")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.total_accounts_container.sizePolicy().hasHeightForWidth())
        self.total_accounts_container.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.total_accounts_container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.total_sub_container = QWidget(self.total_accounts_container)
        self.total_sub_container.setObjectName(u"total_sub_container")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.total_sub_container.sizePolicy().hasHeightForWidth())
        self.total_sub_container.setSizePolicy(sizePolicy1)
        self.horizontalLayout_2 = QHBoxLayout(self.total_sub_container)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.total_accounts = QLCDNumber(self.total_sub_container)
        self.total_accounts.setObjectName(u"total_accounts")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.total_accounts.sizePolicy().hasHeightForWidth())
        self.total_accounts.setSizePolicy(sizePolicy2)
        self.total_accounts.setMinimumSize(QSize(70, 45))
        self.total_accounts.setMaximumSize(QSize(120, 120))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(False)
        self.total_accounts.setFont(font1)
        self.total_accounts.setStyleSheet(u"color: rgb(245, 203, 92);border:none;")
        self.total_accounts.setDigitCount(3)
        self.total_accounts.setSegmentStyle(QLCDNumber.Filled)
        self.total_accounts.setProperty("intValue", 999)

        self.horizontalLayout_2.addWidget(self.total_accounts)

        self.total_account_name = QLabel(self.total_sub_container)
        self.total_account_name.setObjectName(u"total_account_name")
        self.total_account_name.setText("Total Accounts")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.total_account_name.sizePolicy().hasHeightForWidth())
        self.total_account_name.setSizePolicy(sizePolicy3)

        self.horizontalLayout_2.addWidget(self.total_account_name)

        self.verticalLayout.addWidget(self.total_sub_container)

        self.open_manager = QPushButton(self.total_accounts_container)
        self.open_manager.setObjectName(u"open_manager")
        self.open_manager.setText("Open Manager")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        self.open_manager.setFont(font2)
        self.open_manager.setStyleSheet(u"border: \"none\";\n"
                                        "color: rgb(36, 36, 35);\n"
                                        "background-color: rgb(245, 203, 92);\n"
                                        "padding: 5;")

        self.verticalLayout.addWidget(self.open_manager)

        self.horizontalLayout.addWidget(self.total_accounts_container)

        self.favorite_accounts_container = QWidget(self.password_manager_container)
        self.favorite_accounts_container.setObjectName(u"favorite_accounts_container")
        sizePolicy.setHeightForWidth(self.favorite_accounts_container.sizePolicy().hasHeightForWidth())
        self.favorite_accounts_container.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.favorite_accounts_container)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.favorite_sub_container = QWidget(self.favorite_accounts_container)
        self.favorite_sub_container.setObjectName(u"favorite_sub_container")
        self.horizontalLayout_3 = QHBoxLayout(self.favorite_sub_container)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.favorite_accounts = QLCDNumber(self.favorite_sub_container)
        self.favorite_accounts.setObjectName(u"favorite_accounts")
        sizePolicy2.setHeightForWidth(self.favorite_accounts.sizePolicy().hasHeightForWidth())
        self.favorite_accounts.setSizePolicy(sizePolicy2)
        self.favorite_accounts.setMinimumSize(QSize(70, 45))
        self.favorite_accounts.setMaximumSize(QSize(120, 120))
        font3 = QFont()
        font3.setPointSize(20)
        self.favorite_accounts.setFont(font3)
        self.favorite_accounts.setStyleSheet(u"color: rgb(245, 203, 92);border:none;")
        self.favorite_accounts.setDigitCount(3)
        self.favorite_accounts.setProperty("intValue", 999)

        self.horizontalLayout_3.addWidget(self.favorite_accounts)

        self.favorite_account_name = QLabel(self.favorite_sub_container)
        self.favorite_account_name.setObjectName(u"favorite_account_name")
        self.favorite_account_name.setText("Favorite Accounts")

        self.horizontalLayout_3.addWidget(self.favorite_account_name)

        self.verticalLayout_2.addWidget(self.favorite_sub_container)

        self.open_favorite = QPushButton(self.favorite_accounts_container)
        self.open_favorite.setObjectName(u"open_favorite")
        self.open_favorite.setStyleSheet(u"border: \"none\";\n"
                                         "color: rgb(36, 36, 35);\n"
                                         "background-color: rgb(245, 203, 92);\n"
                                         "padding: 5;")
        self.open_favorite.setText("Open favorite")


        self.verticalLayout_2.addWidget(self.open_favorite)

        self.horizontalLayout.addWidget(self.favorite_accounts_container)

        self.create_account_container = QWidget(self.password_manager_container)
        self.create_account_container.setObjectName(u"create_account_container")
        sizePolicy.setHeightForWidth(self.create_account_container.sizePolicy().hasHeightForWidth())
        self.create_account_container.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.create_account_container)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.create_sub_container = QWidget(self.create_account_container)
        self.create_sub_container.setObjectName(u"create_sub_container")
        self.horizontalLayout_4 = QHBoxLayout(self.create_sub_container)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.create_new_account_name = QLabel(self.create_sub_container)
        self.create_new_account_name.setObjectName(u"create_new_account_name")
        self.create_new_account_name.setText("Create New Account")
        self.horizontalLayout_4.addWidget(self.create_new_account_name)

        self.verticalLayout_3.addWidget(self.create_sub_container)

        self.create_button = QPushButton(self.create_account_container)
        self.create_button.setObjectName(u"create_button")
        self.create_button.setStyleSheet(u"border: \"none\";\n"
                                         "color: rgb(36, 36, 35);\n"
                                         "background-color: rgb(245, 203, 92);\n"
                                         "padding: 5;")

        self.verticalLayout_3.addWidget(self.create_button)
        self.create_button.setText("Create")

        self.horizontalLayout.addWidget(self.create_account_container)

        QMetaObject.connectSlotsByName(self.password_manager_container)
    # setupUi




