import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#
# class Organizations:
#
#     btn_admnistration_xpath = "//span[@class='display-flex submenu-title ng-star-inserted']//span[contains(text(), 'Administration')]"
#     btn_organization_xpath = "//ul[@class='ng-star-inserted']//span[contains(text(), ' Organizations ')]"
#     btn_newOrganization_xpath = "//button[@class='ant-btn ant-btn-primary']//span[contains(text(), 'New Organization')]"
#     inp_orgName_xpath = "//input[@id='orgname']"
#     inp_orgAdd_xpath = "//input[@id='orgadd']"
#     inp_orgCity_xpath = "//input[@id='orgcity']"
#     inp_orgState_xpath = "(//input[@class='ant-select-selection-search-input ng-pristine ng-valid ng-touched'])[1]"
#     inp_orgCountry_xpath = "(//input[@class='ant-select-selection-search-input ng-pristine ng-valid ng-touched'])[1]"
#     inp_orgParentOrg_xpath = "(//input[@class='ant-select-selection-search-input ng-pristine ng-valid ng-touched'])[1]"
#     check_status_Active_xpath = "(//span[@class='ant-checkbox'])[1]"
#     check_status_trial_xpath = "(//span[@class='ant-checkbox'])[2]"
#     inp_productName_xpath = "//input[@class='orgproductname']"
#     btn_cancel_xpath = "//span[@class='ng-star-inserted' and text()=' Cancel ']"
#     btn_saveOrg_xpath = "//button[@class='ant-btn ant-btn-primary ng-star-inserted']"
#     inp_searchOrg_xpath = "//input[@placeholder='Search organizations']"
#

class Organizations:

    btn_admnistration_xpath = "//span[@class='display-flex submenu-title ng-star-inserted']//span[contains(text(), 'Administration')]"
    btn_organization_xpath = "//ul[@class='ng-star-inserted']//span[contains(text(), ' Organizations ')]"
    btn_newOrganization_xpath = "//button[@class='ant-btn ant-btn-primary']//span[contains(text(), 'New Organization')]"
    inp_orgName_xpath = "//input[@id='orgname']"
    inp_orgAdd_xpath = "//input[@id='orgadd']"
    inp_orgCity_xpath = "//input[@id='orgcity']"
    inp_orgZipCode_xpath = "//input[@id='orgzipcode']"
    inp_orgState_xpath = "(//nz-select-search[@class='ant-select-selection-search ng-star-inserted']/input)[2]"

    inp_orgCountry_xpath = "(//nz-select-search[@class='ant-select-selection-search ng-star-inserted']/input)[1]"
    inp_orgParentOrg_xpath = "(//nz-select-search[@class='ant-select-selection-search ng-star-inserted']/input)[3]"
    check_status_Active_xpath = "(//span[@class='ant-checkbox'])[1]"
    check_status_trial_xpath = "(//span[@class='ant-checkbox'])[2]"
    inp_productName_xpath = "//input[@id='orgproductname']"
    btn_cancel_xpath = "//span[@class='ng-star-inserted' and text()=' Cancel ']"
    btn_saveOrg_xpath = "//button[@class='ant-btn ant-btn-primary ng-star-inserted']"
    inp_searchOrg_xpath = "//input[@placeholder='Search organizations']"
    alert_text_css = ".ant-notification-notice-message"
    # View Org details:
    view_org_name_xpath = "//input[@id='orgname']"
    view_child_org_xpath = "//button[text()=' {Organizations} ']"
    getchildorgName = "(//div[@class='drawer-table-wrapper']//table)[2]/tbody/tr[i+1]/td[2]/button"
    view_org_address_xpath = "//input[@id='orgadd']"
    view_org_zipcode_xpath = "//input[@id='orgzipcode']"
    view_org_country_xpath = "(//nz-select-item[@class='ant-select-selection-item ng-star-inserted'])[1]"
    view_org_state_xpath = "(//nz-select-item[@class='ant-select-selection-item ng-star-inserted'])[2]"
    view_org_city_xpath = "//input[@id='orgcity']"
    view_org_parentorg_xpath = "(//input[@class='ant-select-selection-search-input ng-untouched ng-pristine'])[3]"



    def __init__(self, driver):
        self.driver = driver
        self.WebDriverWait = WebDriverWait(self.driver, 25)

    def set_input(self, xpath, value):
        self.WebDriverWait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        element = self.driver.find_element(By.XPATH, xpath)
        element.clear()
        element.send_keys(value)

    def click_button(self, xpath):
        self.WebDriverWait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        self.driver.find_element(By.XPATH, xpath).click()

    def toggle_checkbox(self, xpath):
        self.WebDriverWait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        checkbox = self.driver.find_element(By.XPATH, xpath)
        checkbox.click()

    def get_text(self, locator, selector):
        if selector.lower() == 'css':
            self.WebDriverWait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))
            return self.driver.find_element(By.CSS_SELECTOR, locator).text
        elif selector.lower() == 'xpath':
            self.WebDriverWait.until(EC.presence_of_element_located((By.XPATH, locator)))
            return self.driver.find_element(By.XPATH, locator).text

    def getsearchedorganization(self, orgname):
        total_org = self.driver.find_elements(By.XPATH, "//tbody/tr[@class='ant-table-row ng-star-inserted']/td[2]//span")
        for i in range(len(total_org)):
            searchedorg = self.driver.find_element(By.XPATH, f"//tbody/tr[@class='ant-table-row ng-star-inserted'][{i+1}]/td[2]//span").text
            if searchedorg == orgname:
                total_org[i].click()

    def click_child_org(self, orgname):
        listofChildOrg = self.driver.find_elements(By.XPATH, "(//div[@class='drawer-table-wrapper']//table)[2]/tbody/tr/td[2]/button")
        for i in range(len(listofChildOrg)):
            orglist = f"(//div[@class='drawer-table-wrapper']//table)[2]/tbody/tr{i+1}/td[2]/button"
            getorgname = self.driver.find_element(By.XPATH, orglist)
            if getorgname.text == orgname:
                getorgname.click()

    def verifyorg_details(self, orgdetails):
        Orgname = orgdetails[0]
        Address = orgdetails[1]
        Zipcode = orgdetails[2]
        Country = orgdetails[3]
        State = orgdetails[4]
        City = orgdetails[5]
        ParentOrganization = orgdetails[6]
        ProductName = orgdetails[7]







    def get_message(self):
        return self.get_text(self.alert_text_css, 'css')

    def set_org_name(self, name):
        self.set_input(self.inp_orgName_xpath, name)

    def set_org_address(self, address):
        self.set_input(self.inp_orgAdd_xpath, address)

    def set_org_city(self, city):
        self.set_input(self.inp_orgCity_xpath, city)

    def set_org_zipcode(self, code):
        self.set_input(self.inp_orgZipCode_xpath, code)


    def set_org_state(self, state):
        self.set_input(self.inp_orgState_xpath, state)
        self.click_button(f"//nz-option-item[contains(@title, '{state}')]")

    def set_org_country(self, country):
        self.set_input(self.inp_orgCountry_xpath, country)
        time.sleep(5)
        self.click_button(f"//nz-option-item[contains(@title, '{country}')]")

    def set_org_parent_org(self, parent_org):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.driver.find_element(By.XPATH, self.inp_orgParentOrg_xpath))
        self.set_input(self.inp_orgParentOrg_xpath, parent_org)
        time.sleep(3)
        self.click_button(f"//nz-option-item[contains(@title, '{parent_org}')]")

    def activate_status(self):
        self.toggle_checkbox(self.check_status_Active_xpath)

    def enable_trial_status(self):
        self.toggle_checkbox(self.check_status_trial_xpath)

    def set_product_name(self, product_name):
        self.set_input(self.inp_productName_xpath, product_name)

    def click_administration(self):
        self.click_button(self.btn_admnistration_xpath)

    def click_organizations(self):
        self.click_button(self.btn_organization_xpath)

    def click_new_organization(self):
        self.click_button(self.btn_newOrganization_xpath)

    def click_cancel(self):
        self.click_button(self.btn_cancel_xpath)

    def click_save(self):
        self.click_button(self.btn_saveOrg_xpath)

    def search_Parent_Organization(self, org_name):
        self.set_input(self.inp_searchOrg_xpath, org_name)

