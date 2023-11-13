from playwright.sync_api import Page

class ABTestingPage:

    def __init__(self, page: Page):
        self.page = page
        self._page_header = page.get_by_role("heading")