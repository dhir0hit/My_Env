from PyQt6.QtWidgets import QLabel

from src.Bot import Bot
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QLabel, QMainWindow)

from ui.ChatBot.ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, window):
        super(MainWindow, self).__init__()
        self.chatbot = Bot("Rohit")
        print("[+] Opened ChatBot")

        self.Window = window.Window

    def run(self):
        """
        runs the app add chat container in app
        """
        self.chat_bot_container = Ui_MainWindow()
        self.chat_bot_container.setupUi(self.Window.current_app_container)

        # parent = self.Window.current_app_container.parent().layout()
        # parent.replaceWidget(self.Window.current_app_container, self.chat_bot_container)
        self.Window.verticalLayout_7.addWidget(self.chat_bot_container.chatbot_container)

        self.user_message_count = 0
        self.bot_message_count = 0

        self.bot_message("Hello __User__,\n"
                         "Ask me anything\n"
                         "eg. Create a note, Create a Reminder,\n"
                         "Play Music, Or Help to get all command.")

        self.chat_bot_container.send.clicked.connect(lambda: self.new_user_message)
        self.chat_bot_container.send.clicked.connect(self.new_user_message)
        # self.chat_bot_container.lineEdit.returnPressed.connect(lambda: self.new_user_message)
        self.chat_bot_container.lineEdit.returnPressed.connect(self.new_user_message)

    def new_user_message(self):
        """
        called upon when user enter new message
        """
        print("[+] New User Message")
        # getting user message
        user_question = self.chat_bot_container.lineEdit.text()

        # showing user message on screen
        self.user_message(user_question)

        # asking bot to reply user question
        # catching bot reply in variable
        bot_reply = self.chatbot.command(user_question)
        # showing bot message
        self.bot_message(bot_reply)

    def user_message(self, message):
        """
        getting user message and displaying on screen
        :param message: take string as param
        """

        # creating user message UI
        user_message_output = QLabel(message)
        user_message_output.setObjectName(u"user_" + str(self.user_message_count))
        user_message_output.setStyleSheet(u"background-color: rgb(51, 53, 51);")
        user_message_output.setWordWrap(True)
        user_message_output.setMargin(6)

        # Adding UI to chat container
        self.chat_bot_container.verticalLayout_4.addWidget(user_message_output, 0, Qt.AlignRight)
        self.bot_message_count += 1

        # Clearing input in line edit
        self.chat_bot_container.lineEdit.setText("")

    def bot_message(self, message):
        """
        getting bot message and displaying on screen
        :param message: take string as param
        """

        # Creating UI
        bot_message_output = QLabel(message)
        bot_message_output.setObjectName(u"chatbot_" + str(self.bot_message_count))
        bot_message_output.setStyleSheet(u"background-color: rgb(51, 53, 51);")
        bot_message_output.setWordWrap(False)
        bot_message_output.setMargin(6)

        # Adding UI to Chat Container
        self.chat_bot_container.verticalLayout_4.addWidget(bot_message_output, Qt.AlignTop, Qt.AlignLeft)
        self.bot_message_count += 1

