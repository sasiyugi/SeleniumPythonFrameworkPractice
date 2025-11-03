from time import strftime

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver

from utilities import config_utility



@pytest.fixture()
def setup_and_teardown(request):

    global driver
    browser = config_utility.read_config_data("Browser", "browser")
    url = config_utility.read_config_data("Dev", "url")

    driver = None

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        print("no browser located")

    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver

    yield

    driver.quit()

@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name=dynamic_time_stamp(), attachment_type=AttachmentType.PNG)

def dynamic_time_stamp():
    timestamp = strftime("%Y_%m_%d_%H_%M_%S")
    time = timestamp.replace("_", "").strip()
    return time


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


# @pytest.fixture(params=["chrome", "edge"])
# def setup_and_teardown(request):
#     global driver
#     if request.param == "chrome":
#         driver = webdriver.Chrome()
#     elif request.param == "edge":
#         driver  = webdriver.Edge()
#     driver.get("https://tutorialsninja.com/demo/index.php?route=common/home")
#     driver.maximize_window()
#     driver.implicitly_wait(5)
#     request.cls.driver = driver
#     yield
#     time.sleep(2)
#     driver.quit()

# def pytest_addoption(parser):
#     parser.addoption("--browser")

# @pytest.fixture()
# def setup_and_teardown(request):
#     global driver
#     browser = request.config.getoption("--browser")
#     if browser == "chrome":
#         driver = webdriver.Chrome()
#     elif browser == "edge":
#         driver = webdriver.Edge()
#     driver.get("https://tutorialsninja.com/demo/index.php?route=common/home")
#     driver.maximize_window()
#     driver.implicitly_wait(5)
#     request.cls.driver = driver
#     yield
#     driver.quit()


