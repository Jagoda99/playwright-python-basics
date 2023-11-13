from pages.abtesting_page import *
from pages.addremove_page import *

from playwright.sync_api import Page

class MainPage:
    URL = "https://the-internet.herokuapp.com/"

    def __init__(self, page: Page):
        self.page = page

    def load(self):
        self.page.goto(self.URL)
        return self

    def click_link_abtesting(self, link_name):
        self.page.get_by_role("link", name=link_name).click()
        return ABTestingPage(self.page)
    
    def click_link_addremove(self, link_name):
        self.page.get_by_role("link", name=link_name).click()
        return AddRemovePage(self.page)
