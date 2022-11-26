# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'container.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSlider, QVBoxLayout, QWidget)
import image_rc

class Ui_Container(object):
    def setupUi(self, parent):
        self.container = QWidget(parent)
        if not self.container.objectName():
            self.container.setObjectName(u"Form")
        self.container.resize(483, 300)
        self.verticalLayout = QVBoxLayout(self.container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.container = QWidget(self.container)
        self.container.setObjectName(u"container")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.container.sizePolicy().hasHeightForWidth())
        self.container.setSizePolicy(sizePolicy)
        self.container.setMaximumSize(QSize(16777215, 300))
        self.container.setSizeIncrement(QSize(0, 0))
        self.horizontalLayout_4 = QHBoxLayout(self.container)
        self.horizontalLayout_4.setSpacing(15)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.music_container = QWidget(self.container)
        self.music_container.setObjectName(u"music_container")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.music_container.sizePolicy().hasHeightForWidth())
        self.music_container.setSizePolicy(sizePolicy1)
        self.music_container.setMaximumSize(QSize(16777215, 16777215))
        self.music_container.setStyleSheet(u"background-color: rgb(36, 36, 35);")
        self.verticalLayout_9 = QVBoxLayout(self.music_container)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(15, 15, 15, 15)
        self.music_name = QLabel(self.music_container)
        self.music_name.setObjectName(u"music_name")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.music_name.sizePolicy().hasHeightForWidth())
        self.music_name.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setPointSize(16)
        self.music_name.setFont(font)

        self.verticalLayout_9.addWidget(self.music_name)

        self.singer_name = QLabel(self.music_container)
        self.singer_name.setObjectName(u"singer_name")
        sizePolicy2.setHeightForWidth(self.singer_name.sizePolicy().hasHeightForWidth())
        self.singer_name.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setPointSize(10)
        self.singer_name.setFont(font1)

        self.verticalLayout_9.addWidget(self.singer_name)

        self.player_buttons_container = QWidget(self.music_container)
        self.player_buttons_container.setObjectName(u"player_buttons_container")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.player_buttons_container.sizePolicy().hasHeightForWidth())
        self.player_buttons_container.setSizePolicy(sizePolicy3)
        self.horizontalLayout_5 = QHBoxLayout(self.player_buttons_container)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_5 = QPushButton(self.player_buttons_container)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"border: none;")
        icon = QIcon()
        icon.addFile(u":/resources/skip_previous_FILL1_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QSize(30, 30))

        self.horizontalLayout_5.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.player_buttons_container)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setStyleSheet(u"border: none;")
        icon1 = QIcon()
        icon1.addFile(u":/resources/play_arrow_FILL1_wght400_GRAD0_opsz48(1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon1)
        self.pushButton_6.setIconSize(QSize(45, 45))

        self.horizontalLayout_5.addWidget(self.pushButton_6)

        self.pushButton_4 = QPushButton(self.player_buttons_container)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"border: none;")
        icon2 = QIcon()
        icon2.addFile(u":/resources/skip_next_FILL1_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QSize(30, 30))

        self.horizontalLayout_5.addWidget(self.pushButton_4)


        self.verticalLayout_9.addWidget(self.player_buttons_container, 0, Qt.AlignHCenter)

        self.player_progress = QSlider(self.music_container)
        self.player_progress.setObjectName(u"player_progress")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.player_progress.sizePolicy().hasHeightForWidth())
        self.player_progress.setSizePolicy(sizePolicy4)
        self.player_progress.setStyleSheet(u"color: rgb(245, 203, 92);\n"
"\n"
"")
        self.player_progress.setOrientation(Qt.Horizontal)

        self.verticalLayout_9.addWidget(self.player_progress)


        self.horizontalLayout_4.addWidget(self.music_container)

        self.sub_container = QWidget(self.container)
        self.sub_container.setObjectName(u"sub_container")
        self.verticalLayout_10 = QVBoxLayout(self.sub_container)
        self.verticalLayout_10.setSpacing(15)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.weather_container = QWidget(self.sub_container)
        self.weather_container.setObjectName(u"weather_container")
        self.weather_container.setStyleSheet(u"background-color: rgb(36, 36, 35);")
        self.horizontalLayout_6 = QHBoxLayout(self.weather_container)
        self.horizontalLayout_6.setSpacing(15)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(15, 15, 15, 15)
        self.weather_info = QWidget(self.weather_container)
        self.weather_info.setObjectName(u"weather_info")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.weather_info.sizePolicy().hasHeightForWidth())
        self.weather_info.setSizePolicy(sizePolicy5)
        self.verticalLayout_11 = QVBoxLayout(self.weather_info)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(1, -1, -1, -1)
        self.weather_temp = QLabel(self.weather_info)
        self.weather_temp.setObjectName(u"weather_temp")
        font2 = QFont()
        font2.setPointSize(25)
        self.weather_temp.setFont(font2)

        self.verticalLayout_11.addWidget(self.weather_temp)

        self.weather_place = QLabel(self.weather_info)
        self.weather_place.setObjectName(u"weather_place")

        self.verticalLayout_11.addWidget(self.weather_place)


        self.horizontalLayout_6.addWidget(self.weather_info)

        self.weather_logo = QLabel(self.weather_container)
        self.weather_logo.setObjectName(u"weather_logo")

        self.horizontalLayout_6.addWidget(self.weather_logo, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.weather_container)

        self.chatbot_container = QWidget(self.sub_container)
        self.chatbot_container.setObjectName(u"chatbot_container")
        self.chatbot_container.setStyleSheet(u"background-color: rgb(36, 36, 35);")
        self.horizontalLayout_7 = QHBoxLayout(self.chatbot_container)
        self.horizontalLayout_7.setSpacing(15)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(15, 15, 15, 15)
        self.chatbot_logo = QLabel(self.chatbot_container)
        self.chatbot_logo.setObjectName(u"chatbot_logo")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.chatbot_logo.sizePolicy().hasHeightForWidth())
        self.chatbot_logo.setSizePolicy(sizePolicy6)

        self.horizontalLayout_7.addWidget(self.chatbot_logo)

        self.chatbot_info = QWidget(self.chatbot_container)
        self.chatbot_info.setObjectName(u"chatbot_info")
        self.verticalLayout_12 = QVBoxLayout(self.chatbot_info)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.chatbot_name = QLabel(self.chatbot_info)
        self.chatbot_name.setObjectName(u"chatbot_name")
        font3 = QFont()
        font3.setPointSize(15)
        self.chatbot_name.setFont(font3)

        self.verticalLayout_12.addWidget(self.chatbot_name)

        self.chatbot_button = QPushButton(self.chatbot_info)
        self.chatbot_button.setObjectName(u"chatbot_button")
        self.chatbot_button.setStyleSheet(u"border: none;\n"
"padding-top: 5;\n"
"padding-right: 10;\n"
"padding-bottom:  5;\n"
"padding-left: 10;\n"
"background-color: rgb(245, 203, 92);\n"
"color: rgb(51, 53, 51);")

        self.verticalLayout_12.addWidget(self.chatbot_button)


        self.horizontalLayout_7.addWidget(self.chatbot_info)


        self.verticalLayout_10.addWidget(self.chatbot_container)


        self.horizontalLayout_4.addWidget(self.sub_container)


        self.verticalLayout.addWidget(self.container)


        self.retranslateUi(self.container)

        QMetaObject.connectSlotsByName(self.container)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.music_name.setText(QCoreApplication.translate("Form", u"Music Name Written", None))
        self.singer_name.setText(QCoreApplication.translate("Form", u"Music Singer Name", None))
        self.pushButton_5.setText("")
        self.pushButton_6.setText("")
        self.pushButton_4.setText("")
        self.weather_temp.setText(QCoreApplication.translate("Form", u"20 C", None))
        self.weather_place.setText(QCoreApplication.translate("Form", u"Brampton, ON", None))
        self.weather_logo.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><img src=\":/resources/partly_cloudy_day_FILL0_wght400_GRAD0_opsz48.svg\"/></p></body></html>", None))
        self.chatbot_logo.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><img src=\":/resources/smart_toy_FILL0_wght400_GRAD0_opsz48.svg\"/></p></body></html>", None))
        self.chatbot_name.setText(QCoreApplication.translate("Form", u"Chat Bot", None))
        self.chatbot_button.setText(QCoreApplication.translate("Form", u"Chat With Me...", None))
    # retranslateUi

