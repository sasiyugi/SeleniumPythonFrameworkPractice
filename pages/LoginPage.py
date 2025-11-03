from selenium.webdriver.common.by import By
from utilities.log_utility import *


class LoginPage:


    def __init__(self, driver):
        self.driver = driver

    email_textbox_xpath = "//input[@id='input-email']"
    password_textbox_xpath = "//input[@name='password']"
    login_button_xpath = "//input[@value='Login']"

    def email_text_box_data_inject(self, username):
        try:
            log_info("entering text into email")
            self.driver.find_element(By.XPATH, self.email_textbox_xpath).send_keys(username)
        except :
            log_error("failed to enter text into email text box")

    def password_text_box_data_inject(self, password):
        try:
            log_info("entering password")
            self.driver.find_element(By.XPATH, self.password_textbox_xpath).send_keys(password)
        except Exception as e:
            log_error("failed to enter password")

    def click_on_login_button(self):
        try:
            log_info("click on login button")
            self.driver.find_element(By.XPATH, self.login_button_xpath).click()
        except:
            log_error("Failed to click on login button")

    #def common method to login with valid credintials
    def login_with_valid_credintials(self, username, password):
        self.email_text_box_data_inject(username)
        self.password_text_box_data_inject(password)
        self.click_on_login_button()




