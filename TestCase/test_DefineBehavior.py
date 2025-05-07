import time
from PageObject.Insights.DefineBehaviorPage import DefineBehaviorPage
from PageObject.Insights.insightDetails import BIPCasePage

class Test_DefineBehavior:

    # def __init__(self):
    #     pass

    def test_addnewbehavior(self, setup, login):
        self.driver = setup
        self.DFB = DefineBehaviorPage(self.driver)
        self.IDP = BIPCasePage(self.driver)
        self.IDP.click_insight_menu_item()
        self.IDP.click_BIP_menu_item()
        self.IDP.search_student_name("1423")
        self.IDP.click_student_name()
        self.IDP.click_add_new_behavior()
        self.DFB.select_behavior_category(" Self Injury ")
        self.DFB.click_next()
        self.DFB.select_behavior_types(" Picks at skin ", " Hits self in head ", " Bangs head against objects ")
        self.DFB.click_next()
        self.DFB.enter_operational_definition(
            " 1. 100% of the time, I hit my head against a wall or a table. 2. 100% of the time, I hit my head against a wall or a table. 3. 100% of the time, I hit my head against a wall or a table. ")
        self.DFB.click_next()
        self.DFB.select_behavior_frequency(" It usually occurs at least once and possibly several times a day ")
        self.DFB.enter_frequency_count("2")
        self.DFB.select_duration_type(" Minutes ")
        self.DFB.enter_duration("12")
        self.DFB.click_next()
        self.DFB.select_behavior_intensity(" Moderate (Significantly disruptive. While it does not pose or create a dangerous environment, it can sometimes escalate or cause others to escalate further.) ")
        self.DFB.click_next()
        self.DFB.select_multiple_checkboxes(" During class time ", " Social / unstructured time ") # Select Environments
        self.DFB.click_next()
        self.DFB.select_multiple_checkboxes(" Poor sleep ", " Personal issues outside of school ") # Select Setting Events
        self.DFB.click_next()
        self.DFB.select_multiple_checkboxes(" Presentation of self-care task/demand ", " Unexpected transitions or changes ") # Select Antecedents
        self.DFB.click_next()
        self.DFB.select_multiple_checkboxes(" Token or point given ", " Token or point removed ") # Select Consequences
        self.DFB.click_next()
        self.DFB.enter_goal_text(
            " 1. 100% of the time, I hit my head against a wall or a table. 2. 100% of the time, I hit my head against a wall or a table. 3. 100% of the time, I hit my head against a wall or a table. ")
        self.DFB.click_next()
        self.DFB.answer_custom_question_by_index("This is answer for mandatory question no ")
        self.DFB.click_next()
        time.sleep(5)
        self.DFB.click_save()
        message = self.DFB.get_validation_message()
        print(message)
        if "success" in message:
            assert True
        else:
            assert False
        time.sleep(20)

