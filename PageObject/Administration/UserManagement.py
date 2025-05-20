from selenium.webdriver.common.by import By
from PageObject.BasePage import BasePage
import time

class UserManagement(BasePage):
    # Buttons and Inputs
    btn_add_user = (By.XPATH, "//button[.='Add User']")
    input_username = (By.XPATH, "//input[@placeholder='Enter username']")
    input_first_name = (By.XPATH, "//input[@placeholder='First Name']")
    input_last_name = (By.XPATH, "//input[@placeholder='Last Name']")
    search_input = (By.XPATH, "//input[@placeholder='Search users']")
    btn_save_user = (By.XPATH, "//button[.='Add' or .='Save' and not(@disabled)]")
    alert_message = (By.CSS_SELECTOR, ".ant-notification-notice-message")
    # Dropdowns (click to open, then type in the search input, then select option)
    dropdown_school = (By.XPATH, "//nz-select[@formcontrolname='organizationid']")
    dropdown_title = (By.XPATH, "//nz-select[@formcontrolname='titleId']")
    dropdown_status = (By.XPATH, "//nz-select[@formcontrolname='status']")
    # The search input inside any open dropdown panel
    dropdown_search_input = (By.XPATH, "//div[contains(@class,'ant-select-dropdown') and contains(@class,'ng-trigger')]//input[@type='search']")
    # Option in dropdown panel (text match)
    dropdown_option = lambda self, value: (By.XPATH, f"//div[contains(@class,'ant-select-item-option-content') and text()='{value}']")
    # Roles (checkboxes by label text)
    role_checkbox = lambda self, role: (By.XPATH, f"//label[.//span[text()='{role}']]//input[@type='checkbox']")
    # Table row and actions
    user_row = lambda self, username: (By.XPATH, f"//tr[td[contains(., '{username}')]]")
    btn_edit_user = lambda self, username: (By.XPATH, f"//tr[td[contains(., '{username}')]]//button[@title='Edit']")
    btn_delete_user = lambda self, username: (By.XPATH, f"//tr[td[contains(., '{username}')]]//button[@title='Delete']")
    btn_confirm_delete = (By.XPATH, "//button[.='Delete' and not(@disabled)]")
    # --- Bulk User Management Locators ---
    # Checkbox for user row by username
    user_checkbox = lambda self, username: (By.XPATH, f"//tr[td[contains(., '{username}')]]//input[@type='checkbox']")
    # Manage button
    btn_manage = (By.XPATH, "//button[.='Manage']")
    # Manage menu options
    manage_option = lambda self, option_text: (By.XPATH, f"//li[.//span[text()='{option_text}']]")
    # Move Users panel
    move_school_dropdown = (By.XPATH, "//div[contains(@class,'ant-drawer')]//div[.='User\'s School']/following-sibling::div//input")
    move_title_dropdown = (By.XPATH, "//div[contains(@class,'ant-drawer')]//div[.='User\'s Title']/following-sibling::div//input")
    move_dropdown_option = lambda self, value: (By.XPATH, f"//div[contains(@class,'ant-select-item-option-content') and text()='{value}']")
    btn_move_save = (By.XPATH, "//div[contains(@class,'ant-drawer')]//button[.='Save']")
    # Export success message
    export_success_message = (By.XPATH, "//*[contains(text(),'Users data exported successfully')]")
    # Send/Reset Email dialog
    btn_send_reset_ok = (By.XPATH, "//button[.='OK']")
    send_reset_success_message = (By.XPATH, "//*[contains(text(),'Email Invitation has been sent successfully')]")

    def add_user(self, username, first_name, last_name, school, title, status, roles):
        self.click(*self.btn_add_user)
        self.send_keys(*self.input_username, username)
        self.send_keys(*self.input_first_name, first_name)
        self.send_keys(*self.input_last_name, last_name)
        # School dropdown
        self.click(*self.dropdown_school)
        self.send_keys(*self.dropdown_search_input, school)
        self.click(*self.dropdown_option(school))
        # Title dropdown
        self.click(*self.dropdown_title)
        self.send_keys(*self.dropdown_search_input, title)
        self.click(*self.dropdown_option(title))
        # Status dropdown
        self.click(*self.dropdown_status)
        self.send_keys(*self.dropdown_search_input, status)
        self.click(*self.dropdown_option(status))
        # Roles
        for role in roles:
            self.click(*self.role_checkbox(role))
        self.click(*self.btn_save_user)
        time.sleep(1)
        return self.get_validation_messages(*self.alert_message)

    def search_user(self, username):
        self.send_keys(*self.search_input, username)
        time.sleep(4)  # Wait for UI to update
        return self.find_element(*self.user_row(username))

    def edit_user(self, old_username, new_username=None, first_name=None, last_name=None, title=None, status=None):
        self.click(*self.btn_edit_user(old_username))
        if new_username:
            self.send_keys(*self.input_username, new_username)
        if first_name:
            self.send_keys(*self.input_first_name, first_name)
        if last_name:
            self.send_keys(*self.input_last_name, last_name)
        if title:
            self.click(*self.dropdown_title)
            self.send_keys(*self.dropdown_search_input, title)
            self.click(*self.dropdown_option(title))
        if status:
            self.click(*self.dropdown_status)
            self.send_keys(*self.dropdown_search_input, status)
            self.click(*self.dropdown_option(status))
        self.click(*self.btn_save_user)
        time.sleep(1)
        return self.get_validation_messages(*self.alert_message)

    def delete_user(self, username):
        self.click(*self.btn_delete_user(username))
        self.click(*self.btn_confirm_delete)
        time.sleep(1)
        return self.get_validation_messages(*self.alert_message)

    def select_users(self, usernames):
        """Select one or more users by username (checkboxes in table)."""
        for username in usernames:
            self.click(*self.user_checkbox(username))

    def manage_move_user(self, dest_school, dest_title):
        """Move selected users to another organization and title."""
        self.click(*self.btn_manage)
        self.click(*self.manage_option('Move Users'))
        # School dropdown
        self.click(*self.move_school_dropdown)
        self.send_keys(*self.move_school_dropdown, dest_school)
        self.click(*self.move_dropdown_option(dest_school))
        # Title dropdown
        self.click(*self.move_title_dropdown)
        self.send_keys(*self.move_title_dropdown, dest_title)
        self.click(*self.move_dropdown_option(dest_title))
        self.click(*self.btn_move_save)
        time.sleep(1)
        return self.get_validation_messages(*self.alert_message)

    def manage_export_all_users(self):
        """Export all users and assert success message."""
        self.click(*self.btn_manage)
        self.click(*self.manage_option('Export all Users'))
        time.sleep(1)
        return self.get_validation_messages(*self.alert_message)

    def manage_send_reset_email(self):
        """Send new user/reset password email and assert success message."""
        self.click(*self.btn_manage)
        self.click(*self.manage_option('Send New User / Reset Password Email'))
        self.click(*self.btn_send_reset_ok)
        time.sleep(1)
        return self.get_validation_messages(*self.alert_message)

