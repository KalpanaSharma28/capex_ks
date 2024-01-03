import inspect
import logging

from PySide6.QtCore import Qt, QModelIndex
from PySide6.QtGui import QTextDocument, QTextCursor, QTextBlockFormat
from PySide6.QtSql import QSqlRelation, QSqlRelationalTableModel, QSqlTableModel, QSqlRecord


class ModelCapex(QSqlRelationalTableModel):

    def __init__(self):
        super(ModelCapex, self).__init__()
        logging.debug('%s.%s', __name__, inspect.currentframe().f_code.co_name)

        self.setTable("capex")
        self.setEditStrategy(QSqlTableModel.EditStrategy.OnManualSubmit)
        self.setJoinMode(QSqlRelationalTableModel.JoinMode.LeftJoin)

        self.idx_capexid = self.fieldIndex('CapexID')
        self.idx_budgetno = self.fieldIndex('BudgetNo')
        self.idx_proposaldate = self.fieldIndex('ProposalDate')
        self.idx_sn = self.fieldIndex('SN')
        self.idx_detailsdescription = self.fieldIndex('DetailsDescription')
        self.idx_budgetquantity = self.fieldIndex('BudgetQuality')
        self.idx_budgetrate = self.fieldIndex('BudgetRate')
        self.idx_budgetamount = self.fieldIndex('BudgetAmount')
        self.idx_actualquantity = self.fieldIndex('ActualQuantity')
        self.idx_actualrate = self.fieldIndex('ActualRate')
        self.idx_actualamount = self.fieldIndex('ActualAmount')
        self.idx_remarks = self.fieldIndex('Remarks')
        self.idx_unitid = self.fieldIndex('UnitID')
        self.idx_areaid = self.fieldIndex('AreaID')
        self.idx_categoryid = self.fieldIndex('CategoryID')
        self.idx_subcategoryid = self.fieldIndex('SubCategory')
        self.idx_currencyid = self.fieldIndex('CurrencyID')
        self.idx_uomid = self.fieldIndex('UOMID')
        self.idx_recommendationid = self.fieldIndex('RecommendationID')
        self.idx_exptypeid = self.fieldIndex('ExpTypeID')
        self.idx_natureid = self.fieldIndex('NatureID')
        self.idx_frequencyid = self.fieldIndex('FrequencyID')
        self.idx_originid = self.fieldIndex('OriginID')
        self.idx_vendorid = self.fieldIndex('VendorID')
        self.idx_statusid = self.fieldIndex('StatusID')
        self.idx_approverid = self.fieldIndex('ApproverID')
        self.idx_locationid = self.fieldIndex('LocationID')


        self.setHeaderData(self.idx_capexid, Qt.Horizontal, "Capex ID")
        self.setHeaderData(self.idx_budgetno, Qt.Horizontal, "Budget No.")
        self.setHeaderData(self.idx_proposaldate, Qt.Horizontal, "Proposal Date")
        self.setHeaderData(self.idx_sn, Qt.Horizontal, "SN")
        self.setHeaderData(self.idx_detailsdescription, Qt.Horizontal, "Detailed Description")
        self.setHeaderData(self.idx_budgetquantity, Qt.Horizontal, "Budget Quantity")
        self.setHeaderData(self.idx_budgetrate, Qt.Horizontal, "Budget Rate")
        self.setHeaderData(self.idx_budgetamount, Qt.Horizontal, "Budget Amount")
        self.setHeaderData(self.idx_actualamount, Qt.Horizontal, "Actual Amount")
        self.setHeaderData(self.idx_actualrate, Qt.Horizontal, "Actual Rate")
        self.setHeaderData(self.idx_actualquantity, Qt.Horizontal, "Actual Quantity")
        self.setHeaderData(self.idx_remarks, Qt.Horizontal, "Remarks")
        self.setHeaderData(self.idx_approverid, Qt.Horizontal, "Approver ID")
        self.setHeaderData(self.idx_areaid, Qt.Horizontal, "Area ID")
        self.setHeaderData(self.idx_categoryid, Qt.Horizontal, "Category ID")
        self.setHeaderData(self.idx_subcategoryid, Qt.Horizontal, "SubCategory")
        self.setHeaderData(self.idx_currencyid, Qt.Horizontal, "Currency ID")
        self.setHeaderData(self.idx_exptypeid, Qt.Horizontal, "ExpType ID")
        self.setHeaderData(self.idx_frequencyid, Qt.Horizontal, "Frequency ID")
        self.setHeaderData(self.idx_locationid, Qt.Horizontal, "Location ID")
        self.setHeaderData(self.idx_natureid, Qt.Horizontal, "Nature ID")
        self.setHeaderData(self.idx_originid, Qt.Horizontal, "Origin ID")
        self.setHeaderData(self.idx_recommendationid, Qt.Horizontal, "Recommendation ID")
        self.setHeaderData(self.idx_statusid, Qt.Horizontal, "Status ID")
        self.setHeaderData(self.idx_unitid, Qt.Horizontal, "Unit ID")
        self.setHeaderData(self.idx_uomid, Qt.Horizontal, "UOM ID")
        self.setHeaderData(self.idx_vendorid, Qt.Horizontal, "Vendor ID")

        self.setSort(self.idx_capexid, Qt.SortOrder.AscendingOrder)

    """
    def insert_row(self):
        row = self.rowCount()
        record = self.record()

        record.setValue("CapexID", None)
        record.setValue("BudgetNo", "?text?")

        return self.insertRecord(row, record)
    """
    def save_all(self):
        return self.submitAll()