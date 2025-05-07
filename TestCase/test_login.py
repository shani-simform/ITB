import pytest
from PageObject.Auth.LoginObjects import LoginPage


class Test_login:

    username = "shani@simformsolutions.com"
    password =  "Shani@123" #"@PlE8tXcK4oX"
    baseurl = "https://dev.insightstobehavior.net"
    userOtp = "999965"

    # @pytest.fixture(scope="function", autouse=True)
    @pytest.mark.testmarker
    def test_001_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_submit()
        self.lp.set_otp(self.userOtp)
        self.lp.click_submit()
        assert False
        # assert self.lp.get_home_text().lower() == "home".lower()
        # self.lp.click_logout()

    @pytest.mark.dependency(depends=["test_001_login"], skip=True)

    def test_002_rememberme(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.toggle_checkbox()
        self.lp.click_submit()
        self.lp.set_otp(self.userOtp)
        self.lp.click_submit()
        assert self.lp.get_home_text().lower() == "home".lower()

