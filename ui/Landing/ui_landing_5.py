# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Landing-5[UserAgreement].ui'
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
    QPushButton, QRadioButton, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(811, 611)
        MainWindow.setStyleSheet(u"background-color: rgb(36, 36, 35);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(30)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 795, 449))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(14)
        self.label_2.setFont(font1)
        self.label_2.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.verticalWidget = QWidget(self.centralwidget)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.verticalWidget.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_2 = QVBoxLayout(self.verticalWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 1, -1, -1)
        self.horizontalWidget = QWidget(self.verticalWidget)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy1)
        self.horizontalLayout = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 1, -1, -1)
        self.radioButton_3 = QRadioButton(self.horizontalWidget)
        self.radioButton_3.setObjectName(u"radioButton_3")
        sizePolicy1.setHeightForWidth(self.radioButton_3.sizePolicy().hasHeightForWidth())
        self.radioButton_3.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.horizontalWidget)
        self.radioButton_4.setObjectName(u"radioButton_4")
        sizePolicy1.setHeightForWidth(self.radioButton_4.sizePolicy().hasHeightForWidth())
        self.radioButton_4.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.radioButton_4)

        self.radioButton_2 = QRadioButton(self.horizontalWidget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        sizePolicy1.setHeightForWidth(self.radioButton_2.sizePolicy().hasHeightForWidth())
        self.radioButton_2.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.radioButton_2)

        self.radioButton = QRadioButton(self.horizontalWidget)
        self.radioButton.setObjectName(u"radioButton")
        sizePolicy1.setHeightForWidth(self.radioButton.sizePolicy().hasHeightForWidth())
        self.radioButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.radioButton)


        self.verticalLayout_2.addWidget(self.horizontalWidget, 0, Qt.AlignHCenter)

        self.pushButton = QPushButton(self.verticalWidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        self.pushButton.setFont(font2)
        self.pushButton.setLayoutDirection(Qt.RightToLeft)
        self.pushButton.setStyleSheet(u"background-color: rgb(245, 203, 92);\n"
"alternate-background-color: rgb(245, 203, 92);\n"
"color: rgb(36, 36, 35);")
        icon = QIcon()
        icon.addFile(u":/resources/done_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(20, 20))
        self.pushButton.setCheckable(False)

        self.verticalLayout_2.addWidget(self.pushButton, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.verticalWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"User Agreement", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Lacinia quis vel eros donec ac odio tempor. Pulvinar elementum integer enim neque volutpat ac tincidunt vitae semper. Tellus orci ac auctor augue mauris augue neque gravida in. Sit amet nisl purus in. Non pulvinar neque laoreet suspendisse interdum. Tempus quam pellentesque nec nam. Nunc faucibus a pellentesque sit. Dui vivamus arcu felis bibendum. Ac tincidunt vitae semper quis lectus. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Lacinia quis vel eros donec ac odio tempor. Pulvinar elementum integer enim neque volutpat ac tincidunt vitae semper. Tellus orci ac auctor augue mauris augue neque gravida in. Sit amet nisl purus in. Non pulvinar neque laoreet suspendisse interdum. Tempus quam p", None))
        self.radioButton_3.setText("")
        self.radioButton_4.setText("")
        self.radioButton_2.setText("")
        self.radioButton.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Accept", None))
    # retranslateUi

