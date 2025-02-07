import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObject.OrganizationsObjects import Organizations
from PageObject.LoginObjects import LoginPage

class TestOrganizations:

    username = "shani@simformsolutions.com"
    password =  "Shani@123" #"@PlE8tXcK4oX"
    baseurl = "https://dev.insightstobehavior.net"
    userOtp = "999999"

    def test_001_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_submit()
        self.lp.set_otp(self.userOtp)
        self.lp.click_submit()
        assert self.lp.get_home_text().lower() == "home".lower()


    def test_Create_Organization(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_submit()
        self.lp.set_otp(self.userOtp)
        self.lp.click_submit()
        assert self.lp.get_home_text().lower() == "home".lower()

        self.org = Organizations(self.driver)
        self.org.click_administration()
        self.org.click_organizations()
        self.org.click_new_organization()
        self.org.set_org_name("Shani Pate Org")
        self.org.set_org_address("123 Cleveland.")
        self.org.set_org_city("Cleveland")
        self.org.set_org_state("New York")
        self.org.set_org_country("United States")
        self.org.set_org_zipcode("12345")
        self.org.set_org_parent_org("Advance solutionsas")
        self.org.enable_trial_status()
        self.org.activate_status()
        self.org.set_product_name("Insight To Behavior")
        self.org.click_save()
        assert "success" in WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".ant-notification-notice-message"))).text
        time.sleep(10)
