from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    my_account_xpath = "//span[text()='My Account']"
    login_option_xpath = "(//a[text()='Login'])[1]"
    register_option_xpath = "//a[text()='Register']"
    desktop_mousehover_xpath = "(//a[text()='Desktops'])[1]"
    show_all_desktop_options_xpath = "//a[text()='Show AllDesktops']"

    def click_on_my_account_dropdown(self):
        self.driver.find_element(By.XPATH, self.my_account_xpath).click()

    def click_on_login_option(self):
        self.driver.find_element(By.XPATH, self.login_option_xpath).click()

    def click_on_register_option(self):
        self.driver.find_element(By.XPATH, self.register_option_xpath).click()

    def desktop_header_option(self):
        return self.wait_until_element_visible(By.XPATH, self.desktop_mousehover_xpath)

    def show_all_desktop_options(self):
        return self.driver.find_element(By.XPATH, self.show_all_desktop_options_xpath)

    def select_show_all_desktop_options(self):
        self.mouse_hover_element(self.desktop_header_option())
        self.show_all_desktop_options().click()

    # Common method for login
    def click_on_login(self):
        self.click_on_my_account_dropdown()
        self.click_on_login_option()

    #common method for register
    def click_on_register(self):
        self.click_on_my_account_dropdown()
        self.click_on_register_option()


