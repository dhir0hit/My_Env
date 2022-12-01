# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'saved.ui'
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
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(737, 640)
        Form.setStyleSheet(u"background-color: rgb(51, 53, 51);")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 15, -1, 15)
        self.horizontalFrame_4 = QFrame(Form)
        self.horizontalFrame_4.setObjectName(u"horizontalFrame_4")
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalFrame_4)
        self.horizontalLayout_5.setSpacing(22)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_1 = QLabel(self.horizontalFrame_4)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setStyleSheet(u"background-color: rgb(36, 36, 35);\n"
"font: 16pt \"Cambria\";\n"
"color:white;\n"
"border-radius:25%;")
        self.label_1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_1.setMargin(20)

        self.horizontalLayout_5.addWidget(self.label_1)

        self.label_2 = QLabel(self.horizontalFrame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background-color: rgb(36, 36, 35);\n"
"border-radius:25%;\n"
"font: 16pt \"Cambria\";\n"
"color:white;")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_2.setMargin(20)

        self.horizontalLayout_5.addWidget(self.label_2)


        self.horizontalLayout_4.addWidget(self.horizontalFrame_4)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalWidget = QWidget(Form)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalLayout = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 15, -1, 15)
        self.horizontalWidget_2 = QWidget(self.horizontalWidget)
        self.horizontalWidget_2.setObjectName(u"horizontalWidget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_2.setSpacing(22)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.horizontalWidget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"background-color: rgb(36, 36, 35);\n"
"border-radius:25%;\n"
"font: 16pt \"Cambria\";\n"
"color:white;\n"
"")
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_4.setMargin(20)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.label_3 = QLabel(self.horizontalWidget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background-color: rgb(36, 36, 35);\n"
"border-radius:25%;\n"
"font: 16pt \"Cambria\";\n"
"color:white;")
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_3.setMargin(20)

        self.horizontalLayout_2.addWidget(self.label_3)


        self.horizontalLayout.addWidget(self.horizontalWidget_2)


        self.verticalLayout.addWidget(self.horizontalWidget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_1.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

