"""Test to ensure that a Weight ob works correctly"""
from openeobs_mobile.data import WEIGHT_DATA
from openeobs_mobile.login_page import LoginPage
from openeobs_mobile.list_page import ListPage
from openeobs_mobile.patient_page import PatientPage
from tests.test_common import TestCommon
from openeobs_mobile.task_page_locators import successful_submit
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui
from openeobs_mobile.patient_page_locators import open_obs_menu_weight


class TestWeightObsPage(TestCommon):
    """
    Setup a session and test that a weight observation can be submitted
    """

    def setUp(self):
        self.driver.get("http://localhost:8069/mobile/login")
        self.login_page = LoginPage(self.driver)
        self.patient_list_page = ListPage(self.driver)
        self.login_page.login('nasir', 'nasir')
        self.patient_list_page.go_to_patient_list()

    def test_weight_obs(self):
        """
        Test that a weight observation can be submitted
        """
        weight_input = WEIGHT_DATA

        patients = self.patient_list_page.get_list_items()

        PatientPage(self.driver).select_patient(patients)
        PatientPage(self.driver).open_form(open_obs_menu_weight)
        PatientPage(self.driver).enter_obs_data(weight_input)

        success = 'Successfully Submitted Weight Observation'
        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((
                successful_submit))
        )

        response = self.driver.find_element(*successful_submit)

        self.assertEqual(success, response.text,
                         'Weight observation unsuccessful')
