# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)
import image_rc

class Ui_MainWindow(object):
    def __init__(self):
        self.send = None
        self.chatbot_container = None

    def setupUi(self, parent):
        self.window = QWidget(parent)
        self.window.setObjectName(u"window")
        self.window.resize(800, 600)
        self.chatbot_container = QWidget(self.window)
        self.chatbot_container.setObjectName(u"chatbot_container")
        self.chatbot_container.setStyleSheet(u"background-color: rgb(51, 53, 51);")
        self.verticalLayout = QVBoxLayout(self.chatbot_container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.main_body = QWidget(self.chatbot_container)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setStyleSheet(u"background-color: rgb(36, 36, 35);")
        self.verticalLayout_2 = QVBoxLayout(self.main_body)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.scrollArea = QScrollArea(self.main_body)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"border: \"none\";")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 776, 532))
        self.scrollAreaWidgetContents.setLayoutDirection(Qt.LeftToRight)
        self.scrollAreaWidgetContents.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, 20, 20, 20)
        self.chat = QWidget(self.scrollAreaWidgetContents)
        self.chat.setObjectName(u"chat")
        self.verticalLayout_4 = QVBoxLayout(self.chat)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")

        self.verticalLayout_3.addWidget(self.chat, 0, Qt.AlignBottom)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.input_bar = QWidget(self.main_body)
        self.input_bar.setObjectName(u"input_bar")
        self.input_bar.setStyleSheet(u"background-color: rgb(51, 53, 51);")
        self.horizontalLayout_2 = QHBoxLayout(self.input_bar)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 1, -1, 1)
        self.lineEdit = QLineEdit(self.input_bar)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(True)
        self.lineEdit.setMinimumSize(QSize(0, 36))
        self.lineEdit.setSizeIncrement(QSize(0, 0))
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet(u"color: rgb(245, 203, 92);\n"
"background-color: rgb(51, 53, 51);\n"
"border: \"none\";")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.send = QPushButton(self.input_bar)
        self.send.setObjectName(u"send")
        self.send.setMinimumSize(QSize(0, 36))
        self.send.setStyleSheet(u"color: rgb(245, 203, 92);\n"
"background-color: rgb(51, 53, 51);\n"
"padding: 5;\n"
"border: none;")
        icon = QIcon()
        icon.addFile(u":/resources/subdirectory_arrow_left_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.send.setIcon(icon)
        self.send.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.send)


        self.verticalLayout_2.addWidget(self.input_bar)


        self.verticalLayout.addWidget(self.main_body)

        # parent.setCentralWidget(self.chatbot_container)

        self.retranslateUi(self.window)

        QMetaObject.connectSlotsByName(self.window)
    # setupUi

    def retranslateUi(self, parent):
        self.window.setWindowTitle(QCoreApplication.translate("parent", u"parent", None))
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("parent", u"Type Here...", None))
        self.send.setText("")
    # retranslateUi

