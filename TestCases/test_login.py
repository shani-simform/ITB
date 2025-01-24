import time
import pytest
from PageObjects.LoginObjects import LoginPage

class Test_login():

    username = "shanipatel@yopmail.com"
    password = "Shani@123"
    baseurl = "https://dev.insightstobehavior.net"
    userOtp = "999999"

    def test_001_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        self.lp.set_otp(self.userOtp)
        self.lp.click_login()
        assert self.lp.get_home_text().lower() == "home".lower()

    @pytest.mark.dependency(depends=["test_001_login"], skip=True)
    def test_002_rememberme(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.toggle_checkbox()
        self.lp.click_login()
        self.lp.set_otp(self.userOtp)
        self.lp.click_login()
