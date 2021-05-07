from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(
            '/Users/jaehyunan/Desktop/JH_Automation/chromedriver')
        print("Launching Chrome browser...........")
    elif browser == 'firefox':
        driver = webdriver.Firefox(
            '/Users/jaehyunan/Desktop/JH_Automation/geckodriver')
        print("Launching FireFox browser...........")
    driver.implicitly_wait(3)
    driver.maximize_window()
    return driver


def pytest_addoption(parser):  # This will getdthe value from hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


############ PYTEST HTML REPORT ##############
# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Pavan'


# It is hook for delete/Modify Enviroment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
