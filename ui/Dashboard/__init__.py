from PySide6.QtCore import Qt, QMetaObject
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QLabel, QMainWindow)

from ui.Dashboard.ui_dashboard import Ui_MainWindow

from ui.Dashboard.ui_container import Ui_Container
from ui.Dashboard.ui_pass_manager import Ui_password_manager_container
from utils.PasswordManager import PasswordManager

# Main window of Landing Page
# TODO: if user is not sign in show main page otherwise direct user to dashboard


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        print("[+] Opened Dashboard ... ")
        # getting mainWindow UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # password manager container in UI
        self.pass_manager = Ui_password_manager_container()
        self.pass_manager.setupUi(self.ui.current_app_container)

        # top container in UI
        self.container = Ui_Container()
        self.container.setupUi(self.ui.current_app_container)

        # Adding Container and Password Manager to vertical layout
        self.ui.verticalLayout_7.addWidget(self.container.container)
        self.ui.verticalLayout_7.addWidget(self.pass_manager.password_manager_container)

        # connecting function to button to unlock
        self.pass_manager.unlock_button.clicked.connect(self.try_unlock)

        # TODO: add functionality

    @Slot()
    #
    # method to show user input to
    # user enter password
    #
    def try_unlock(self):
        print("[+] Unlocking...")

        # removing password manager container
        self.ui.verticalLayout_7.removeWidget(self.pass_manager.password_manager_container)
        self.pass_manager.password_manager_container.hide()
        # setting up new password manager container
        self.pass_manager.__unlocking__(self.ui.current_app_container)
        # adding new password manager container to vertical layout
        self.ui.verticalLayout_7.addWidget(self.pass_manager.password_manager_container)

        # connecting function to buttons
        self.pass_manager.pushButton.clicked.connect(self.unlock_manager)
        self.pass_manager.lineEdit.returnPressed.connect(self.unlock_manager)

    @Slot()
    #
    # Method to unlock password manager
    # on Dashboard
    #
    def unlock_manager(self):
        # getting user input password
        password = self.pass_manager.lineEdit.text()
        # creating new instance of password manager
        password_manager = PasswordManager()

        if not password != "":
            # if Field is empty
            print("[-] Empty Field")

            # Showing user error
            self.pass_manager.manager_name.setText("Empty Field!")
            self.pass_manager.manager_name.setStyleSheet("color: red;")  # changing color

        elif password_manager.unlock_manager(password):
            # opening function if password correct
            self.unlocked()
            print("[+] Unlocked...")

        else:
            # if password is wrong
            print("[-] Wrong Password...")

            # Showing user error
            self.pass_manager.manager_name.setText("Wrong Password!")
            self.pass_manager.manager_name.setStyleSheet("color: red;")  # changing color

    def unlocked(self):
        # creating new instance of password manager
        password_manager = PasswordManager()

        # removing password manager container
        self.ui.verticalLayout_7.removeWidget(self.pass_manager.password_manager_container)
        self.pass_manager.password_manager_container.hide()
        # setting up new password manager container
        self.pass_manager.__unlocked__(self.ui.current_app_container)
        # adding new password manager container to vertical layout
        self.ui.verticalLayout_7.addWidget(self.pass_manager.password_manager_container)

        # -
        # Setting number of total and favorite accounts
        # -
        self.pass_manager.total_accounts.display(password_manager.TotalAccounts)
        self.pass_manager.favorite_accounts.display(password_manager.FavoriteAccounts)

        # -
        # opening password Manager
        # -
        # self.pass_manager.open_manager.clicked.connect()
        # self.pass_manager.open_favorite.clicked.connect()
        # self.pass_manager.create_button.clicked.connect()


