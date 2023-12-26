# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindoweCoCZV.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMdiArea, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QToolBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionApprover = QAction(MainWindow)
        self.actionApprover.setObjectName(u"actionApprover")
        self.actionArea = QAction(MainWindow)
        self.actionArea.setObjectName(u"actionArea")
        self.actionCategory = QAction(MainWindow)
        self.actionCategory.setObjectName(u"actionCategory")
        self.actionCurrency = QAction(MainWindow)
        self.actionCurrency.setObjectName(u"actionCurrency")
        self.actionExpType = QAction(MainWindow)
        self.actionExpType.setObjectName(u"actionExpType")
        self.actionFrequency = QAction(MainWindow)
        self.actionFrequency.setObjectName(u"actionFrequency")
        self.actionLocation = QAction(MainWindow)
        self.actionLocation.setObjectName(u"actionLocation")
        self.actionNature = QAction(MainWindow)
        self.actionNature.setObjectName(u"actionNature")
        self.actionOrigin = QAction(MainWindow)
        self.actionOrigin.setObjectName(u"actionOrigin")
        self.actionRecommendation = QAction(MainWindow)
        self.actionRecommendation.setObjectName(u"actionRecommendation")
        self.actionStatus = QAction(MainWindow)
        self.actionStatus.setObjectName(u"actionStatus")
        self.actionSubcategory = QAction(MainWindow)
        self.actionSubcategory.setObjectName(u"actionSubcategory")
        self.actionUOM = QAction(MainWindow)
        self.actionUOM.setObjectName(u"actionUOM")
        self.actionVendor = QAction(MainWindow)
        self.actionVendor.setObjectName(u"actionVendor")
        self.actionUnit = QAction(MainWindow)
        self.actionUnit.setObjectName(u"actionUnit")
        self.actionCapex = QAction(MainWindow)
        self.actionCapex.setObjectName(u"actionCapex")
        icon = QIcon()
        icon.addFile(u"icons/Dev.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCapex.setIcon(icon)
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        icon1 = QIcon()
        icon1.addFile(u"icons/close.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionClose.setIcon(icon1)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.mdiArea = QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName(u"mdiArea")

        self.verticalLayout.addWidget(self.mdiArea)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuCapex = QMenu(self.menubar)
        self.menuCapex.setObjectName(u"menuCapex")
        self.menuOptions = QMenu(self.menubar)
        self.menuOptions.setObjectName(u"menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuCapex.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menuCapex.addAction(self.actionCapex)
        self.menuCapex.addAction(self.actionClose)
        self.menuOptions.addAction(self.actionApprover)
        self.menuOptions.addAction(self.actionArea)
        self.menuOptions.addAction(self.actionCategory)
        self.menuOptions.addAction(self.actionCurrency)
        self.menuOptions.addAction(self.actionExpType)
        self.menuOptions.addAction(self.actionFrequency)
        self.menuOptions.addAction(self.actionLocation)
        self.menuOptions.addAction(self.actionNature)
        self.menuOptions.addAction(self.actionOrigin)
        self.menuOptions.addAction(self.actionRecommendation)
        self.menuOptions.addAction(self.actionStatus)
        self.menuOptions.addAction(self.actionSubcategory)
        self.menuOptions.addAction(self.actionUnit)
        self.menuOptions.addAction(self.actionUOM)
        self.menuOptions.addAction(self.actionVendor)
        self.toolBar.addAction(self.actionCapex)
        self.toolBar.addAction(self.actionClose)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Capex Application", None))
        self.actionApprover.setText(QCoreApplication.translate("MainWindow", u"Approver", None))
        self.actionArea.setText(QCoreApplication.translate("MainWindow", u"Area", None))
        self.actionCategory.setText(QCoreApplication.translate("MainWindow", u"Category", None))
        self.actionCurrency.setText(QCoreApplication.translate("MainWindow", u"Currency", None))
        self.actionExpType.setText(QCoreApplication.translate("MainWindow", u"ExpType", None))
        self.actionFrequency.setText(QCoreApplication.translate("MainWindow", u"Frequency", None))
        self.actionLocation.setText(QCoreApplication.translate("MainWindow", u"Location", None))
        self.actionNature.setText(QCoreApplication.translate("MainWindow", u"Nature", None))
        self.actionOrigin.setText(QCoreApplication.translate("MainWindow", u"Origin", None))
        self.actionRecommendation.setText(QCoreApplication.translate("MainWindow", u"Recommendation", None))
        self.actionStatus.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.actionSubcategory.setText(QCoreApplication.translate("MainWindow", u"Subcategory", None))
        self.actionUOM.setText(QCoreApplication.translate("MainWindow", u"UOM", None))
        self.actionVendor.setText(QCoreApplication.translate("MainWindow", u"Vendor", None))
        self.actionUnit.setText(QCoreApplication.translate("MainWindow", u"Unit", None))
        self.actionCapex.setText(QCoreApplication.translate("MainWindow", u"Capex", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.menuCapex.setTitle(QCoreApplication.translate("MainWindow", u"Capex", None))
        self.menuOptions.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

