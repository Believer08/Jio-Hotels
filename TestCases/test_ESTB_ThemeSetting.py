import time
import pytest
from datetime import datetime
from Pages.ESTB_ThemeSetting import ESTB_ThemeSetting
from TestCases.BaseTest import BaseTest
from pytest_check import check

mandatoryField_popup = "Mandatory fields are empty."
badEmailPassCombination = "Bad Email Password Combination."
wrongOtp = "Wrong OTP"
invalidMail = "Invalid email"
unregisteredMail = "The given email is Invalid"
dataUpdatedMsg = "Data updated successfully"
invalidTxtColourMsg = "Invalid Text Color"
invalidBGColourMsg = "Invalid Background Color"
screenSaverDeleteMsg = "Screen deleted successfully"


class Test_ESTB_ThemeSetting(BaseTest):

    @pytest.fixture(autouse=True)
    def test_refreshBrowser(self):
        self.driver.refresh()

    def test_menuListOfESTB_ThemeSetting(self):
        with check:
            HomePage = ESTB_ThemeSetting(self.driver)
            optionsCount = HomePage.goToESTB_ThemeSetting().verifyMenuOptionsOnESTB_ThemeSettingPage()
            assert optionsCount == 5

    def test_enableNoEffectButton(self):
        with check:
            HomePage = ESTB_ThemeSetting(self.driver)
            assert HomePage.goToESTB_ThemeSetting().enableNoEffectBtn().getTextFromSuccessPopup() == dataUpdatedMsg
        with check:
            assert HomePage.verifyEnableNoEffectBtn()

    def test_disableNoEffectButton(self):
        with check:
            HomePage = ESTB_ThemeSetting(self.driver)
            assert HomePage.goToESTB_ThemeSetting().disableNoEffectBtn().getTextFromSuccessPopup() == dataUpdatedMsg
        with check:
            assert not HomePage.verifyEnableNoEffectBtn()

    def test_ValidColourCode(self):
        with check:
            HomePage = ESTB_ThemeSetting(self.driver)
            assert HomePage.goToESTB_ThemeSetting().goToBottomNavigation().enterValidColourCode().getTextFromSuccessPopup() == dataUpdatedMsg
        with check:
            assert HomePage.verifySavedTextColourCode()
        with check:
            assert HomePage.verifySavedBackgroundColourCode()

    def test_InvalidColourCode(self):
        with check:
            HomePage = ESTB_ThemeSetting(self.driver)
            assert HomePage.goToESTB_ThemeSetting().goToBottomNavigation().enterInvalidColourCode().getTextFromWarningPopup() == invalidTxtColourMsg

    def test_BlankColourCode(self):
        with check:
            HomePage = ESTB_ThemeSetting(self.driver)
            assert HomePage.goToESTB_ThemeSetting().goToBottomNavigation().dontEnterColourCode().getTextFromWarningPopup() == invalidTxtColourMsg

    def test_NotepadPositionEffect_ValidBGColour(self):
        with check:
            HomePage = ESTB_ThemeSetting(self.driver)
            assert HomePage.goToESTB_ThemeSetting().goToServiceNotepad().selectNotepadPositionEffectValidBGColour().getTextFromSuccessPopup() == dataUpdatedMsg
        with check:
            assert HomePage.verifySavedBackgroundColourCode_ForNotepad()

    def test_NotepadPositionEffect_InvalidBGColour(self):
        with check:
            HomePage = ESTB_ThemeSetting(self.driver)
            assert HomePage.goToESTB_ThemeSetting().goToServiceNotepad().selectNotepadPositionEffectInvalidBGColour().getTextFromWarningPopup() == invalidBGColourMsg

    def test_menuListOfWidget(self):
        with check:
            HomePage = ESTB_ThemeSetting(self.driver)
            assert HomePage.goToESTB_ThemeSetting().goToWidget().verifyMenuOptionsOnWidgetPage() == 4

    def test_chooseTempScale(self):
        with check:
            HomePage = ESTB_ThemeSetting(self.driver)
            ele = HomePage.goToESTB_ThemeSetting().goToWidget().chooseTempScale()
            assert ele.getTextFromSuccessPopup() == dataUpdatedMsg
        with check:
            assert ele.verifySelectedTempScale()

    def test_characterLimitForSuffix(self):
        with check:
            HomePage = ESTB_ThemeSetting(self.driver)
            assert HomePage.goToESTB_ThemeSetting().goToWidget().characterLimit() is None

    def test_screensaverEditDeleteBtn(self):
        with check:
            HomePage = ESTB_ThemeSetting(self.driver)
            assert HomePage.goToESTB_ThemeSetting().goToWidget().addScreenSaver().verifyEditDeleteOptions()
        HomePage.deleteCreatedScreensaver()

    def test_deleteScreensaver_Popup(self):
        with check:
            HomePage = ESTB_ThemeSetting(self.driver)
            assert HomePage.goToESTB_ThemeSetting().goToWidget().addScreenSaver().verifyDeleteScreensaver_popup()
        HomePage.deleteCreatedScreensaver()

    def test_deleteScreensaver_CancelBtn(self):
        with check:
            HomePage = ESTB_ThemeSetting(self.driver)
            assert HomePage.goToESTB_ThemeSetting().goToWidget().addScreenSaver().verifyDeleteScreensaver_CancelBtn()
        HomePage.deleteCreatedScreensaver()

    def test_deleteScreensaver(self):
        with check:
            HomePage = ESTB_ThemeSetting(self.driver)
            assert HomePage.goToESTB_ThemeSetting().goToWidget().addScreenSaver().deleteCreatedScreensaver().getTextFromSuccessPopup() == screenSaverDeleteMsg
        with check:
            assert HomePage.verifyDeleteScreensaver()

    def test_dateThemeSettingPage(self):
        with check:
            HomePage = ESTB_ThemeSetting(self.driver)
            actualDate = HomePage.goToESTB_ThemeSetting().dateOnThemeSettingsPage()
            today = datetime.now()
            expectedDate = today.strftime("%d %B, %Y")
            assert actualDate == expectedDate

    def test_backBtnThemeSettingPage(self):
        with check:
            HomePage = ESTB_ThemeSetting(self.driver)
            assert HomePage.goToESTB_ThemeSetting().verifyBackBtn()

    def test_manualStbMappingPage(self):
        with check:
            HomePage = ESTB_ThemeSetting(self.driver)
            assert HomePage.goToESTB_ThemeSetting().goToManualStbMapping().verifyMSM_Page_title()
        with check:
            assert HomePage.verifyMSM_pinTextbox()

    def test_manualStbMapping_setStbPin(self):
        with check:
            HomePage = ESTB_ThemeSetting(self.driver)
            HomePage.goToESTB_ThemeSetting().goToManualStbMapping().setStbPin()
            # sp = HomePage.getTextFromSuccessPopup()
            # assert sp == "Pin Updated Successfully"
        with check:
            assert HomePage.verifyChangedPin()

    def test_manualStbMapping_backBtn(self):
        with check:
            HomePage = ESTB_ThemeSetting(self.driver)
            assert HomePage.goToESTB_ThemeSetting().goToManualStbMapping().verifyBackBtn()

    def test_setPin_OnlyDigit_CharLength(self):
        with check:
            HomePage = ESTB_ThemeSetting(self.driver)
            assert HomePage.goToESTB_ThemeSetting().goToManualStbMapping().verifyOnlyDigit()
        with check:
            assert HomePage.verify_Min_MaxLength_stbPin()

    def test_manualStbMapping_showPassBtn(self):
        with check:
            HomePage = ESTB_ThemeSetting(self.driver)
            assert HomePage.goToESTB_ThemeSetting().goToManualStbMapping().verifyShowPassBtn()




