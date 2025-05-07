from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObject.BasePage import BasePage


class DefineBehaviorPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # Locator templates
    QUESTION_BADGE =  (By.CSS_SELECTOR, ".badge")
    RADIO_OPTION    =  (By.XPATH, "//nz-radio-group[@id='{group_id}']//span[text()='{label}']")
    CHECKBOX_OPTION =  (By.XPATH, "//nz-checkbox-group//label[.//span[text()='{label}']]")
    TEXT_INPUT      =  (By.XPATH, "//input[@formcontrolname='{field_name}']")
    BTN_NEXT        =  (By.XPATH, "//button[@nztype='primary' and .//span[text()=' Next ']]")
    BTN_PREV        =  (By.XPATH, "//button[@nztype='default' and .//span[text()=' Prev ']]")
    BTN_SAVE_LATER  =  (By.XPATH, "//button[.//span[text()=' Save for later ']]")
    BTN_SAVE        =  (By.XPATH, "//button[.//span[text()=' Save ']]")
    VAL_MESSAGE     =  (By.XPATH, "//*[contains(@class, 'ant-notification-notice-message')]/div")

    def get_current_step(self) -> int:
        text = self.get_text(*self.QUESTION_BADGE)      # e.g. “1/11”
        return int(text.split("/")[0])

    def select_radio(self, label: str):
        locator = (By.XPATH, self.RADIO_OPTION[1].format(group_id="behaviorCategory", label=label))
        self.click(*locator)

    def select_checkbox(self, label: str):
        locator = (By.XPATH, self.CHECKBOX_OPTION[1].format(label=label))
        self.click(*locator)

    def enter_text(self, field_name: str, value: str):
        locator = (By.XPATH, self.TEXT_INPUT[1].format(field_name=field_name))
        self.send_keys(*locator, value)

    def click_next(self):
        self.click(*self.BTN_NEXT)

    def click_prev(self):
        self.click(*self.BTN_PREV)

    def click_save_later(self):
        self.click(*self.BTN_SAVE_LATER)

    def click_save(self):
        self.click(*self.BTN_SAVE)

    # Question 1: Category (Radio Buttons)
    def select_behavior_category(self, category_name):
        locator = (By.XPATH, f"//nz-radio-group[@formcontrolname='behaviorCategoryId']//span[contains(text(), '{category_name}')]")
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    # Question 2: Behavior Types (Dynamic Checkboxes)
    def select_behavior_types(self, *types):
        for behavior_type in types:
            locator = (By.XPATH, f"//div[@class='checkbox-wrapper']//label[span[contains(text(), '{behavior_type}')]]")
            self.wait.until(EC.element_to_be_clickable(locator)).click()
            #todo: add the other text in the field
            # if "Other".lower() in behavior_type.lower():
            #     self.enter_text("behaviorType", behavior_type)
            #     break

    # Question 3: Operational Definition (Textarea)
    def enter_operational_definition(self, text):
        locator = (By.XPATH, "//textarea[@formcontrolname='operationalDefinition']")
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    # Question 4: Frequency Section
    def select_behavior_frequency(self, frequency_text):
        locator = (By.XPATH, f"//nz-radio-group[@formcontrolname='behaviourFrequencyId']//span[contains(text(), '{frequency_text}')]")
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def enter_frequency_count(self, count):
        locator = (By.XPATH, "//input[@formcontrolname='behaviourFrequencyCount']")
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(str(count))

    def select_duration_type(self, duration_type_text):
        locator = (By.XPATH, f"//nz-radio-group[@formcontrolname='isDurationRequired']//span[contains(text(), '{duration_type_text}')]")
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def enter_duration(self, duration):
        locator = (By.XPATH, "//input[@formcontrolname='duration']")
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(str(duration))

    # Question 5: Intensity (Radio Buttons)
    def select_behavior_intensity(self, intensity_text):
        locator = (By.XPATH, f"//nz-radio-group[@formcontrolname='behaviourIntensityId']//span[contains(text(), '{intensity_text}')]")
        self.wait.until(EC.element_to_be_clickable(locator)).click()
        if "Moderate" or "Major" in intensity_text:
            by, locator = (By.XPATH, "//button/span[contains(text(), ' I Understand ')]")
            self.click(by, locator)

    # Question 6–9: Checkboxes for Environments, Setting Events, Antecedents, Consequences
    def select_multiple_checkboxes(self, *label_text):
        for label in label_text:
            locator = (By.XPATH, f"//label[span[contains(text(), '{label}')]]")
            self.wait.until(EC.element_to_be_clickable(locator)).click()

    # Question 10: Goals (Textarea, ignore district instructions)
    def enter_goal_text(self, goal_text):
        locator = (By.XPATH, "//textarea[@formcontrolname='goals']")
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(goal_text)

    # Question 11: Custom Questions with Dynamic Inputs
    def answer_custom_question_by_index(self, answer):
        locator = (By.XPATH, f"//*[contains(@class, 'ant-form-item-required')]/ancestor::nz-form-item//following-sibling::nz-form-control//input")
        questions = self.driver.find_elements(*locator)
        for i, question in enumerate(questions):
            question.send_keys(answer+f"{i + 1}")

    def get_validation_message(self):
        return self.get_text(*self.VAL_MESSAGE)