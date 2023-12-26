import inspect
import logging
from PySide6.QtCore import Qt, QModelIndex
from PySide6.QtGui import QTextDocument, QTextCursor, QTextBlockFormat
from PySide6.QtSql import QSqlRelation, QSqlRelationalTableModel, QSqlTableModel, QSqlRecord

class ModelCategory(QSqlRelationalTableModel):

    def __init__(self):
        super(ModelCategory, self).__init__()
        logging.debug('%s.%s', __name__, inspect.currentframe().f_code.co_name)

        self.setTable("Category")
        self.setEditStrategy(QSqlTableModel.EditStrategy.OnManualSubmit)
        self.setJoinMode(QSqlRelationalTableModel.JoinMode.LeftJoin)

        self.idx_id = self.fieldIndex('CategoryID')
        self.idx_name = self.fieldIndex('CategoryName')

        self.setHeaderData(self.idx_id, Qt.Horizontal, "ID")
        self.setHeaderData(self.idx_name, Qt.Horizontal, "Category Name")

        self.setSort(self.idx_name, Qt.SortOrder.AscendingOrder)

    def insert_row(self):
        row = self.rowCount()
        record = self.record()

        record.setValue("CategoryID", None)
        record.setValue("CategoryName", "?name?")

        return self.insertRecord(row, record)

    def save_all(self):
        return self.submitAll()
