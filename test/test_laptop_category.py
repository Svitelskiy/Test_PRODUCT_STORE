from pages.main_page import DemoMainPage, LaptopCategory


def test_check_laptops_category(browser):
    DemoMainPage(browser).navigate_to_laptops_category()
    LaptopCategory(browser)
