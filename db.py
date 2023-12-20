"""
The CapexDB class handles database file open operations and return a database connection.

The database connection with default connection name is returned.
Therefore, the data widgets gets the default connection,
if ``capexDB`` instance has been created before initializing the widget.

"""
import inspect
import logging
import os
import sys

from PySide6.QtSql import QSqlDatabase


class CapexDB(QSqlDatabase):
    """CapexDB QSqlDatabase Class"""
    def __init__(self, db_name = None):
        super().__init__()
        logging.debug('%s.%s', __name__, inspect.currentframe().f_code.co_name)
        if db_name is None:
            dir = (os.path.dirname(__file__))
            db_dir = os.path.join(dir, 'data')
            logging.debug('%s = %s', "db_dir", db_dir)
            db_name = os.path.join(db_dir, "capex.sqlite")
            logging.debug('%s = %s', "db_name", db_name)
        self.open(db_name)

    def open(self, db_name):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(db_name)

        if db.open():
            logging.debug('%s : %s', "DB Connected", db_name)
            logging.debug('%s : %s', "db.tables", db.tables())

            return db
        else:
            logging.error('%s : %s', 'Connection Failed', str(db.lastError()))
            sys.exit(1)
