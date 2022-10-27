
from selene.support.shared import browser
from ui.model.controls import table


dialog = browser.element('.modal-content')
rows = table.rows(inside=dialog)
