from test_common import TestCommon
from openeobs_selenium.login_page import LoginPage
from openeobs_selenium.task_page import TaskPage
from openeobs_selenium.list_page import ListPage


class TestSMPatientPage(TestCommon):
    def setUp(self):
        self.driver.get("http://localhost:8069/mobile/")
        self.login_page = LoginPage(self.driver)
        self.task_list_page = ListPage(self.driver)
        self.patient_list_page = ListPage(self.driver)
        self.login_page.login('saint', 'saint')
        self.task_list_page.go_to_task_list()

    def test_can_logout(self):
        self.task_list_page.logout()
        self.assertTrue(self.task_list_page.is_login_page(), 'did notget to the logout')

    def test_has_no_task(self):
        """
        Test that task list show no task for user
        """
        task_list=[]

        for patient in self.task_list_page.get_list_items():
            task_list.append(patient)
            self.assertEquals(task_list,[],'There are no tasks')

    def test_go_to_patients_list_page(self):
        """
        Test that senior manager can go on patients list
        """

        self.patient_list_page.go_to_patient_list()
        self.assertTrue(self.patient_page.is_patient_list_page(),'Did not go to patient page correctly')

    def test_can_not_take_patient_observation(self):
        """
        Test that user can not take observation
        """
        self.patient_list_page.go_to_patient_list()

        patients = self.patient_list_page.get_list_items()
        patients_to_test = patients[0]
        patients_to_test.click()









