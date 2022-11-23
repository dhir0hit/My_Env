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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget)
import image_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(51, 53, 51);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top_bar = QWidget(self.centralwidget)
        self.top_bar.setObjectName(u"top_bar")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_bar.sizePolicy().hasHeightForWidth())
        self.top_bar.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.top_bar)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, 5, 20, 5)
        self.app_name = QLabel(self.top_bar)
        self.app_name.setObjectName(u"app_name")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.app_name.setFont(font)
        self.app_name.setStyleSheet(u"color: rgb(245, 203, 92);")

        self.horizontalLayout.addWidget(self.app_name)

        self.current_app = QLabel(self.top_bar)
        self.current_app.setObjectName(u"current_app")
        font1 = QFont()
        font1.setPointSize(16)
        self.current_app.setFont(font1)

        self.horizontalLayout.addWidget(self.current_app, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.top_bar)

        self.main_body = QWidget(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setStyleSheet(u"background-color: rgb(36, 36, 35);")
        self.verticalLayout_2 = QVBoxLayout(self.main_body)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.scrollArea = QScrollArea(self.main_body)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 772, 482))
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
        # self.chat_bot_1 = QLabel(self.chat)
        # self.chat_bot_1.setObjectName(u"chat_bot_1")
        # self.chat_bot_1.setStyleSheet(u"background-color: rgb(51, 53, 51);")
        # self.chat_bot_1.setWordWrap(True)
        # self.chat_bot_1.setMargin(6)
        #
        # self.verticalLayout_4.addWidget(self.chat_bot_1, 0, Qt.AlignLeft)
        #
        # self.user_1 = QLabel(self.chat)
        # self.user_1.setObjectName(u"user_1")
        # self.user_1.setStyleSheet(u"background-color: rgb(51, 53, 51);")
        # self.user_1.setWordWrap(True)
        # self.user_1.setMargin(6)
        #
        # self.verticalLayout_4.addWidget(self.user_1, 0, Qt.AlignRight)


        self.verticalLayout_3.addWidget(self.chat, 0, Qt.AlignBottom)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.input_bar = QWidget(self.main_body)
        self.input_bar.setObjectName(u"input_bar")
        self.horizontalLayout_2 = QHBoxLayout(self.input_bar)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 1, -1, -1)
        self.lineEdit = QLineEdit(self.input_bar)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(True)
        self.lineEdit.setMinimumSize(QSize(0, 36))
        self.lineEdit.setSizeIncrement(QSize(0, 0))
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet(u"color: rgb(245, 203, 92);\n"
"background-color: rgb(51, 53, 51);")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.send = QPushButton(self.input_bar)
        self.send.setObjectName(u"send")
        self.send.setMinimumSize(QSize(0, 36))
        self.send.setStyleSheet(u"color: rgb(245, 203, 92);\n"
"background-color: rgb(51, 53, 51);")
        icon = QIcon()
        icon.addFile(u":/resources/subdirectory_arrow_left_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.send.setIcon(icon)
        self.send.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.send)


        self.verticalLayout_2.addWidget(self.input_bar)


        self.verticalLayout.addWidget(self.main_body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.app_name.setText(QCoreApplication.translate("MainWindow", u"My Env", None))
        self.current_app.setText(QCoreApplication.translate("MainWindow", u"ChatBot", None))
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type Here...", None))
        self.send.setText("")
    # retranslateUi

