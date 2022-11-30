from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QMainWindow)

from ui.PasswordManager.ui_passwordManager_dashboard import Ui_password_manager_dashboard

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)
import image_rc

class MainWindow(QMainWindow):
    def __init__(self, window):
        super(MainWindow, self).__init__()
        print("[+] Opened Password Manager")

        self.upper_class = window
        self.Window = window.Window

    def run(self):
        """
        Run the app
        add elements in app
        """

        # password manager dashboard container in UI
        self.password_manager_dashboard = Ui_password_manager_dashboard()
        self.password_manager_dashboard.setupUi(self.Window.current_app_container)

        self.Window.verticalLayout_7.addWidget(self.password_manager_dashboard.password_manager_container)

        # Add item in favorite container
        self.password_manager_dashboard.FavoriteScrollContainer.addWidget(self.addAccount())
        # self.upper_class.password_manager()


    def addAccount(self):
        account_container = QWidget()
        if not account_container.objectName():
            account_container.setObjectName(u"Form")
        account_container.resize(607, 120)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(account_container.sizePolicy().hasHeightForWidth())
        account_container.setSizePolicy(sizePolicy)
        account_container.setStyleSheet(u"background-color: rgb(51, 53, 51);")
        horizontalLayout = QHBoxLayout(account_container)
        horizontalLayout.setSpacing(20)
        horizontalLayout.setObjectName(u"horizontalLayout")
        horizontalLayout.setContentsMargins(10, 10, 10, 10)
        label = QLabel(account_container)
        label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(label.sizePolicy().hasHeightForWidth())
        label.setSizePolicy(sizePolicy1)

        horizontalLayout.addWidget(label)

        verticalWidget = QWidget(account_container)
        verticalWidget.setObjectName(u"verticalWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(verticalWidget.sizePolicy().hasHeightForWidth())
        verticalWidget.setSizePolicy(sizePolicy2)
        verticalLayout = QVBoxLayout(verticalWidget)
        verticalLayout.setObjectName(u"verticalLayout")
        label_3 = QLabel(verticalWidget)
        label_3.setObjectName(u"label_3")

        verticalLayout.addWidget(label_3)

        label_2 = QLabel(verticalWidget)
        label_2.setObjectName(u"label_2")

        verticalLayout.addWidget(label_2)


        horizontalLayout.addWidget(verticalWidget)

        QMetaObject.connectSlotsByName(account_container)
        label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><img src=\":/resources/deer_logo_template_dark_flat_handdrawn_design_6854205.jpg\" wdith=\"100\" height=\"100\"/></p></body></html>", None))
        label_3.setText(QCoreApplication.translate("Form", u"__Platform__", None))
        label_2.setText(QCoreApplication.translate("Form", u"__Email__", None))

        return account_container
