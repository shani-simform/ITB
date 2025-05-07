import time

from PageObject.Administration.OrganizationsObjects import Organizations


class TestOrganizations:

    username = "shani@simformsolutions.com"
    password =  "Shani@123" #"@PlE8tXcK4oX"
    baseurl = "https://dev.insightstobehavior.net"
    userOtp = "999999"

    # @pytest.fixture(scope="function", autouse=True)
    # def test_001_login(self, setup):
    #     self.driver = setup
    #     self.driver.get(self.baseurl)
    #     self.lp = LoginPage(self.driver)
    #     self.lp.set_username(self.username)
    #     self.lp.set_password(self.password)
    #     self.lp.click_submit()
    #     self.lp.set_otp(self.userOtp)
    #     self.lp.click_submit()
    #     self.lp.select_organization()
    #     assert self.lp.get_home_text().lower() == "home".lower()


    def test_Create_Organization(self, setup, login):
        self.driver = setup
        self.org = Organizations(self.driver)
        self.org.click_administration()
        self.org.click_organizations()
        self.org.click_new_organization()
        self.org.set_org_name("Shani Pate Org")
        self.org.set_org_address("123 Cleveland.")
        self.org.set_org_zipcode("12345")
        self.org.set_org_country("United States")
        self.org.set_org_state("New York")
        self.org.set_org_city("Cleveland")
        self.org.set_org_parent_org("Advance solutionsas")
        self.org.enable_trial_status()
        self.org.activate_status()
        self.org.set_product_name("Insight To Behavior")
        self.org.click_save()
        message = self.org.get_message()
        assert "success" in message

    def test_Search_Organization(self, setup,login):
        self.org = Organizations(self.driver)
        self.org.click_administration()
        self.org.click_organizations()
        self.org.search_Parent_Organization("Advance solutionsas")
        self.org.getsearchedorganization("Advance solutionsas")
        # self.org.click
        time.sleep(20)
