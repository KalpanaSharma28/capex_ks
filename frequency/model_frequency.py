import inspect
import logging
from PySide6.QtCore import Qt, QModelIndex
from PySide6.QtGui import QTextDocument, QTextCursor, QTextBlockFormat
from PySide6.QtSql import QSqlRelation, QSqlRelationalTableModel, QSqlTableModel, QSqlRecord

class ModelFrequency(QSqlRelationalTableModel):

    def __init__(self):
        super(ModelFrequency, self).__init__()
        logging.debug('%s.%s', __name__, inspect.currentframe().f_code.co_name)

        self.setTable("Frequency")
        self.setEditStrategy(QSqlTableModel.EditStrategy.OnManualSubmit)
        self.setJoinMode(QSqlRelationalTableModel.JoinMode.LeftJoin)

        self.idx_id = self.fieldIndex('FrequencyID')
        self.idx_name = self.fieldIndex('FrequencyName')

        self.setHeaderData(self.idx_id, Qt.Horizontal, "ID")
        self.setHeaderData(self.idx_name, Qt.Horizontal, "Frequency Name")

        self.setSort(self.idx_name, Qt.SortOrder.AscendingOrder)

    def insert_row(self):
        row = self.rowCount()
        record = self.record()

        record.setValue("FrequencyID", None)
        record.setValue("FrequencyName", "?name?")

        return self.insertRecord(row, record)

    def save_all(self):
        return self.submitAll()
