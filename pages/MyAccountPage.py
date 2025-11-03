from selenium.webdriver.common.by import By


class MyAccountPage:

    def __init__(self, driver):
        self.driver = driver

    my_account_header_text_xpath = "//h2[text()='My Account']"

    def my_account_header_text_validation(self):
        return self.driver.find_element(By.XPATH, self.my_account_header_text_xpath).text