# PageObjects/bip_case_page.py
from selenium.webdriver.common.by import By
from PageObject.BasePage import BasePage


class BIPCasePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    CLOSE_DRAWER_XPATH = (By.XPATH, "//button[@aria-label='Close']")
    STUDENT_MORE_OPTIONS_XPATH = (By.XPATH, "//div[contains(@class,'action-dropdown')]//button")
    MANAGE_ATTACHMENT_XPATH = (By.XPATH, "//button[@title=' Manage student attachment ']")
    MANAGE_STUDENT_TEAM_XPATH = (By.XPATH, "//button[@title=' Manage student team ']")
    EDIT_CASE_DETAILS_XPATH = (By.XPATH, "//button[@title=' Edit case details ']")
    ADD_NEW_BEHAVIOR_XPATH = (By.XPATH, "//button[.//span[text()=' Add New Behavior ']]")
    ADD_DATA_XPATH = (By.XPATH, "//button[.//span[text()=' Add Data ']]")
    BEHAVIOR_OPTIONS_XPATH = (By.XPATH, "//div[contains(@class,'cta-btns')]//button[contains(@class,'ant-dropdown-trigger')]")
    BEHAVIOR_INFO_XPATH = (By.XPATH, "//svg-icon[@src='/assets/icon/icon-info.svg']/ancestor::button")
    BEHAVIOR_ACTIVE_TOGGLE_XPATH = (By.XPATH, "//span[text()='Active']/following-sibling::nz-switch//button")
    SUBCARD_DETAILS_XPATH = (By.XPATH, "//button[@nztype='link' and .//span[text()=' Details ']]")
    SUBCARD_ASSESSMENT_FBA_XPATH = (By.XPATH, "//button[@nztype='link' and .//span[text()=' Assessment FBA ']]")
    SUBCARD_STRATEGIES_XPATH = (By.XPATH, "//button[@nztype='link' and .//span[text()=' Strategies ']]")
    SUBCARD_DATA_XPATH = (By.XPATH, "//button[@nztype='link' and .//span[text()=' Data ']]")
    MENU_BEHAVIOR_INTERVENTION_PLAN_XPATH = (By.XPATH, "//ul[contains(@class,'ant-dropdown-menu')]//li[.//span[text()='Behavior Intervention Plan']]")
    MENU_DATA_LOG_XPATH = (By.XPATH, "//ul[contains(@class,'ant-dropdown-menu')]//li[.//span[text()='Data Log']]")
    MENU_PROGRESS_REPORT_MANAGER_XPATH = (By.XPATH, "//ul[contains(@class,'ant-dropdown-menu')]//li[.//span[text()='Progress Report Manager']]")
    MENU_QUICK_GUIDE_TO_PLAN_XPATH = (By.XPATH, "//ul[contains(@class,'ant-dropdown-menu')]//li[.//span[text()='Quick Guide to Plan']]")
    MENU_REFERENCE_MATERIAL_XPATH = (By.XPATH, "//ul[contains(@class,'ant-dropdown-menu')]//li[.//span[text()='Reference Material']]")
    INSIGHT_MENU_ITEM_XPATH = (By.XPATH, "//li/span/span[text()='Insights']")
    BIP_MENU_ITEM_LINK_XPATH = (By.XPATH, "//div[@class='ant-tabs-nav-list']/div[2]/button")
    SEARCH_STUDENT_NAME_INPUT_XPATH = (By.XPATH, "//input[@placeholder='Student name']")
    CLICK_SEARCH_STUDENT_NAME_XPATH = (By.XPATH, "//tbody/tr[2]/td[2]/button")
    SPINNERS_XPATH = (By.XPATH, "//span[@class='ant-spin-dot ant-spin-dot-spin ng-star-inserted']")

    def wait_for_spinner(self):
        self.wait_for_element_to_appear(*self.SPINNERS_XPATH)
        self.wait_for_element_to_disappear(*self.SPINNERS_XPATH)

    def click_student_name(self):
        self.wait_for_spinner()
        self.click(*self.CLICK_SEARCH_STUDENT_NAME_XPATH)

    def search_student_name(self, student_name):
        self.send_keys(*self.SEARCH_STUDENT_NAME_INPUT_XPATH, student_name)

    def click_BIP_menu_item(self):
        self.click(*self.BIP_MENU_ITEM_LINK_XPATH)

    def click_insight_menu_item(self):
        self.click(*self.INSIGHT_MENU_ITEM_XPATH)

    # --- Drawer controls ---
    def click_close_drawer(self):
        self.click(*self.CLOSE_DRAWER_XPATH)

    # --- Student header actions ---
    def click_student_more_options(self):
        self.click(*self.STUDENT_MORE_OPTIONS_XPATH)

    def click_manage_attachment(self):
        self.click(*self.MANAGE_ATTACHMENT_XPATH)

    def click_manage_student_team(self):
        self.click(*self.MANAGE_STUDENT_TEAM_XPATH)

    def click_edit_case_details(self):
        self.click(*self.EDIT_CASE_DETAILS_XPATH)

    # --- Behavior section CTAs ---
    def click_add_new_behavior(self):
        self.click(*self.ADD_NEW_BEHAVIOR_XPATH)

    def click_add_data(self):
        self.click(*self.ADD_DATA_XPATH)

    def click_behavior_options(self):
        self.click(*self.BEHAVIOR_OPTIONS_XPATH)

    # --- Behavior card actions ---
    def click_behavior_info(self):
        self.click(*self.BEHAVIOR_INFO_XPATH)

    def toggle_behavior_active(self):
        self.click(*self.BEHAVIOR_ACTIVE_TOGGLE_XPATH)

    # --- Sub‑card navigations ---
    def click_subcard_details(self):
        self.click(*self.SUBCARD_DETAILS_XPATH)

    def click_subcard_assessment_fba(self):
        self.click(*self.SUBCARD_ASSESSMENT_FBA_XPATH)

    def click_subcard_strategies(self):
        self.click(*self.SUBCARD_STRATEGIES_XPATH)

    def click_subcard_data(self):
        self.click(*self.SUBCARD_DATA_XPATH)

        # --- Dropdown menu item clicks ---

    def click_menu_behavior_intervention_plan(self):
        self.click(*self.MENU_BEHAVIOR_INTERVENTION_PLAN_XPATH)

    def click_menu_data_log(self):
        self.click(*self.MENU_DATA_LOG_XPATH)

    def click_menu_progress_report_manager(self):
        self.click(*self.MENU_PROGRESS_REPORT_MANAGER_XPATH)

    def click_menu_quick_guide_to_plan(self):
        self.click(*self.MENU_QUICK_GUIDE_TO_PLAN_XPATH)

    def click_menu_reference_material(self):
        self.click(*self.MENU_REFERENCE_MATERIAL_XPATH)