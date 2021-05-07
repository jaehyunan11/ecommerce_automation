import pytest
import time
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
# Package -> Module -> Class -> Method
from utilities.customLogger import LogGen


class Test_001_Login:
    # Config.ini -> Utilities -> Read common properties
    # If config info is change, please update in config.ini file
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("**************** Test_001_Login ****************")
        self.logger.info(
            "**************** Verifying Home Page Title ****************")
        self.driver = setup
        self.logger.info("**** Opening URL ****")
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            self.logger.info(
                "**************** Home page title test is passed ****************")
            self.driver.close()
            assert True

        else:
            # Fail test case
            self.logger.error(
                "**************** Home page title test is failed ****************")
            self.driver.save_screenshot(
                "./Screenshots/test_homePageTitle.png")
            self.driver.close()

            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info(
            "**************** Verifying Login Test ****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info(
                "**************** Login test is passed ****************")
            self.driver.close()
            assert True

        else:
            # Fail test case
            self.logger.error(
                "**************** Login test is failed ****************")
            self.driver.save_screenshot(
                "./Screenshots/test_login.png")
            self.driver.close()
            assert False
