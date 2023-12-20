import inspect
import logging

from PySide6.QtCore import Qt, QModelIndex
from PySide6.QtGui import QTextDocument, QTextCursor, QTextBlockFormat
from PySide6.QtSql import (QSqlRelationalTableModel, QSqlTableModel, QSqlRecord, QSqlRelation)


class ModelLocation(QSqlRelationalTableModel):
    """
    Location Model based on QSqlRelationalTableModel.

    In this model, we:

    - set Database Table
    - set edit strategy for manual submit
    - define field index variables
    - define colum names
    - sort column
    - insert row function
    """

    def __init__(self):
        super(ModelLocation, self).__init__()
        logging.debug('%s.%s', __name__, inspect.currentframe().f_code.co_name)

        self.setTable("Location")
        self.setEditStrategy(QSqlTableModel.EditStrategy.OnManualSubmit)
        self.setJoinMode(QSqlRelationalTableModel.JoinMode.LeftJoin)

        self.idx_id = self.fieldIndex('LocationID')
        self.idx_name = self.fieldIndex('LocationName')

        self.setHeaderData(self.idx_id, Qt.Horizontal, "ID")
        self.setHeaderData(self.idx_name, Qt.Horizontal, "Location Name")

        self.setSort(self.idx_name, Qt.SortOrder.AscendingOrder)

    def insert_row(self):
        """Create a new record and inserts in the Model.

        The save call is not part of this function. :py:func:`save_all` must be called from parent Widget.
        Returns boolean results of success or failure.

        :return: bool
        """
        row = self.rowCount()
        record = self.record()

        record.setValue("LocationID", None)
        record.setValue("LocationName", "?name?")

        return self.insertRecord(row, record)

    def save_all(self):
        """Submit all changes to the model to the database.

        The save call is required after any changes, insertion, or deletion in the data model.

        Returns boolean results of success or failure.

        :return: bool
        """
        return self.submitAll()
