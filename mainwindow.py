from PySide6.QtWidgets import QMainWindow, QMdiSubWindow, QWidget, QVBoxLayout
from ui_mainwindow import Ui_MainWindow
from location.ui_location import Ui_Form


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.actionLocation.triggered.connect(self.new_location)


    def new_location(self):
        print("todo: open new location widget")
        subwindow = QMdiSubWindow()
        subwindow.setWidget(Ui_Form().setupUi(Ui_Form()))
        self.mdiArea.addSubWindow(subwindow)
        subwindow.show()









