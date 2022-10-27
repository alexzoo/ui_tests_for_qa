
from selene.support.shared import browser
import os


def upload(relative_path):
    """
    upload file
    """
    browser.element('#uploadPicture').send_keys(os.path.abspath(relative_path))