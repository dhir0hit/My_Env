from PySide6.QtCore import Qt
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow

from main import MyEnv
from ui.Landing.ui_landing_1 import Ui_MainWindow as Ui_MainWindow_1
from ui.Landing.ui_landing_2 import Ui_MainWindow as Ui_MainWindow_2
from ui.Landing.ui_landing_5 import Ui_MainWindow as Ui_MainWindow_5


# Main window of Landing Page
# TODO: if user is not sign in show main page otherwise direct user to dashboard
class MainWindow(QMainWindow):
    def __init__(self, myenv):
        super(MainWindow, self).__init__()
        self.myenv = myenv
        self.ui = Ui_MainWindow_1()
        self.ui.setupUi(self)

        self.ui.nav_indicator_1.click()
        self._setup_nav()
        self.ui.next_button.clicked.connect(self.nav_2)

    def _setup_nav(self):
        self.ui.nav_indicator_1.clicked.connect(self.nav_1)
        self.ui.nav_indicator_2.clicked.connect(self.nav_2)
        self.ui.nav_indicator_3.clicked.connect(self.nav_3)
        self.ui.nav_indicator_4.clicked.connect(self.nav_4)

    @Slot()
    def nav_1(self):
        self.ui = Ui_MainWindow_1()
        self.ui.setupUi(self)
        self.ui.nav_indicator_1.click()
        self._setup_nav()
        self.ui.next_button.clicked.connect(self.nav_2)

    @Slot()
    def nav_2(self):
        self.ui = Ui_MainWindow_2()
        self.ui.setupUi(self)
        self.ui.nav_indicator_2.click()
        self._setup_nav()
        self.ui.next_button.clicked.connect(self.nav_3)

    @Slot()
    def nav_3(self):
        self.ui = Ui_MainWindow_2()
        self.ui.setupUi(self)
        self.ui.ltop_container.setLayoutDirection(Qt.RightToLeft)
        self.ui.nav_indicator_3.click()
        self._setup_nav()
        self.ui.next_button.clicked.connect(self.nav_4)

    @Slot()
    def nav_4(self):
        self.ui = Ui_MainWindow_2()
        self.ui.setupUi(self)
        self.ui.nav_indicator_4.click()
        self._setup_nav()
        self.ui.next_button.clicked.connect(self.nav_5)

    @Slot()
    def nav_5(self):
        self.ui = Ui_MainWindow_5()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.__continue__)
        self.ui.nav_indicator_4.click()

    @Slot()
    def __continue__(self):
        self.myenv.open_app()

