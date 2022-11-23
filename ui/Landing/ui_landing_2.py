# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Landing-2.ui'
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
    QPushButton, QRadioButton, QSizePolicy, QVBoxLayout,
    QWidget)
import image_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(832, 531)
        MainWindow.setStyleSheet(u"background-color: rgb(36, 36, 35);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.landingpage_container = QWidget(self.centralwidget)
        self.landingpage_container.setObjectName(u"landingpage_container")
        self.verticalLayout_2 = QVBoxLayout(self.landingpage_container)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ltop_container = QWidget(self.landingpage_container)
        self.ltop_container.setObjectName(u"ltop_container")
        self.ltop_container.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout_2 = QHBoxLayout(self.ltop_container)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.image = QLabel(self.ltop_container)
        self.image.setObjectName(u"image")

        self.horizontalLayout_2.addWidget(self.image, 0, Qt.AlignHCenter)

        self.info_container = QWidget(self.ltop_container)
        self.info_container.setObjectName(u"info_container")
        self.info_container.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_5 = QVBoxLayout(self.info_container)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, -1, -1, -1)
        self.heading = QLabel(self.info_container)
        self.heading.setObjectName(u"heading")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.heading.sizePolicy().hasHeightForWidth())
        self.heading.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(30)
        self.heading.setFont(font)

        self.verticalLayout_5.addWidget(self.heading)

        self.details = QLabel(self.info_container)
        self.details.setObjectName(u"details")
        sizePolicy.setHeightForWidth(self.details.sizePolicy().hasHeightForWidth())
        self.details.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(13)
        self.details.setFont(font1)

        self.verticalLayout_5.addWidget(self.details)


        self.horizontalLayout_2.addWidget(self.info_container)


        self.verticalLayout_2.addWidget(self.ltop_container)

        self.navigation_container = QWidget(self.landingpage_container)
        self.navigation_container.setObjectName(u"navigation_container")
        sizePolicy.setHeightForWidth(self.navigation_container.sizePolicy().hasHeightForWidth())
        self.navigation_container.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(self.navigation_container)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.nav_indicator_container = QWidget(self.navigation_container)
        self.nav_indicator_container.setObjectName(u"nav_indicator_container")
        self.horizontalLayout = QHBoxLayout(self.nav_indicator_container)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.nav_indicator_1 = QRadioButton(self.nav_indicator_container)
        self.nav_indicator_1.setObjectName(u"nav_indicator_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.nav_indicator_1.sizePolicy().hasHeightForWidth())
        self.nav_indicator_1.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.nav_indicator_1)

        self.nav_indicator_2 = QRadioButton(self.nav_indicator_container)
        self.nav_indicator_2.setObjectName(u"nav_indicator_2")
        sizePolicy1.setHeightForWidth(self.nav_indicator_2.sizePolicy().hasHeightForWidth())
        self.nav_indicator_2.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.nav_indicator_2)

        self.nav_indicator_3 = QRadioButton(self.nav_indicator_container)
        self.nav_indicator_3.setObjectName(u"nav_indicator_3")
        sizePolicy1.setHeightForWidth(self.nav_indicator_3.sizePolicy().hasHeightForWidth())
        self.nav_indicator_3.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.nav_indicator_3)

        self.nav_indicator_4 = QRadioButton(self.nav_indicator_container)
        self.nav_indicator_4.setObjectName(u"nav_indicator_4")
        sizePolicy1.setHeightForWidth(self.nav_indicator_4.sizePolicy().hasHeightForWidth())
        self.nav_indicator_4.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.nav_indicator_4)


        self.verticalLayout_4.addWidget(self.nav_indicator_container, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.next_button = QPushButton(self.navigation_container)
        self.next_button.setObjectName(u"next_button")
        sizePolicy1.setHeightForWidth(self.next_button.sizePolicy().hasHeightForWidth())
        self.next_button.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(12)
        self.next_button.setFont(font2)
        self.next_button.setLayoutDirection(Qt.RightToLeft)
        self.next_button.setStyleSheet(u"background-color: rgb(245, 203, 92);\n"
"color: rgb(36, 36, 35);")
        icon = QIcon()
        icon.addFile(u":/resources/arrow_forward_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.next_button.setIcon(icon)
        self.next_button.setIconSize(QSize(24, 16))

        self.verticalLayout_4.addWidget(self.next_button, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.navigation_container)


        self.verticalLayout.addWidget(self.landingpage_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.image.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/resources/deer_logo_template_dark_flat_handdrawn_design_6854205.jpg\" width='370'/></p></body></html>", None))
        self.heading.setText(QCoreApplication.translate("MainWindow", u"Password Manager", None))
        self.details.setText(QCoreApplication.translate("MainWindow", u"Save your Password \n"
"in Password Manager within My Env \n"
"\n"
"Your Password will be dafe within our Password \n"
"Manager with perfect encryption of password", None))
        self.nav_indicator_1.setText("")
        self.nav_indicator_2.setText("")
        self.nav_indicator_3.setText("")
        self.nav_indicator_4.setText("")
        self.next_button.setText(QCoreApplication.translate("MainWindow", u"Next", None))
    # retranslateUi

