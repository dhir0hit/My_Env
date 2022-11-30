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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import image_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 658)
        MainWindow.setStyleSheet(u"background-color: rgb(36, 36, 35);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 2)
        self.body_container = QWidget(self.centralwidget)
        self.body_container.setObjectName(u"body_container")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.body_container.sizePolicy().hasHeightForWidth())
        self.body_container.setSizePolicy(sizePolicy)
        self.body_container.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.body_container)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.side_nav_container = QWidget(self.body_container)
        self.side_nav_container.setObjectName(u"side_nav_container")
        self.side_nav_container.setMaximumSize(QSize(265, 16777215))
        self.verticalLayout = QVBoxLayout(self.side_nav_container)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.user_info_container = QWidget(self.side_nav_container)
        self.user_info_container.setObjectName(u"user_info_container")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.user_info_container.sizePolicy().hasHeightForWidth())
        self.user_info_container.setSizePolicy(sizePolicy1)
        self.user_info_container.setStyleSheet(u"background-color: rgb(51, 53, 51);")
        self.verticalLayout_4 = QVBoxLayout(self.user_info_container)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(16, 16, 16, 16)
        self.user_initials = QLabel(self.user_info_container)
        self.user_initials.setObjectName(u"user_initials")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.user_initials.sizePolicy().hasHeightForWidth())
        self.user_initials.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setPointSize(30)
        self.user_initials.setFont(font)
        self.user_initials.setStyleSheet(u"background-color: rgb(245, 203, 92);\n"
"border-radius:8;\n"
"color: rgb(51, 53, 51);")
        self.user_initials.setMargin(4)

        self.verticalLayout_4.addWidget(self.user_initials, 0, Qt.AlignRight)

        self.user_name = QLabel(self.user_info_container)
        self.user_name.setObjectName(u"user_name")
        font1 = QFont()
        font1.setPointSize(20)
        self.user_name.setFont(font1)
        self.user_name.setStyleSheet(u"color: rgb(232, 237, 223);")

        self.verticalLayout_4.addWidget(self.user_name)

        self.user_mail = QLabel(self.user_info_container)
        self.user_mail.setObjectName(u"user_mail")
        font2 = QFont()
        font2.setPointSize(10)
        self.user_mail.setFont(font2)

        self.verticalLayout_4.addWidget(self.user_mail)


        self.verticalLayout.addWidget(self.user_info_container)

        self.navigation_container = QWidget(self.side_nav_container)
        self.navigation_container.setObjectName(u"navigation_container")
        self.navigation_container.setStyleSheet(u"background-color: rgb(51, 53, 51);\n"
"")
        self.verticalLayout_5 = QVBoxLayout(self.navigation_container)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, 10, 10, 10)
        self.navigation = QWidget(self.navigation_container)
        self.navigation.setObjectName(u"navigation")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.navigation.sizePolicy().hasHeightForWidth())
        self.navigation.setSizePolicy(sizePolicy3)
        self.verticalLayout_6 = QVBoxLayout(self.navigation)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.nav_dashboard = QPushButton(self.navigation)
        self.nav_dashboard.setObjectName(u"nav_dashboard")
        sizePolicy1.setHeightForWidth(self.nav_dashboard.sizePolicy().hasHeightForWidth())
        self.nav_dashboard.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setPointSize(14)
        self.nav_dashboard.setFont(font3)
        self.nav_dashboard.setStyleSheet(u"border: none;\n"
"background-color: rgb(36, 36, 35);\n"
"padding: 3;")
        icon = QIcon()
        icon.addFile(u":/resources/dashboard_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.nav_dashboard.setIcon(icon)
        self.nav_dashboard.setIconSize(QSize(20, 20))

        self.verticalLayout_6.addWidget(self.nav_dashboard)

        self.nav_notes = QPushButton(self.navigation)
        self.nav_notes.setObjectName(u"nav_notes")
        sizePolicy1.setHeightForWidth(self.nav_notes.sizePolicy().hasHeightForWidth())
        self.nav_notes.setSizePolicy(sizePolicy1)
        self.nav_notes.setFont(font3)
        self.nav_notes.setStyleSheet(u"border: none;\n"
"padding: 3;")
        icon1 = QIcon()
        icon1.addFile(u":/resources/note_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.nav_notes.setIcon(icon1)
        self.nav_notes.setIconSize(QSize(20, 20))

        self.verticalLayout_6.addWidget(self.nav_notes)

        self.nav_pass_manager = QPushButton(self.navigation)
        self.nav_pass_manager.setObjectName(u"nav_pass_manager")
        self.nav_pass_manager.setFont(font3)
        self.nav_pass_manager.setStyleSheet(u"border: none;\n"
"padding: 3;")
        icon2 = QIcon()
        icon2.addFile(u":/resources/lock_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.nav_pass_manager.setIcon(icon2)
        self.nav_pass_manager.setIconSize(QSize(20, 20))

        self.verticalLayout_6.addWidget(self.nav_pass_manager)

        self.nav_weather = QPushButton(self.navigation)
        self.nav_weather.setObjectName(u"nav_weather")
        self.nav_weather.setFont(font3)
        self.nav_weather.setStyleSheet(u"border: none;\n"
"padding: 3;")
        icon3 = QIcon()
        icon3.addFile(u":/resources/cloud_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.nav_weather.setIcon(icon3)
        self.nav_weather.setIconSize(QSize(20, 20))

        self.verticalLayout_6.addWidget(self.nav_weather)

        self.nav_music_player = QPushButton(self.navigation)
        self.nav_music_player.setObjectName(u"nav_music_player")
        self.nav_music_player.setFont(font3)
        self.nav_music_player.setStyleSheet(u"border: none;\n"
"padding: 3;")
        icon4 = QIcon()
        icon4.addFile(u":/resources/music_note_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.nav_music_player.setIcon(icon4)
        self.nav_music_player.setIconSize(QSize(20, 20))

        self.verticalLayout_6.addWidget(self.nav_music_player)

        self.nav_chat_bot = QPushButton(self.navigation)
        self.nav_chat_bot.setObjectName(u"nav_chat_bot")
        self.nav_chat_bot.setFont(font3)
        self.nav_chat_bot.setStyleSheet(u"border: none;\n"
"padding: 3;")
        icon5 = QIcon()
        icon5.addFile(u":/resources/smart_toy_.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.nav_chat_bot.setIcon(icon5)
        self.nav_chat_bot.setIconSize(QSize(20, 20))

        self.verticalLayout_6.addWidget(self.nav_chat_bot)


        self.verticalLayout_5.addWidget(self.navigation, 0, Qt.AlignTop)


        self.verticalLayout.addWidget(self.navigation_container)


        self.horizontalLayout.addWidget(self.side_nav_container)

        self.main_container = QWidget(self.body_container)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setStyleSheet(u"background-color: rgb(51, 53, 51);")
        self.verticalLayout_3 = QVBoxLayout(self.main_container)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.top_nav = QWidget(self.main_container)
        self.top_nav.setObjectName(u"top_nav")
        sizePolicy1.setHeightForWidth(self.top_nav.sizePolicy().hasHeightForWidth())
        self.top_nav.setSizePolicy(sizePolicy1)
        self.top_nav.setStyleSheet(u"border-style: solid;\n"
"border-width: 2;\n"
"border-bottom-color: rgb(36, 36, 35);")
        self.horizontalLayout_3 = QHBoxLayout(self.top_nav)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(20, 11, 20, 11)
        self.app_name = QLabel(self.top_nav)
        self.app_name.setObjectName(u"app_name")
        font4 = QFont()
        font4.setPointSize(20)
        font4.setBold(True)
        self.app_name.setFont(font4)
        self.app_name.setStyleSheet(u"border: none;\n"
"color: rgb(245, 203, 92);")

        self.horizontalLayout_3.addWidget(self.app_name)

        self.current_app_name = QLabel(self.top_nav)
        self.current_app_name.setObjectName(u"current_app_name")
        self.current_app_name.setFont(font1)
        self.current_app_name.setLayoutDirection(Qt.LeftToRight)
        self.current_app_name.setStyleSheet(u"border: none;")

        self.horizontalLayout_3.addWidget(self.current_app_name, 0, Qt.AlignRight)


        self.verticalLayout_3.addWidget(self.top_nav)

        self.current_app_container = QWidget(self.main_container)
        self.current_app_container.setObjectName(u"current_app_container")
        self.verticalLayout_7 = QVBoxLayout(self.current_app_container)
        self.verticalLayout_7.setSpacing(15)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(15, 15, 15, 15)

        self.verticalLayout_3.addWidget(self.current_app_container)


        self.horizontalLayout.addWidget(self.main_container)


        self.verticalLayout_2.addWidget(self.body_container)

        self.extra_buttons = QWidget(self.centralwidget)
        self.extra_buttons.setObjectName(u"extra_buttons")
        sizePolicy2.setHeightForWidth(self.extra_buttons.sizePolicy().hasHeightForWidth())
        self.extra_buttons.setSizePolicy(sizePolicy2)
        self.horizontalLayout_2 = QHBoxLayout(self.extra_buttons)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.profile = QPushButton(self.extra_buttons)
        self.profile.setObjectName(u"profile")
        self.profile.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.profile.sizePolicy().hasHeightForWidth())
        self.profile.setSizePolicy(sizePolicy1)
        self.profile.setMaximumSize(QSize(16777215, 16777215))
        self.profile.setStyleSheet(u"background-color: rgb(51, 53, 51);\n"
"border: \"none\";\n"
"padding-top: 2;\n"
"padding-right: 12;\n"
"padding-bottom:  2;\n"
"padding-left: 12;\n"
"selection-background-color: rgb(36, 36, 35);")
        icon6 = QIcon()
        icon6.addFile(u":/resources/edit_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.profile.setIcon(icon6)
        self.profile.setIconSize(QSize(16, 16))
        self.profile.setCheckable(False)

        self.horizontalLayout_2.addWidget(self.profile)

        self.settings = QPushButton(self.extra_buttons)
        self.settings.setObjectName(u"settings")
        sizePolicy1.setHeightForWidth(self.settings.sizePolicy().hasHeightForWidth())
        self.settings.setSizePolicy(sizePolicy1)
        self.settings.setMaximumSize(QSize(16777215, 16777215))
        self.settings.setStyleSheet(u"background-color: rgb(51, 53, 51);\n"
"border: \"none\";\n"
"padding-top: 2;\n"
"padding-right: 12;\n"
"padding-bottom:  2;\n"
"padding-left: 12;\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/resources/settings_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settings.setIcon(icon7)

        self.horizontalLayout_2.addWidget(self.settings)


        self.verticalLayout_2.addWidget(self.extra_buttons, 0, Qt.AlignRight)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.profile.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"My Env", None))
        self.user_initials.setText(QCoreApplication.translate("MainWindow", u"UN", None))
        self.user_name.setText(QCoreApplication.translate("MainWindow", u"User_Name", None))
        self.user_mail.setText(QCoreApplication.translate("MainWindow", u"mail@mail.com", None))
        self.nav_dashboard.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.nav_notes.setText(QCoreApplication.translate("MainWindow", u"Notes", None))
        self.nav_pass_manager.setText(QCoreApplication.translate("MainWindow", u"Password Manager", None))
        self.nav_weather.setText(QCoreApplication.translate("MainWindow", u"Weather", None))
        self.nav_music_player.setText(QCoreApplication.translate("MainWindow", u"Music Player", None))
        self.nav_chat_bot.setText(QCoreApplication.translate("MainWindow", u"Chat Bot", None))
        self.app_name.setText(QCoreApplication.translate("MainWindow", u"My Env", None))
        self.current_app_name.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.profile.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

