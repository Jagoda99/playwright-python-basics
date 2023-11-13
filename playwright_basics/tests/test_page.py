import re
import pytest
from playwright.sync_api import Page, expect
from pages.main_page import *

def test_main_page_click(page : Page):
    main_page = MainPage(page)
    main_page.load()
    abtesting_page = main_page.click_link_abtesting("A/B Testing")
    expect(abtesting_page._page_header).to_be_visible()

def test_add_and_remove(page : Page):
    main_page = MainPage(page)
    main_page.load()
    addremove_page = main_page.click_link_addremove("Add/Remove Elements")
    addremove_page.click_add_btn()
    expect(addremove_page._delete_btn).to_be_visible()
