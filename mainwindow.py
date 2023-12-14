from PySide6.QtWidgets import QMainWindow, QMdiSubWindow, QWidget
from ui_mainwindow import Ui_MainWindow
from location.ui_location import Ui_Form


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.actionLocation.triggered.connect(self.new_location)


    def new_location(self):
        self.local = Ui_Form()
        self.local_widget = QWidget()
        self.local.setupUi(self.local_widget)
        self.mdiArea.addSubWindow(self.local_widget)
        self.local_widget.show()




