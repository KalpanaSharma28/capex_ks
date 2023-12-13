import sys
from PySide6.QtWidgets import QApplication, QWidget
from ui_location import Ui_Form

class location_widget(QWidget, Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app_location = QApplication(sys.argv)
    local = location_widget()
    local.show()
    sys.exit(app_location.exec())