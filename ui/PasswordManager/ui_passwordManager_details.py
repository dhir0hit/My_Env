# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PasswordManager_Details.ui'
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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import image_rc

class Ui_password_manager_detail(object):
    def setupUi(self, parent):
        self.account_detail_container = QWidget(parent)
        if not self.account_detail_container.objectName():
            self.account_detail_container.setObjectName(u"Form")
        self.account_detail_container.resize(711, 446)
        self.account_detail_container.setStyleSheet(u"background-color: rgb(36, 36, 35);")
        self.verticalLayout_2 = QVBoxLayout(self.account_detail_container)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 15, 15, 15)
        self.top_info_container = QWidget(self.account_detail_container)
        self.top_info_container.setObjectName(u"top_info_container")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_info_container.sizePolicy().hasHeightForWidth())
        self.top_info_container.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.top_info_container)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.icon = QLabel(self.top_info_container)
        self.icon.setObjectName(u"icon")
        self.icon.setMinimumSize(QSize(0, 0))
        self.icon.setMaximumSize(QSize(150, 150))
        self.icon.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.icon)

        self.top_sub_container = QWidget(self.top_info_container)
        self.top_sub_container.setObjectName(u"top_sub_container")
        self.verticalLayout = QVBoxLayout(self.top_sub_container)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self._platform = QLabel(self.top_sub_container)
        self._platform.setObjectName(u"_platform")
        font = QFont()
        font.setPointSize(30)
        self._platform.setFont(font)

        self.verticalLayout.addWidget(self._platform)

        self._id = QLabel(self.top_sub_container)
        self._id.setObjectName(u"_id")
        font1 = QFont()
        font1.setPointSize(8)
        self._id.setFont(font1)

        self.verticalLayout.addWidget(self._id, 0, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.top_sub_container)


        self.verticalLayout_2.addWidget(self.top_info_container)

        self.line = QFrame(self.account_detail_container)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.main_container = QWidget(self.account_detail_container)
        self.main_container.setObjectName(u"main_container")
        sizePolicy.setHeightForWidth(self.main_container.sizePolicy().hasHeightForWidth())
        self.main_container.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.main_container)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.username_top_container = QWidget(self.main_container)
        self.username_top_container.setObjectName(u"username_top_container")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.username_top_container.sizePolicy().hasHeightForWidth())
        self.username_top_container.setSizePolicy(sizePolicy1)
        self.horizontalLayout_2 = QHBoxLayout(self.username_top_container)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self._username = QLabel(self.username_top_container)
        self._username.setObjectName(u"_username")
        font2 = QFont()
        font2.setPointSize(15)
        self._username.setFont(font2)

        self.horizontalLayout_2.addWidget(self._username)

        self.pushButton = QPushButton(self.username_top_container)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"border: \"none\";\n"
"padding: 6;")
        icon1 = QIcon()
        icon1.addFile(u":/resources/content_copy_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(17, 17))

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout_3.addWidget(self.username_top_container)

        self.Username = QLabel(self.main_container)
        self.Username.setObjectName(u"Username")
        font3 = QFont()
        font3.setPointSize(10)
        self.Username.setFont(font3)

        self.verticalLayout_3.addWidget(self.Username)

        self.password_top_container = QWidget(self.main_container)
        self.password_top_container.setObjectName(u"password_top_container")
        sizePolicy1.setHeightForWidth(self.password_top_container.sizePolicy().hasHeightForWidth())
        self.password_top_container.setSizePolicy(sizePolicy1)
        self.horizontalLayout_3 = QHBoxLayout(self.password_top_container)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self._password = QLabel(self.password_top_container)
        self._password.setObjectName(u"_password")
        self._password.setFont(font2)

        self.horizontalLayout_3.addWidget(self._password)

        self.PasswordCopyButton = QPushButton(self.password_top_container)
        self.PasswordCopyButton.setObjectName(u"PasswordCopyButton")
        self.PasswordCopyButton.setStyleSheet(u"border: \"none\";\n"
"padding: 6;")
        self.PasswordCopyButton.setIcon(icon1)
        self.PasswordCopyButton.setIconSize(QSize(17, 17))

        self.horizontalLayout_3.addWidget(self.PasswordCopyButton)


        self.verticalLayout_3.addWidget(self.password_top_container)

        self.password_container = QWidget(self.main_container)
        self.password_container.setObjectName(u"password_container")
        self.horizontalLayout_4 = QHBoxLayout(self.password_container)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.Password = QLabel(self.password_container)
        self.Password.setObjectName(u"Password")
        self.Password.setFont(font3)

        self.horizontalLayout_4.addWidget(self.Password)

        self.ShowPassword = QPushButton(self.password_container)
        self.ShowPassword.setObjectName(u"ShowPassword")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ShowPassword.sizePolicy().hasHeightForWidth())
        self.ShowPassword.setSizePolicy(sizePolicy2)
        self.ShowPassword.setStyleSheet(u"border: \"none\";\n"
"padding: 5;")
        icon2 = QIcon()
        icon2.addFile(u":/resources/visibility_FILL1_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ShowPassword.setIcon(icon2)
        self.ShowPassword.setIconSize(QSize(16, 16))

        self.horizontalLayout_4.addWidget(self.ShowPassword)


        self.verticalLayout_3.addWidget(self.password_container)


        self.verticalLayout_2.addWidget(self.main_container)

        self.line_2 = QFrame(self.account_detail_container)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.bottom_container = QWidget(self.account_detail_container)
        self.bottom_container.setObjectName(u"bottom_container")
        self.verticalLayout_4 = QVBoxLayout(self.bottom_container)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.website_container = QWidget(self.bottom_container)
        self.website_container.setObjectName(u"website_container")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.website_container.sizePolicy().hasHeightForWidth())
        self.website_container.setSizePolicy(sizePolicy3)
        self.verticalLayout_5 = QVBoxLayout(self.website_container)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self._website = QLabel(self.website_container)
        self._website.setObjectName(u"_website")
        self._website.setFont(font2)

        self.verticalLayout_5.addWidget(self._website)

        self.Website = QLabel(self.website_container)
        self.Website.setObjectName(u"Website")
        self.Website.setFont(font3)

        self.verticalLayout_5.addWidget(self.Website)


        self.verticalLayout_4.addWidget(self.website_container, 0, Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.bottom_container)


        self.retranslateUi(self.account_detail_container)

        QMetaObject.connectSlotsByName(self.account_detail_container)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.icon.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><img src=\":/resources/deer_logo_template_dark_flat_handdrawn_design_6854205.jpg\" width=\"150\" height=\"150\" /></p></body></html>", None))
        self._platform.setText(QCoreApplication.translate("Form", u"Platform", None))
        self._id.setText(QCoreApplication.translate("Form", u"Id", None))
        self._username.setText(QCoreApplication.translate("Form", u"Username", None))
        self.pushButton.setText("")
        self.Username.setText(QCoreApplication.translate("Form", u"__username__", None))
        self._password.setText(QCoreApplication.translate("Form", u"Password", None))
        self.PasswordCopyButton.setText("")
        self.Password.setText(QCoreApplication.translate("Form", u"__password__", None))
        self.ShowPassword.setText("")
        self._website.setText(QCoreApplication.translate("Form", u"Website", None))
        self.Website.setText(QCoreApplication.translate("Form", u"__website__", None))
    # retranslateUi

