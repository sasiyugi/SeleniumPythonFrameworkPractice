from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class AccountSuccessPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    account_success_header_xpath = "//div[@id='content']//h1"

    def account_success_header(self):
        element = self.wait_until_element_visible(By.XPATH, self.account_success_header_xpath).text
        return element
