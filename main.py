import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication

from ui import (MainWindow, Landing)


class MyEnv:
    def __init__(self):
        self.MainWindow = Landing.MainWindow(self)
        self.window = None
        self.show_window()

    @Slot()
    def open_app(self):
        print("[+] Opening App")
        self.MainWindow = MainWindow()
        self.show_window()

    # @Slot()
    # def show_chatbot(self):
    #     print("[+] Opening Chatbot")

    def show_window(self):
        self.window = self.MainWindow
        self.window.setGeometry(150, 100, 830, 600)
        self.window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_env = MyEnv()

    sys.exit(app.exec())

