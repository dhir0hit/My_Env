from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QMainWindow)

from ui.PasswordManager.ui_passwordManager_create import Ui_password_manager_create
from src.PasswordManager import PasswordManager
from src.Account import Account

class MainWindow(QMainWindow):
    def __init__(self, window):
        super(MainWindow, self).__init__()
        print("[+] Opened Password Manager Create")

        self.Window = window.Window

    def run(self, account):
        """
        Run the app
        add elements in app
        """
        self.password_manager_data = account

        self.account_create = Ui_password_manager_create()
        self.account_create.setupUi(self.Window.current_app_container)

        self.Window.verticalLayout_7.addWidget(self.account_create.account_create_container)
        self.account_create.Create_Button.clicked.connect(lambda: self.get_input())

    def get_input(self):
        # getting input values
        _username = self.account_create.user_input.text()
        _password = self.account_create.password_input.text()
        _platform = self.account_create.platform_input.text()
        _website = self.account_create.website_input.text()

        # creating new account instance
        account = Account(_username, _password, _platform, _website)

        self.password_manager_data.pass_manager.new_account(account)
        print(account.get_all())

        # Removing values from inputs
        self.account_create.user_input.setText("")
        self.account_create.password_input.setText("")
        self.account_create.platform_input.setText("")
        self.account_create.website_input.setText("")

