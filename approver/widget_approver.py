import logging
from PySide6.QtCore import Qt, QCoreApplication
from PySide6.QtWidgets import QAbstractItemView, QWidget
from approver.model_approver import ModelApprover
from approver.ui_approver import Ui_Form

class WidgetApprover(QWidget, Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowTitle(QCoreApplication.translate("maintain_approver", "Maintain Approver", None))

        self.model_approver = ModelApprover()
        self.tableView.setModel(self.model_approver)

        self.setup_tableview()
        self.connect_signals()
        self.initialize_widgets()
        self.select_data()

    def setup_tableview(self):
        self.tableView.setColumnHidden(self.model_approver.idx_id, False)
        self.tableView.setColumnHidden(self.model_approver.idx_name, False)

        self.tableView.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableView.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

    def connect_signals(self):
        self.button_create.clicked.connect(self.insert_row)
        self.button_submit.clicked.connect(self.save_all)
        self.button_close.clicked.connect(self.close_widget)

    def initialize_widgets(self):
        pass

    def select_data(self):
        if self.model_approver.select():
            self.tableView.resizeColumnsToContents()
        else:
            logging.debug("No records selected from model.")

    def insert_row(self):
        self.row = self.model_approver.insert_row()

    def save_all(self):
        self.button_submit.setFocus()
        self.model_approver.save_all()

    def close_widget(self):
        self.parentWidget().close()
