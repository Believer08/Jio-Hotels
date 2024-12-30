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


class GuestServices(BasePage):

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
    guestServices = (By.CSS_SELECTOR, ".dashboard-nav-item.nav_hotel_services")
    guestAdministration = (By.CSS_SELECTOR, ".dashboard-nav-item[href='/jiohotels/guest_services/guest_administration']")
    guestServicesDD_elements = (By.XPATH, "//div[@id='hotel_services'][@class='panel-collapse collapse show']//li//a")
    guestAdTitle = (By.CSS_SELECTOR, ".page-title")
    enterGuestNameTB = (By.CSS_SELECTOR, "#guest_first_name")
    saveBtnGuestName = (By.CSS_SELECTOR, "#update_guest_data")
    checkOutBtnPopup = (By.CSS_SELECTOR, "#checkout_guest_data")
    cancelBtnPopup = (By.CSS_SELECTOR, "span[data-dismiss='modal']")
    X_BtnPopup = (By.CSS_SELECTOR, "div[id='checkoutmodal'] button[aria-label='Close']")
    checkoutPopupWindow = (By.XPATH, "//div[@class='modal fade show'][@id='checkoutmodal']")
    grpCount = (By.CSS_SELECTOR, "div[class='left-heading'] p")
    searchGuest = (By.CSS_SELECTOR, "#guest_search_field")
    noDataText = (By.CSS_SELECTOR, ".dataTables_empty")

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
        time.sleep(1)
        self.click(self.stbMapping)
        self.wait_for_page_load()
        return GuestServices(self.driver)

    def goToGuestAdministration(self):
        time.sleep(1)
        self.click(self.chooseHotel)
        self.click(self.subProperty1st)
        self.wait_for_page_load()
        time.sleep(1)
        self.scroll_to_element(self.guestServices)
        self.click(self.guestServices)
        self.wait_for_page_load()
        self.click(self.guestAdministration)
        return GuestServices(self.driver)

    def clickOnGuestServicesDD(self):
        self.wait_for_page_load()
        self.click(self.chooseHotel)
        self.click(self.subProperty1st)
        time.sleep(1)
        self.scroll_to_element(self.guestServices)
        self.click(self.guestServices)
        self.wait_for_page_load()
        return GuestServices(self.driver)

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
        return GuestServices(self.driver)

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
                return GuestServices(self.driver)
            else:
                pass
                return GuestServices(self.driver)
        else:
            return GuestServices(self.driver)

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
            return GuestServices(self.driver)
        else:
            pass
            return GuestServices(self.driver)

    def createGroup(self):
        global r_grpName
        self.click(self.manageGrp)
        self.click(self.addGrp)
        r_grpName = ''.join(
            secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(5))
        self.send_keys(self.grpNameTextbox, f"{r_grpName}")
        self.click(self.saveGrp)
        return GuestServices(self.driver)

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
        return GuestServices(self.driver)

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
        return GuestServices(self.driver)

    def deleteStb(self):
        self.refresh_page()
        self.wait_for_page_load()
        self.click(self.stbMappingTitle)
        self.scroll_to_element((By.XPATH, f"//button[@data-serial-num='{r_serialNum}']"))
        self.click((By.XPATH, f"//button[@data-serial-num='{r_serialNum}']"))
        self.click(self.deleteStbPopup)
        return GuestServices(self.driver)

    def verifyGuestServicesDD(self):
        global result
        if self.return_elements_count(self.guestServicesDD_elements) >= 1:
            valid_elements = ["Guest Administration", "Butler Service", "DnD Service", "Make Up Room",
                              "Emergency Service"]
            elements = self.find_elements(self.guestServicesDD_elements)
            for element in elements:
                if element.text in valid_elements:
                    result = "true"
                else:
                    return False
            return result
        else:
            return False

    def createSTB(self):
        self.goToSTB_Mapping()
        self.createGroup()
        self.goToSTB_Mapping()
        self.createSTB_Manually()
        return GuestServices(self.driver)

    def verifyGuestAdTitle(self):
        if self.get_element_text(self.guestAdTitle) == "Guest Administration":
            return True
        else:
            return False

    def verifyCreatedSTBSerialNumOnGuestAdPage(self):
        if self.return_elements_count((By.XPATH, f"//td[.='{r_serialNum}']")) == 1:
            return True
        else:
            return False

    def verifyEditBtnForCreatedSTBOnGuestAdPage(self):
        if self.return_elements_count((By.XPATH, f"//td[.='{r_serialNum}']/following-sibling::td//div//span[@data-target='#editguestadminmodal']")) == 1:

            return True
        else:
            return False

    def AddGuestNameToCreatedSTB(self):
        global r_guestName
        editBtn = (By.XPATH, f"//td[.='{r_serialNum}']/following-sibling::td//div//span[@data-target='#editguestadminmodal']")
        self.click(editBtn)
        r_string = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(4))
        r_guestName = "TestGuest_" + r_string
        self.send_keys(self.enterGuestNameTB, r_guestName)
        self.click(self.saveBtnGuestName)
        return GuestServices(self.driver)

    def EditGuestNameToCreatedSTB(self):
        global r_guestName_edited
        editBtn = (By.XPATH, f"//td[.='{r_serialNum}']/following-sibling::td//div//span[@data-target='#editguestadminmodal']")
        self.click(editBtn)
        self.find_element(self.enterGuestNameTB).clear()
        time.sleep(0.3)
        r_string = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(4))
        r_guestName_edited = "TestGuest_" + r_string
        self.send_keys(self.enterGuestNameTB, r_guestName_edited)
        self.click(self.saveBtnGuestName)
        return GuestServices(self.driver)

    def AddGuestNameToCreatedSTB_SplChar(self):
        editBtn = (By.XPATH, f"//td[.='{r_serialNum}']/following-sibling::td//div//span[@data-target='#editguestadminmodal']")
        self.click(editBtn)
        self.send_keys(self.enterGuestNameTB, "!@#$%")
        return GuestServices(self.driver)

    def verifyGuestNameTB_IsEmpty(self):
        if self.get_element_attribute(self.enterGuestNameTB, "value") == "":
            return True
        else:
            return False

    def clickOnSaveBtn(self):
        editBtn = (By.XPATH, f"//td[.='{r_serialNum}']/following-sibling::td//div//span[@data-target='#editguestadminmodal']")
        self.click(editBtn)
        self.click(self.saveBtnGuestName)
        return GuestServices(self.driver)

    def checkOutCreatedGuest(self):
        time.sleep(0.6)
        checkoutBtn = (By.XPATH, f"//td[.='{r_serialNum}']/following-sibling::td//div//button[@data-target='#checkoutmodal']")
        self.click(checkoutBtn)
        self.click(self.checkOutBtnPopup)
        return GuestServices(self.driver)

    def checkOutCreatedGuest_CancelBtn(self):
        time.sleep(0.6)
        checkoutBtn = (By.XPATH, f"//td[.='{r_serialNum}']/following-sibling::td//div//button[@data-target='#checkoutmodal']")
        self.click(checkoutBtn)
        time.sleep(0.6)
        self.click(self.cancelBtnPopup)
        return GuestServices(self.driver)

    def checkOutCreatedGuest_X_Btn(self):
        time.sleep(0.6)
        checkoutBtn = (By.XPATH, f"//td[.='{r_serialNum}']/following-sibling::td//div//button[@data-target='#checkoutmodal']")
        self.click(checkoutBtn)
        time.sleep(0.6)
        self.click(self.X_BtnPopup)
        return GuestServices(self.driver)

    def verifyAddedGuestName(self):
        guestName = (By.XPATH, f"//td[.='{r_serialNum}']/following-sibling::td//div//p")
        if self.get_element_text(guestName) == r_guestName:
            return True
        else:
            return False

    def verifyAddedGuestName_NotTheir(self):
        guestName = (By.XPATH, f"//td[.='{r_serialNum}']/following-sibling::td//div//p")
        if self.return_elements_count(guestName) == 0:
            return True
        else:
            return False

    def verifyEditedGuestName(self):
        guestName = (By.XPATH, f"//td[.='{r_serialNum}']/following-sibling::td//div//p")
        if self.get_element_text(guestName) == r_guestName_edited:
            return True
        else:
            return False

    def verifyCheckoutPopupWindowNotTheir(self):
        time.sleep(1)
        if self.return_elements_count(self.checkoutPopupWindow) == 0:
            return True
        else:
            return False

    def deleteAllGroups(self):
        time.sleep(1)
        self.refresh_page()
        self.click(self.manageGrp)
        c = self.get_element_text(self.grpCount)
        count = int(c.split(":")[1].strip())
        if count >= 1:
            for i in range(1, count + 1):
                self.wait_for_page_load()
                self.click((By.XPATH, "(//img[@src='/jiohotels/images/users/delete.svg'])[1]"))
                time.sleep(0.3)
                self.scroll_to_element(self.deleteGrpPopup)
                self.click(self.deleteGrpPopup)
                time.sleep(4)
        return GuestServices(self.driver)

    def searchAddedGuest_SerialNum(self):
        time.sleep(4)
        self.send_keys(self.searchGuest, r_serialNum)
        time.sleep(1.5)
        return GuestServices(self.driver)

    def searchAddedGuest_RoomNum(self):
        time.sleep(4)
        self.send_keys(self.searchGuest, r_roomNum)
        time.sleep(1.5)
        return GuestServices(self.driver)

    def searchAddedGuest_randomText(self):
        time.sleep(4)
        self.send_keys(self.searchGuest, "zzzzzzzzyyy")
        time.sleep(1.5)
        return GuestServices(self.driver)
    def searchAddedGuest_GuestName(self):
        time.sleep(4)
        self.send_keys(self.searchGuest, r_guestName)
        time.sleep(1.5)
        return GuestServices(self.driver)

    def searchAddedGuest_ClearText(self):
        time.sleep(4)
        self.find_element(self.searchGuest).clear()
        time.sleep(0.5)
        self.find_element(self.searchGuest).send_keys(Keys.BACKSPACE)
        time.sleep(1.5)
        return GuestServices(self.driver)

    def verifyNoDataText(self):
        if self.get_element_text(self.noDataText) == "No data available in table":
            return True
        else:
            return False

