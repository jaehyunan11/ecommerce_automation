import pytest
import time
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
# Package -> Module -> Class -> Method
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test_002_DDT_Login:
    # Config.ini -> Utilities -> Read common properties
    # If config info is change, please update in config.ini file
    baseURL = ReadConfig.getApplicationURL()
    path = "./TestData/LoginData.xlsx"
    # username = ReadConfig.getUseremail()
    # password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info(
            "**************** Test_002_DDT_Login ****************")
        self.logger.info(
            "**************** Verifying Login DDT test ****************")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        # Get the data from excel file

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of Rows i a Excel:", self.rows)

        lst_status = []  # empty list variable
        for r in range(2, self.rows+1):
            self.user = XLUtils.readData(self.path, "Sheet1", r, 1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.exp = XLUtils.readData(self.path, "Sheet1", r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("*** Passed ***")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("*** Failed ***")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("*** Failed ***")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("*** Passed ***")
                    lst_status.append("Pass")
        if "Fail" not in lst_status:
            self.logger.info("**** Login DDT Test passed.....^__^ **** ")
            self.driver.close()
            assert True
        else:
            self.logger.info("**** Login DDT Test Failed **** .....")
            self.driver.close()
            assert False
        print(lst_status)
        self.logger.info("******** End of Login DDT Test *********")
        self.logger.info("******** Completed TC_LoginDDT_002 *********")
