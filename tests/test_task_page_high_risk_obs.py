"""Test to ensure that a high risk NEWS ob works correctly"""
from openeobs_mobile.data import HIGH_RISK_SCORE_9_EWS_DATA
from openeobs_mobile.login_page import LoginPage
from openeobs_mobile.list_page import ListPage
from openeobs_mobile.patient_page import PatientPage
from tests.test_common import TestCommon
from openeobs_mobile.locators import PatientPageLocators, TaskPageLocators
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui


class TestHighRiskPage(TestCommon):
    """
    Setup a session and test that a high risk NEWS observation
    can be submitted, and that the correct action triggers
    """
    def setUp(self):
        self.driver.get("http://localhost:8069/mobile/login")
        self.login_page = LoginPage(self.driver)
        self.patient_list_page = ListPage(self.driver)
        self.login_page.login('nasir', 'nasir')
        self.patient_list_page.go_to_patient_list()

    def test_high_risk_obs(self):
        """
        Test that an 'immediately inform medical team' task is triggered
        after a high NEWS score
        """
        high_score = HIGH_RISK_SCORE_9_EWS_DATA

        patients = self.patient_list_page.get_list_items()

        PatientPage(self.driver).select_patient(patients)
        PatientPage\
            (self.driver).open_form(
                PatientPageLocators.open_obs_menu_news_item)
        PatientPage(self.driver).enter_obs_data(high_score)

        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(TaskPageLocators.confirm_submit)
        ).click()

        task = 'Immediately inform medical team'
        response = ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((
                TaskPageLocators.related_task))
        )
        self.assertEqual(task, response.text,
                         'Incorrect triggered action for high risk ob')
