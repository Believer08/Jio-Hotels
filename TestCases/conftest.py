import json
import pytest
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from Utilities import configReader
from selenium import webdriver


driver = None


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser")
    if browser_name == "chrome":
        # service = Service(r'..\\Utilities\\chromedriver.exe')
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "IE":
        driver = webdriver.Ie()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    # service = Service(r'..\\utils\\chromedriver.exe')
    # options = webdriver.ChromeOptions()
    # options.add_argument("--disable-popup-blocking")
    # options.add_argument("--disable-web-security")
    # driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    env = configReader.getConfigData("configuration", "Environment")
    if env == "prod":
        driver.get("https://devices.cms.jio.com/jiohotels/users/sign_in")
        driver.maximize_window()
        with open("JioHotels_cookies_prod.json", 'r') as file:
            cookies = json.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.refresh()
        driver.refresh()
        request.cls.driver = driver
        yield driver
        driver.close()
    elif env == "pre-prod":
        driver.get("https://preprod.devices.cms.jio.com/jiohotels/users/sign_in")
        driver.maximize_window()
        with open("JioHotels_cookies_preprod.json", 'r') as file:
            cookies = json.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.refresh()
        driver.refresh()
        request.cls.driver = driver
        yield driver
        driver.close()


@pytest.fixture()
def log_on_failure(request, setup):
    yield
    item = request.node
    driver = setup
    value = None
    if item.rep_call.failed:
        value = "Fail"
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
        # log.logger.info("{} : ".format(item.name) + value)
    elif item.rep_call.passed:
        value = "Pass"
        # log.logger.info("Testcase {} Passed.".format(item.name))
        # log.logger.info("{} : ".format(item.name) + value)
        pass
    elif item.rep_call.broken:
        # value = "Broken"
        # log.logger.info("Testcase {} Broken.".format(item.name))
        # log.logger.info("{} : ".format(item.name) + value)
        pass