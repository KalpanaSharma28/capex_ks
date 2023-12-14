from PySide6.QtWidgets import QMainWindow, QMdiSubWindow, QWidget
from ui_mainwindow import Ui_MainWindow
from location.ui_location import Ui_Form


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.actionLocation.triggered.connect(self.new_location)

    def new_location(self, location_widget):
        print("todo: open new location widget")
        self.local = Ui_Form()
        self.local.setupUi(self)
        self.mdiArea.addSubWindow(self.local)
        self.local.show()

    """
        print("todo: open new location widget")
        self.subwindow = QMdiSubWindow()
        self.subwindow.setWidget(Ui_Form().setupUi(Ui_Form))
        self.mdiArea.addSubWindow(self.subwindow)
        self.subwindow.show()

"""







