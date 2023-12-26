import logging
from PySide6.QtCore import Qt, QCoreApplication
from PySide6.QtWidgets import QAbstractItemView, QWidget
from nature.model_nature import ModelNature
from nature.ui_nature import Ui_Form

class WidgetNature(QWidget, Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowTitle(QCoreApplication.translate("maintain_nature", "Maintain Nature", None))

        self.model_nature = ModelNature()
        self.tableView.setModel(self.model_nature)

        self.setup_tableview()
        self.connect_signals()
        self.initialize_widgets()
        self.select_data()

    def setup_tableview(self):
        self.tableView.setColumnHidden(self.model_nature.idx_id, False)
        self.tableView.setColumnHidden(self.model_nature.idx_name, False)

        self.tableView.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableView.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

    def connect_signals(self):
        self.button_create.clicked.connect(self.insert_row)
        self.button_submit.clicked.connect(self.save_all)
        self.button_close.clicked.connect(self.close_widget)

    def initialize_widgets(self):
        pass

    def select_data(self):
        if self.model_nature.select():
            self.tableView.resizeColumnsToContents()
        else:
            logging.debug("No records selected from model.")

    def insert_row(self):
        self.row = self.model_nature.insert_row()

    def save_all(self):
        self.button_submit.setFocus()
        self.model_nature.save_all()

    def close_widget(self):
        self.parentWidget().close()
