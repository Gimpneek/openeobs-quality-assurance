from openeobs_selenium.page_helpers import BasePage, LoginPageLocators


class LoginPage(BasePage):
    """
    Login Page methods and helps etc
    """

    def login(self, username, password):
        """
        Fill out the login form and press the submit button
        :param username: Username to login with
        :param password: Password for the username supplied
        """
        username_el = self.driver.find_element(*LoginPageLocators.username_el)
        password_el = self.driver.find_element(*LoginPageLocators.password_el)
        login_button = self.driver.find_element(
            *LoginPageLocators.login_button_el
        )
        username_el.send_keys(username)
        password_el.send_keys(password)
        login_button.click()

    def has_logged_in(self):
        """
        Check that the current page is the task list (which is the screen seen
        on logging in
        :return: Boolean of if on the task list
        """
        return '/mobile/tasks/' in self.driver.current_url

    def shows_login_error(self):
        """
        Check that the login page shows an error message
        :return: Boolean of if the error message is shown
        """
        error_el = self.driver.find_element(*LoginPageLocators.error_el)
        return error_el.text == 'Invalid username/password'

