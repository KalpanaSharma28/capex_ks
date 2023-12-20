from PySide6.QtWidgets import QMainWindow, QMdiSubWindow, QWidget
from ui_mainwindow import Ui_MainWindow
from location.widget_location import WidgetLocation


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.widget_location = None
        self.setupUi(self)
        self.actionLocation.triggered.connect(self.new_location)

    def new_location(self):
        self.widget_location = WidgetLocation()
        self.mdiArea.addSubWindow(self.widget_location)
        self.widget_location.show()
