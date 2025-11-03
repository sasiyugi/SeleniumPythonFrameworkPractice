import allure
from selenium.webdriver.common.by import By

from pages.HomePage import HomePage
from tests.BaseTest import BaseTest


class TestValidation(BaseTest):

    # def test_validate_search_box(self):
    #     search = self.driver.find_element(By.XPATH, "//div[@id='search']//input")
    #     search.send_keys("iphone")
    #     assert search.get_attribute("value").__eq__(
    #         "iphone"), "text in search box is not matched assertion error is occured"

    @allure.severity(allure.severity_level.CRITICAL)

    def test_add_item_into_cart_with_dynamic_price(self):

        home_page = HomePage(self.driver)
        home_page.select_show_all_desktop_options()


        prices = self.driver.find_elements(By.XPATH, "//span[@class='price-tax']")
        for price in prices:
            pr = price.text.replace("Ex Tax:$", "").replace(".00", "").strip()
            p = int(pr)
            if p == 101:
                price.find_element(By.XPATH,
                                   "./ancestor::div[@class='product-thumb']//span[text()='Add to Cart']").click()
                break

        actual_text = self.driver.find_element(By.XPATH, "//*[text()=' Success: You have added ']").text
        assert "Success" in actual_text, "something wrong in add item to cart"








