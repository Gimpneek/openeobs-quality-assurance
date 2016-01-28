"""Methods for the patient page"""

from openeobs_mobile.page_helpers import BasePage
from openeobs_mobile.locators import PatientPageLocators, TaskPageLocators
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


class PatientPage(BasePage):
    """
    Patient Page methods and helps etc
    """

    def open_adhoc_obs_menu(self):
        """
        Open up the adhoc observation menu
        """
        obs_button = self.driver.find_element(
            *PatientPageLocators.adhoc_obs_menu_button
        )
        obs_button.click()
        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.ID, 'obs_menu'))
        )
        return self.driver.find_element(*PatientPageLocators.open_obs_menu)

    def adhoc_obs_menu_is_open(self):
        """
        Check that adhoc obs menu is up
        :return: Boolean of if the menu is open or not
        """
        try:
            self.driver.find_element(
                *PatientPageLocators.open_obs_menu
            )
        except NoSuchElementException:
            return False
        return True

    def has_no_patient_data(self):
        """
        Check that the patient's record shows data
        :return: Boolean if error message is shown or not
        """
        chart = self.driver.find_element(*PatientPageLocators.graph_chart)
        return chart.text == 'No observation data available for patient'

    def tabs_are_shown(self):
        """
        Check that the tabs are visible
        :return: Boolean of if the tabs are visible or not
        """
        try:
            self.driver.find_element(
                *PatientPageLocators.table_tab_button
            )
            self.driver.find_element(
                *PatientPageLocators.graph_tab_button
            )
        except NoSuchElementException:
            return False
        return True

    def chart_is_shown(self):
        """
        Check that the chart is visible
        :return: Boolean of if the tabs are visible or not
        """
        try:
            self.driver.find_element(
                *PatientPageLocators.graph_chart_svg
            )
        except NoSuchElementException:
            return False
        return True

    def tabular_values_are_shown(self):
        """
        Check that the tabular values table is shown
        :return: Boolean of if the tabular values table is shown
        """
        try:
            self.driver.find_element(
                *PatientPageLocators.tabular_values_table
            )
        except NoSuchElementException:
            return False
        return True

    def obs_table_is_shown(self):
        """
        Check that the obs table is shown
        :return: Boolean of if the obs table is shown
        """
        try:
            self.driver.find_element(
                *PatientPageLocators.table_container
            )
        except NoSuchElementException:
            return False
        return True

    def change_to_chart(self):
        """
        Change the tabs so shows the chart
        """
        tab = self.driver.find_element(
            *PatientPageLocators.graph_tab_button
        )
        tab.click()
        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR,
                                              '#graph-content #chart svg'))
        )

    def change_to_table(self):
        """
        Change the tabs so shows the table
        """
        tab = self.driver.find_element(
            *PatientPageLocators.table_tab_button
        )
        tab.click()
        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR,
                                              '#table-content table'))
        )

    def rangify_control_is_shown(self):
        """
        Check that the rangify control is shown
        :return: Boolean of if the rangify control is shown
        """
        try:
            self.driver.find_element(
                *PatientPageLocators.rangify_control
            )
        except NoSuchElementException:
            return False
        return True

    def get_context_graph(self):
        """
        Get the context graph element
        :return: The WebElement of the context graph
        """
        return self.driver.find_element(
            *PatientPageLocators.chart_context_graph
        )

    def get_focus_graphs(self):
        """
        Get the focus graphs of the obs chart
        :return: A list of focus graph WebElements
        """
        return self.driver.find_elements(
            *PatientPageLocators.chart_focus_graphs
        )

    @staticmethod
    def get_graph_label(graph):
        """
        Get the label for a graph WebElement
        :param graph: The graph WebElement to do operation on
        :return: Label as text
        """
        label = graph.find_element(
            *PatientPageLocators.chart_graph_label
        )
        return label.text

    @staticmethod
    def get_graph_measurement(graph):
        """
        Get the measurement for a graph WebElement
        :param graph: The graph WebElement to do operation on
        :return: Label as text
        """
        measurement = graph.find_element(
            *PatientPageLocators.chart_graph_measurement
        )
        return measurement.text

    @staticmethod
    def get_graph_measurements(graph):
        """
        Get the measurements (as in multiple) for a graph WebElement
        :param graph: The graph WebElement to do operation on
        :return: Label as text
        """
        measurements = graph.find_elements(
            *PatientPageLocators.chart_graph_measurement
        )
        return measurements

    def get_tabular_values(self):
        """
        Get tabular values table
        :return: tabular values WebElement
        """
        return self.driver.find_element(
            *PatientPageLocators.tabular_values_table
        )

    @staticmethod
    def get_table_headers(table):
        """
        Get the table headers for the supplied table
        :param table: A table to get headers from
        :return: A list of table header strings
        """
        headers = table.find_elements(
            *PatientPageLocators.table_header
        )
        return [header.text for header in headers]

    @staticmethod
    def get_table_data(table_row):
        """
        Get the table data for the supplied table row
        :param table_row: A row in the table to get data from
        :return: A list of table data strings
        """
        data = table_row.find_elements(
            *PatientPageLocators.table_data
        )
        return [entry.text for entry in data]

    @staticmethod
    def get_table_rows(table):
        """
        Get the table rows for the supplied table
        :param table: A table to get rows from
        :return: A list of table rows
        """
        rows = table.find_elements(
            *PatientPageLocators.table_row
        )
        return rows

    def get_obs_table(self):
        """
        Get observation table table
        :return: tabular values WebElement
        """
        return self.driver.find_element(
            *PatientPageLocators.table_container
        )

    @staticmethod
    def select_patient(patients):
        """
        Select a patient to observe
        :param patients: a list of patients
        """
        patient_to_test = patients[0]
        patient_to_test.click()

    def open_form(self, form_id):
        """
        Open an observation form
        :param form_id: The type of observation
        """
        self.open_adhoc_obs_menu()

        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(form_id)).click()

        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(TaskPageLocators.task_form)
        )

    def enter_obs_data(self, data):
        """
        Enter data into an observation form
        :param data: The data to be entered
        """
        new_dict = {}

        for field, value in data.iteritems():
            if self.driver.find_element_by_name(field).is_displayed():
                input_field = self.driver.find_element_by_name(field)
                input_field.send_keys(value)
                input_field.send_keys(Keys.TAB)
            else:
                new_dict[field] = value

        if new_dict:
            self.enter_obs_data(new_dict)
        else:
            self.driver.find_element(
                *TaskPageLocators.task_form_submit).click()
