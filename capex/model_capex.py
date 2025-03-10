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
        self.idx_subcategoryid = self.fieldIndex('SubCategoryID')
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
        self.setHeaderData(self.idx_approverid, Qt.Horizontal, "Approver")
        self.setHeaderData(self.idx_areaid, Qt.Horizontal, "Area")
        self.setHeaderData(self.idx_categoryid, Qt.Horizontal, "Category")
        self.setHeaderData(self.idx_subcategoryid, Qt.Horizontal, "SubCategory")
        self.setHeaderData(self.idx_currencyid, Qt.Horizontal, "Currency")
        self.setHeaderData(self.idx_exptypeid, Qt.Horizontal, "ExpType")
        self.setHeaderData(self.idx_frequencyid, Qt.Horizontal, "Frequency")
        # `ID` is not required in display captions. `Location ID` changed to `Location`.
        #  TODO: Make similar change in other captions with ID.
        self.setHeaderData(self.idx_locationid, Qt.Horizontal, "Location")
        self.setHeaderData(self.idx_natureid, Qt.Horizontal, "Nature")
        self.setHeaderData(self.idx_originid, Qt.Horizontal, "Origin")
        self.setHeaderData(self.idx_recommendationid, Qt.Horizontal, "Recommendation")
        self.setHeaderData(self.idx_statusid, Qt.Horizontal, "Status")
        self.setHeaderData(self.idx_unitid, Qt.Horizontal, "Unit")
        self.setHeaderData(self.idx_uomid, Qt.Horizontal, "UOM")
        self.setHeaderData(self.idx_vendorid, Qt.Horizontal, "Vendor")

        self.setSort(self.idx_capexid, Qt.SortOrder.AscendingOrder)

        # QSqlRelation Object is created first and then it is used in setRelation function
        #   to make code simple to read - one step at a time.
        self.relation_location = QSqlRelation("Location", "LocationID", "LocationName")
        self.setRelation(self.idx_locationid, self.relation_location)

        # Adding this propery, it will be possible to refer to related model:
        #   Currently this is not used in the capex program.
        # self.relational_model_location = self.relationModel(self.idx_locationid)

        self.relation_approver = QSqlRelation("Approver", "ApproverID", "ApproverName")
        self.setRelation(self.idx_approverid, self.relation_approver)

        self.relation_area = QSqlRelation("Area", "AreaID", "AreaName")
        self.setRelation(self.idx_areaid, self.relation_area)

        self.relation_category = QSqlRelation("Category", "CategoryID", "Categoryname")
        self.setRelation(self.idx_categoryid, self.relation_category)

        self.relation_currency = QSqlRelation("Currency", "CurrencyID", "CurrencyName")
        self.setRelation(self.idx_currencyid, self.relation_currency)

        self.relation_exptype = QSqlRelation("Exptype", "ExptypeID", "ExptypeName")
        self.setRelation(self.idx_exptypeid, self.relation_exptype)

        self.relation_frequency = QSqlRelation("Frequency", "FrequencyID", "FrequencyName")
        self.setRelation(self.idx_frequencyid, self.relation_frequency)

        self.relation_nature = QSqlRelation("Nature", "NatureID", "NatureName")
        self.setRelation(self.idx_natureid, self.relation_nature)

        self.relation_origin = QSqlRelation("Origin", "OriginID", "OriginName")
        self.setRelation(self.idx_originid, self.relation_origin)

        self.relation_recommendation = QSqlRelation("Recommendation", "RecommendationID", "Recommendation")
        self.setRelation(self.idx_recommendationid, self.relation_recommendation)

        self.relation_status = QSqlRelation("Status", "StatusID", "StatusName")
        self.setRelation(self.idx_statusid, self.relation_status)

        self.relation_subcategory = QSqlRelation("SubCategory", "SubCategoryID", "SubCategoryName")
        self.setRelation(self.idx_subcategoryid, self.relation_subcategory)

        self.relation_unit = QSqlRelation("Unit", "UnitID", "UnitName")
        self.setRelation(self.idx_unitid, self.relation_unit)

        self.relation_uom = QSqlRelation("UOM", "UOMID", "UOMName")
        self.setRelation(self.idx_uomid, self.relation_uom)

        self.relation_vendor = QSqlRelation("Vendor", "VendorID", "VendorName")
        self.setRelation(self.idx_vendorid, self.relation_vendor)


    def insert_row(self):
        row = self.rowCount()
        record = self.record()

        record.setValue("CapexID", None)
        record.setValue("BudgetNo", "?Budget No?")
        record.setValue("ProposalDate", "?Proposal Date?")
        record.setValue("SN","?SN?")
        record.setValue("DetailsDescription", "?Details Description?")
        record.setValue("BudgetQuality", "?Budget Quality?")
        record.setValue("BudgetRate", "?Budget Rate?")
        record.setValue("BudgetAmount", "?Budget Amount?")
        record.setValue("ActualQuantity", "?Actual Quantity?")
        record.setValue("ActualRate", "?Actual Rate?")
        record.setValue("ActualAmount", "?Actual Amount?")
        record.setValue("Remarks", "?Remarks?")

        return self.insertRecord(row, record)

    def save_all(self):
        return self.submitAll()
