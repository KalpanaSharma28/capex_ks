import logging

from PySide6.QtCore import Qt, QCoreApplication
from PySide6.QtWidgets import QAbstractItemView, QWidget

from location.model_location import ModelLocation
from location.ui_location import Ui_Form


class WidgetLocation(QWidget, Ui_Form):
    """ **Widget for Location**

    The class is responsible for displaying the location.
    A new location can also be added to the Location Table from this widget.

    The class naming convention:
      - Start each word with a capital letter. Do not separate words with underscores.
      - This style is called camel case or pascal case.
      - Examples: Location, WidgetLocation

    The class instance naming convention:
      - The instance of the class will be created with the lowercase words with underscore.
      - Use a lowercase word or words. Separate words with underscores to improve readability.
      - Examples: location, widget_location
    """

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowTitle(QCoreApplication.translate("maintain_locations", "Maintain Locations", None))

        self.model_location = ModelLocation()
        self.tableView.setModel(self.model_location)

        self.setup_tableview()
        self.connect_signals()
        self.initialize_widgets()
        self.select_data()

    def setup_tableview(self):
        self.tableView.setColumnHidden(self.model_location.idx_id, False)
        self.tableView.setColumnHidden(self.model_location.idx_name, False)

        self.tableView.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableView.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

    def connect_signals(self):
        self.button_create.clicked.connect(self.insert_row)
        self.button_submit.clicked.connect(self.save_all)
        self.button_close.clicked.connect(self.close_widget)

    def initialize_widgets(self):
        pass

    def select_data(self):
        """Select data from Model with specified filters."""
        if self.model_location.select():
            self.tableView.resizeColumnsToContents()
        else:
            logging.debug("No records selected from model.")

    def insert_row(self):
        """Create an empty row and insert in the model."""
        self.row = self.model_location.insert_row()

    def save_all(self):
        """
        Save all changes to the Data Model.

        The explict ``setFocus`` call is to exit from any edited text field.
        If we directly call save method, the changes in the field being edited, are not saved.
        """
        self.button_submit.setFocus()
        self.model_location.save_all()

    def close_widget(self):
        self.parentWidget().close()
