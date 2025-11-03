import random
from time import strftime

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_until_element_visible(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(ec.visibility_of_element_located((locator_type, locator)))

    def scroll_into_pixels_y_axis(self):
        self.driver.execute_script("window.scrollBy(0, 500);")

    def mouse_hover_element(self, element1):
        act = ActionChains(self.driver)
        return act.move_to_element(element1).click().perform()

    def dynamic_email(self):
        timestamp = strftime("%Y_%m_%d_%H_%M_%S")
        time = timestamp.replace("_", "").strip()
        return "tests" + time + "@gmail.com"

    def get_random_phone_number(self):
        first_digit = str(random.choice([7, 8, 9]))
        remaining_digits = ''.join(str(random.randint(0, 9)) for _ in range(9))
        return first_digit + remaining_digits
