# PageObjects/base_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=50):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find_element(self, by, locator):
        return self.wait.until(EC.presence_of_element_located((by, locator)))

    def click(self, by, locator):
        element = self.wait.until(EC.element_to_be_clickable((by, locator)))
        element.click()

    def send_keys(self, by, locator, value):
        element = self.wait.until(EC.visibility_of_element_located((by, locator)))
        element.clear()
        element.send_keys(value)

    def get_validation_messages(self, by, locator):
        return self.wait.until(EC.visibility_of_element_located((by, locator))).text

    def get_text(self, by, locator):
        return self.wait.until(EC.presence_of_element_located((by, locator))).text

    def wait_for_element_to_disappear(self, by, locator):
        self.wait.until(EC.invisibility_of_element_located((by, locator)))

    def wait_for_element_to_appear(self, by, locator):
        self.wait.until(EC.presence_of_element_located((by, locator)))