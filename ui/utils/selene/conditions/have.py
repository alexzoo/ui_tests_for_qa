import datetime

from selene import have
from selene.support.conditions.have import *  # noqa
from selene.support.conditions.be import *  # noqa

import ui


def date(value: datetime.date):  # noqa
    return have.value(value.strftime(ui.config.datetime_input_format))
