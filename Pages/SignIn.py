import json
import time

from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Utilities import configReader

validUserEmailId = "omkar.berde@ril.com"
validUserPassword = "Test@321"
invalidUserEmailId = "qwerty"
invalidUserPassword = "qwerty"
UserName = configReader.getConfigData("configuration", "UserName")
Password = configReader.getConfigData("configuration", "Password")


class SignIn(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    sendOtpBtn = (By.ID, "send_otp")
    alertPopup = (By.XPATH, "//h5[@id='warningModalLabel']//following-sibling::span")
    userName = (By.ID, "user_email")
    userPass = (By.ID, "user_password")
    badEmailPassCombination = (By.XPATH, "//span[@id='badEmail'][@style='display: inline;']")
    otpTextbox = (By.ID, "user_login_otp")
    loginBtn = (By.ID, "verify_otp")
    wrongOtp = (By.ID, "otpSent")
    nonEditableUserNameTextbox = (By.XPATH, "//input[@id='user_email'][@style='pointer-events: none;']")
    nonEditablePasswordTextbox = (By.XPATH, "//input[@id='user_password'][@style='pointer-events: none;']")
    showPassBtn = (By.ID, "eye-icon")
    forgotPassBtn = (By.CLASS_NAME, "forget-password")
    forgotPass_EmailTextbox = (By.ID, "email_address")
    submitBtn = (By.ID, "submit_button")
    invalidMailWarnMsg = (By.XPATH, "//span[@id='error'][@style='color: red;']")
    unregisteredMailWarnMsg = (By.XPATH, "//div[@id='error_msg']")

    def deleteCookies(self):
        time.sleep(1)
        self.wait_for_page_load()
        self.delete_all_cookies()
        self.refresh_page()
        self.refresh_page()
        self.wait_for_page_load()
        return SignIn(self.driver)

    def loadCookies(self):
        env = configReader.getConfigData("configuration", "Environment")
        if env == "prod":
            self.driver.get("https://devices.cms.jio.com/jiohotels/users/sign_in")
            self.driver.maximize_window()
            with open("JioHotels_cookies_prod.json", 'r') as file:
                cookies = json.load(file)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()
            self.driver.refresh()
        elif env == "pre-prod":
            self.driver.get("https://preprod-jiosignage.jio.com/v2/dashboard")
            self.driver.maximize_window()
            with open("JioSignAge_cookies_preprod.json", 'r') as file:
                cookies = json.load(file)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()
            self.driver.refresh()

    def clickOnSendOtpBtn(self):
        self.click(self.sendOtpBtn)
        return SignIn(self.driver)

    def clickOnLoginBtn(self):
        self.click(self.loginBtn)
        return SignIn(self.driver)

    def getTextFromAlertPopup(self):
        return self.get_element_text(self.alertPopup)

    def getTextFromWarnMsg(self):
        return self.get_element_text(self.badEmailPassCombination)

    def getTextFromWrongOtpMsg(self):
        return self.get_element_text(self.wrongOtp)

    def enterInvalidEmailValidPass(self):
        self.wait_for_page_load()
        self.send_keys(self.userName, f"{invalidUserEmailId}")
        self.send_keys(self.userPass, f"{validUserPassword}")
        return SignIn(self.driver)

    def enterValidEmailInvalidPass(self):
        self.wait_for_page_load()
        self.send_keys(self.userName, f"{validUserEmailId}")
        self.send_keys(self.userPass, f"{invalidUserPassword}")
        return SignIn(self.driver)

    def enterInvalidEmailInvalidPass(self):
        self.wait_for_page_load()
        self.send_keys(self.userName, f"{invalidUserEmailId}")
        self.send_keys(self.userPass, f"{invalidUserPassword}")
        return SignIn(self.driver)

    def enterValidEmailValidPass(self):
        self.wait_for_page_load()
        self.send_keys(self.userName, f"{UserName}")
        self.send_keys(self.userPass, f"{Password}")
        return SignIn(self.driver)

    def enterWrongOtp(self):
        self.wait_for_page_load()
        time.sleep(1)
        self.send_keys(self.otpTextbox, "123456")
        return SignIn(self.driver)

    def isPresentNonEditableUserNameTextbox(self):
        self.wait_for_page_load()
        return self.is_element_present(self.nonEditableUserNameTextbox)

    def isPresentNonEditablePasswordTextbox(self):
        self.wait_for_page_load()
        return self.is_element_present(self.nonEditablePasswordTextbox)

    def verifyDisabledResendOtpBtn(self):
        self.wait_for_page_load()
        time.sleep(3)
        return self.get_element_attribute(self.sendOtpBtn, "disabled")

    def verifyShowPassword(self):
        self.send_keys(self.userPass, f"{Password}")
        self.click(self.showPassBtn)
        return self.get_element_attribute(self.userPass, "type")

    def clickOnForgotPassword(self):
        self.wait_for_page_load()
        self.click(self.forgotPassBtn)
        return SignIn(self.driver)

    def verifyForgotPass_unregisteredMail(self):
        self.send_keys(self.forgotPass_EmailTextbox, "qwerty@gmail.com")
        self.click(self.submitBtn)
        l = self.return_elements_count(self.invalidMailWarnMsg)
        if l == 1:
            return self.get_element_text(self.invalidMailWarnMsg)
        else:
            return False

    def verifyForgotPass_InvalidMail(self):
        self.send_keys(self.forgotPass_EmailTextbox, "testingril.com")
        self.click(self.submitBtn)
        l = self.return_elements_count(self.invalidMailWarnMsg)
        if l == 1:
            return self.get_element_text(self.invalidMailWarnMsg)
        else:
            return False
