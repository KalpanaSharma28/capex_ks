import inspect
import logging
from PySide6.QtCore import Qt, QModelIndex
from PySide6.QtGui import QTextDocument, QTextCursor, QTextBlockFormat
from PySide6.QtSql import  QSqlRelation, QSqlRelationalTableModel, QSqlTableModel, QSqlRecord

class ModelCurrency(QSqlRelationalTableModel):

    def __init__(self):
        super(ModelCurrency, self).__init__()
        logging.debug('%s.%s', __name__, inspect.currentframe().f_code.co_name)

        self.setTable("Currency")
        self.setEditStrategy(QSqlTableModel.EditStrategy.OnManualSubmit)
        self.setJoinMode(QSqlRelationalTableModel.JoinMode.LeftJoin)

        self.idx_id = self.fieldIndex('CurrencyID')
        self.idx_name = self.fieldIndex('CurrencyName')

        self.setHeaderData(self.idx_id, Qt.Horizontal, "ID")
        self.setHeaderData(self.idx_name, Qt.Horizontal, "Currency Name")

        self.setSort(self.idx_name, Qt.SortOrder.AscendingOrder)

    def insert_row(self):
        row = self.rowCount()
        record = self.record()

        record.setValue("CurrencyID", None)
        record.setValue("CurrencyName", "?name?")

        return self.insertRecord(row, record)

    def save_all(self):
        return self.submitAll()
