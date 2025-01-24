from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    username_input_css = "#email"
    password_input_css = "#password"
    rememberMe_css = "input[type='checkbox']"
    forgotPassword_btn_css = ".login-form-forgot"
    submit_btn_css = "button[type='submit']"
    passwordEyeButton_btn_css = "span[type='suffix']"
    otp_input_css = "#otp"
    resend_btn_css = ".right"
    backToLogin_btn_css = ".back-link"
    validation_txt_css = ".text"
    home_txt_css = ".header-title"
    logout_btn_xpath = "//span[contains(text(), 'Logout')]"
    forgotMessage_css = ".ant-message-notice-content.ng-tns-c744004138-20"

    def __init__(self, driver):
        self.driver = driver
        self.WebDriverWait = WebDriverWait(self.driver, 10)

    def get_text(self, locator):
        self.WebDriverWait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))
        return self.driver.find_element(By.CSS_SELECTOR, locator).text

    def click_button(self, selector, locator):
        if selector.lower() == "xpath":
            self.WebDriverWait.until(EC.element_to_be_clickable((By.XPATH, locator)))
            self.driver.find_element(By.XPATH, locator).click()
        elif selector.lower() == "css":
            self.WebDriverWait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator)))
            self.driver.find_element(By.CSS_SELECTOR, locator).click()
        else:
            return ValueError(f"unsupported selector type {selector}")

    def set_input(self, locator, value):
        self.WebDriverWait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))
        element = self.driver.find_element(By.CSS_SELECTOR, locator)
        element.clear()
        element.send_keys(value)

    def toggle_checkbox(self):
        self.WebDriverWait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.rememberMe_css)))
        checkbox = self.driver.find_element(By.CSS_SELECTOR, self.rememberMe_css)
        checkbox.click()

    def set_username(self, username):
        self.set_input(self.username_input_css, username)

    def set_password(self, password):
        self.set_input(self.password_input_css, password)

    def click_login(self):
        self.click_button('css', self.submit_btn_css)

    def click_forgot_password(self):
        self.click_button('css', self.forgotPassword_btn_css)

    def click_password_eye_button(self):
        self.click_button('css', self.passwordEyeButton_btn_css)

    def set_otp(self, otp):
        self.set_input(self.otp_input_css, otp)

    def click_resend(self):
        self.click_button('css', self.resend_btn_css)

    def click_back_to_login(self):
        self.click_button('css', self.backToLogin_btn_css)

    def get_validation_message(self):
        return self.get_text(self.validation_txt_css)

    def get_home_text(self):
        return self.get_text(self.home_txt_css)