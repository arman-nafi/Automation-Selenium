import allure
from seleniumbase import BaseCase
import pytest
import logging

logging.basicConfig(filename='test.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@allure.severity(allure.severity_level.NORMAL)
class AddNewAdmin(BaseCase):

    def login(self):
        self.open("https://pos.tmss-ict.com/admin/login")
        username = '//*[@id="username"]'
        password = "/html/body/div/div[2]/div[1]/form/div[3]/div/input"
        btnLogin = "/html/body/div/div[2]/div[1]/form/div[4]/button"
        self.type(username, "username")
        self.type(password, "password")
        self.click(btnLogin)

    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_user(self):
        self.login()

        # Locators
        clkadmin = '//*[@id="nav"]/li[3]/ul/li[1]/a'
        clkaddnew = '//*[@id="content"]/div/div[2]/div/div/div[1]/div/div[1]/span'
        setname = '//*[@id="validate-1"]/div[1]/div[1]/div/input'
        setuser = '//*[@id="validate-1"]/div[1]/div[2]/div/input'
        setemail = '//*[@id="validate-1"]/div[1]/div[3]/div/input'
        setpassword = '//*[@id="validate-1"]/div[1]/div[4]/div/input'
        clkactive = '//*[@id="validate-1"]/div[1]/div[5]/div/label[1]'
        clksubmit = '//*[@id="validate-1"]/div[2]/input'
        clkclose = '//*[@id="content"]/div/div[2]/div/div/div[1]/div/div[3]/div/div[2]/div/div[1]/button/span'
        errormsg = '//*[@id="validate-1"]/div[1]/div[1]/div[2]/span'

        self.click(clkadmin)
        assert self.is_element_visible(clkadmin), "Element 'clkadmin' is not visible"
        self.click(clkaddnew)
        assert self.is_element_visible(clkaddnew), "Element 'clkaddnew' is not visible"

        # Fill in the form fields
        self.type(setname, "Test User Name")
        self.type(setuser, "Test User")
        self.type(setemail, "test@gmail.com")
        self.type(setpassword, "password")
        self.click(clkactive)

        self.wait(2)

        # Submit the form
        self.click(clksubmit)

        # Check if user already exists
        if self.is_element_visible(errormsg):
            error_text = self.get_text(errormsg)
            if "The username has already been taken." in error_text:
                logging.info("User already exists")
            else:
                logging.error("Unknown error occurred")
        else:
            logging.info("User add successful")
