import logging
from PySide6.QtCore import Qt, QCoreApplication
from PySide6.QtWidgets import QAbstractItemView, QWidget
from frequency.model_frequency import ModelFrequency
from frequency.ui_frequency import Ui_Form

class WidgetFrequency(QWidget, Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowTitle(QCoreApplication.translate("maintain_frequency", "Maintain Frequency", None))

        self.model_frequency = ModelFrequency()
        self.tableView.setModel(self.model_frequency)

        self.setup_tableview()
        self.connect_signals()
        self.initialize_widgets()
        self.select_data()

    def setup_tableview(self):
        self.tableView.setColumnHidden(self.model_frequency.idx_id, False)
        self.tableView.setColumnHidden(self.model_frequency.idx_name, False)

        self.tableView.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableView.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

    def connect_signals(self):
        self.button_create.clicked.connect(self.insert_row)
        self.button_submit.clicked.connect(self.save_all)
        self.button_close.clicked.connect(self.close_widget)

    def initialize_widgets(self):
        pass

    def select_data(self):
        if self.model_frequency.select():
            self.tableView.resizeColumnsToContents()
        else:
            logging.debug("No records selected from model.")

    def insert_row(self):
        self.row = self.model_frequency.insert_row()

    def save_all(self):
        self.button_submit.setFocus()
        self.model_frequency.save_all()

    def close_widget(self):
        self.parentWidget().close()
