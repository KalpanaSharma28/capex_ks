import sys
import inspect
import logging

from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow
from db import CapexDB


if __name__ == "__main__":
    logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
    logging.debug('%s.%s', __name__, inspect.currentframe().f_code.co_name)

    capex_db = CapexDB()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
