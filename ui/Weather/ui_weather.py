# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'weather.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_WeatherApp(object):
    def setupUi(self, parent):
        self.weather_app_container = QWidget(parent)
        if not self.weather_app_container.objectName():
            self.weather_app_container.setObjectName(u"Form")
        self.weather_app_container.resize(870, 681)
        self.weather_app_container.setStyleSheet(u"background-color: rgb(51, 53, 51);")
        self.verticalLayout = QVBoxLayout(self.weather_app_container)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(25, 20, 25, 20)
        self.Firstone = QWidget(self.weather_app_container)
        self.Firstone.setObjectName(u"Firstone")
        self.Firstone.setLayoutDirection(Qt.LeftToRight)
        self.Firstone.setStyleSheet(u"background-color: rgb(36, 36, 35);\n"
"\n"
"border-bottom-left-radius:25%;\n"
"border-top-right-radius:160%;\n"
"border-bottom-right-radius:13%;")
        self.verticalLayout_3 = QVBoxLayout(self.Firstone)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(1, -1, 1, -1)
        self.horizontalWidget = QWidget(self.Firstone)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalWidget.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(1, -1, -1, -1)
        self.temp = QLabel(self.horizontalWidget)
        self.temp.setObjectName(u"temp")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.temp.sizePolicy().hasHeightForWidth())
        self.temp.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Cambria Math"])
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        self.temp.setFont(font)
        self.temp.setStyleSheet(u"\n"
"font: 22pt \"Cambria Math\";\n"
"color:white;\n"
"")
        self.temp.setMargin(10)

        self.horizontalLayout_2.addWidget(self.temp)

        self.city = QLabel(self.horizontalWidget)
        self.city.setObjectName(u"city")
        self.city.setStyleSheet(u"font: 16pt \"Cambria\";\n"
"color:white;\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.city.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.city.setMargin(45)

        self.horizontalLayout_2.addWidget(self.city)


        self.verticalLayout_3.addWidget(self.horizontalWidget)


        self.verticalLayout.addWidget(self.Firstone)

        self.SeconDone = QWidget(self.weather_app_container)
        self.SeconDone.setObjectName(u"SeconDone")
        self.SeconDone.setStyleSheet(u"background-color: rgb(51, 53, 51);")
        self.verticalLayout_2 = QVBoxLayout(self.SeconDone)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(1, -1, 1, -1)
        self.verticalWidget = QWidget(self.SeconDone)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.verticalWidget.setStyleSheet(u"background-color: rgb(36, 36, 35);\n"
"border-radius:25%;")
        self.verticalLayout_5 = QVBoxLayout(self.verticalWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.description = QLabel(self.verticalWidget)
        self.description.setObjectName(u"description")
        self.description.setStyleSheet(u"color:white;\n"
"font: 22pt \"Cambria\";")
        self.description.setMargin(10)

        self.verticalLayout_5.addWidget(self.description)

        self.date = QLabel(self.verticalWidget)
        self.date.setObjectName(u"date")
        self.date.setStyleSheet(u"color:white;\n"
"font: 16pt \"Cambria\";")
        self.date.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.date.setMargin(10)

        self.verticalLayout_5.addWidget(self.date)


        self.verticalLayout_2.addWidget(self.verticalWidget)


        self.verticalLayout.addWidget(self.SeconDone)

        self.thirdone = QWidget(self.weather_app_container)
        self.thirdone.setObjectName(u"thirdone")
        self.horizontalLayout = QHBoxLayout(self.thirdone)
        self.horizontalLayout.setSpacing(27)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(1, -1, 1, -1)
        self.Wind = QWidget(self.thirdone)
        self.Wind.setObjectName(u"Wind")
        self.verticalLayout_6 = QVBoxLayout(self.Wind)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalWidget_2 = QWidget(self.Wind)
        self.verticalWidget_2.setObjectName(u"verticalWidget_2")
        self.verticalWidget_2.setStyleSheet(u"background-color: rgb(36, 36, 35);\n"
"border-radius:13%;")
        self.verticalLayout_7 = QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.wind = QLabel(self.verticalWidget_2)
        self.wind.setObjectName(u"wind")
        self.wind.setStyleSheet(u"font: 20pt \"Cambria\";\n"
"color:white;")
        self.wind.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.wind)

        self.windspeed = QLabel(self.verticalWidget_2)
        self.windspeed.setObjectName(u"windspeed")
        self.windspeed.setStyleSheet(u"font: 16pt \"Cambria\";\n"
"color:white;")
        self.windspeed.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.windspeed)


        self.verticalLayout_6.addWidget(self.verticalWidget_2)


        self.horizontalLayout.addWidget(self.Wind)

        self.Humidity = QWidget(self.thirdone)
        self.Humidity.setObjectName(u"Humidity")
        self.verticalLayout_8 = QVBoxLayout(self.Humidity)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalWidget_3 = QWidget(self.Humidity)
        self.verticalWidget_3.setObjectName(u"verticalWidget_3")
        self.verticalWidget_3.setStyleSheet(u"background-color: rgb(36, 36, 35);\n"
"border-radius:13%;")
        self.verticalLayout_9 = QVBoxLayout(self.verticalWidget_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.humd = QLabel(self.verticalWidget_3)
        self.humd.setObjectName(u"humd")
        self.humd.setStyleSheet(u"font: 20pt \"Cambria\";\n"
"color:white;")
        self.humd.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.humd)

        self.humdpercentage = QLabel(self.verticalWidget_3)
        self.humdpercentage.setObjectName(u"humdpercentage")
        self.humdpercentage.setStyleSheet(u"font: 16pt \"Cambria\";\n"
"color:white;")
        self.humdpercentage.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.humdpercentage)


        self.verticalLayout_8.addWidget(self.verticalWidget_3)


        self.horizontalLayout.addWidget(self.Humidity)

        self.Precepitation = QWidget(self.thirdone)
        self.Precepitation.setObjectName(u"Precepitation")
        self.verticalLayout_4 = QVBoxLayout(self.Precepitation)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalWidget_4 = QWidget(self.Precepitation)
        self.verticalWidget_4.setObjectName(u"verticalWidget_4")
        self.verticalWidget_4.setStyleSheet(u"background-color: rgb(36, 36, 35);\n"
"border-radius:13%;")
        self.verticalLayout_10 = QVBoxLayout(self.verticalWidget_4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.precp = QLabel(self.verticalWidget_4)
        self.precp.setObjectName(u"precp")
        self.precp.setStyleSheet(u"font: 20pt \"Cambria\";\n"
"color:white;")
        self.precp.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.precp)

        self.precppercentage = QLabel(self.verticalWidget_4)
        self.precppercentage.setObjectName(u"precppercentage")
        self.precppercentage.setStyleSheet(u"font: 16pt \"Cambria\";\n"
"color:white;")
        self.precppercentage.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.precppercentage)


        self.verticalLayout_4.addWidget(self.verticalWidget_4)


        self.horizontalLayout.addWidget(self.Precepitation)


        self.verticalLayout.addWidget(self.thirdone)


        self.retranslateUi(self.weather_app_container)

        QMetaObject.connectSlotsByName(self.weather_app_container)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.temp.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.city.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.description.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.date.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.wind.setText(QCoreApplication.translate("Form", u"Wind ", None))
        self.windspeed.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.humd.setText(QCoreApplication.translate("Form", u" Humidity ", None))
        self.humdpercentage.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.precp.setText(QCoreApplication.translate("Form", u" Precepitation ", None))
        self.precppercentage.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

