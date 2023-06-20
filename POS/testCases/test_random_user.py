import allure
from seleniumbase import BaseCase
import pytest
import random
import string

class AddNewAdminRandom(BaseCase):

    def login(self):

        self.open("https://pos.tmss-ict.com/admin/login")
        username = '//*[@id="username"]'
        password = "/html/body/div/div[2]/div[1]/form/div[3]/div/input"
        btnLogin = "/html/body/div/div[2]/div[1]/form/div[4]/button"
        self.type(username, "username")
        self.type(password, "password")
        self.click(btnLogin)

    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_user_random(self):

        self.login()

        # Locators

        clkadmin = '//*[@id="nav"]/li[3]/ul/li[1]/a'
        clkaddnew = '//*[@id="content"]/div/div[2]/div/div/div[1]/div/div[1]/span'
        setname = '//*[@id="validate-1"]/div[1]/div[1]/div/input'
        setuser = '//*[@id="validate-1"]/div[1]/div[2]/div/input'
        setemail = '//*[@id="validate-1"]/div[1]/div[3]/div/input'
        setpassword = '//*[@id="validate-1"]/div[1]/div[4]/div/input'
        #clkinactive = '//*[@id="validate-1"]/div[1]/div[5]/div/label[2]'
        clkactive = '//*[@id="validate-1"]/div[1]/div[5]/div/label[1]'
        clksubmit = '//*[@id="validate-1"]/div[2]/input'
        clkclose = '//*[@id="content"]/div/div[2]/div/div/div[1]/div/div[3]/div/div[2]/div/div[1]/button/span'
        errormsg = '//*[@id="validate-1"]/div[1]/div[1]/div[2]/span'

        self.click(clkadmin)
        assert self.is_element_visible(clkadmin), "Element 'clkadmin' is not visible"
        self.click(clkaddnew)
        assert self.is_element_visible(clkaddnew), "Element 'clkaddnew' is not visible"

        # Generate random values
        random_name = ''.join(random.choices(string.ascii_letters, k=10))
        random_username = ''.join(random.choices(string.ascii_lowercase, k=8))
        random_email = ''.join(random.choices(string.ascii_lowercase, k=8)) + "@gmail.com"
        random_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

        # Fill in the form fields with random values
        self.type(setname, random_name)
        self.type(setuser, random_username)
        self.type(setemail, random_email)
        self.type(setpassword, random_password)
        self.click(clkactive)

        # Submit the form
        self.click(clksubmit)

        # Check if user already exists
        if self.is_element_visible(errormsg):
            error_text = self.get_text(errormsg)
            if "User already exists" in error_text:
                print("User already exists")
            else:
                print("Unknown error occurred")
        else:
            print("User add successful")



