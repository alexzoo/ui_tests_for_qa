from selene.support.shared import browser

from ui.utils.selene import command


def scroll_one_page():
    browser.perform(command.js.scroll_one_page)
