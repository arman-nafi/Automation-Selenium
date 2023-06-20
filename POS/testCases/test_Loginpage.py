import allure
from seleniumbase import BaseCase
import pytest
import random
import string
import logging

logging.basicConfig(filename='test.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

username = '//*[@id="username"]'
password = "/html/body/div/div[2]/div[1]/form/div[3]/div/input"
btnLogin = "/html/body/div/div[2]/div[1]/form/div[4]/button"
errormgs = '/html/body/div/div[2]/div[1]/div'

@pytest.mark.usefixtures()
class LoginTest(BaseCase):

    @allure.severity(allure.severity_level.MINOR)
    def test_home_page_title(self):
        self.open("https://pos.tmss-ict.com/admin/login")
        title = self.get_title()
        logging.info("Home Page Title: %s", title)
        self.assert_title("POS")
        self.save_screenshot("Homepage.png")
        with open("Homepage.png", "rb") as file:
            allure.attach(file.read(), name="Homepage", attachment_type=allure.attachment_type.PNG)

    @allure.severity(allure.severity_level.MINOR)
    def test_valid_username_password(self):
        self.open("https://pos.tmss-ict.com/admin/login")
        self.type(username, "username")
        self.type(password, "password")
        self.click(btnLogin)
        title = self.get_title()
        logging.info("Login Page Title: %s", title)
        self.assert_title("POS")
        self.save_screenshot("Loginpage.png")
        with open("Loginpage.png", "rb") as file:
            allure.attach(file.read(), name="Loginpage", attachment_type=allure.attachment_type.PNG)

    @allure.severity(allure.severity_level.CRITICAL)
    def test_invalid_username(self):
        self.open("https://pos.tmss-ict.com/admin/login")
        random_name = ''.join(random.choices(string.ascii_letters, k=10))
        self.type(username, random_name)
        self.type(password, "password")
        self.click(btnLogin)
        if self.is_element_visible(errormgs):
            error_text = self.get_text(errormgs)
            if "Invalid username and password" in error_text:
                logging.info("Invalid username test passed")
            else:
                logging.error("Unknown error occurred")
        else:
            logging.error("Login successful test failed")

    @allure.severity(allure.severity_level.CRITICAL)
    def test_invalid_password(self):
        self.open("https://pos.tmss-ict.com/admin/login")
        random_password = ''.join(random.choices(string.ascii_letters, k=10))
        self.type(username, "username")
        self.type(password, random_password)
        self.click(btnLogin)
        if self.is_element_visible(errormgs):
            error_text = self.get_text(errormgs)
            if "Invalid username and password" in error_text:
                logging.info("Invalid Password test passed")
            else:
                logging.error("Unknown error occurred")
        else:
            logging.error("Login successful test failed")
