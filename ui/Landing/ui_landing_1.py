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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)
import image_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(732, 591)
        MainWindow.setStyleSheet(u"background-color: rgb(36, 36, 35);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.info_container = QWidget(self.centralwidget)
        self.info_container.setObjectName(u"info_container")
        self.verticalLayout = QVBoxLayout(self.info_container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.heading = QLabel(self.info_container)
        self.heading.setObjectName(u"heading")
        font = QFont()
        font.setPointSize(40)
        self.heading.setFont(font)

        self.verticalLayout.addWidget(self.heading, 0, Qt.AlignHCenter)

        self.ImageContainer = QWidget(self.info_container)
        self.ImageContainer.setObjectName(u"ImageContainer")
        self.verticalLayout_5 = QVBoxLayout(self.ImageContainer)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.image = QLabel(self.ImageContainer)
        self.image.setObjectName(u"image")
        self.image.setMaximumSize(QSize(400, 400))
        self.image.setFrameShape(QFrame.NoFrame)
        self.image.setAlignment(Qt.AlignCenter)
        self.image.setMargin(29)

        self.verticalLayout_5.addWidget(self.image, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.ImageContainer)

        self.detail = QLabel(self.info_container)
        self.detail.setObjectName(u"detail")
        self.detail.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.detail)

        self.navigation_container = QWidget(self.info_container)
        self.navigation_container.setObjectName(u"navigation_container")
        self.verticalLayout_3 = QVBoxLayout(self.navigation_container)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.nav_indicator_container = QWidget(self.navigation_container)
        self.nav_indicator_container.setObjectName(u"nav_indicator_container")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nav_indicator_container.sizePolicy().hasHeightForWidth())
        self.nav_indicator_container.setSizePolicy(sizePolicy)
        self.nav_indicator_container.setMaximumSize(QSize(132, 31))
        self.horizontalLayout = QHBoxLayout(self.nav_indicator_container)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.nav_indicator_1 = QRadioButton(self.nav_indicator_container)
        self.nav_indicator_1.setObjectName(u"nav_indicator_1")
        sizePolicy.setHeightForWidth(self.nav_indicator_1.sizePolicy().hasHeightForWidth())
        self.nav_indicator_1.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.nav_indicator_1)

        self.nav_indicator_2 = QRadioButton(self.nav_indicator_container)
        self.nav_indicator_2.setObjectName(u"nav_indicator_2")
        sizePolicy.setHeightForWidth(self.nav_indicator_2.sizePolicy().hasHeightForWidth())
        self.nav_indicator_2.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.nav_indicator_2)

        self.nav_indicator_3 = QRadioButton(self.nav_indicator_container)
        self.nav_indicator_3.setObjectName(u"nav_indicator_3")
        sizePolicy.setHeightForWidth(self.nav_indicator_3.sizePolicy().hasHeightForWidth())
        self.nav_indicator_3.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.nav_indicator_3)

        self.nav_indicator_4 = QRadioButton(self.nav_indicator_container)
        self.nav_indicator_4.setObjectName(u"nav_indicator_4")
        sizePolicy.setHeightForWidth(self.nav_indicator_4.sizePolicy().hasHeightForWidth())
        self.nav_indicator_4.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.nav_indicator_4)


        self.verticalLayout_3.addWidget(self.nav_indicator_container, 0, Qt.AlignHCenter)

        self.button_container = QWidget(self.navigation_container)
        self.button_container.setObjectName(u"button_container")
        self.verticalLayout_4 = QVBoxLayout(self.button_container)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.next_button = QPushButton(self.button_container)
        self.next_button.setObjectName(u"next_button")
        sizePolicy.setHeightForWidth(self.next_button.sizePolicy().hasHeightForWidth())
        self.next_button.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        self.next_button.setFont(font1)
        self.next_button.setLayoutDirection(Qt.RightToLeft)
        self.next_button.setAutoFillBackground(False)
        self.next_button.setStyleSheet(u"background-color: rgb(245, 203, 92);\n"
"alternate-background-color: rgb(245, 203, 92);\n"
"color: rgb(36, 36, 35);")
        icon = QIcon()
        icon.addFile(u":/resources/arrow_forward_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.next_button.setIcon(icon)
        self.next_button.setIconSize(QSize(24, 17))

        self.verticalLayout_4.addWidget(self.next_button)


        self.verticalLayout_3.addWidget(self.button_container, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.navigation_container)


        self.verticalLayout_2.addWidget(self.info_container)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.next_button.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.heading.setText(QCoreApplication.translate("MainWindow", u"Welcome to My Env", None))
        self.image.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/resources/deer_logo_template_dark_flat_handdrawn_design_6854205.jpg\" width='250'/></p></body></html>", None))
        self.detail.setText(QCoreApplication.translate("MainWindow", u"An Enviroment for you to have all your stuff in one place", None))
        self.nav_indicator_1.setText("")
        self.nav_indicator_2.setText("")
        self.nav_indicator_3.setText("")
        self.nav_indicator_4.setText("")
        self.next_button.setText(QCoreApplication.translate("MainWindow", u"Next", None))
    # retranslateUi

