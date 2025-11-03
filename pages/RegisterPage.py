from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class RegisterPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    first_name_textbox_xpath = "//input[@name='firstname']"
    last_name_textbox_xpath = "//input[@name='lastname']"
    email_textbox_xpath = "//input[@name='email']"
    telephone_textbox_xpath = "//input[@id='input-telephone']"
    password_textbox_xpath = "//input[@name='password']"
    confirm_password_textbox_xpath = "//input[@name='confirm']"
    privacy_policy_checkbox_xpath = "//input[@name='agree']"
    continue_button_xpath = "//input[@value='Continue']"


    def firstname_textbox_data_inject(self, firstname):
        self.driver.find_element(By.XPATH, self.first_name_textbox_xpath).send_keys(firstname)

    def lastname_textbox_data_inject(self, lastname):
        self.driver.find_element(By.XPATH, self.last_name_textbox_xpath).send_keys(lastname)

    def email_textbox_data_inject(self):
        self.driver.find_element(By.XPATH, self.email_textbox_xpath).send_keys(self.dynamic_email())

    def telephone_text_box_data_inject(self):
        self.driver.find_element(By.XPATH, self.telephone_textbox_xpath).send_keys(self.get_random_phone_number())

    def password_textbox_data_inject(self, password):
        self.scroll_into_pixels_y_axis()
        self.driver.find_element(By.XPATH, self.password_textbox_xpath).send_keys(password)

    def confirm_password_textbox_data_inject(self, confirm_password):
        self.driver.find_element(By.XPATH, self.confirm_password_textbox_xpath).send_keys(confirm_password)

    def select_privacy_policy_checkbox(self):
        self.driver.find_element(By.XPATH, self.privacy_policy_checkbox_xpath).click()

    def click_on_continue_button(self):
        self.driver.find_element(By.XPATH, self.continue_button_xpath).click()

   #common method for new register account
    def register_new_account(self, firstname, lastname, password, confirm_password):
        self.firstname_textbox_data_inject(firstname)
        self.lastname_textbox_data_inject(lastname)
        self.email_textbox_data_inject()
        self.telephone_text_box_data_inject()
        self.password_textbox_data_inject(password)
        self.confirm_password_textbox_data_inject(confirm_password)
        self.select_privacy_policy_checkbox()
        self.click_on_continue_button()







