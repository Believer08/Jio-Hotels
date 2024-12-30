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


class IAU_SelectFeatureAccess(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    successImg = (By.XPATH, "(//img[@alt='Success'])[1]")
    warningImg = (By.XPATH, "(//img[@alt='Warning'])[1]")
    successPopupMsg = (By.CSS_SELECTOR, "#noticeContent")
    warningPopupMsg = (By.CSS_SELECTOR, "#alertContent")
    chooseHotel = (By.ID, "open_Model")
    subProperty1st = (By.XPATH, "(//p[normalize-space()='Sub Property'])[1]")
    IAU_SFA = (By.CSS_SELECTOR, ".dashboard-nav-item[href='/jiohotels/invite_user']")
    plusBtn = (By.CSS_SELECTOR, "img[alt='Add Property']")
    IUWindow = (By.CSS_SELECTOR, "#inviteUserModal.modal.fade.show")
    userNameTB = (By.CSS_SELECTOR, "#user_name")
    editUserNameTB = (By.CSS_SELECTOR, "#reset_edit_name")
    emailTB = (By.CSS_SELECTOR, "#user_email")
    mobileNumTB = (By.CSS_SELECTOR, "#user_phone")
    editMobileNumTB = (By.CSS_SELECTOR, "#reset_edit_phone")
    selectUserTypeDD = (By.CSS_SELECTOR, "#select_user_type")
    editSelectUserTypeDD = (By.CSS_SELECTOR, "#edit_select_user_type")
    addBtn = (By.CSS_SELECTOR, "#add_user")
    resetBtn = (By.CSS_SELECTOR, "#reset_users")
    selectUserTypeDDElements = (By.CSS_SELECTOR, "#select_user_type option")
    selectFeatureAccessDDElements = (By.XPATH, "//select[@id='roles']//option")
    selectFeatureAccessDD = (By.XPATH, "//select[@id='roles']")
    searchBox = (By.CSS_SELECTOR, "input[class='form-control search mt-2 global_search_field']")
    deleteBtn_Popup = (By.CSS_SELECTOR, "#delete_user")
    selectFeatureAccessNotThere = (By.XPATH, "//div[@id='feature_dropdown'][@style='display: none;']")
    stbMappingTextWith_X = (By.XPATH, "//li[.='× STB Mapping']")
    stbMapping_X_Btn = (By.CSS_SELECTOR, "li[title=' STB Mapping'] span")
    inviteUserPopup = (By.XPATH, "//div[@class='modal fade show'][@id='inviteUserModal']")
    editUserPopup = (By.XPATH, "//div[@id='editUserModal'][@class='modal fade show']")
    cancelBtnEditUserPage = (By.CSS_SELECTOR, "#reset_vals")
    updateBtnEditUserPage = (By.CSS_SELECTOR, "#update_user")
    X_btnInviteUserPage = (By.XPATH, "//h2[.='Invite a User']//following-sibling::button")
    cancelBtn_DeleteUser = (By.CSS_SELECTOR, ".btn.btn-cancel")
    deleteUserPopup = (By.XPATH, "//div[@id='deleteUserModal'][@class='modal fade show']")
    tableRow = (By.XPATH, "//table[@id='user_listing']//tbody//tr")
    userCount = (By.CSS_SELECTOR, "div[class='left-heading'] p")
    serialNum_elements = (By.XPATH, "//table[@id='user_listing']//tbody//td[2]")
    date = (By.CSS_SELECTOR, ".page-date.text-end")

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

    def goTo_InviteUser_SFA(self):
        self.click(self.chooseHotel)
        self.wait_for_page_load()
        self.click(self.subProperty1st)
        self.click(self.IAU_SFA)
        self.wait_for_page_load()
        return IAU_SelectFeatureAccess(self.driver)

    def clickOnInviteUser(self):
        self.click(self.plusBtn)
        return IAU_SelectFeatureAccess(self.driver)

    def verifyInviteUserWindow(self):
        if self.return_elements_count(self.IUWindow) == 1:
            return True
        else:
            return False

    def verifyDataOnIUWindow(self):
        r1 = self.return_elements_count(self.userNameTB)
        r2 = self.return_elements_count(self.emailTB)
        r3 = self.return_elements_count(self.mobileNumTB)
        r4 = self.return_elements_count(self.selectUserTypeDD)
        r5 = self.return_elements_count(self.addBtn)
        if r1 and r2 and r3 and r4 and r5 == 1:
            return True
        else:
            return False

    def verifyDisabledResetBtn(self):
        if not self.find_element(self.resetBtn).is_enabled():
            return True
        else:
            return False

    def verifySelectUserDDElements(self):
        global result
        valid_elements = ["", "Select User Type", "Admin", "Property Admin", "Executive", "Supervisor", "Assistant",
                          "Marketing", "Others", "View Only"]
        elements = self.find_elements(self.selectUserTypeDDElements)
        for element in elements:
            if element.text in valid_elements:
                result = "true"
            else:
                return False
        return result

    def enterUserName(self):
        global r_userName
        r_string = ''.join(
            secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(4))
        r_userName = "TestUser " + r_string
        self.send_keys(self.userNameTB, r_userName)
        return IAU_SelectFeatureAccess(self.driver)

    def enterEmail(self):
        time.sleep(0.3)
        global r_email
        r_string = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(4))
        r_email = r_string + "@auto.com"
        self.send_keys(self.emailTB, r_email)
        return IAU_SelectFeatureAccess(self.driver)

    def enterMobileNumber(self):
        global r_MobileNum
        r_string = ''.join(
            secrets.choice('0123456789') for _ in range(9))
        r_MobileNum = int("6" + r_string)
        self.send_keys(self.mobileNumTB, r_MobileNum)
        return IAU_SelectFeatureAccess(self.driver)

    def enterMobileNumber_9Digit(self):
        global r_MobileNum
        r_string = ''.join(
            secrets.choice('0123456789') for _ in range(8))
        r_MobileNum = int("6" + r_string)
        self.send_keys(self.mobileNumTB, r_MobileNum)
        return IAU_SelectFeatureAccess(self.driver)

    def enterEmail_duplicate(self):
        time.sleep(0.3)
        self.send_keys(self.emailTB, r_email)
        return IAU_SelectFeatureAccess(self.driver)

    def enterEmail_InvalidMail_SplChar(self):
        time.sleep(0.3)
        self.send_keys(self.emailTB, "test#$@123@auto.com")
        return IAU_SelectFeatureAccess(self.driver)

    def enterEmail_InvalidMail(self):
        time.sleep(0.3)
        self.send_keys(self.emailTB, "testauto")
        return IAU_SelectFeatureAccess(self.driver)

    def enterEmail_InvalidMail_2EmailIDs(self):
        time.sleep(0.3)
        self.send_keys(self.emailTB, "test675@auto.com;test665@auto.com")
        return IAU_SelectFeatureAccess(self.driver)

    def enterUserName_SplChar(self):
        self.send_keys(self.userNameTB, "!@#$")
        return IAU_SelectFeatureAccess(self.driver)

    def enterMobileNum_SplChar(self):
        self.send_keys(self.mobileNumTB, "!@#$")
        return IAU_SelectFeatureAccess(self.driver)

    def enterMobileNum_Alphabets(self):
        time.sleep(2)
        self.send_keys(self.mobileNumTB, "abcd")
        return IAU_SelectFeatureAccess(self.driver)

    def selectUser_Admin(self):
        self.select_dropdown_by_visible_text(self.selectUserTypeDD, "Admin")
        return IAU_SelectFeatureAccess(self.driver)

    def selectUser_PropertyAdmin(self):
        self.select_dropdown_by_visible_text(self.selectUserTypeDD, "Property Admin")
        return IAU_SelectFeatureAccess(self.driver)

    def createUser_Admin(self):
        self.clickOnInviteUser()
        self.enterUserName()
        self.enterEmail()
        self.enterMobileNumber()
        self.selectUser_Admin()
        self.scroll_to_element(self.addBtn)
        self.click(self.addBtn)
        return IAU_SelectFeatureAccess(self.driver)

    def createUser_Admin_InvalidMail_SplChar(self):
        self.clickOnInviteUser()
        self.enterUserName()
        self.enterEmail_InvalidMail_SplChar()
        self.enterMobileNumber()
        self.selectUser_Admin()
        self.scroll_to_element(self.addBtn)
        self.click(self.addBtn)
        return IAU_SelectFeatureAccess(self.driver)

    def createUser_Admin_InvalidMail(self):
        self.clickOnInviteUser()
        self.enterUserName()
        self.enterEmail_InvalidMail()
        self.enterMobileNumber()
        self.selectUser_Admin()
        self.scroll_to_element(self.addBtn)
        self.click(self.addBtn)
        return IAU_SelectFeatureAccess(self.driver)

    def createUser_Admin_InvalidMail_2EmailIDs(self):
        self.clickOnInviteUser()
        self.enterUserName()
        self.enterEmail_InvalidMail_2EmailIDs()
        self.enterMobileNumber()
        self.selectUser_Admin()
        self.scroll_to_element(self.addBtn)
        self.click(self.addBtn)
        return IAU_SelectFeatureAccess(self.driver)

    def createUser_Admin_InvalidMobileNum(self):
        self.clickOnInviteUser()
        self.enterUserName()
        self.enterEmail()
        self.enterMobileNumber_9Digit()
        self.selectUser_Admin()
        self.scroll_to_element(self.addBtn)
        self.click(self.addBtn)
        return IAU_SelectFeatureAccess(self.driver)

    def createUser_Admin_existingEmail(self):
        time.sleep(0.5)
        self.clickOnInviteUser()
        self.enterUserName()
        self.enterEmail_duplicate()
        self.enterMobileNumber()
        self.selectUser_Admin()
        self.scroll_to_element(self.addBtn)
        self.click(self.addBtn)
        return IAU_SelectFeatureAccess(self.driver)

    def createUser_Admin_X_Btn(self):
        self.clickOnInviteUser()
        self.enterUserName()
        self.enterEmail()
        self.enterMobileNumber()
        self.selectUser_Admin()
        self.click(self.X_btnInviteUserPage)
        return IAU_SelectFeatureAccess(self.driver)

    def createUser_Admin_WithoutUserType(self):
        self.clickOnInviteUser()
        self.enterUserName()
        self.enterEmail()
        self.enterMobileNumber()
        self.scroll_to_element(self.addBtn)
        self.click(self.addBtn)
        return IAU_SelectFeatureAccess(self.driver)

    def createUser_PropertyAdmin_withoutAdd(self):
        self.clickOnInviteUser()
        self.enterUserName()
        self.enterEmail()
        self.enterMobileNumber()
        self.selectUser_PropertyAdmin()
        return IAU_SelectFeatureAccess(self.driver)

    def createUser_PropertyAdmin(self):
        self.clickOnInviteUser()
        self.enterUserName()
        self.enterEmail()
        self.enterMobileNumber()
        self.selectUser_PropertyAdmin()
        self.select_dropdown_by_visible_text(self.selectFeatureAccessDD, "STB Mapping")
        self.scroll_to_element(self.addBtn)
        self.click(self.addBtn)
        return IAU_SelectFeatureAccess(self.driver)

    def createUser_PropertyAdmin_WithoutSelectFeatureAccess(self):
        self.clickOnInviteUser()
        self.enterUserName()
        self.enterEmail()
        self.enterMobileNumber()
        self.selectUser_PropertyAdmin()
        self.click(self.addBtn)
        return IAU_SelectFeatureAccess(self.driver)

    def createUser_PropertyAdmin_STBMapping_withoutAdd(self):
        self.clickOnInviteUser()
        self.enterUserName()
        self.enterEmail()
        self.enterMobileNumber()
        self.selectUser_PropertyAdmin()
        self.select_dropdown_by_visible_text(self.selectFeatureAccessDD, "STB Mapping")
        return IAU_SelectFeatureAccess(self.driver)

    def clickOnResetBtn(self):
        time.sleep(1)
        self.scroll_to_element(self.resetBtn)
        self.click(self.resetBtn)
        return IAU_SelectFeatureAccess(self.driver)

    def deleteAutoCreatedUser(self):
        time.sleep(2)
        self.refresh_page()
        self.send_keys(self.searchBox, "auto")
        c = self.return_elements_count((By.XPATH, "//button[@data-bs-target='#deleteUserModal']"))
        self.goTo_InviteUser_SFA()
        if c >= 1:
            for i in range(1, c + 1):
                self.send_keys(self.searchBox, "auto")
                self.wait_for_page_load()
                self.click((By.XPATH, "(//button[@data-bs-target='#deleteUserModal'])[1]"))
                time.sleep(1)
                self.click(self.deleteBtn_Popup)
                self.wait_for_page_load()
                time.sleep(4)
        return IAU_SelectFeatureAccess(self.driver)

    def verifySelectFeatureAccessDD(self):
        if self.return_elements_count(self.selectFeatureAccessNotThere) == 0:
            return True
        else:
            return False

    def verifySelectFeatureAccessDDElements(self):
        global result
        valid_elements = ["STB Mapping", "Manage Content", "Notification", "Message Authority", "In Room Dining",
                          "Order History", "Questionnaires",
                          "Charts", "Guest Administration", "Butler Service", "DnD Service", "Make Up Room",
                          "Emergency Service", "Welcome Letter", "Amenities Items", "Guest Request", "Hotspot",
                          "Theme Setting"]
        elements = self.find_elements(self.selectFeatureAccessDDElements)
        for element in elements:
            if element.text in valid_elements:
                result = "true"
            else:
                return False
        return result

    def verifySTBMappingTextWith_XBtn(self):
        if self.return_elements_count(self.stbMappingTextWith_X) == 1:
            return True
        else:
            return False

    def verifySTBMappingTextWith_XBtn_NotThere(self):
        if self.return_elements_count(self.stbMappingTextWith_X) == 0:
            return True
        else:
            return False

    def clickOnStbMapping_X_Btn(self):
        time.sleep(1)
        self.click(self.stbMapping_X_Btn)
        return IAU_SelectFeatureAccess(self.driver)

    def valueOfUserNameTB(self):
        return self.get_element_attribute(self.userNameTB, "value")

    def valueOfEmailTB(self):
        return self.get_element_attribute(self.emailTB, "value")

    def valueOfMobileNumTB(self):
        return self.get_element_attribute(self.mobileNumTB, "value")

    def valueOfUserTypeDD(self):
        return self.get_element_attribute(self.selectUserTypeDD, "value")

    def clickOnEditBtnOfCreatedUser(self):
        self.scroll_to_element((By.XPATH, f"//button[@data-property-name='{r_userName}']"))
        self.click((By.XPATH, f"//button[@data-property-name='{r_userName}']"))
        return IAU_SelectFeatureAccess(self.driver)

    def verifyEditUserPopupIsDisplayed(self):
        if self.return_elements_count(self.editUserPopup) == 1:
            return True
        else:
            return False

    def verifyUserNameOnEditUserWindow(self):
        if self.get_element_attribute(self.editUserNameTB, "value") == r_userName:
            return True
        else:
            return False

    def verifyMobileNumOnEditUserWindow(self):
        if self.get_element_attribute(self.editMobileNumTB, "value") == str(r_MobileNum):
            return True
        else:
            return False

    def verifyUserTypeOnEditUserWindow(self):
        if self.get_element_attribute(self.editSelectUserTypeDD, "value") == "Admin":
            return True
        else:
            return False

    def verifyEditIUWindow(self):
        r1 = self.return_elements_count(self.editUserNameTB)
        r2 = self.return_elements_count(self.editMobileNumTB)
        r3 = self.return_elements_count(self.editSelectUserTypeDD)
        r4 = self.return_elements_count(self.cancelBtnEditUserPage)
        r5 = self.return_elements_count(self.updateBtnEditUserPage)
        if r1 and r2 and r3 and r4 and r5 == 1:
            return True
        else:
            return False

    def enterEditedUserName(self):
        global r_userName_edited
        r_string = ''.join(
            secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(4))
        r_userName_edited = "TestUser " + r_string
        self.find_element(self.editUserNameTB).clear()
        time.sleep(0.33)
        self.send_keys(self.editUserNameTB, r_userName_edited)
        return IAU_SelectFeatureAccess(self.driver)

    def clickOnUpdate_EditUserPage(self):
        self.click(self.updateBtnEditUserPage)
        return IAU_SelectFeatureAccess(self.driver)

    def editUserNameOfCreatedUser(self):
        self.clickOnEditBtnOfCreatedUser()
        self.enterEditedUserName()
        return IAU_SelectFeatureAccess(self.driver)

    def verifyTextFromSuccessPopupIfUpdateBtnIsEnabled(self):
        global temp1
        if self.find_element(self.updateBtnEditUserPage).is_enabled():
            self.click(self.updateBtnEditUserPage)
            ele = self.return_elements_count(self.successImg)
            if ele == 1:
                temp1 = 1
                if self.get_element_text(self.successPopupMsg) == "User detail added successfully":
                    return True
                else:
                    temp1 = 0
                    return False
            else:
                temp1 = 0
                return False
        else:
            temp1 = 0
            return False

    def verifyEditedUserNameInSummary(self):
        if temp1 == 1:
            if self.return_elements_count((By.XPATH, f"//td[.='{r_userName_edited}']")) == 1:
                return True
            else:
                return False
        else:
            return False

    def verifyUserNameInSummary_NotTheir(self):
        time.sleep(3)
        if self.return_elements_count((By.XPATH, f"//td[.='{r_userName}']")) == 0:
            return True
        else:
            return False

    def verifyUserNameInSummary(self):
        if self.return_elements_count((By.XPATH, f"//td[.='{r_userName}']")) == 1:
            return True
        else:
            return False
    def verifyEmailInSummary(self):
        if self.return_elements_count((By.XPATH, f"//td[.='{r_email}']")) == 1:
            return True
        else:
            return False

    def verifyInviteUserPopup_NotTheir(self):
        if self.return_elements_count(self.inviteUserPopup) == 0:
            return True
        else:
            return False

    def deleteCreatedUser_CancelBtn(self):
        deleteBtn = (By.XPATH, f"//button[@data-user-name='{r_userName}']")
        self.scroll_to_element(deleteBtn)
        self.click(deleteBtn)
        time.sleep(0.7)
        self.click(self.cancelBtn_DeleteUser)
        return IAU_SelectFeatureAccess(self.driver)

    def deleteCreatedUser(self):
        deleteBtn = (By.XPATH, f"//button[@data-user-name='{r_userName}']")
        self.scroll_to_element(deleteBtn)
        self.click(deleteBtn)
        time.sleep(0.7)
        self.click(self.deleteBtn_Popup)
        return IAU_SelectFeatureAccess(self.driver)

    def verifyDeleteUserPopupInNotTheir(self):
        if self.return_elements_count(self.deleteUserPopup) == 0:
            return True
        else:
            return False

    def clickOnAddBtn(self):
        self.scroll_to_element(self.addBtn)
        self.click(self.addBtn)
        return IAU_SelectFeatureAccess(self.driver)

    def searchCreatedUser(self):
        time.sleep(3)
        self.send_keys(self.searchBox, r_userName)
        time.sleep(1)
        return IAU_SelectFeatureAccess(self.driver)

    def verifyOneRow(self):
        if self.return_elements_count(self.tableRow) == 1:
            return True
        else:
            return False

    def getCurrantUserCount(self):
        time.sleep(2)
        self.refresh_page()
        self.wait_for_page_load()
        c = self.get_element_text(self.userCount)
        count = int(c.split(":")[1].strip())
        return count

    def verifySequenceIsAscending_SerialNum(self):
        time.sleep(2)
        serialNums = []
        names = self.find_elements(self.serialNum_elements)
        for name in names:
            serialNum = name.text
            serialNums.append(serialNum)
        result = is_ascending(serialNums)
        return result

    def verifyCreate5Users_Admin(self):
        global result_created5Users
        result_created5Users = 0
        for i in range(1,6):
            self.createUser_Admin()
            if self.verifyUserNameInSummary():
                if self.verifyEmailInSummary():
                    result_created5Users += 1
                else:
                    return 0
            else:
                return 0
        return result_created5Users

    def verifyAddedUserRole_PropertyAdmin(self):
        role = (By.XPATH, f"//td[.='{r_userName}']/following-sibling::td[.='Property Admin  ']")
        if self.return_elements_count(role) == 1:
            if self.get_element_text(role) == "Property Admin":
                return True
            else:
                return False
        else:
            return False

    def userName_MaxLength(self):
        return self.get_element_attribute(self.userNameTB, "maxlength")

    def enterUserName_50Char(self):
        global r_userName
        r_string = ''.join(
            secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(50))
        self.send_keys(self.userNameTB, r_string)
        return IAU_SelectFeatureAccess(self.driver)

    def verify20CharEntered(self):
        time.sleep(0.70)
        if len(self.get_element_attribute(self.userNameTB, "value")) == 20:
            return True
        else:
            return False

    def dateOnIAU_SelectFeatureAccessPage(self):
        return self.get_element_text(self.date)