import datetime
import selene
from selenium.webdriver.common.keys import Keys
from ui.model.data import user
import sys


class DatePicker:

    def __init__(self, element: selene.Element):
        self.element = element

    def set_date(self, date: datetime.date):
        """
        set date
        """
        modifier_key = Keys.COMMAND if sys.platform == 'darwin' else Keys.CONTROL
        self.element.send_keys(
            modifier_key + 'a' + Keys.NULL,
            user.format_input_date(date),
        ).press_enter()
        return self

    def assert_value(self, date: datetime.date):
        """
        just an example for advocates of including assertions into PageObjects
        see https://martinfowler.com/bliki/PageObject.html for more details
        """
        self.element.should(selene.have.value(user.format_input_date(date)))
        return self


