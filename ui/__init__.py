from src.Account import Account
from ui.Dashboard import MainWindow as Dashboard
from ui.ChatBot import MainWindow as ChatBot
from ui.PasswordManager import MainWindow as PasswordManager
from ui.PasswordManager.Detail import MainWindow as PasswordManagerDetail

from ui.ui_dashboard import Ui_MainWindow

from PySide6.QtWidgets import (QMainWindow,
                               QWidget)


#
# Main window
# opens dashboard onload
#
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # creating new instance of main window ui
        self.Window = Ui_MainWindow()
        self.Window.setupUi(self)  # setting up ui

        self.dashboard()  # calling dashboard method to load ui

        # navigation controls
        self.Window.nav_dashboard.clicked.connect(self.dashboard)
        self.Window.nav_chat_bot.clicked.connect(self.chat_bot)
        self.Window.nav_pass_manager.clicked.connect(self.password_manager)

    def dashboard(self):
        """
        Dashboard method
        loads up dashboard ui and connect buttons within
        """
        print("[+] Opening Dashboard... ")
        # calling remove old elements
        # to remove any components in app
        self._remove_old_elements_()
        # getting dashboard ui instance
        app = Dashboard(self)
        app.run()  # running dashboard

        # connecting the buttons
        app.container.chatbot_button.clicked.connect(self.chat_bot)

        # changing navigation list color
        self._change_all_background_()
        self.Window.nav_dashboard.setStyleSheet("border: none; "
                                                "padding: 3; "
                                                "background-color: rgb(36, 36, 35);")

    def chat_bot(self):
        """
        chat_bot method
        loads up dashboard ui and connect buttons within
        """

        print("[+] Opening Chatbot...")
        # calling remove old elements
        # to remove any components in app
        self._remove_old_elements_()
        # getting chatbot ui instance
        app = ChatBot(self)
        app.run()   # running chatbot

        # changing navigation list color
        self._change_all_background_()
        self.Window.nav_chat_bot.setStyleSheet("border: none; "
                                               "padding: 3; "
                                               "background-color: rgb(36, 36, 35);")

    def password_manager(self):
        """
        password manager method
        loads up password manager UI
        """
        print("[+] Opening Password Manager...")
        # calling remove old elements
        # to remove any components in app
        self._remove_old_elements_()
        # getting password manager ui instance
        app = PasswordManager(self)
        app.run()   # running Password Manager

        # changing navigation list color
        self._change_all_background_()
        self.Window.nav_pass_manager.setStyleSheet("border: none; "
                                                   "padding: 3; "
                                                   "background-color: rgb(36, 36, 35);")

    def password_manager_detail(self, account):
        """
        password manager detail
        """
        print("[+] Opening Password Manager Details...")
        # calling remove old elements
        # to remove any components in app
        self._remove_old_elements_()
        # getting password manager detail ui instance
        app = PasswordManagerDetail(self)
        app.run(account)

        # changing navigation list color
        self._change_all_background_()
        self.Window.nav_pass_manager.setStyleSheet("border: none; "
                                                   "padding: 3; "
                                                   "background-color: rgb(36, 36, 35);")

    def password_manager_create(self):
        """
        password manager create
        """
        print("[+] Opening Password Manager Create...")
        

    def _remove_old_elements_(self):
        """
        @private method
        to remove all the existing elements from app
        and hide them
        """
        x = self.Window.current_app_container.findChildren(QWidget)
        for i in x:
            self.Window.verticalLayout_7.removeWidget(i)
            i.hide()

    def _change_all_background_(self):
        """
        Changing navigation color to background color
        """
        self.Window.nav_dashboard.setStyleSheet("border: none; "
                                                "padding: 3; "
                                                "background-color: rgb(51, 53, 51);")
        self.Window.nav_notes.setStyleSheet("border: none; "
                                            "padding: 3; "
                                            "background-color: rgb(51, 53, 51);")
        self.Window.nav_pass_manager.setStyleSheet("border: none; "
                                                   "padding: 3; "
                                                   "background-color: rgb(51, 53, 51);")
        self.Window.nav_weather.setStyleSheet("border: none; "
                                              "padding: 3; "
                                              "background-color: rgb(51, 53, 51);")
        self.Window.nav_music_player.setStyleSheet("border: none; "
                                                   "padding: 3; "
                                                   "background-color: rgb(51, 53, 51);")
        self.Window.nav_chat_bot.setStyleSheet("border: none; "
                                               "padding: 3; "
                                               "background-color: rgb(51, 53, 51);")
