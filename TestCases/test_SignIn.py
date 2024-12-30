import time
import pytest
from Pages.SignIn import SignIn
from TestCases.BaseTest import BaseTest
from pytest_check import check

mandatoryField_popup = "Mandatory fields are empty."
badEmailPassCombination = "Bad Email Password Combination."
wrongOtp = "Wrong OTP"
invalidMail = "Invalid email"
unregisteredMail = "The given email is Invalid"


class Test_SignIn(BaseTest):

    @pytest.fixture(autouse=True)
    def test_refreshBrowser(self):
        self.driver.refresh()

    def test_OtpBtnWithoutEmailPass(self):
        with check:
            HomePage = SignIn(self.driver)
            ele = HomePage.deleteCookies().clickOnSendOtpBtn()
            popup = ele.getTextFromAlertPopup()
            ele.loadCookies()
            assert popup == mandatoryField_popup  # Validated Mandatory OTP Popup

    def test_OtpBtnWithInvalidEmailValidPass(self):
        with check:
            HomePage = SignIn(self.driver)
            ele = HomePage.deleteCookies().enterInvalidEmailValidPass().clickOnSendOtpBtn()
            warnMsg = ele.getTextFromWarnMsg()
            ele.loadCookies()
            assert warnMsg == badEmailPassCombination  # Validated Bad Email Combination Warning Message

    def test_OtpBtnWithValidEmailInvalidPass(self):
        with check:
            HomePage = SignIn(self.driver)
            ele = HomePage.deleteCookies().enterValidEmailInvalidPass().clickOnSendOtpBtn()
            warnMsg = ele.getTextFromWarnMsg()
            ele.loadCookies()
            assert warnMsg == badEmailPassCombination  # Validated Bad Email Combination Warning Message

    def test_OtpBtnWithInvalidEmailInvalidPass(self):
        with check:
            HomePage = SignIn(self.driver)
            ele = HomePage.deleteCookies().enterInvalidEmailInvalidPass().clickOnSendOtpBtn()
            warnMsg = ele.getTextFromWarnMsg()
            ele.loadCookies()
            assert warnMsg == badEmailPassCombination  # Validated Bad Email Combination Warning Message

    def test_enabledResendOtpBtnAfter1Min(self):
        with check:
            HomePage = SignIn(self.driver)
            ele = HomePage.deleteCookies().enterValidEmailValidPass().clickOnSendOtpBtn()
            r1 = ele.verifyDisabledResendOtpBtn()
            assert r1 == "true"  # Validated Resend Button is disabled
        with check:
            time.sleep(60)
            r2 = ele.verifyDisabledResendOtpBtn()
            ele.loadCookies()
            assert r2 is None  # Validated Resend Button is enabled

    def test_wrongOtp(self):
        with check:
            HomePage = SignIn(self.driver)
            ele = HomePage.deleteCookies().enterValidEmailValidPass().clickOnSendOtpBtn().enterWrongOtp().clickOnLoginBtn()
            warnMsg = ele.getTextFromWrongOtpMsg()
            ele.loadCookies()
            assert warnMsg == wrongOtp  # Validated Wrong OTP Warning Message
        time.sleep(60)  # Added a 1-minute wait before proceeding to the next TC

    def test_notEditableEmailPassTextbox(self):
        with check:
            HomePage = SignIn(self.driver)
            ele = HomePage.deleteCookies().enterValidEmailValidPass().clickOnSendOtpBtn()
            assert ele.isPresentNonEditableUserNameTextbox()  # Validated Non Editable Email Textbox
        with check:
            assert ele.isPresentNonEditablePasswordTextbox()  # Validated Non Editable Password Textbox
        ele.loadCookies()
        time.sleep(60)  # Added a 1-minute wait before proceeding to the next TC

    def test_disabledResendOtpBtn(self):
        with check:
            HomePage = SignIn(self.driver)
            ele = HomePage.deleteCookies().enterValidEmailValidPass().clickOnSendOtpBtn()
            r1 = ele.verifyDisabledResendOtpBtn()
            ele.loadCookies()
            assert r1 == "true"  # Validated Resend Button is disabled

    def test_showPassword(self):
        with check:
            HomePage = SignIn(self.driver)
            ele = HomePage.deleteCookies()
            assert ele.verifyShowPassword() == "text"  # Validated Show Password Btn
        ele.loadCookies()

    def test_forgotPasswordForUnregisteredMail(self):
        with check:
            HomePage = SignIn(self.driver)
            ele = HomePage.deleteCookies().clickOnForgotPassword()
            assert ele.verifyForgotPass_unregisteredMail() == invalidMail  # Validated Invalid Mail Warning Message
        ele.loadCookies()

    def test_forgotPasswordForInvalidMail(self):
        with check:
            HomePage = SignIn(self.driver)
            ele = HomePage.deleteCookies().clickOnForgotPassword()
            assert ele.verifyForgotPass_InvalidMail() == invalidMail  # Validated Invalid Mail Warning Message
        ele.loadCookies()
