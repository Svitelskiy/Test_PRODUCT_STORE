from pages.main_page import DemoMainPage, MonitorsCategory


def test_check_monitors_category(browser):
    DemoMainPage(browser).navigate_to_monitors_category()
    MonitorsCategory(browser)