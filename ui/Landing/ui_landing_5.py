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
        MainWindow.setStyleSheet(u"background-color: rgb(36, 36, 35);color:#fff;")
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -1476, 774, 1925))
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
        self.nav_indicator_1 = QRadioButton(self.horizontalWidget)
        self.nav_indicator_1.setObjectName(u"nav_indicator_1")
        sizePolicy1.setHeightForWidth(self.nav_indicator_1.sizePolicy().hasHeightForWidth())
        self.nav_indicator_1.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.nav_indicator_1)

        self.nav_indicator_2 = QRadioButton(self.horizontalWidget)
        self.nav_indicator_2.setObjectName(u"nav_indicator_2")
        sizePolicy1.setHeightForWidth(self.nav_indicator_2.sizePolicy().hasHeightForWidth())
        self.nav_indicator_2.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.nav_indicator_2)

        self.nav_indicator_3 = QRadioButton(self.horizontalWidget)
        self.nav_indicator_3.setObjectName(u"nav_indicator_3")
        sizePolicy1.setHeightForWidth(self.nav_indicator_3.sizePolicy().hasHeightForWidth())
        self.nav_indicator_3.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.nav_indicator_3)

        self.nav_indicator_4 = QRadioButton(self.horizontalWidget)
        self.nav_indicator_4.setObjectName(u"nav_indicator_4")
        sizePolicy1.setHeightForWidth(self.nav_indicator_4.sizePolicy().hasHeightForWidth())
        self.nav_indicator_4.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.nav_indicator_4)


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
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Terms and Conditions</span></p><p><br/></p><p><span style=\" font-weight:600;\">General Terms</span></p><p>By accessing and placing an order with My ENB, you confirm that you are in agreement with and bound by the terms of service contained in the Terms &amp; Conditions outlined below. These terms apply to the entire website and any email or other type of communication between you and My ENB</p><p>Under no circumstances shall My ENB team be liable for any direct, indirect, special, incidental or consequential damages, including. but not limited to, loss of data or profit, arising out of the use, or the inability to use, the materials on this site, even if My ENB team or an authorized representative has been advised of the possibility of such damages. If your use of materials from this site results in the need for servicing, repair or correction of equipment or data, you assume any costs thereof.</p><p>My ENB will not be responsible for any"
                        " outcome that may occur during the course of usage of our resources. We reserve the rights to change prices and reserve the change prices and revise the resources usage policy in any moment.</p><p><br/></p><p><span style=\" font-weight:600;\">License</span></p><p>My ENB grants you a revocable, non-exclusive, non- transferable, limited license to download, install and use the app strictly in accordance with the terms of this Agreement. These Terms &amp; Conditions are a contract between you and My ENB (we.&quot; *our,&quot; or</p><p>&quot;us&quot;) grants you a revocable, non-exclusive, non- transferable, limited license to download, install and use the app strictly in accordance with terms of this Agreement.</p><p><br/></p><p><span style=\" font-weight:600;\">Definitions and key terms</span></p><p>\u2022 Cookie: small amount of data generated by a website and saved by your web browser. It is used to identify your browser, provide analytics, remember information about you such as your language preference or log"
                        "in information.</p><p>\u2022 Company: when this policy mentions &quot;Company.&quot; &quot;we,&quot; *us,&quot; or &quot;our,&quot; it refers to My ENB that is responsible for your information under this Privacy Policy.</p><p>\u2022 Country: where My ENB or the owners/founders of My ENB are based, in this case is Canada.</p><p>\u2022 Customer: refers to the company, organization or person that signs up to use the My ENB Service to manage the relationships with your consumers or service users.</p><p>\u2022 Device: any internet connected device such as a phone, tablet, computer or any other device that can be used to visit My ENB and use the services.</p><p>\u2022 IP address: Every device connected to the Internet is assigned a number known as an Internet protocol (IP) address. These numbers are usually assigned in geographic blocks. An IP address can often be used to identify the location from which a device is connecting to the Internet.</p><p>Restrictions</p><p>You agree not to, and you will not permit others"
                        " to:</p><p>\u2022 License, sell, rent, lease, assign, distribute, transmit, host, outsource, disclose or otherwise commercially exploit the se make the platform available to any third party.</p><p>\u2022 Modify, make derivative works of, disassemble, decrypt, reverse compile or reverse engineer any part of the service.</p><p>\u2022 Remove, alter or obscure any proprietary notice (including any notice of copyright or trademark) of or its affiliates, partners or licensors of others. </p><p><br/></p><p><span style=\" font-weight:600;\">Contact us: </span></p><p>Don\u2019t hesitate to contact us if u have any questions.</p><p>Via the link: github.com/dhir0hit/my_env/issues</p><p><br/></p></body></html>", None))
        self.nav_indicator_1.setText("")
        self.nav_indicator_2.setText("")
        self.nav_indicator_3.setText("")
        self.nav_indicator_4.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Accept", None))
    # retranslateUi

