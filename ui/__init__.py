from ui.Dashboard import MainWindow as Dashboard
from ui.ChatBot import MainWindow as ChatBot
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


