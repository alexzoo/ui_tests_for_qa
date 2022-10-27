
from selene.support.shared import browser

from ui import have
from ui.utils.selene import command

ads = browser.all('[id^=google_ads][id$=container__]')


def remove_ads(*, amount, timeout):
    if ads.with_(timeout=timeout).wait.until(have.size_greater_than_or_equal(amount)):
        ads.perform(command.js.remove)
