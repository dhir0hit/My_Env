from PySide6.QtCore import Qt, QMetaObject
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QLabel, QMainWindow)

from ui.Dashboard.ui_dashboard import Ui_MainWindow

from ui.Dashboard.ui_container import Ui_Container
from ui.Dashboard.ui_pass_manager import Ui_password_manager_container
from utils.PasswordManager import PasswordManager


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        print("[+] Opened Settings...")



