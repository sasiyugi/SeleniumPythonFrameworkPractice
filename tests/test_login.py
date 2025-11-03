import time

import allure
import pytest

from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from pages.MyAccountPage import MyAccountPage
from tests.BaseTest import BaseTest
from utilities import excel_utility
from utilities.log_utility import log_info





@pytest.mark.parametrize("username, password", excel_utility.read_data_from_excel(r"C:\Users\sasik\PycharmProjects\FrameworkPractice\files\login_excel.xlsx", "Sheet1"))
class TestLogin(BaseTest):

    #@pytest.mark.parametrize("username, password", [["sasikumar@gmail.com", "12345678"]])
    @allure.severity(allure.severity_level.MINOR)
    def test_login_(self,username, password):

        home_page = HomePage(self.driver)
        home_page.click_on_login()

        login_page = LoginPage(self.driver)
        login_page.login_with_valid_credintials(username, password)

        account_page = MyAccountPage(self.driver)
        actual_result = account_page.my_account_header_text_validation()
        print(actual_result)


        expected_text = "My Account"
        assert actual_result.__eq__(expected_text), "login issue"
        log_info("Test passed")





