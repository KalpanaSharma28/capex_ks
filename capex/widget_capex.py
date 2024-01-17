import logging

from PySide6.QtCore import Qt, QCoreApplication
from PySide6.QtWidgets import QAbstractItemView, QWidget
from PySide6.QtSql import QSqlRelationalDelegate

from capex.model_capex import ModelCapex
from capex.ui_capex import Ui_Form_capex


class WidgetCapex(QWidget, Ui_Form_capex):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowTitle(QCoreApplication.translate("maintain_capex", "Capex", None))

        self.model_capex = ModelCapex()
        self.tableView.setModel(self.model_capex)
        # For ComboBox for Foreign Key fields in capex table.
        #   See also usage in setup_tableview function.
        self.relational_delegate = QSqlRelationalDelegate()

        self.setup_tableview()
        self.connect_signals()
        self.initialize_widgets()
        self.select_data()

    def setup_tableview(self):
        self.tableView.setColumnHidden(self.model_capex.idx_capexid, True)
        self.tableView.setColumnHidden(self.model_capex.idx_budgetno, False)
        self.tableView.setColumnHidden(self.model_capex.idx_proposaldate, False)
        self.tableView.setColumnHidden(self.model_capex.idx_sn, False)
        self.tableView.setColumnHidden(self.model_capex.idx_detailsdescription, False)
        self.tableView.setColumnHidden(self.model_capex.idx_budgetquantity, False)
        self.tableView.setColumnHidden(self.model_capex.idx_budgetrate, False)
        self.tableView.setColumnHidden(self.model_capex.idx_budgetamount, False)
        self.tableView.setColumnHidden(self.model_capex.idx_actualquantity, False)
        self.tableView.setColumnHidden(self.model_capex.idx_actualrate, False)
        self.tableView.setColumnHidden(self.model_capex.idx_actualamount, False)
        self.tableView.setColumnHidden(self.model_capex.idx_remarks, False)
        self.tableView.setColumnHidden(self.model_capex.idx_unitid, False)
        self.tableView.setColumnHidden(self.model_capex.idx_categoryid, False)
        self.tableView.setColumnHidden(self.model_capex.idx_subcategoryid, False)
        self.tableView.setColumnHidden(self.model_capex.idx_currencyid, False)
        self.tableView.setColumnHidden(self.model_capex.idx_uomid, False)
        self.tableView.setColumnHidden(self.model_capex.idx_recommendationid, False)
        self.tableView.setColumnHidden(self.model_capex.idx_exptypeid, False)
        self.tableView.setColumnHidden(self.model_capex.idx_natureid, False)
        self.tableView.setColumnHidden(self.model_capex.idx_frequencyid, False)
        self.tableView.setColumnHidden(self.model_capex.idx_originid, False)
        self.tableView.setColumnHidden(self.model_capex.idx_vendorid, False)
        self.tableView.setColumnHidden(self.model_capex.idx_statusid, False)
        self.tableView.setColumnHidden(self.model_capex.idx_approverid, False)
        self.tableView.setColumnHidden(self.model_capex.idx_locationid, False)

        self.tableView.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableView.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableView.setItemDelegate(self.relational_delegate)

    def connect_signals(self):
        self.button_submit.clicked.connect(self.save_all)
        self.button_close.clicked.connect(self.close_widget)

    def initialize_widgets(self):
        pass

    def select_data(self):
        if self.model_capex.select():
            self.tableView.resizeColumnsToContents()
        else:
            logging.debug("No records selected from model.")

    def save_all(self):
        self.button_submit.setFocus()
        self.model_capex.save_all()

    def close_widget(self):
        self.parentWidget().close()
