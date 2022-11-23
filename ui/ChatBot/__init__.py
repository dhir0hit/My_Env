from PyQt6.QtWidgets import QLabel

from ui.ChatBot.Bot import Bot
from PySide6.QtCore import Qt
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QLabel, QMainWindow)

from ui.ChatBot.ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.chatbot = Bot("rohit")

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.send.clicked.connect(self.new_user_message)

        self.user_message_count = 0
        self.bot_message_count = 0

        self.bot_message("Hello __User__,\n"
                         "Ask me anything\n"
                         "eg. Create a note, Create a Reminder,\n"
                         "Play Music, Or Help to get all command.")

    @Slot()
    def new_user_message(self):
        user_question = self.ui.lineEdit.text()
        self.user_message(user_question)

        bot_reply = self.chatbot.command(user_question)
        self.bot_message(bot_reply)

    def user_message(self, message):
        user_message_output = QLabel(message)
        user_message_output.setObjectName(u"user_" + str(self.user_message_count))
        user_message_output.setStyleSheet(u"background-color: rgb(51, 53, 51);")
        user_message_output.setWordWrap(True)
        user_message_output.setMargin(6)

        self.ui.verticalLayout_4.addWidget(user_message_output, 0, Qt.AlignRight)
        self.bot_message_count += 1
        # Clearing input
        self.ui.lineEdit.setText("")

    def bot_message(self, message):
        bot_message_output = QLabel(message)
        bot_message_output.setObjectName(u"chatbot_" + str(self.bot_message_count))
        bot_message_output.setStyleSheet(u"background-color: rgb(51, 53, 51);")
        bot_message_output.setWordWrap(False)
        bot_message_output.setMargin(6)
        bot_message_output.setMinimumHeight(10)

        self.ui.verticalLayout_4.addWidget(bot_message_output, Qt.AlignTop, Qt.AlignLeft)
        self.bot_message_count += 1