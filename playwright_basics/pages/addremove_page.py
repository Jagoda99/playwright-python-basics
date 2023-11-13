from playwright.sync_api import Page

class AddRemovePage:

    def __init__(self, page: Page):
        self.page = page
        self._add_btn = page.get_by_role("button", name="Add Element")
        self._delete_btn = page.get_by_role("button", name="Delete")

    def click_add_btn(self):
        self._add_btn.click()

    def click_delete_btn(self):
        self._delete_btn.click()