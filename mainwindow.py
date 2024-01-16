from PySide6.QtWidgets import QMainWindow, QMdiSubWindow, QWidget
from ui_mainwindow import Ui_MainWindow
from location.widget_location import WidgetLocation
from approver.widget_approver import WidgetApprover
from area.widget_area import WidgetArea
from category.widget_category import WidgetCategory
from currency.widget_currency import WidgetCurrency
from exptype.widget_exptype import WidgetExptype
from frequency.widget_frequency import WidgetFrequency
from nature.widget_nature import WidgetNature
from origin.widget_origin import WidgetOrigin
from recommendation.widget_recommendation import WidgetRecommendation
from status.widget_status import WidgetStatus
from subcategory.widget_subcategory import WidgetSubcategory
from Unit.widget_unit import WidgetUnit
from uom.widget_uom import WidgetUOM
from vendor.widget_vendor import WidgetVendor
from capex.widget_capex import WidgetCapex


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.widget_location = None
        self.widget_approver = None
        self.widget_area = None
        self.widget_category = None
        self.widget_currency = None
        self.widget_exptype = None
        self.widget_frequency = None
        self.widget_nature = None
        self.widget_origin = None
        self.widget_recommendation = None
        self.widget_status = None
        self.widget_subcategory = None
        self.widget_unit = None
        self.widget_uom = None
        self.widget_vendor = None
        self.widget_capex = None

        self.setupUi(self)
        self.actionLocation.triggered.connect(self.new_location)
        self.actionApprover.triggered.connect(self.new_approver)
        self.actionArea.triggered.connect(self.new_area)
        self.actionCategory.triggered.connect(self.new_category)
        self.actionCurrency.triggered.connect(self.new_currency)
        self.actionExpType.triggered.connect(self.new_exptype)
        self.actionFrequency.triggered.connect(self.new_frequency)
        self.actionNature.triggered.connect(self.new_nature)
        self.actionOrigin.triggered.connect(self.new_origin)
        self.actionRecommendation.triggered.connect(self.new_recommendation)
        self.actionStatus.triggered.connect(self.new_status)
        self.actionSubcategory.triggered.connect(self.new_subcategory)
        self.actionUnit.triggered.connect(self.new_unit)
        self.actionUOM.triggered.connect(self.new_uom)
        self.actionVendor.triggered.connect(self.new_vendor)

        self.actionCapex.triggered.connect(self.capex)

        self.actionClose.triggered.connect(self.close)

    def new_location(self):
        self.widget_location = WidgetLocation()
        self.mdiArea.addSubWindow(self.widget_location)
        self.widget_location.show()

    def new_approver(self):
        self.widget_approver = WidgetApprover()
        self.mdiArea.addSubWindow(self.widget_approver)
        self.widget_approver.show()

    def new_area(self):
        self.widget_area = WidgetArea()
        self.mdiArea.addSubWindow(self.widget_area)
        self.widget_area.show()

    def new_category(self):
        self.widget_category = WidgetCategory()
        self.mdiArea.addSubWindow(self.widget_category)
        self.widget_category.show()

    def new_currency(self):
        self.widget_currency = WidgetCurrency()
        self.mdiArea.addSubWindow(self.widget_currency)
        self.widget_currency.show()

    def new_exptype(self):
        self.widget_exptype = WidgetExptype()
        self.mdiArea.addSubWindow(self.widget_exptype)
        self.widget_exptype.show()

    def new_frequency(self):
        self.widget_frequency = WidgetFrequency()
        self.mdiArea.addSubWindow(self.widget_frequency)
        self.widget_frequency.show()

    def new_nature(self):
        self.widget_nature = WidgetNature()
        self.mdiArea.addSubWindow(self.widget_nature)
        self.widget_nature.show()

    def new_origin(self):
        self.widget_origin = WidgetOrigin()
        self.mdiArea.addSubWindow(self.widget_origin)
        self.widget_origin.show()

    def new_recommendation(self):
        self.widget_recommendation = WidgetRecommendation()
        self.mdiArea.addSubWindow(self.widget_recommendation)
        self.widget_recommendation.show()

    def new_status(self):
        self.widget_status = WidgetStatus()
        self.mdiArea.addSubWindow(self.widget_status)
        self.widget_status.show()

    def new_subcategory(self):
        self.widget_subcategory = WidgetSubcategory()
        self.mdiArea.addSubWindow(self.widget_subcategory)
        self.widget_subcategory.show()

    def new_unit(self):
        self.widget_unit = WidgetUnit()
        self.mdiArea.addSubWindow(self.widget_unit)
        self.widget_unit.show()

    def new_uom(self):
        self.widget_uom = WidgetUOM()
        self.mdiArea.addSubWindow(self.widget_uom)
        self.widget_uom.show()

    def new_vendor(self):
        self.widget_vendor = WidgetVendor()
        self.mdiArea.addSubWindow(self.widget_vendor)
        self.widget_vendor.show()

    def capex(self):
        self.widget_capex = WidgetCapex()
        self.mdiArea.addSubWindow(self.widget_capex)
        self.widget_capex.show()
