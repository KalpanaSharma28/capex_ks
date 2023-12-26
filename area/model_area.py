import inspect
import logging
from PySide6.QtCore import Qt, QModelIndex
from PySide6.QtGui import QTextDocument, QTextCursor, QTextBlockFormat
from PySide6.QtSql import (QSqlRelationalTableModel, QSqlTableModel, QSqlRecord, QSqlRelation)

class ModelArea(QSqlRelationalTableModel):

    def __init__(self):
        super(ModelArea, self).__init__()
        logging.debug('%s.%s', __name__, inspect.currentframe().f_code.co_name)

        self.setTable("Area")
        self.setEditStrategy(QSqlTableModel.EditStrategy.OnManualSubmit)
        self.setJoinMode(QSqlRelationalTableModel.JoinMode.LeftJoin)

        self.idx_id = self.fieldIndex('AreaID')
        self.idx_name = self.fieldIndex('AreaName')

        self.setHeaderData(self.idx_id, Qt.Horizontal, "ID")
        self.setHeaderData(self.idx_name, Qt.Horizontal, "Area Name")

        self.setSort(self.idx_name, Qt.SortOrder.AscendingOrder)

    def insert_row(self):
        row = self.rowCount()
        record = self.record()

        record.setValue("AreaID", None)
        record.setValue("AreaName", "?name?")

        return self.insertRecord(row, record)

    def save_all(self):
        return self.submitAll()
