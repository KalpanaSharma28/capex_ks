# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'capexqJIRdu.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QPushButton,
    QSizePolicy, QSpacerItem, QTableView, QVBoxLayout,
    QWidget)

class Ui_Form_capex(object):
    def setupUi(self, Form_capex):
        if not Form_capex.objectName():
            Form_capex.setObjectName(u"Form_capex")
        Form_capex.resize(275, 247)
        self.verticalLayout_2 = QVBoxLayout(Form_capex)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableView = QTableView(Form_capex)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_create = QPushButton(Form_capex)
        self.button_create.setObjectName(u"button_create")

        self.horizontalLayout.addWidget(self.button_create)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.button_submit = QPushButton(Form_capex)
        self.button_submit.setObjectName(u"button_submit")

        self.horizontalLayout.addWidget(self.button_submit)

        self.button_close = QPushButton(Form_capex)
        self.button_close.setObjectName(u"button_close")

        self.horizontalLayout.addWidget(self.button_close)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form_capex)

        QMetaObject.connectSlotsByName(Form_capex)
    # setupUi

    def retranslateUi(self, Form_capex):
        Form_capex.setWindowTitle(QCoreApplication.translate("Form_capex", u"Capex", None))
        self.button_create.setText(QCoreApplication.translate("Form_capex", u"Create", None))
        self.button_submit.setText(QCoreApplication.translate("Form_capex", u"Submit", None))
        self.button_close.setText(QCoreApplication.translate("Form_capex", u"Close", None))
    # retranslateUi

