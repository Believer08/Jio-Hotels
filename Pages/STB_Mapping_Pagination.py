import json
import os
import random
import secrets
import time
import autoit
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Utilities import configReader

UserName = configReader.getConfigData("configuration", "UserName")
Password = configReader.getConfigData("configuration", "Password")


def is_ascending(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True


def is_descending(lst):
    for i in range(len(lst) - 1):
        if lst[i] < lst[i + 1]:
            return False
    return True


class STB_Mapping_Pagination(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    successImg = (By.XPATH, "(//img[@alt='Success'])[1]")
    warningImg = (By.XPATH, "(//img[@alt='Warning'])[1]")
    successPopupMsg = (By.CSS_SELECTOR, "#noticeContent")
    warningPopupMsg = (By.CSS_SELECTOR, "#alertContent")
    chooseHotel = (By.ID, "open_Model")
    subProperty1st = (By.XPATH, "(//p[normalize-space()='Sub Property'])[1]")
    stbMapping = (By.CSS_SELECTOR, ".dashboard-nav-item[href='/jiohotels/stbs']")
    stbMappingTitle = (By.CSS_SELECTOR, "a[data-toggle='collapse'][data-parent='#accordion']")
    stbMappingTable = (
        By.CSS_SELECTOR, "div[class='card stb-data-card'] div div[class='table-responsive stb-table-responsive']")
    chooseFile = (By.CSS_SELECTOR, "label[for='file']")
    uploadFileBtn = (By.CSS_SELECTOR, "#upload_anchor")
    automationGrpTabBtn = (By.XPATH, "//button[.=' Automation ']")
    stb_count = (By.CSS_SELECTOR, "#room_count")
    selectAllCheckBox = (By.CSS_SELECTOR, "#head_checkbox")
    deleteBtn = (By.CSS_SELECTOR, "#bulk_delete")
    deletePopupBtn = (By.CSS_SELECTOR, "#bulk_delete1")
    rejectedCount = (By.XPATH, "//div[@id='rejectedListModal']//p[2]")
    createdCount = (By.XPATH, "//div[@id='rejectedListModal']//p[1]")
    cancelBtn = (By.XPATH, "//button[@class='btn btn-reset-stb']")
    roomNumTextbox = (By.CSS_SELECTOR, "input[placeholder='Room No']")
    serialNumTextbox = (By.CSS_SELECTOR, "input[placeholder='STB Serial No.']")
    addBtn = (By.CSS_SELECTOR, "#add-mapping")
    saveBtn = (By.CSS_SELECTOR, "#save_stb")
    resetBtn = (By.CSS_SELECTOR, "button[class='btn btn-reset-stb ']")
    addMoreBtn = (By.CSS_SELECTOR, "#addMoreRooms")
    addRoomsPopup = (By.XPATH, '//div[@class="modal fade show"][@id="addRoomsModal"]')
    manageGrp = (By.CSS_SELECTOR, "#manage-mapping")
    addGrp = (By.CSS_SELECTOR, "img[alt='Add Group']")
    grpNameTextbox = (By.CSS_SELECTOR, "#group_name")
    saveGrp = (By.CSS_SELECTOR, "#save_group")
    deleteGrpPopup = (By.CSS_SELECTOR, "#delete_id")
    deleteStbPopup = (By.CSS_SELECTOR, "#delete_single_stb")
    selectGrp = (By.CSS_SELECTOR, "#groupSelect")
    mainProperty1st = (By.XPATH, "(//p[normalize-space()='Main Property'])[1]")
    subPropertyList = (By.XPATH, "//a[normalize-space()='Sub Property List']")
    addProperty = (By.CSS_SELECTOR, "img[alt='Add Property']")
    propertyNameTextBox = (By.CSS_SELECTOR, "#property_name")
    propertyLocationTB = (By.CSS_SELECTOR, "#property_location")
    propertyCodeTB = (By.CSS_SELECTOR, "#property_code")
    propertyTypeTB = (By.CSS_SELECTOR, "#property_type")
    encaptoDeviceIdTB = (By.CSS_SELECTOR, "#encapto_device_id")
    encaptoAuthIdTB = (By.CSS_SELECTOR, "#encapto_auth_id")
    latitude = (By.CSS_SELECTOR, "#lattitude")
    longitude = (By.CSS_SELECTOR, "#longitude")
    addSubPropertyBtn = (By.CSS_SELECTOR, "#add_sub_property")
    deleteSubPropertyBtn = (By.CSS_SELECTOR, "#delete_sub_property")
    updateBtnPopup = (By.XPATH, "(//button[@id='edit_update_button'])[1]")
    popup = (By.XPATH, "//div[@class='modal fade show']")
    editRoomNameTB = (By.CSS_SELECTOR, "#stb_edit_room")
    editSerialNumTB = (By.CSS_SELECTOR, "#stb_edit_serial")
    roomNumCol = (By.XPATH, "//th[.='Room Number']")
    serialNumCol = (By.XPATH, "//th[.='Serial Number']")
    downloadRecordBtn = (By.CSS_SELECTOR, "a[id='download_report'] b")
    downloadPopupBtn = (By.CSS_SELECTOR, "#r1")
    clearDataBtn = (By.CSS_SELECTOR, "#clear_cache")
    cancelBtn_bulkUpload = (By.XPATH, "//button[@class='btn btn-reset-stb']")
    downloadRejectedBtn = (By.CSS_SELECTOR, "#rejected_stb")
    X_btn = (By.CSS_SELECTOR, "div[id='rejectedListModal'] button[aria-label='Close']")
    numOfRows = (By.XPATH, "//td[@class='sorting_1']")
    nextPage = (By.XPATH, "(//a[@rel='next'])[2]")
    previousPage = (By.XPATH, "(//a[@rel='prev'])[1]")
    page1 = (By.XPATH, "//span[.='1']")
    page2 = (By.XPATH, "//span[.='2']")
    automationGrpName = (By.XPATH, "//td[.='Automation']")
    downloadRecordsPopup = (By.XPATH, "//div[@class='modal fade show'][@id='download_report_modal']")
    checkBoxes = (By.XPATH, "//input[@type='checkbox'][@class='stbreport']")
    checkBox_All = (By.CSS_SELECTOR, "#All")
    resetBtn_DownloadRecords = (By.XPATH, "//span[.='Reset']")
    searchBar = (By.XPATH, "//input[@id='global_stb_search']")
    editRoomNum = (By.CSS_SELECTOR, "#stb_edit_room")
    X_Btn_downLoadRecords = (By.CSS_SELECTOR, "div[id='download_report_modal'] button[aria-label='Close']")

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

    def goToSTB_Mapping(self):
        self.click(self.chooseHotel)
        self.click(self.subProperty1st)
        self.click(self.stbMapping)
        self.wait_for_page_load()
        return STB_Mapping_Pagination(self.driver)

    def goToSTB_SubPropertyList(self):
        self.click(self.chooseHotel)
        self.click(self.mainProperty1st)
        self.click(self.subPropertyList)
        self.wait_for_page_load()
        return STB_Mapping_Pagination(self.driver)

    def verifySTB_MappingPageTitle(self):
        return self.find_element(self.stbMappingTitle).is_displayed()

    def verifySTB_MappingPageTable(self):
        return self.find_element(self.stbMappingTable).is_displayed()

    def bulkUpload_5Devices(self):
        self.click(self.chooseFile)
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\bulk_upload_5_STB.csv'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(3)
        self.click(self.uploadFileBtn)
        return STB_Mapping_Pagination(self.driver)

    def bulkUpload_25Devices(self):
        self.click(self.chooseFile)
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\bulk_upload_25_STBs.csv'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(3)
        self.click(self.uploadFileBtn)
        return STB_Mapping_Pagination(self.driver)

    def bulkUpload_25Devices_WithGrpName(self):
        self.click(self.chooseFile)
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\bulk_upload_25_STBs_AutomationGrp.csv'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(3)
        self.click(self.uploadFileBtn)
        return STB_Mapping_Pagination(self.driver)

    def bulkUpload_25Devices_5DevicesFromAutomationGrp(self):
        self.click(self.chooseFile)
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\bulk_upload_25_STBs_5_AutomationGrpStbs.csv'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(3)
        self.click(self.uploadFileBtn)
        return STB_Mapping_Pagination(self.driver)

    def bulkUpload_SerialNumMissing(self):
        self.click(self.chooseFile)
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\bulk_upload_SerialNumMiss.csv'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(3)
        self.click(self.uploadFileBtn)
        return STB_Mapping_Pagination(self.driver)

    def bulkUpload_DuplicateStb(self):
        self.refresh_page()
        time.sleep(1)
        self.click(self.chooseFile)
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\bulk_upload_DuplicateSTBs.csv'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(3)
        self.click(self.uploadFileBtn)
        return STB_Mapping_Pagination(self.driver)

    def bulkUpload_ValidInvalidStbs(self):
        self.refresh_page()
        time.sleep(1)
        self.click(self.chooseFile)
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\bulk_upload_ValidPlusInvalidSerialNum.csv'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(3)
        self.click(self.uploadFileBtn)
        return STB_Mapping_Pagination(self.driver)

    def bulkUpload_1_ValidStb(self):
        self.refresh_page()
        time.sleep(1)
        self.click(self.chooseFile)
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\bulk_upload_1_ValidStb.csv'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(3)
        self.click(self.uploadFileBtn)
        return STB_Mapping_Pagination(self.driver)

    def bulkUpload_withSerialNumRoomNumOnly(self):
        self.click(self.chooseFile)
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\bulk_upload_SerialNum_RoomNum.csv'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(3)
        self.click(self.uploadFileBtn)
        return STB_Mapping_Pagination(self.driver)

    def bulkUpload_DuplicateSerialNum(self):
        self.click(self.chooseFile)
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\bulk_upload_DuplicateSerialNum.csv'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(3)
        self.click(self.uploadFileBtn)
        return STB_Mapping_Pagination(self.driver)

    def getCurrantSTBCount_AutomationGrp(self):
        if self.return_elements_count(self.automationGrpTabBtn) == 1:
            self.click(self.stbMappingTitle)
            self.scroll_to_element(self.automationGrpTabBtn)
            self.scroll_to_element(self.automationGrpTabBtn)
            self.click(self.automationGrpTabBtn)
            self.wait_for_page_load()
            time.sleep(2)
            c = self.get_element_text(self.stb_count)
            count = int(c.split(":")[1].strip())
            return count
        else:
            return 0

    def getCurrantSTBCount(self):
        time.sleep(2)
        self.refresh_page()
        self.wait_for_page_load()
        c = self.get_element_text(self.stb_count)
        count = int(c.split(":")[1].strip())
        return count

    def deleteAllStbFrom_AutomationGrp(self):
        ele = self.return_elements_count(self.automationGrpTabBtn)
        if ele == 1:
            self.click(self.stbMappingTitle)
            self.scroll_to_element(self.automationGrpTabBtn)
            self.scroll_to_element(self.automationGrpTabBtn)
            self.click(self.automationGrpTabBtn)
            self.wait_for_page_load()
            time.sleep(2)
            self.click(self.stbMappingTitle)
            time.sleep(1)
            c = self.get_element_text(self.stb_count)
            count = int(c.split(":")[1].strip())
            if count >= 1:
                self.scroll_to_element(self.selectAllCheckBox)
                self.click(self.selectAllCheckBox)
                self.click(self.deleteBtn)
                self.click(self.deletePopupBtn)
                return STB_Mapping_Pagination(self.driver)
            else:
                pass
                return STB_Mapping_Pagination(self.driver)
        else:
            return STB_Mapping_Pagination(self.driver)

    def deleteAllStb(self):
        self.refresh_page()
        self.wait_for_page_load()
        self.click(self.stbMappingTitle)
        self.wait_for_page_load()
        time.sleep(1)
        c = self.get_element_text(self.stb_count)
        count = int(c.split(":")[1].strip())
        if count >= 1:
            self.scroll_to_element(self.selectAllCheckBox)
            self.click(self.selectAllCheckBox)
            self.click(self.deleteBtn)
            self.click(self.deletePopupBtn)
            return STB_Mapping_Pagination(self.driver)
        else:
            pass
            return STB_Mapping_Pagination(self.driver)

    def verifyRejectedCount(self):
        createdText = self.get_element_text(self.createdCount)
        createdCount = int(createdText.split('-')[-1].strip())
        rejectedText = self.get_element_text(self.rejectedCount)
        rejectedCount = int(rejectedText.split('-')[-1].strip())
        time.sleep(1)
        self.execute_script(self.cancelBtn)
        if createdCount == 0:
            if rejectedCount == 1:
                return True
            else:
                return False
        else:
            return False

    def verifyCreatedRejectedCount_DuplicateSTB(self):
        createdText = self.get_element_text(self.createdCount)
        createdCount = int(createdText.split('-')[-1].strip())
        rejectedText = self.get_element_text(self.rejectedCount)
        rejectedCount = int(rejectedText.split('-')[-1].strip())
        if createdCount == 1:
            if rejectedCount == 1:
                return True
            else:
                return False
        else:
            return False

    def verifyCreatedRejectedCount_ValidInvalidStb(self):
        createdText = self.get_element_text(self.createdCount)
        createdCount = int(createdText.split('-')[-1].strip())
        rejectedText = self.get_element_text(self.rejectedCount)
        rejectedCount = int(rejectedText.split('-')[-1].strip())
        time.sleep(1)
        self.execute_script(self.cancelBtn)
        if createdCount == 1:
            if rejectedCount == 1:
                return True
            else:
                return False
        else:
            return False

    def createSTB_Manually_User(self):
        self.refresh_page()
        self.click(self.addBtn)
        self.send_keys(self.roomNumTextbox, "Auto21")
        self.send_keys(self.serialNumTextbox, "QWERTYUIOP01234")
        self.click(self.saveBtn)
        return STB_Mapping_Pagination(self.driver)

    def verifyManualMappingPage(self):
        self.click(self.addBtn)
        r1 = self.return_elements_count(self.resetBtn)
        r2 = self.return_elements_count(self.saveBtn)
        r3 = self.return_elements_count(self.addMoreBtn)
        if r1 + r2 + r3 == 3:
            return True
        else:
            return False

    def verifyAddRoomsPopup(self):
        return self.find_element(self.addRoomsPopup).is_displayed()

    def clickOnSaveBtn(self):
        self.execute_script(self.saveBtn)
        return STB_Mapping_Pagination(self.driver)

    def verifySaveBtnWithRoomNumDetails(self):
        self.click(self.addBtn)
        self.send_keys(self.roomNumTextbox, "QWERTY")
        self.click(self.saveBtn)
        return STB_Mapping_Pagination(self.driver)

    def createGroup(self):
        global r_grpName
        self.click(self.manageGrp)
        self.click(self.addGrp)
        r_grpName = ''.join(
            secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(5))
        self.send_keys(self.grpNameTextbox, f"{r_grpName}")
        self.click(self.saveGrp)
        return STB_Mapping_Pagination(self.driver)

    def deleteGroup(self):
        time.sleep(1)
        self.refresh_page()
        self.click(self.manageGrp)
        self.scroll_to_element((By.XPATH, f"//button[@data-groupname='{r_grpName}']"))
        self.scroll_to_element((By.XPATH, f"//button[@data-groupname='{r_grpName}']"))
        self.scroll_to_bottom()
        self.click((By.XPATH, f"//button[@data-groupname='{r_grpName}']"))
        self.scroll_to_element(self.deleteGrpPopup)
        self.click(self.deleteGrpPopup)
        return STB_Mapping_Pagination(self.driver)

    def createSTB_Manually(self):
        global r_roomNum
        global r_serialNum
        self.refresh_page()
        self.click(self.addBtn)
        r_roomNum = ''.join(
            secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(5))
        self.send_keys(self.roomNumTextbox, f"{r_roomNum}")
        r_serialNum = ''.join(
            secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(15))
        self.send_keys(self.serialNumTextbox, f"{r_serialNum}")
        self.select_dropdown_by_visible_text(self.selectGrp, f"{r_grpName}")
        self.click(self.saveBtn)
        return STB_Mapping_Pagination(self.driver)

    def createSTB_Manually_AlphabetRoomNum(self):
        global r_roomNum_Alpha
        global r_serialNum
        self.refresh_page()
        self.click(self.addBtn)
        r_roomNum_Alpha = ''.join(
            secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(5))
        self.send_keys(self.roomNumTextbox, f"{r_roomNum_Alpha}")
        r_serialNum = ''.join(
            secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(15))
        self.send_keys(self.serialNumTextbox, f"{r_serialNum}")
        self.select_dropdown_by_visible_text(self.selectGrp, f"{r_grpName}")
        self.click(self.saveBtn)
        return STB_Mapping_Pagination(self.driver)

    def createSTB_Manually_duplicate(self):
        self.refresh_page()
        self.click(self.addBtn)
        self.send_keys(self.roomNumTextbox, f"{r_roomNum}")
        self.send_keys(self.serialNumTextbox, f"{r_serialNum}")
        self.select_dropdown_by_visible_text(self.selectGrp, f"{r_grpName}")
        self.click(self.saveBtn)
        return STB_Mapping_Pagination(self.driver)

    def createSTB_Manually_duplicateRoomNum(self):
        global r_serialNum2
        self.refresh_page()
        self.click(self.addBtn)
        self.send_keys(self.roomNumTextbox, f"{r_roomNum}")
        r_serialNum2 = ''.join(
            secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(15))
        self.send_keys(self.serialNumTextbox, f"{r_serialNum2}")
        self.select_dropdown_by_visible_text(self.selectGrp, f"{r_grpName}")
        self.click(self.saveBtn)
        return STB_Mapping_Pagination(self.driver)

    def deleteStb(self):
        self.refresh_page()
        self.wait_for_page_load()
        self.click(self.stbMappingTitle)
        self.scroll_to_element((By.XPATH, f"//button[@data-serial-num='{r_serialNum}']"))
        self.click((By.XPATH, f"//button[@data-serial-num='{r_serialNum}']"))
        self.click(self.deleteStbPopup)
        return STB_Mapping_Pagination(self.driver)

    def verifyAddedStb_serialNum(self):
        return self.find_element((By.XPATH, f"//td[normalize-space()='{r_serialNum}']")).is_displayed()

    def verifyAddedStb_roomNum(self):
        time.sleep(1)
        self.refresh_page()
        return self.find_element((By.XPATH, f"//td[normalize-space()='{r_roomNum}']")).is_displayed()

    def verifyAddedStb_grpName(self):
        return self.find_element((By.XPATH, f"//td[normalize-space()='{r_grpName}']")).is_displayed()

    def verifyWarnPopup_duplicateSerialNum(self):
        if self.getTextFromWarningPopup() == f"STB With Serial Number {r_serialNum} Already exists.":
            return True
        else:
            return False

    def createSTB_Manually_5devices_withoutSave(self):
        self.click(self.addBtn)
        for i in range(1, 6):
            global r_roomNum
            global r_serialNum
            r_roomNum = ''.join(
                secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(5))
            self.send_keys((By.XPATH, f"(//input[@placeholder='Room No'])[{i}]"), f"{r_roomNum}")
            r_serialNum = ''.join(
                secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(15))
            self.send_keys((By.XPATH, f"(//input[@name='serial-no[]'])[{i}]"), f"{r_serialNum}")
            self.select_dropdown_by_visible_text(
                (By.XPATH, f"(//select[@class='group_class stb-group-select'][@name='stb-group-name'])[{i}]"),
                f"{r_grpName}")
            self.click(self.addMoreBtn)
        self.scroll_to_element((By.XPATH, f"(//button[@class='stb-action-btn delete_btn '])[6]"))
        self.click((By.XPATH, f"(//button[@class='stb-action-btn delete_btn '])[6]"))
        return STB_Mapping_Pagination(self.driver)

    def createSTB_Manually_8devices_withoutSave(self):
        self.click(self.addBtn)
        for i in range(1, 9):
            global r_roomNum
            global r_serialNum
            r_roomNum = ''.join(
                secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(5))
            self.send_keys((By.XPATH, f"(//input[@placeholder='Room No'])[{i}]"), f"{r_roomNum}")
            r_serialNum = ''.join(
                secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(15))
            self.send_keys((By.XPATH, f"(//input[@name='serial-no[]'])[{i}]"), f"{r_serialNum}")
            self.select_dropdown_by_visible_text(
                (By.XPATH, f"(//select[@class='group_class stb-group-select'][@name='stb-group-name'])[{i}]"),
                f"{r_grpName}")
            self.click(self.addMoreBtn)
        return self.close_alert_and_get_its_text()

    def verifySequence5(self):
        global r
        for i in range(1, 6):
            ele = self.get_element_text((By.XPATH, f"(//tr[@class='appended-row']//td[@class='serialNo'])[{i}]"))
            if ele == str(i):
                r = "Pass"
            else:
                return False
        if r == "Pass":
            return True
        else:
            return False

    def delete2_3_STB(self):
        for i in range(2, 4):
            self.scroll_to_element((By.XPATH, f"(//button[@class='stb-action-btn delete_btn '])[{i}]"))
            self.click((By.XPATH, f"(//button[@class='stb-action-btn delete_btn '])[{i}]"))
        return STB_Mapping_Pagination(self.driver)

    def verifySequenceAfterDelete2_3(self):
        global r
        for i in range(1, 4):
            ele = self.get_element_text((By.XPATH, f"(//tr[@class='appended-row']//td[@class='serialNo'])[{i}]"))
            if ele == str(i):
                r = "Pass"
            else:
                return False
        if r == "Pass":
            return True
        else:
            return False

    def createSTB_ResetBtn(self):
        global r_roomNum
        global r_serialNum
        self.refresh_page()
        self.click(self.addBtn)
        r_roomNum = ''.join(
            secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(5))
        self.send_keys(self.roomNumTextbox, f"{r_roomNum}")
        r_serialNum = ''.join(
            secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(15))
        self.send_keys(self.serialNumTextbox, f"{r_serialNum}")
        self.select_dropdown_by_visible_text(self.selectGrp, f"{r_grpName}")
        self.click(self.resetBtn)
        return STB_Mapping_Pagination(self.driver)

    def verifyRoomNumTextbox(self):
        return self.get_element_attribute(self.roomNumTextbox, 'value')

    def verifySerialNumTextbox(self):
        return self.get_element_attribute(self.serialNumTextbox, 'value')

    def verifyGroupName(self):
        return self.get_element_attribute(self.selectGrp, 'value')

    def verifyPageRefreshed(self):
        return self.driver.execute_script("return performance.navigation.type")

    def createSTB_Manually_forRefresh(self):
        global r_roomNum
        global r_serialNum
        self.click(self.addBtn)
        r_roomNum = ''.join(
            secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(5))
        self.send_keys(self.roomNumTextbox, f"{r_roomNum}")
        r_serialNum = ''.join(
            secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(15))
        self.send_keys(self.serialNumTextbox, f"{r_serialNum}")
        self.select_dropdown_by_visible_text(self.selectGrp, f"{r_grpName}")
        before_source = self.driver.page_source
        self.click(self.saveBtn)
        time.sleep(3)
        after_source = self.driver.page_source
        if before_source == after_source:
            return False
        else:
            return True

    def createSubProperty(self):
        global r_subPropertyName
        global r_subPropertyCode
        self.click(self.addProperty)
        r_subPropertyName = ''.join(
            secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(8))
        self.send_keys(self.propertyNameTextBox, f"{r_subPropertyName}")
        self.send_keys(self.propertyLocationTB, "auto")
        r_subPropertyCode = ''.join(
            secrets.choice('0123456789') for _ in range(5))
        self.send_keys(self.propertyCodeTB, f"{r_subPropertyCode}")
        self.send_keys(self.propertyTypeTB, "auto")
        self.send_keys(self.encaptoDeviceIdTB, "0000")
        self.send_keys(self.encaptoAuthIdTB, "0001")
        self.send_keys(self.latitude, "1010")
        self.send_keys(self.longitude, "0101")
        self.click(self.addSubPropertyBtn)
        time.sleep(3)
        return STB_Mapping_Pagination(self.driver)

    def deleteCreatedSubProperty(self):
        self.click(self.chooseHotel)
        self.click(self.mainProperty1st)
        self.click(self.subPropertyList)
        self.wait_for_page_load()
        self.click((By.XPATH,
                    f"//td[.='{r_subPropertyName}']//ancestor::tr//following::td//div//button[@data-bs-target='#deletePropertyModal']"))
        self.click(self.deleteSubPropertyBtn)
        self.wait_for_page_load()
        return STB_Mapping_Pagination(self.driver)

    def goToCreatedSubProperty_StbMapping(self):
        self.wait_for_page_load()
        self.click(self.chooseHotel)
        self.click((By.XPATH, f"//h5[contains(.,'{r_subPropertyName}')]"))
        self.click(self.stbMapping)
        self.wait_for_page_load()
        return STB_Mapping_Pagination(self.driver)

    def verifyAddedStb_serialNum_notThere(self):
        return self.return_elements_count((By.XPATH, f"//td[normalize-space()='{r_serialNum}']"))

    def verifyAddedStb_roomNum_notThere(self):
        time.sleep(1)
        self.refresh_page()
        return self.return_elements_count((By.XPATH, f"//td[normalize-space()='{r_roomNum}']"))

    def verifyAddedStb_grpName_notThere(self):
        return self.return_elements_count((By.XPATH, f"//td[normalize-space()='{r_grpName}']"))

    def createSTB_Manually_8devices(self):
        self.click(self.addBtn)
        for i in range(1, 9):
            global r_roomNum
            global r_serialNum
            r_roomNum = ''.join(
                secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(5))
            self.send_keys((By.XPATH, f"(//input[@placeholder='Room No'])[{i}]"), f"{r_roomNum}")
            r_serialNum = ''.join(
                secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(15))
            self.send_keys((By.XPATH, f"(//input[@name='serial-no[]'])[{i}]"), f"{r_serialNum}")
            self.select_dropdown_by_visible_text(
                (By.XPATH, f"(//select[@class='group_class stb-group-select'][@name='stb-group-name'])[{i}]"),
                f"{r_grpName}")
            self.click(self.addMoreBtn)
        self.close_alert_and_get_its_text()
        self.clickOnSaveBtn()
        return STB_Mapping_Pagination(self.driver)

    def createSTB_Manually_8devices_sequence(self):
        self.click(self.addBtn)
        for i in range(1, 9):
            global r_roomNum
            global r_serialNum
            self.send_keys((By.XPATH, f"(//input[@placeholder='Room No'])[{i}]"), f"{i}")
            self.send_keys((By.XPATH, f"(//input[@name='serial-no[]'])[{i}]"), f"{i}")
            self.select_dropdown_by_visible_text(
                (By.XPATH, f"(//select[@class='group_class stb-group-select'][@name='stb-group-name'])[{i}]"),
                f"{r_grpName}")
            self.click(self.addMoreBtn)
        self.close_alert_and_get_its_text()
        self.clickOnSaveBtn()
        return STB_Mapping_Pagination(self.driver)

    def verifySequenceOf8devices(self):
        c1 = int(self.get_element_text((By.XPATH, f"//td//div//a[.='1']//ancestor::tr//td[2]")))
        for i in range(2, 9):
            c = int(self.get_element_text((By.XPATH, f"//td//div//a[.='{i}']//ancestor::tr//td[2]")))
            if c == c1 + 1:
                return True
            else:
                return False

    def verifySequenceOf7devices_afterDelete(self):
        self.refresh_page()
        self.wait_for_page_load()
        self.click(self.stbMappingTitle)
        self.scroll_to_element((By.XPATH, f"//button[@data-serial-num='1']"))
        self.click((By.XPATH, f"//button[@data-serial-num='1']"))
        self.click(self.deleteStbPopup)
        c1 = int(self.get_element_text((By.XPATH, f"//td//div//a[.='2']//ancestor::tr//td[2]")))
        for i in range(3, 9):
            c = int(self.get_element_text((By.XPATH, f"//td//div//a[.='{i}']//ancestor::tr//td[2]")))
            if c == c1 + 1:
                return True
            else:
                return False

    def clickOnEditStbBtn(self):
        self.refresh_page()
        self.wait_for_page_load()
        self.click(self.stbMappingTitle)
        self.wait_for_page_load()
        self.click((By.XPATH, f"//td[normalize-space()='{r_serialNum}']//following-sibling::td//div//button["
                              f"@data-bs-target='#editStbModal']"))

        return STB_Mapping_Pagination(self.driver)

    def verifyEditStb_updateBtnDisabled(self):
        r = str(self.find_element(self.updateBtnPopup).is_enabled())
        if r == "True":
            return False
        else:
            return True

    def verifyEditStbPopup(self):
        return self.find_element(self.popup).is_displayed()

    def verifyEditRoomSerialNum(self):
        global r_roomNum_edited
        global r_serialNum_edited
        self.clickOnEditStbBtn()
        self.find_element(self.editRoomNameTB).clear()
        self.find_element(self.editSerialNumTB).clear()
        r_roomNum_edited = ''.join(
            secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(5))
        self.send_keys(self.editRoomNameTB, f"{r_roomNum_edited}")
        time.sleep(1)
        r_serialNum_edited = ''.join(
            secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(5))
        self.send_keys(self.editSerialNumTB, f"{r_serialNum_edited}")
        self.click(self.updateBtnPopup)
        return STB_Mapping_Pagination(self.driver)

    def verifyEditedStb_roomNum(self):
        time.sleep(1)
        self.refresh_page()
        return self.find_element((By.XPATH, f"//td[normalize-space()='{r_roomNum_edited}']")).is_displayed()

    def verifyEditedStb_serialNum(self):
        return self.find_element((By.XPATH, f"//td[normalize-space()='{r_serialNum_edited}']")).is_displayed()

    def verifyEditSerialNum_SpecialChar(self):
        self.clickOnEditStbBtn()
        self.find_element(self.editSerialNumTB).clear()
        time.sleep(1)
        self.send_keys(self.editSerialNumTB, "!@#$%")
        return STB_Mapping_Pagination(self.driver)

    def clickOnUpdate(self):
        self.click(self.updateBtnPopup)
        return STB_Mapping_Pagination(self.driver)

    def verifyInAscending_RoomNum(self):
        time.sleep(2)
        userNames = []
        names = self.find_elements((By.XPATH, "//td//div//a"))
        for name in names:
            userName = name.text
            userNames.append(userName)
        result = is_ascending(userNames)
        return result

    def verifyIsDescending_RoomNum(self):
        time.sleep(2)
        userNames = []
        names = self.find_elements((By.XPATH, "//td//div//a"))
        for name in names:
            userName = name.text
            userNames.append(userName)
        result = is_descending(userNames)
        return result

    def clickOnRoomNumCol(self):
        self.wait_for_page_load()
        self.click(self.stbMappingTitle)
        self.click(self.roomNumCol)
        return STB_Mapping_Pagination(self.driver)

    def verifyInAscending_SerialNum(self):
        time.sleep(2)
        userNames = []
        names = self.find_elements((By.XPATH, "//td[@class='sorting_1']"))
        for name in names:
            userName = name.text
            userNames.append(userName)
        result = is_ascending(userNames)
        return result

    def verifyIsDescending_SerialNum(self):
        time.sleep(2)
        userNames = []
        names = self.find_elements((By.XPATH, "//td[@class='sorting_1']"))
        for name in names:
            userName = name.text
            userNames.append(userName)
        result = is_descending(userNames)
        return result

    def clickOnSerialNumCol(self):
        self.wait_for_page_load()
        self.click(self.stbMappingTitle)
        self.click(self.serialNumCol)
        return STB_Mapping_Pagination(self.driver)

    def downloadRecord(self):
        self.wait_for_page_load()
        self.click(self.stbMappingTitle)
        self.click(self.downloadRecordBtn)
        self.scroll_to_element(self.downloadPopupBtn)
        self.click(self.downloadPopupBtn)
        return STB_Mapping_Pagination(self.driver)

    def ClickOnDownloadRecords(self):
        self.wait_for_page_load()
        self.click(self.stbMappingTitle)
        self.click(self.downloadRecordBtn)
        return STB_Mapping_Pagination(self.driver)

    def ClickOnDownloadRecords_only(self):
        self.scroll_to_element(self.downloadRecordBtn)
        self.click(self.downloadRecordBtn)
        return STB_Mapping_Pagination(self.driver)

    def is_Disabled_clearDataBtn(self):
        r = self.find_element(self.clearDataBtn).is_enabled()
        if not r:
            return True
        else:
            return False

    def verifyCancel_DownloadRejectedBtn(self):
        r2 = self.return_elements_count(self.downloadRecordBtn)
        r1 = self.return_elements_count(self.cancelBtn)
        r = r1 + r2
        if r == 2:
            return True
        else:
            return False

    def clickOnCancel(self):
        time.sleep(1)
        self.execute_script(self.cancelBtn)
        time.sleep(1)
        return STB_Mapping_Pagination(self.driver)

    def click_X_Cancel(self):
        time.sleep(1)
        self.execute_script(self.X_btn)
        time.sleep(1)
        return STB_Mapping_Pagination(self.driver)

    def verifyPopup_NotThere(self):
        r = self.return_elements_count(self.popup)
        if r == 0:
            return True
        else:
            return False

    def verifyAddedStb_serialNum_AUTOMATION56789(self):
        return self.find_element((By.XPATH, f"//td[normalize-space()='AUTOMATION56789']")).is_displayed()

    def verifyAddRoomsPopup_NotTheir(self):
        r = self.return_elements_count(self.addRoomsPopup)
        if r == 0:
            return True
        else:
            return False

    def getRowCount(self):
        return self.return_elements_count(self.numOfRows)

    def verifySerialNumbers1_20(self):
        for i in range(1, 21):
            c = self.return_elements_count((By.XPATH, f"//td[@class='sorting_1'][.='{i}']"))
            if c == 0:
                return False
            else:
                return True

    def verifySerialNumbers21_40(self):
        stb_count = self.getCurrantSTBCount()
        if stb_count <= 40:
            for i in range(21, stb_count+1):
                c = self.return_elements_count((By.XPATH, f"//td[@class='sorting_1'][.='{i}']"))
                if c == 0:
                    return False
                else:
                    return True
        else:
            for i in range(21, 41):
                c = self.return_elements_count((By.XPATH, f"//td[@class='sorting_1'][.='{i}']"))
                if c == 0:
                    return False
                else:
                    return True

    def clickOnNextArrow(self):
        self.click(self.stbMappingTitle)
        self.scroll_to_element(self.nextPage)
        time.sleep(1)
        self.click(self.nextPage)
        return STB_Mapping_Pagination(self.driver)

    def clickOnPreviousArrow(self):
        self.scroll_to_element(self.previousPage)
        time.sleep(1)
        self.click(self.previousPage)
        return STB_Mapping_Pagination(self.driver)

    def verifyPage2(self):
        r = self.return_elements_count(self.page2)
        if r == 1:
            return True
        else:
            return False

    def verifyPage1(self):
        r = self.return_elements_count(self.page1)
        if r == 1:
            return True
        else:
            return False

    def verifyAutomationGrpNames(self):
        if self.return_elements_count(self.automationGrpName) == 20:
            return True
        else:
            return False

    def verifyAutomationTab(self):
        if self.return_elements_count(self.automationGrpTabBtn) == 1:
            return True
        else:
            return False

    def clickOnAutomationGrpTab(self):
        self.click(self.stbMappingTitle)
        self.scroll_to_element(self.automationGrpTabBtn)
        self.click(self.automationGrpTabBtn)
        return STB_Mapping_Pagination(self.driver)

    def verifyDownloadRecordsPopup(self):
        r = self.return_elements_count(self.downloadRecordsPopup)
        if r == 1:
            return True
        else:
            return False

    def clickOnAllCheckBox(self):
        self.click(self.checkBox_All)
        return STB_Mapping_Pagination(self.driver)

    def clickOnResetBtn(self):
        self.scroll_to_element(self.resetBtn_DownloadRecords)
        self.click(self.resetBtn_DownloadRecords)
        return STB_Mapping_Pagination(self.driver)

    def verifyAllCheckBoxAreChecked(self):
        global checked
        checkboxes = self.find_elements(self.checkBoxes)
        for checkbox in checkboxes:
            r = checkbox.is_selected()
            if r:
                checked = "True"
            else:
                return False
        return checked

    def verifyAllCheckBoxAreUnchecked(self):
        global unchecked
        checkboxes = self.find_elements(self.checkBoxes)
        for checkbox in checkboxes[1:]:
            r = checkbox.is_selected()
            if not r:
                unchecked = "True"
            else:
                return False
        return unchecked

    def verifySearchAddedDevice(self):
        self.send_keys(self.searchBar, f"{r_roomNum}")
        time.sleep(1)
        return self.verifyAddedStb_roomNum()

    def verifySearchAddedDevice_DeleteText(self):
        self.send_keys(self.searchBar, "poiuy")
        time.sleep(1)
        self.find_element(self.searchBar).send_keys(Keys.BACKSPACE)
        self.find_element(self.searchBar).send_keys(Keys.BACKSPACE)
        self.find_element(self.searchBar).send_keys(Keys.BACKSPACE)
        self.find_element(self.searchBar).send_keys(Keys.BACKSPACE)
        self.find_element(self.searchBar).send_keys(Keys.BACKSPACE)
        return self.verifyAddedStb_roomNum()

    def verifySearch_DummySearch(self):
        self.refresh_page()
        self.send_keys(self.searchBar, "poiuyt")
        time.sleep(1)
        c = self.get_element_text(self.stb_count)
        count = int(c.split(":")[1].strip())
        if count == 0:
            return True
        else:
            return False

    def verifyEditRoomNum(self):
        if self.find_element(self.editRoomNameTB).get_attribute('value') == f"{r_roomNum}":
            return True
        else:
            return False

    def verifyEditSerialNum(self):
        if self.find_element(self.editSerialNumTB).get_attribute('value') == f"{r_serialNum}":
            return True
        else:
            return False

    def clickOnXBtn(self):
        time.sleep(1)
        self.execute_script(self.X_Btn_downLoadRecords)
        return STB_Mapping_Pagination(self.driver)

    def clickOnXBtn00(self):
        time.sleep(1)
        self.execute_script(self.X_Btn_downLoadRecords)
        return STB_Mapping_Pagination(self.driver)