import json
import random
import secrets
import time

from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Utilities import configReader

UserName = configReader.getConfigData("configuration", "UserName")
Password = configReader.getConfigData("configuration", "Password")


class ESTB_ThemeSetting(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    chooseHotel = (By.ID, "open_Model")
    subProperty1st = (By.XPATH, "(//p[normalize-space()='Sub Property'])[1]")
    settingIcon = (By.XPATH, "//img[@alt='Setting']")
    layoutStyle = (By.XPATH, "//a[normalize-space()='Layout Style']")
    bottomNavigation = (By.XPATH, "//a[normalize-space()='Bottom Navigation']")
    serviceNotepad = (By.XPATH, "//a[normalize-space()='Service Notepad']")
    widget = (By.XPATH, "//a[normalize-space()='Widget']")
    msm = (By.XPATH, "//a[normalize-space()='Manual STB Setting']")
    tv = (By.XPATH, "//a[normalize-space()='TV']")
    noEffectBtn = (By.CSS_SELECTOR, "#flexSwitchCheckDefault")
    layoutStyle_SaveBtn = (By.CSS_SELECTOR, "div[class='theme-main1'] button:nth-child(1)")
    bottomNavigation_SaveBtn = (By.CSS_SELECTOR, "#bottom_bar")
    serviceNotepad_SaveBtn = (By.CSS_SELECTOR, ".btn.btn-save-stb.service_notepad")
    weather_SaveBtn = (By.CSS_SELECTOR, "#weather")
    successImg = (By.XPATH, "//img[@alt='Success']")
    warningImg = (By.XPATH, "//img[@alt='Warning']")
    successPopupMsg = (By.CSS_SELECTOR, "#noticeContent")
    warningPopupMsg = (By.CSS_SELECTOR, "#alertContent")
    textColourTextbox = (By.CSS_SELECTOR, "input[class$='text_color']")
    backgroundColourTextbox = (By.CSS_SELECTOR, "input[class$='background_color']")
    textColour = (By.CSS_SELECTOR, "input[name='text_color']")
    backgroundColour = (By.CSS_SELECTOR, "input[name='background_color']")
    notepadPositionDD = (By.CSS_SELECTOR, "select[name='position']")
    notepadPositionDD_Top = (By.CSS_SELECTOR, "option[value='top']")
    notepadPositionDD_Bottom = (By.CSS_SELECTOR, "option[value='bottom']")
    notepadEffectDD = (By.XPATH, "//select[@name='notepad_effect']")
    notepadEffectDD_linear = (By.CSS_SELECTOR, "option[value='linear']")
    notepadEffectDD_Circular = (By.CSS_SELECTOR, "option[value='Circular']")
    widget_welcomeNote = (By.CSS_SELECTOR, "#nav-welcome-tab")
    widget_date_Time = (By.CSS_SELECTOR, "#nav-date-tab")
    widget_weather = (By.CSS_SELECTOR, "#nav-weather-tab")
    widget_screenSaver = (By.CSS_SELECTOR, "#nav-screensaver-tab")
    radio_weather_centigrade = (By.CSS_SELECTOR, 'input[value="Centigrade"]')
    radio_weather_fahrenheit = (By.CSS_SELECTOR, 'input[value="Fahrenheite"]')
    radio_suffix_other = (By.CSS_SELECTOR, " #chkdisplay")
    textBox_suffix_other = (By.CSS_SELECTOR, "#user_suffix_title")
    plusIconAddScreensaver = (By.CSS_SELECTOR, ".imgeprop")
    screenSaverNameTextbox = (By.CSS_SELECTOR, "input[class='screen_name_add']")
    screensaverSaveBtn = (By.CSS_SELECTOR, "#save_app")
    popup_deleteBtn = (By.CSS_SELECTOR, "#delete_id")
    popup_cancelBtn = (By.XPATH, "//button[@class='btn btn-modal-solid'][normalize-space()='Cancel']")
    delete_popup = (By.XPATH, "//h2[contains(.,'Delete Screensaver')]")
    dateThemeSettingPage = (By.CSS_SELECTOR, ".dateicon")
    backBtnThemeSettingPage = (By.CSS_SELECTOR, "img[alt='back']")
    dashboardTitle = (By.CSS_SELECTOR, ".page-title.dashboard-page-heading")
    msm_title = (By.CSS_SELECTOR, ".page-title")
    msm_pinTextbox = (By.CSS_SELECTOR, "#property_password")
    msm_updateBtn = (By.CSS_SELECTOR, "#password_update")
    msm_pinSettingWarnMsg = (By.CSS_SELECTOR, "#property_setting_pin")
    msm_showPassIcon = (By.CSS_SELECTOR, "#eye-icon")

    def getTextFromSuccessPopup(self):
        ele = self.return_elements_count(self.successImg)
        if ele == 1:
            return self.get_element_text(self.successPopupMsg)
        else:
            return False

    def getTextFromWarningPopup(self):
        ele = self.return_elements_count(self.warningImg)
        if ele == 1:
            return self.get_element_text(self.warningPopupMsg)
        else:
            return False

    def goToESTB_ThemeSetting(self):
        self.click(self.chooseHotel)
        self.click(self.subProperty1st)
        self.click(self.settingIcon)
        return ESTB_ThemeSetting(self.driver)

    def verifyMenuOptionsOnESTB_ThemeSettingPage(self):
        ele1 = len(self.find_elements(self.layoutStyle))
        ele2 = len(self.find_elements(self.bottomNavigation))
        ele3 = len(self.find_elements(self.serviceNotepad))
        ele4 = len(self.find_elements(self.widget))
        ele5 = len(self.find_elements(self.tv))
        return ele1 + ele2 + ele3 + ele4 + ele5

    def enableNoEffectBtn(self):
        ele = self.find_element(self.noEffectBtn).is_selected()
        if ele:
            self.click(self.noEffectBtn)
            self.wait_for_page_load()
            self.scroll_to_bottom()
            # self.scroll_to_element(self.layoutStyle_SaveBtn)
            self.click(self.layoutStyle_SaveBtn)
            self.click(self.noEffectBtn)
            self.wait_for_page_load()
            self.scroll_to_bottom()
            # self.scroll_to_element(self.layoutStyle_SaveBtn)
            self.click(self.layoutStyle_SaveBtn)
        else:
            self.click(self.noEffectBtn)
            self.wait_for_page_load()
            self.scroll_to_bottom()
            # self.scroll_to_element(self.layoutStyle_SaveBtn)
            self.click(self.layoutStyle_SaveBtn)
        return ESTB_ThemeSetting(self.driver)

    def disableNoEffectBtn(self):
        ele = self.find_element(self.noEffectBtn).is_selected()
        if not ele:
            self.click(self.noEffectBtn)
            self.wait_for_page_load()
            self.scroll_to_bottom()
            # self.scroll_to_element(self.layoutStyle_SaveBtn)
            self.click(self.layoutStyle_SaveBtn)
            self.click(self.noEffectBtn)
            self.wait_for_page_load()
            self.scroll_to_bottom()
            # self.scroll_to_element(self.layoutStyle_SaveBtn)
            self.click(self.layoutStyle_SaveBtn)
        else:
            self.click(self.noEffectBtn)
            self.wait_for_page_load()
            self.scroll_to_bottom()
            # self.scroll_to_element(self.layoutStyle_SaveBtn)
            self.click(self.layoutStyle_SaveBtn)
        return ESTB_ThemeSetting(self.driver)

    def goToBottomNavigation(self):
        self.click(self.bottomNavigation)
        return ESTB_ThemeSetting(self.driver)

    def goToServiceNotepad(self):
        self.click(self.serviceNotepad)
        return ESTB_ThemeSetting(self.driver)

    def goToWidget(self):
        self.click(self.widget)
        return ESTB_ThemeSetting(self.driver)

    def goToManualStbMapping(self):
        self.click(self.msm)
        return ESTB_ThemeSetting(self.driver)

    def verifyEnableNoEffectBtn(self):
        self.refresh_page()
        return self.find_element(self.noEffectBtn).is_selected()

    def enterValidColourCode(self):
        self.find_element(self.textColourTextbox).clear()
        self.find_element(self.backgroundColourTextbox).clear()
        colors = ['#FF5733', '#33FF57', '#3357FF', '#F1C40F', '#8E44AD']
        global selected_color
        selected_color = random.choice(colors)
        self.send_keys(self.textColourTextbox, f"{selected_color}")
        self.send_keys(self.backgroundColourTextbox, f"{selected_color}")
        self.click(self.bottomNavigation_SaveBtn)
        return ESTB_ThemeSetting(self.driver)

    def enterInvalidColourCode(self):
        self.find_element(self.textColourTextbox).clear()
        self.find_element(self.backgroundColourTextbox).clear()
        self.send_keys(self.textColourTextbox, "qqqqq")
        self.send_keys(self.backgroundColourTextbox, "qqqqq")
        self.click(self.bottomNavigation_SaveBtn)
        return ESTB_ThemeSetting(self.driver)

    def dontEnterColourCode(self):
        self.find_element(self.textColourTextbox).clear()
        self.find_element(self.backgroundColourTextbox).clear()
        self.click(self.bottomNavigation_SaveBtn)
        return ESTB_ThemeSetting(self.driver)

    def verifySavedTextColourCode(self):
        self.refresh_page()
        colour_code_textColour = self.get_element_attribute(self.textColour, "value")
        if colour_code_textColour.upper() == selected_color:
            return True
        else:
            return False

    def verifySavedBackgroundColourCode(self):
        self.refresh_page()
        colour_code_backGroundColour = self.get_element_attribute(self.backgroundColour, "value")
        if colour_code_backGroundColour.upper() == selected_color:
            return True
        else:
            return False

    def selectNotepadPositionEffectValidBGColour(self):
        top = self.find_element(self.notepadPositionDD_Top).is_selected()
        if top:
            self.select_dropdown_by_visible_text(self.notepadPositionDD, "Bottom")
        else:
            self.select_dropdown_by_visible_text(self.notepadPositionDD, "Top")
        linear = self.find_element(self.notepadEffectDD_linear).is_selected()
        if linear:
            self.select_dropdown_by_value(self.notepadEffectDD, "Circular")
        else:
            self.select_dropdown_by_value(self.notepadEffectDD, "linear")
        colors = ['#FF5733', '#33FF57', '#3357FF', '#F1C40F', '#8E44AD']
        global notepad_selected_color
        notepad_selected_color = random.choice(colors)
        self.find_element(self.backgroundColourTextbox).clear()
        self.send_keys(self.backgroundColourTextbox, f"{notepad_selected_color}")
        self.click(self.serviceNotepad_SaveBtn)
        return ESTB_ThemeSetting(self.driver)

    def selectNotepadPositionEffectInvalidBGColour(self):
        top = self.find_element(self.notepadPositionDD_Top).is_selected()
        if top:
            self.select_dropdown_by_visible_text(self.notepadPositionDD, "Bottom")
        else:
            self.select_dropdown_by_visible_text(self.notepadPositionDD, "Top")
        linear = self.find_element(self.notepadEffectDD_linear).is_selected()
        if linear:
            self.select_dropdown_by_value(self.notepadEffectDD, "Circular")
        else:
            self.select_dropdown_by_value(self.notepadEffectDD, "linear")
        self.find_element(self.backgroundColourTextbox).clear()
        self.send_keys(self.backgroundColourTextbox, "qqqqq")
        self.click(self.serviceNotepad_SaveBtn)
        return ESTB_ThemeSetting(self.driver)

    def verifySavedBackgroundColourCode_ForNotepad(self):
        self.refresh_page()
        colour_code_backGroundColour = self.get_element_attribute(self.backgroundColour, "value")
        if colour_code_backGroundColour.upper() == notepad_selected_color:
            return True
        else:
            return False

    def verifyMenuOptionsOnWidgetPage(self):
        ele1 = len(self.find_elements(self.widget_welcomeNote))
        ele2 = len(self.find_elements(self.widget_date_Time))
        ele3 = len(self.find_elements(self.widget_weather))
        ele4 = len(self.find_elements(self.widget_screenSaver))
        return ele1 + ele2 + ele3 + ele4

    def chooseTempScale(self):
        global weatherScale
        self.click(self.widget_weather)
        c = self.find_element(self.radio_weather_centigrade).is_selected()
        if c:
            self.click(self.radio_weather_fahrenheit)
            self.wait_for_page_load()
            self.scroll_to_bottom()
            # self.scroll_to_element(self.weather_SaveBtn)
            self.click(self.weather_SaveBtn)
            weatherScale = "Fahrenheit"
        else:
            self.click(self.radio_weather_centigrade)
            self.wait_for_page_load()
            self.scroll_to_bottom()
            # self.scroll_to_element(self.weather_SaveBtn)
            self.click(self.weather_SaveBtn)
            weatherScale = "Centigrade"
        return ESTB_ThemeSetting(self.driver)

    def verifySelectedTempScale(self):
        self.refresh_page()
        if weatherScale == "Centigrade":
            return self.find_element(self.radio_weather_centigrade).is_selected()
        else:
            return self.find_element(self.radio_weather_fahrenheit).is_selected()

    def characterLimit(self):
        self.click(self.widget_welcomeNote)
        self.wait_for_page_load()
        self.scroll_to_bottom()
        self.click(self.radio_suffix_other)
        return self.get_element_attribute(self.textBox_suffix_other, "maxlength")

    def enterScreensaverName(self):
        global r_ScreensaverName
        r_ScreensaverName = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(5))
        self.send_keys(self.screenSaverNameTextbox, f"{r_ScreensaverName}")
        return ESTB_ThemeSetting(self.driver)

    def addScreenSaver(self):
        self.click(self.widget_screenSaver)
        self.click(self.plusIconAddScreensaver)
        self.enterScreensaverName()
        self.scroll_to_bottom()
        # self.scroll_to_element(self.screensaverSaveBtn)
        self.click(self.screensaverSaveBtn)
        time.sleep(2)
        return ESTB_ThemeSetting(self.driver)

    def verifyEditDeleteOptions(self):
        self.refresh_page()
        self.click((By.CSS_SELECTOR, f"div[title='{r_ScreensaverName}'] ~ div img"))
        edit = len(self.driver.find_elements(By.XPATH,
                                             f"//div[@title='{r_ScreensaverName}']//parent::div//following-sibling::div//div//div[text()='Edit']"))
        delete = len(self.driver.find_elements(By.XPATH,
                                               f"//div[@title='{r_ScreensaverName}']//parent::div//following-sibling::div//div//div[text()='Delete']"))
        r = edit + delete
        if r == 2:
            return True
        else:
            return False

    def deleteCreatedScreensaver(self):
        self.refresh_page()
        self.click((By.CSS_SELECTOR, f"div[title='{r_ScreensaverName}'] ~ div img"))
        self.click((By.XPATH, f"//div[@title='{r_ScreensaverName}']//parent::div//following-sibling::div//div//div[text()='Delete']"))
        self.click(self.popup_deleteBtn)
        return ESTB_ThemeSetting(self.driver)

    def verifyDeleteScreensaver(self):
        self.refresh_page()
        r = self.return_elements_count((By.CSS_SELECTOR, f"div[title='{r_ScreensaverName}'] ~ div img"))
        if r == 0:
            return True
        else:
            return False

    def verifyDeleteScreensaver_CancelBtn(self):
        self.refresh_page()
        self.click((By.CSS_SELECTOR, f"div[title='{r_ScreensaverName}'] ~ div img"))
        self.click((By.XPATH, f"//div[@title='{r_ScreensaverName}']//parent::div//following-sibling::div//div//div[text()='Delete']"))
        self.click(self.popup_cancelBtn)
        r = self.return_elements_count((By.CSS_SELECTOR, f"div[title='{r_ScreensaverName}'] ~ div img"))
        if r == 1:
            return True
        else:
            return False

    def verifyDeleteScreensaver_popup(self):
        self.refresh_page()
        self.click((By.CSS_SELECTOR, f"div[title='{r_ScreensaverName}'] ~ div img"))
        self.click((By.XPATH, f"//div[@title='{r_ScreensaverName}']//parent::div//following-sibling::div//div//div[text()='Delete']"))
        return self.is_element_visible(self.delete_popup)

    def dateOnThemeSettingsPage(self):
        return self.get_element_text(self.dateThemeSettingPage)

    def verifyBackBtn(self):
        self.click(self.backBtnThemeSettingPage)
        r = self.return_elements_count(self.dashboardTitle)
        if r == 1:
            return True
        else:
            return False

    def verifyMSM_Page_title(self):
        title = self.get_element_text(self.msm_title)
        if title in " STB Setting Pin":
            return True
        else:
            return False

    def verifyMSM_pinTextbox(self):
        tb = self.return_elements_count(self.msm_pinTextbox)
        if tb == 1:
            return True
        else:
            return False

    def setStbPin(self):
        global r_StbPin
        self.find_element(self.msm_pinTextbox).clear()
        r_StbPin = ''.join(
            secrets.choice('1234567890') for _ in range(4))
        self.send_keys(self.msm_pinTextbox, f"{r_StbPin}")
        self.click(self.msm_updateBtn)
        return ESTB_ThemeSetting(self.driver)

    def verifyChangedPin(self):
        actual_pin = self.find_element(self.msm_pinTextbox).get_attribute('value')
        if actual_pin == r_StbPin:
            return True
        else:
            return False

    def verifyOnlyDigit(self):
        self.find_element(self.msm_pinTextbox).clear()
        self.send_keys(self.msm_pinTextbox, "@ab#")
        warn_msg = self.get_element_text(self.msm_pinSettingWarnMsg)
        if warn_msg in "Please enter only digits":
            return True
        else:
            return False

    def verify_Min_MaxLength_stbPin(self):
        maxLength = self.get_element_attribute(self.msm_pinTextbox, "maxlength")
        minLength = self.get_element_attribute(self.msm_pinTextbox, "minlength")
        if maxLength == minLength == "4":
            return True
        else:
            return False

    def verifyShowPassBtn(self):
        default_tb = self.get_element_attribute(self.msm_pinTextbox, "type")
        if default_tb == "password":
            self.click(self.msm_showPassIcon)
            tb = self.get_element_attribute(self.msm_pinTextbox, "type")
            if tb == "text":
                return True
            else:
                return False
        else:
            return False
