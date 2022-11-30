from PySide6.QtWidgets import (QMainWindow)
from ui.PasswordManager.ui_passwordManager_list import Ui_accounts_list

from PySide6.QtCore import (QCoreApplication, QMetaObject)
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QSizePolicy, QVBoxLayout, QWidget)

from src.Account import Account
from src.PasswordManager import PasswordManager


class MainWindow(QMainWindow):
    def __init__(self, window):
        super(MainWindow, self).__init__()
        print("[+] Opened Password Manager List....")

        self.Window = window.Window

    def run(self, list_account):
        """
        Run the app
        , Send favorite list for favorite account page
        , Send total list for total accounts page
        :param list_account: list of accounts class
        :return:
        """
        # creating instance of ui
        self.account_list = Ui_accounts_list()
        self.account_list.setupUi(self.Window.current_app_container)
        # adding ui in app
        self.Window.verticalLayout_7.addWidget(self.account_list.accounts_list)

        # Looping through list of account to add them one by one
        for account in list_account:
            self.account_list.account_list_container.addWidget(self.addAccount(account))

    def addAccount(self, account):
        """
        Method to add account in list
        :param: takes account class as a parameter
        """
        account_container = QWidget()
        if not account_container.objectName():
            account_container.setObjectName(u"Form")
        account_container.resize(607, 120)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(account_container.sizePolicy().hasHeightForWidth())
        account_container.setSizePolicy(sizePolicy)
        account_container.setStyleSheet(u"background-color: rgb(51, 53, 51);")
        horizontalLayout = QHBoxLayout(account_container)
        horizontalLayout.setSpacing(20)
        horizontalLayout.setObjectName(u"horizontalLayout")
        horizontalLayout.setContentsMargins(10, 10, 10, 10)
        label = QLabel(account_container)
        label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(label.sizePolicy().hasHeightForWidth())
        label.setSizePolicy(sizePolicy1)

        horizontalLayout.addWidget(label)

        verticalWidget = QWidget(account_container)
        verticalWidget.setObjectName(u"verticalWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(verticalWidget.sizePolicy().hasHeightForWidth())
        verticalWidget.setSizePolicy(sizePolicy2)
        verticalLayout = QVBoxLayout(verticalWidget)
        verticalLayout.setObjectName(u"verticalLayout")
        label_3 = QLabel(verticalWidget)
        label_3.setObjectName(u"label_3")

        verticalLayout.addWidget(label_3)

        label_2 = QLabel(verticalWidget)
        label_2.setObjectName(u"label_2")

        verticalLayout.addWidget(label_2)

        horizontalLayout.addWidget(verticalWidget)

        QMetaObject.connectSlotsByName(account_container)
        label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><img src=\":/resources/deer_logo_template_dark_flat_handdrawn_design_6854205.jpg\" wdith=\"100\" height=\"100\"/></p></body></html>", None))
        label_3.setText(QCoreApplication.translate("Form", account.Platform(), None))
        label_2.setText(QCoreApplication.translate("Form", account.Username(), None))

        return account_container

