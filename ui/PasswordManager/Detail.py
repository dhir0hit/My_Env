from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QMainWindow)
import pyperclip
from ui.PasswordManager.ui_passwordManager_details import Ui_password_manager_detail


class MainWindow(QMainWindow):
    def __init__(self, window):
        super(MainWindow, self).__init__()
        print("[+] Opened Password Manager")

        self.Window = window.Window
        self.password_hidden = ""
        self.password_shown = ""
        self.is_hidden_password = True

    def run(self, account):
        """
        Run the app
        add elements in app
        """
        self.password_shown = account.Password()
        self.password_hidden = "•" * len(self.password_shown)

        # password manager detail container in UI
        self.password_manager_detail = Ui_password_manager_detail()
        self.password_manager_detail.setupUi(self.Window.current_app_container)

        self.Window.verticalLayout_7.addWidget(self.password_manager_detail.account_detail_container)

        self.password_manager_detail._platform.setText(account.Platform())
        self.password_manager_detail._id.setText(str(account.Id()))
        self.password_manager_detail.Username.setText(account.Username())
        self.password_manager_detail.Password.setText(self.password_hidden)
        self.password_manager_detail.Website.setText(account.Website())

        self.password_manager_detail.ShowPassword.clicked.connect(lambda: self.display_password())
        self.password_manager_detail.PasswordCopyButton.clicked.connect(
            lambda: pyperclip.copy(account.Password()))
        self.password_manager_detail.pushButton.clicked.connect(
            lambda: pyperclip.copy(account.Username()))

    def display_password(self):
        """
        Display password and hide password when called
        and change background of button
        """
        print("Hello")
        if self.is_hidden_password:
            # showing password
            self.password_manager_detail.Password.setText(self.password_shown)
            # Changing stylesheet
            self.password_manager_detail.ShowPassword.setStyleSheet(" border: 'none'; "
                                                                    "padding: 5; "
                                                                    "border-radius: 4; "
                                                                    "background-color: rgb(245, 203, 92);")
        else:
            # Hiding password
            self.password_manager_detail.Password.setText(self.password_hidden)
            # Changing stylesheet
            self.password_manager_detail.ShowPassword.setStyleSheet(" border: 'none'; "
                                                                    "padding: 5; "
                                                                    "border-radius: 4; "
                                                                    "background-color: rgb(36, 36, 35);")

        # changing bool value is hidden password
        self.is_hidden_password = not self.is_hidden_password
