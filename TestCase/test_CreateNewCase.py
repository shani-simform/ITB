import time
from PageObject.Insights.CreateNewCase import CreateNewCase
from PageObject.Insights.insightDetails import BIPCasePage

class Test_DefineBehavior:


    def test_addnewbehavior(self, setup, login):
        self.driver = setup
        self.cnc = CreateNewCase(self.driver)
        self.cnc.click_insight_menu_item()
        self.cnc.click_new_incident_tracker()
        self.cnc.enter_student_id("123458542")
        self.cnc.enter_student_firstname("shaniTest")
        self.cnc.enter_student_lastname("Test")
        self.cnc.enter_student_dob("04/30/2025")
        self.cnc.select_student_gender("Male")
        self.cnc.select_student_race("Asian")
        self.cnc.select_student_behavior_category("Bus")
        self.cnc.select_student_behavior_subcategory("Aggression Towards Others")
        self.cnc.select_student_schedule("shani schedule 002")
        self.cnc.select_student_language()
        self.cnc.click_submit_button()


        time.sleep(10)
