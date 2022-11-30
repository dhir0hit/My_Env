# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PasswordManager.ui'
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
    QScrollArea, QSizePolicy, QVBoxLayout, QWidget)
import image_rc

class Ui_password_manager_dashboard(object):
    def setupUi(self, parent):
        self.password_manager_container = QWidget(parent)
        if not self.password_manager_container.objectName():
            self.password_manager_container.setObjectName(u"password_manager_container")
        self.password_manager_container.resize(955, 670)
        self.password_manager_container.setStyleSheet(u"background-color: rgb(51, 53, 51);")
        self.verticalLayout = QVBoxLayout(self.password_manager_container)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.top_container = QWidget(self.password_manager_container)
        self.top_container.setObjectName(u"top_container")
        self.horizontalLayout = QHBoxLayout(self.top_container)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.favorite_scroll_container = QScrollArea(self.top_container)
        self.favorite_scroll_container.setObjectName(u"favorite_scroll_container")
        self.favorite_scroll_container.setStyleSheet(u"border:  \"none\";\n"
"background-color: rgb(36, 36, 35);")
        self.favorite_scroll_container.setWidgetResizable(True)
        self.favorite_scroll_area = QWidget()
        self.favorite_scroll_area.setObjectName(u"favorite_scroll_area")
        self.favorite_scroll_area.setGeometry(QRect(0, 0, 452, 279))
        self.FavoriteScrollContainer = QVBoxLayout(self.favorite_scroll_area)
        self.FavoriteScrollContainer.setObjectName(u"verticalLayout_14")
        # self.label_13 = QLabel(self.favorite_scroll_area)
        # self.label_13.setObjectName(u"label_13")
        #
        # self.verticalLayout_14.addWidget(self.label_13)

        self.favorite_scroll_container.setWidget(self.favorite_scroll_area)

        self.horizontalLayout.addWidget(self.favorite_scroll_container)

        self.top_sub_container = QWidget(self.top_container)
        self.top_sub_container.setObjectName(u"top_sub_container")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_sub_container.sizePolicy().hasHeightForWidth())
        self.top_sub_container.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.top_sub_container)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.favorite_info_container = QWidget(self.top_sub_container)
        self.favorite_info_container.setObjectName(u"favorite_info_container")
        self.favorite_info_container.setStyleSheet(u"background-color: rgb(36, 36, 35);")
        self.verticalLayout_4 = QVBoxLayout(self.favorite_info_container)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(15, 15, 20, 15)
        self.label = QLabel(self.favorite_info_container)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(30)
        self.label.setFont(font)

        self.verticalLayout_4.addWidget(self.label, 0, Qt.AlignRight)

        self.account_count_contaienr = QWidget(self.favorite_info_container)
        self.account_count_contaienr.setObjectName(u"account_count_contaienr")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.account_count_contaienr.sizePolicy().hasHeightForWidth())
        self.account_count_contaienr.setSizePolicy(sizePolicy1)
        self.horizontalLayout_3 = QHBoxLayout(self.account_count_contaienr)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.FavoriteAccounts = QLabel(self.account_count_contaienr)
        self.FavoriteAccounts.setObjectName(u"FavoriteAccounts")
        font1 = QFont()
        font1.setPointSize(12)
        self.FavoriteAccounts.setFont(font1)

        self.horizontalLayout_3.addWidget(self.FavoriteAccounts)

        self.accounts = QLabel(self.account_count_contaienr)
        self.accounts.setObjectName(u"accounts")
        self.accounts.setFont(font1)

        self.horizontalLayout_3.addWidget(self.accounts)


        self.verticalLayout_4.addWidget(self.account_count_contaienr, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.favorite_info_container)

        self.top_sub_sub_container = QWidget(self.top_sub_container)
        self.top_sub_sub_container.setObjectName(u"top_sub_sub_container")
        self.top_sub_sub_container.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.top_sub_sub_container)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(20, 0, 0, 0)
        self.total_account_container = QWidget(self.top_sub_sub_container)
        self.total_account_container.setObjectName(u"total_account_container")
        self.total_account_container.setStyleSheet(u"background-color: rgb(36, 36, 35);")
        self.verticalLayout_8 = QVBoxLayout(self.total_account_container)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(15, 15, 20, 15)
        self.total_acounts = QLabel(self.total_account_container)
        self.total_acounts.setObjectName(u"total_acounts")
        font2 = QFont()
        font2.setPointSize(25)
        self.total_acounts.setFont(font2)

        self.verticalLayout_8.addWidget(self.total_acounts)

        self.total_account_sub_container = QWidget(self.total_account_container)
        self.total_account_sub_container.setObjectName(u"total_account_sub_container")
        self.horizontalLayout_4 = QHBoxLayout(self.total_account_sub_container)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.TotalAccounts = QLabel(self.total_account_sub_container)
        self.TotalAccounts.setObjectName(u"TotalAccounts")
        self.TotalAccounts.setFont(font1)

        self.horizontalLayout_4.addWidget(self.TotalAccounts)

        self.total_accounts_button = QPushButton(self.total_account_sub_container)
        self.total_accounts_button.setObjectName(u"total_accounts_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.total_accounts_button.sizePolicy().hasHeightForWidth())
        self.total_accounts_button.setSizePolicy(sizePolicy2)
        self.total_accounts_button.setMinimumSize(QSize(180, 0))
        font3 = QFont()
        font3.setPointSize(10)
        self.total_accounts_button.setFont(font3)
        self.total_accounts_button.setStyleSheet(u"background-color: rgb(245, 203, 92);\n"
"color: rgb(36, 36, 35);\n"
"border: \"none\";\n"
"padding: 4;")

        self.horizontalLayout_4.addWidget(self.total_accounts_button)


        self.verticalLayout_8.addWidget(self.total_account_sub_container)


        self.verticalLayout_5.addWidget(self.total_account_container)


        self.verticalLayout_2.addWidget(self.top_sub_sub_container)


        self.horizontalLayout.addWidget(self.top_sub_container)


        self.verticalLayout.addWidget(self.top_container)

        self.bottom_container = QWidget(self.password_manager_container)
        self.bottom_container.setObjectName(u"bottom_container")
        self.bottom_container.setStyleSheet(u"QScrollBar {\n"
"	 background: rgb(207, 219, 213)\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.bottom_container)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 1)
        self.filter_scroll_container = QScrollArea(self.bottom_container)
        self.filter_scroll_container.setObjectName(u"filter_scroll_container")
        self.filter_scroll_container.setStyleSheet(u"border:  \"none\";\n"
"background-color: rgb(36, 36, 35);\n"
"\n"
"QScrollbar {\n"
"	\n"
"	background-color: rgb(245, 203, 92);\n"
"}")
        self.filter_scroll_container.setWidgetResizable(True)
        self.filter_scroll_area = QWidget()
        self.filter_scroll_area.setObjectName(u"filter_scroll_area")
        self.filter_scroll_area.setGeometry(QRect(0, 0, 452, 312))
        self.filter_scroll_area.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.filter_scroll_area)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.filter_container = QWidget(self.filter_scroll_area)
        self.filter_container.setObjectName(u"filter_container")
        self.verticalLayout_12 = QVBoxLayout(self.filter_container)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(5, 5, 5, 5)
        self.new_filter_container = QWidget(self.filter_container)
        self.new_filter_container.setObjectName(u"new_filter_container")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.new_filter_container.sizePolicy().hasHeightForWidth())
        self.new_filter_container.setSizePolicy(sizePolicy3)
        self.new_filter_container.setStyleSheet(u"background-color: rgb(51, 53, 51);")
        self.horizontalLayout_8 = QHBoxLayout(self.new_filter_container)
        self.horizontalLayout_8.setSpacing(20)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 10, 10, 10)
        self.NewAccounts = QLabel(self.new_filter_container)
        self.NewAccounts.setObjectName(u"NewAccounts")
        sizePolicy1.setHeightForWidth(self.NewAccounts.sizePolicy().hasHeightForWidth())
        self.NewAccounts.setSizePolicy(sizePolicy1)
        font4 = QFont()
        font4.setPointSize(18)
        self.NewAccounts.setFont(font4)

        self.horizontalLayout_8.addWidget(self.NewAccounts)

        self.new_container = QWidget(self.new_filter_container)
        self.new_container.setObjectName(u"new_container")
        font5 = QFont()
        font5.setPointSize(15)
        self.new_container.setFont(font5)
        self.verticalLayout_13 = QVBoxLayout(self.new_container)
        self.verticalLayout_13.setSpacing(10)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.new_2 = QLabel(self.new_container)
        self.new_2.setObjectName(u"new_2")
        self.new_2.setFont(font4)

        self.verticalLayout_13.addWidget(self.new_2)

        self.navigate_new = QPushButton(self.new_container)
        self.navigate_new.setObjectName(u"navigate_new")
        self.navigate_new.setFont(font5)
        self.navigate_new.setStyleSheet(u"background-color: rgb(245, 203, 92);\n"
"color: rgb(36, 36, 35);\n"
"padding: 3;")

        self.verticalLayout_13.addWidget(self.navigate_new)


        self.horizontalLayout_8.addWidget(self.new_container)


        self.verticalLayout_12.addWidget(self.new_filter_container)

        self.favorite_filter_container = QWidget(self.filter_container)
        self.favorite_filter_container.setObjectName(u"favorite_filter_container")
        sizePolicy3.setHeightForWidth(self.favorite_filter_container.sizePolicy().hasHeightForWidth())
        self.favorite_filter_container.setSizePolicy(sizePolicy3)
        self.favorite_filter_container.setStyleSheet(u"background-color: rgb(51, 53, 51);")
        self.horizontalLayout_7 = QHBoxLayout(self.favorite_filter_container)
        self.horizontalLayout_7.setSpacing(20)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 10, 10, 10)
        self.FavoriteAccounts_2 = QLabel(self.favorite_filter_container)
        self.FavoriteAccounts_2.setObjectName(u"FavoriteAccounts_2")
        sizePolicy1.setHeightForWidth(self.FavoriteAccounts_2.sizePolicy().hasHeightForWidth())
        self.FavoriteAccounts_2.setSizePolicy(sizePolicy1)
        self.FavoriteAccounts_2.setFont(font4)

        self.horizontalLayout_7.addWidget(self.FavoriteAccounts_2)

        self.favorite_sub_container = QWidget(self.favorite_filter_container)
        self.favorite_sub_container.setObjectName(u"favorite_sub_container")
        self.verticalLayout_11 = QVBoxLayout(self.favorite_sub_container)
        self.verticalLayout_11.setSpacing(10)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.favorite = QLabel(self.favorite_sub_container)
        self.favorite.setObjectName(u"favorite")
        font6 = QFont()
        font6.setPointSize(16)
        self.favorite.setFont(font6)

        self.verticalLayout_11.addWidget(self.favorite)

        self.navigate_favorite = QPushButton(self.favorite_sub_container)
        self.navigate_favorite.setObjectName(u"navigate_favorite")
        self.navigate_favorite.setFont(font5)
        self.navigate_favorite.setStyleSheet(u"background-color: rgb(245, 203, 92);\n"
"color: rgb(36, 36, 35);\n"
"padding: 3;")

        self.verticalLayout_11.addWidget(self.navigate_favorite)


        self.horizontalLayout_7.addWidget(self.favorite_sub_container)


        self.verticalLayout_12.addWidget(self.favorite_filter_container)


        self.verticalLayout_10.addWidget(self.filter_container)

        self.filter_scroll_container.setWidget(self.filter_scroll_area)

        self.horizontalLayout_2.addWidget(self.filter_scroll_container)

        self.verticalWidget_2 = QWidget(self.bottom_container)
        self.verticalWidget_2.setObjectName(u"verticalWidget_2")
        sizePolicy.setHeightForWidth(self.verticalWidget_2.sizePolicy().hasHeightForWidth())
        self.verticalWidget_2.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalWidget_3 = QWidget(self.verticalWidget_2)
        self.verticalWidget_3.setObjectName(u"verticalWidget_3")
        self.verticalLayout_6 = QVBoxLayout(self.verticalWidget_3)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(19, 0, 0, 0)
        self.verticalWidget = QWidget(self.verticalWidget_3)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.verticalWidget.setStyleSheet(u"background-color: rgb(36, 36, 35);")
        self.verticalLayout_9 = QVBoxLayout(self.verticalWidget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(15, 15, 20, 15)
        self.label_6 = QLabel(self.verticalWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.verticalLayout_9.addWidget(self.label_6)

        self.horizontalWidget = QWidget(self.verticalWidget)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_2 = QPushButton(self.horizontalWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(180, 0))
        self.pushButton_2.setFont(font3)
        self.pushButton_2.setStyleSheet(u"background-color: rgb(245, 203, 92);\n"
"color: rgb(36, 36, 35);\n"
"border: \"none\";\n"
"padding: 4;")

        self.horizontalLayout_5.addWidget(self.pushButton_2)


        self.verticalLayout_9.addWidget(self.horizontalWidget, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.verticalWidget)


        self.verticalLayout_3.addWidget(self.verticalWidget_3)

        self.verticalWidget_4 = QWidget(self.verticalWidget_2)
        self.verticalWidget_4.setObjectName(u"verticalWidget_4")
        self.verticalWidget_4.setStyleSheet(u"background-color: rgb(36, 36, 35);")
        self.verticalLayout_7 = QVBoxLayout(self.verticalWidget_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(15, 15, 20, 15)
        self.horizontalWidget1 = QWidget(self.verticalWidget_4)
        self.horizontalWidget1.setObjectName(u"horizontalWidget1")
        sizePolicy2.setHeightForWidth(self.horizontalWidget1.sizePolicy().hasHeightForWidth())
        self.horizontalWidget1.setSizePolicy(sizePolicy2)
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalWidget1)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_8 = QLabel(self.horizontalWidget1)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font3)

        self.horizontalLayout_6.addWidget(self.label_8)


        self.verticalLayout_7.addWidget(self.horizontalWidget1, 0, Qt.AlignRight)

        self.label_7 = QLabel(self.verticalWidget_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.verticalLayout_7.addWidget(self.label_7, 0, Qt.AlignRight)


        self.verticalLayout_3.addWidget(self.verticalWidget_4)


        self.horizontalLayout_2.addWidget(self.verticalWidget_2)


        self.verticalLayout.addWidget(self.bottom_container)


        self.retranslateUi(self.password_manager_container)

        QMetaObject.connectSlotsByName(self.password_manager_container)
    # setupUi

    def retranslateUi(self, password_manager_container):
        password_manager_container.setWindowTitle(QCoreApplication.translate("password_manager_container", u"Form", None))
        self.label.setText(QCoreApplication.translate("password_manager_container", u"Favorite Accounts", None))
        self.FavoriteAccounts.setText(QCoreApplication.translate("password_manager_container", u"999", None))
        self.accounts.setText(QCoreApplication.translate("password_manager_container", u"accounts", None))
        self.total_acounts.setText(QCoreApplication.translate("password_manager_container", u"Total Accounts", None))
        self.TotalAccounts.setText(QCoreApplication.translate("password_manager_container", u"999", None))
        self.total_accounts_button.setText(QCoreApplication.translate("password_manager_container", u"Show Accounts", None))
        self.NewAccounts.setText(QCoreApplication.translate("password_manager_container", u"999", None))
        self.new_2.setText(QCoreApplication.translate("password_manager_container", u"New", None))
        self.navigate_new.setText(QCoreApplication.translate("password_manager_container", u"Navigate", None))
        self.FavoriteAccounts_2.setText(QCoreApplication.translate("password_manager_container", u"<html><head/><body><p>999</p></body></html>", None))
        self.favorite.setText(QCoreApplication.translate("password_manager_container", u"Favorite", None))
        self.navigate_favorite.setText(QCoreApplication.translate("password_manager_container", u"Navigate", None))
        self.label_6.setText(QCoreApplication.translate("password_manager_container", u"Create Accounts", None))
        self.pushButton_2.setText(QCoreApplication.translate("password_manager_container", u"Create", None))
        self.label_8.setText(QCoreApplication.translate("password_manager_container", u"Different kind of filter are applied to help find accounts", None))
        self.label_7.setText(QCoreApplication.translate("password_manager_container", u"Filters", None))
    # retranslateUi