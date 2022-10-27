
from selene.support.shared import browser


def set_option(label_prefix: str, number: int):
    """
    set option in radio button control
    """
    browser.element(f'[for={label_prefix}-radio-{number}]').click()

    