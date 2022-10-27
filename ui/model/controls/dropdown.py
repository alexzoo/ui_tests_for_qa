
from selene import have, Element
from selene.support.shared import browser


def select(element: Element, option):
    element.click()
    browser.all('[id^=react-select][id*=-option-]').element_by(have.exact_text(f'{option}')).click()