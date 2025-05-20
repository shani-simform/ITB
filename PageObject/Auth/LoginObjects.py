from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObject.BasePage import BasePage

class LoginPage(BasePage):

    username_input_xpath = "//*[@id='email']"
    password_input_xpath = "//*[@id='password']"
    rememberMe_xpath = "//span[@class='ant-checkbox']/input"
    forgotPassword_btn_xpath = "//a[@class='login-form-forgot']"
    submit_btn_xpath = "//button[@type='submit']"
    passwordEyeButton_btn_xpath = "//span[@type='suffix']"
    otp_input_xpath = "//*[@id='otp']"
    resend_btn_xpath = "//*[@class='right']"
    backToLogin_btn_xpath = "//*[@class='back-link']"
    validation_txt_xpath = "//*[@class='text']"
    home_txt_xpath = "//*[@class='header-title']"
    logout_btn_xpath = "//span[contains(text(), 'Logout')]"
    switchorg_xpath = "(// button[@class='ant-btn ant-btn-default ng-star-inserted'])[1]"
    
    email_input_css = "input[placeholder='Enter your email']"
    password_input_css = "input[type='password']"
    remember_me_checkbox_css = "input[type='checkbox']" 
    forgot_password_link_css = "a:contains('Forgot password')"
    sign_in_button_css = "button:contains('Sign in')"
    password_eye_button_css = ".password-eye"
    email_error_message_css = ".error-message"
    login_error_message_css = ".alert-error-message"
    
    school_table_css = "table.school-selection-table"
    school_select_button_css = "button:contains('Select')"
    
    username_reset_input_css = "input[placeholder='Enter username']"
    reset_password_button_css = "button:contains('Reset password')"
    back_to_sign_in_link_css = "a:contains('Back to sign in')"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.WebDriverWait = WebDriverWait(self.driver, 25)

    def toggle_checkbox(self):
        self.WebDriverWait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.rememberMe_xpath)))
        checkbox = self.driver.find_element(By.CSS_SELECTOR, self.rememberMe_xpath)
        checkbox.click()

    def set_username(self, username):
        locator = (By.XPATH, self.username_input_xpath)
        self.send_keys(*locator, username)

    def select_organization(self):
        locator = (By.XPATH, self.switchorg_xpath)
        self.click(*locator)

    def set_password(self, password):
        locator = (By.XPATH, self.password_input_xpath)
        self.send_keys(*locator, password)

    # Used to click on the login and submit the form.
    def click_submit(self):
        locators = (By.XPATH, self.submit_btn_xpath)
        self.click(*locators)

    def click_logout(self):
        locators = (By.XPATH, self.logout_btn_xpath)
        self.click(*locators)

    def click_forgot_password(self):
        locator = By.XPATH, self.forgotPassword_btn_xpath
        self.click(*locator)

    def click_password_eye_button(self):
        locator = By.XPATH, self.passwordEyeButton_btn_xpath
        self.click(*locator)

    def set_otp(self, otp):
        locator = (By.XPATH, self.otp_input_xpath)
        self.send_keys(*locator, otp)

    def click_resend(self):
        locator = (By.XPATH, self.resend_btn_xpath)
        self.click(*locator)

    def click_back_to_login(self):
        locator = By.XPATH, self.backToLogin_btn_xpath
        self.click(*locator)

    def get_validation_message(self):
        locator = (By.XPATH, self.validation_txt_xpath)
        return self.get_text(*locator)

    def get_home_text(self):
        locator = (By.XPATH, self.home_txt_xpath)
        return self.get_text(*locator)
        
    def set_email(self, email):
        locator = (By.CSS_SELECTOR, self.email_input_css)
        self.send_keys(*locator, email)
        
    def set_password_new(self, password):
        locator = (By.CSS_SELECTOR, self.password_input_css)
        self.send_keys(*locator, password)
        
    def click_remember_me(self):
        locator = (By.CSS_SELECTOR, self.remember_me_checkbox_css)
        self.click(*locator)
        
    def click_forgot_password_new(self):
        locator = (By.CSS_SELECTOR, self.forgot_password_link_css)
        self.click(*locator)
        
    def click_sign_in(self):
        locator = (By.CSS_SELECTOR, self.sign_in_button_css)
        self.click(*locator)
    
    def click_password_eye_new(self):
        locator = (By.CSS_SELECTOR, self.password_eye_button_css)
        self.click(*locator)
        
    def get_email_error_message(self):
        locator = (By.CSS_SELECTOR, self.email_error_message_css)
        return self.get_text(*locator)
        
    def get_login_error_message(self):
        locator = (By.CSS_SELECTOR, self.login_error_message_css)
        return self.get_text(*locator)
        
    def select_school(self, index=0):
        """Select a school from the table by index (0-based)"""
        buttons = self.driver.find_elements(By.CSS_SELECTOR, self.school_select_button_css)
        if index < len(buttons):
            buttons[index].click()
            
    def get_school_names(self):
        """Get all school names from the table"""
        cells = self.driver.find_elements(By.CSS_SELECTOR, f"{self.school_table_css} td:first-child")
        return [cell.text for cell in cells]
    
    def set_username_for_reset(self, username):
        locator = (By.CSS_SELECTOR, self.username_reset_input_css)
        self.send_keys(*locator, username)
        
    def click_reset_password(self):
        locator = (By.CSS_SELECTOR, self.reset_password_button_css)
        self.click(*locator)
        
    def click_back_to_sign_in(self):
        locator = (By.CSS_SELECTOR, self.back_to_sign_in_link_css)
        self.click(*locator)

