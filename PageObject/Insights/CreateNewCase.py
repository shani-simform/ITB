from selenium.webdriver.common.by import By
from PageObject.BasePage import BasePage
from selenium.webdriver.common.keys import Keys


class CreateNewCase(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    CLOSE_DRAWER_XPATH = (By.XPATH, "//button[@aria-label='Close']")
    INSIGHT_MENU_ITEM_XPATH = (By.XPATH, "//li/span/span[text()='Insights']")
    BIP_MENU_ITEM_LINK_XPATH = (By.XPATH, "//div[@class='ant-tabs-nav-list']/div[2]/button")
    SEARCH_STUDENT_NAME_INPUT_XPATH = (By.XPATH, "//input[@placeholder='Student name']")
    CLICK_SEARCH_STUDENT_NAME_XPATH = (By.XPATH, "//tbody/tr[2]/td[2]/button")
    SPINNERS_XPATH = (By.XPATH, "//span[@class='ant-spin-dot ant-spin-dot-spin ng-star-inserted']")
    NEW_INCIDENT_TRACKER = (By.XPATH, "//*[text()=' New Incident Tracker ']")
    SEARCH_STUDENT = (By.XPATH, "//*[@placeholder='Search student']")
    STUDENT_ID = (By.XPATH, "//*[@placeholder='Student ID']")
    # SELECT_STUDENT_SCHOOL = (By.XPATH, "//*[@nzerrortip="Please select student's school."]//input")
    SELECT_STUDENT_SCHOOL = (By.XPATH, "//*[@nzerrortip=\"Please select student's school.\"]//input")
    ENTER_STUDENT_FIRSTNAME = (By.XPATH, "//*[@placeholder='Enter first name']")
    ENTER_STUDENT_LASTNAME = (By.XPATH, "//*[@placeholder='Enter last name']")
    ENTER_STUDENT_DOB = (By.XPATH, "//input[@placeholder='Select Date']")
    SELECT_STUDENT_GENDER = (By.XPATH, "//*[@nzerrortip='Please select gender.']//input")
    SELECT_STUDENT_RACE = (By.XPATH, "//*[@nzerrortip='Please select race.']//input")
    SELECT_STUDENT_GEN_EDUCATION = (By.XPATH, "//*[@nzerrortip='Please select general education.']//input")
    SELECT_STUDENT_SPECIAL_EDUCATION = (By.XPATH, "//*[@nzerrortip='Please select special education.']//input")
    SELECT_STUDENT_BEHAVIOR_CATEGORY = (By.XPATH, "//*[@nzerrortip='Please select Behavior category.']//input")
    SELECT_STUDENT_BEHAVIOR_SUBCATEGORY = (By.XPATH, "//*[@nzerrortip='Please select Behavior sub-type.']//input")
    SELECT_STUDENT_SCHEDULE = (By.XPATH, "//*[@nzerrortip='Please select student schedule.']//input")
    SELECT_STUDENT_LANGUAGE = (By.XPATH, "//*[@class='radio-wrapper']//span[@class='ant-radio']/input")
    ENTER_STUDENT_NOTE = (By.XPATH, "//textarea[@id='note']")
    SELECT_TRAINING_STUDENT = (By.XPATH, "//*[@nzerrortip='Please select training student.']//nz-select-item")
    SELECT_STUDENT_SAFETYPLAN = (By.XPATH, "//*[@nzerrortip='Please select safety plan.']//nz-select-item")
    SELECT_DROPDOWN_VALUE = (By.XPATH, "//nz-option-item[contains(@title, '{value}')]")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")

    def search_student(self, studentname):
        self.send_keys(*self.SEARCH_STUDENT, studentname)
        self.click(By.XPATH, self.SELECT_DROPDOWN_VALUE[1].format(value="Shani"))

    def enter_student_id(self, studentid):
        self.wait_for_spinner()
        self.send_keys(*self.STUDENT_ID, studentid)

    def select_student_school(self, schoolname):
        self.click(*self.SELECT_STUDENT_SCHOOL)
        self.click(By.XPATH, self.SELECT_DROPDOWN_VALUE[1].format(value=schoolname))

    def enter_student_firstname(self, firstname):
        self.send_keys(*self.ENTER_STUDENT_FIRSTNAME, firstname)

    def enter_student_lastname(self, lastname):
        self.send_keys(*self.ENTER_STUDENT_LASTNAME, lastname)

    def enter_student_dob(self, studentdob):
        self.send_keys(*self.ENTER_STUDENT_DOB, studentdob)

    def select_student_gender(self, gender):
        self.click(*self.SELECT_STUDENT_GENDER)
        self.click(By.XPATH, self.SELECT_DROPDOWN_VALUE[1].format(value=gender))

    def select_student_race(self, studentrace):
        self.click(*self.SELECT_STUDENT_RACE)
        self.click(By.XPATH, self.SELECT_DROPDOWN_VALUE[1].format(value=studentrace))

    def select_student_gen_education(self, geneducation):
        self.click(*self.SELECT_STUDENT_GEN_EDUCATION)
        self.click(By.XPATH, self.SELECT_DROPDOWN_VALUE[1].format(value=geneducation))

    def select_student_special_education(self, speceducation):
        self.click(*self.SELECT_STUDENT_SPECIAL_EDUCATION)
        self.click(By.XPATH, self.SELECT_DROPDOWN_VALUE[1].format(value=speceducation))

    def select_student_behavior_category(self, behaviorcategory):
        self.click(*self.SELECT_STUDENT_BEHAVIOR_CATEGORY)
        self.click(By.XPATH, self.SELECT_DROPDOWN_VALUE[1].format(value=behaviorcategory))

    def select_student_behavior_subcategory(self, behaviorsubcategory):
        self.click(*self.SELECT_STUDENT_BEHAVIOR_SUBCATEGORY)
        self.click(By.XPATH, self.SELECT_DROPDOWN_VALUE[1].format(value=behaviorsubcategory))

    def select_student_schedule(self, studentschedule):
        self.send_keys(*self.ENTER_STUDENT_NOTE, Keys.ESCAPE)
        try:
            self.click(*self.SELECT_STUDENT_SCHEDULE)
            self.click(By.XPATH, self.SELECT_DROPDOWN_VALUE[1].format(value=studentschedule))
        except:
            pass

    def select_student_language(self):
        self.click(*self.SELECT_STUDENT_LANGUAGE)

    def enter_student_note(self, studentnote):
        self.send_keys(*self.ENTER_STUDENT_NOTE, studentnote)

    def click_submit_button(self):
        self.click(*self.SUBMIT_BUTTON)

    def click_new_incident_tracker(self):
        self.click(*self.NEW_INCIDENT_TRACKER)

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