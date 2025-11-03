import os.path

import allure
import pytest

from pages.AccountSuccessPage import AccountSuccessPage
from pages.HomePage import HomePage
from pages.RegisterPage import RegisterPage
from tests.BaseTest import BaseTest
from utilities import excel_utility


class TestRegistration(BaseTest):

    loc = os.path.dirname(os.getcwd()) + "//FrameworkPractice//files//register.xlsx"
    #loc = r"C:\Users\sasik\PycharmProjects\FrameworkPractice\files\register.xlsx"

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("firstname, lastname, password, confirm_password", excel_utility.read_data_from_excel(loc, "Sheet1"))
    def test_register_new_account(self, firstname, lastname, password, confirm_password):

        home_page = HomePage(self.driver)
        home_page.click_on_register()

        register_page = RegisterPage(self.driver)
        register_page.register_new_account(firstname, lastname, password, confirm_password)

        account_success_page = AccountSuccessPage(self.driver)
        actual_result = account_success_page.account_success_header()

        print(actual_result)
        expected_result = "Your Account Has Been Created!"
        assert actual_result.__eq__(expected_result), "actual text and expected text is not matched"







