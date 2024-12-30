import json
import random
import secrets
import time

from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Utilities import configReader

UserName = configReader.getConfigData("configuration", "UserName")
Password = configReader.getConfigData("configuration", "Password")


class Questionnaires(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    successImg = (By.XPATH, "//img[@alt='Success']")
    warningImg = (By.XPATH, "//img[@alt='Warning']")
    successPopupMsg = (By.CSS_SELECTOR, "#noticeContent")
    warningPopupMsg = (By.CSS_SELECTOR, "#alertContent")
    chooseHotel = (By.ID, "open_Model")
    subProperty1st = (By.XPATH, "(//p[normalize-space()='Sub Property'])[1]")
    quesDD = (By.CSS_SELECTOR, ".dashboard-nav-item.nav_questionnaires")
    ques = (By.XPATH, "//div[@class='panel-collapse collapse show']//div//ul//li[1]//a")
    charts = (By.XPATH, "//div[@class='panel-collapse collapse show']//div//ul//li[2]//a")
    ques_title = (By.CSS_SELECTOR, "div[class='card quest-data-card'] h1")
    ques1_textbox = (By.CSS_SELECTOR, "#q0")
    ques2_textbox = (By.XPATH, "//input[@id='q1']")
    ques2_X_Icon = (By.XPATH, "//img[@id='q1']")
    addMore = (By.CSS_SELECTOR, "#addq")
    saveBtn = (By.CSS_SELECTOR, "#save_questions")
    addedQuesCount = (By.XPATH, "//input[@class='form-control input-quest read-only-quest']")
    deleteIconQues1 = (By.XPATH, "(//img[@alt='delete'])[1]")
    deleteBtn_Popup = (By.CSS_SELECTOR, "#delete_questions")
    cancelBtn_Popup = (By.XPATH, "//button[normalize-space()='Cancel']")
    editIconQues1 = (By.CSS_SELECTOR, "div[id='questions-0'] button[class='quest-action-btn editquestModal'] img")
    editQuesTextbox = (By.XPATH, "//input[@id='question']")
    updateBtn = (By.CSS_SELECTOR, "#update_questions")
    deletePopup = (By.XPATH, "//div[@class='modal fade show']")
    new_TextBox = (By.XPATH, "//input[@class='form-control input-quest new']")
    chartPageTitle = (By.CSS_SELECTOR, ".page-title")
    createdQues1 = (By.XPATH, "//div[@class='question-name']")
    FA_DD_count = (By.XPATH, "//select[@id='myList']//option")
    quesCountOnChartsPage = (By.XPATH, "//div[@class='question-name']")
    dateOnChartsPage = (By.CSS_SELECTOR, "#page-date2")
    X_icon = (By.CSS_SELECTOR, "button[onclick='reloadPage()']")
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

    def goToQuestionnaires(self):
        self.click(self.chooseHotel)
        self.click(self.subProperty1st)
        self.click(self.quesDD)
        return Questionnaires(self.driver)

    def goToQuestionnairesPage(self):
        self.click(self.ques)
        return Questionnaires(self.driver)

    def goToChartsPage(self):
        self.click(self.charts)
        return Questionnaires(self.driver)

    def verifyQuesDD(self):
        q = self.return_elements_count(self.ques)
        c = self.return_elements_count(self.charts)
        if q+c == 2:
            return True
        else:
            return False

    def verifyQuesTitle(self):
        if self.get_element_text(self.ques_title) == "Feedback Survey Question":
            return True
        else:
            return False

    def verifyElementsFromQuesPage(self):
        tb = self.return_elements_count(self.ques1_textbox)
        a = self.return_elements_count(self.addMore)
        s = self.return_elements_count(self.saveBtn)
        if tb+a+s == 3:
            return True
        else:
            return False

    def deleteAddedQuestions(self):
        ques_count = self.return_elements_count(self.addedQuesCount)
        i = 1
        for i in range(i, ques_count+1):
            self.click(self.deleteIconQues1)
            self.execute_script(self.deleteBtn_Popup)
            time.sleep(2)
        return Questionnaires(self.driver)

    def addQues1(self):
        time.sleep(3)
        global r_Ques1
        r_Ques1 = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10))
        self.click(self.ques1_textbox)
        self.send_keys(self.ques1_textbox, f"{r_Ques1}")
        self.click(self.saveBtn)
        return Questionnaires(self.driver)

    def verifyAddedQues1(self):
        actual_ques1 = self.get_element_attribute(self.ques1_textbox, "value")
        if actual_ques1 == r_Ques1:
            return True
        else:
            return False

    def verifyUpdatedQues1(self):
        time.sleep(3)
        actual_ques1 = self.get_element_attribute(self.ques1_textbox, "value")
        if actual_ques1 == r_Edited_Ques1:
            return True
        else:
            return False

    def clickOnAddMore(self):
        self.click(self.addMore)
        return Questionnaires(self.driver)

    def verifyQues2Textbox(self):
        tb = self.return_elements_count(self.ques2_textbox)
        x_icon = self.return_elements_count(self.ques2_X_Icon)
        if tb+x_icon == 2:
            return True
        else:
            return False

    def verifyClickOn_X_icon(self):
        self.click(self.ques2_X_Icon)
        tb = self.return_elements_count(self.ques2_textbox)
        x_icon = self.return_elements_count(self.ques2_X_Icon)
        if tb + x_icon == 0:
            return True
        else:
            return False

    def editQues1(self):
        time.sleep(3)
        global r_Edited_Ques1
        r_Edited_Ques1 = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10))
        self.click(self.editIconQues1)
        self.find_element(self.editQuesTextbox).clear()
        self.send_keys(self.editQuesTextbox, f"{r_Edited_Ques1}")
        self.click(self.updateBtn)
        return Questionnaires(self.driver)

    def verifyDelete_CancelBtn(self):
        self.click(self.deleteIconQues1)
        time.sleep(1)
        self.click(self.cancelBtn_Popup)
        r = self.return_elements_count(self.deletePopup)
        if r == 0:
            return True
        else:
            return False

    def verifyDeleteQues(self):
        time.sleep(3)
        r = self.return_elements_count(self.editIconQues1)
        if r == 0:
            return True
        else:
            return False

    def verifyNoMaxLength(self):
        maxLength = self.get_element_attribute(self.ques1_textbox, "maxlength")
        if maxLength is None:
            return True
        else:
            return False

    def addQues1_withSplChar(self):
        time.sleep(3)
        global r_Ques1_withSplChar
        r_Ques1_withSplChar = ''.join(
            secrets.choice('!@#$%^&*()') for _ in range(10))
        self.click(self.ques1_textbox)
        self.send_keys(self.ques1_textbox, f"{r_Ques1_withSplChar}")
        self.click(self.saveBtn)
        return Questionnaires(self.driver)

    def verifyAddedQues1_withSplChar(self):
        actual_ques1 = self.get_element_attribute(self.ques1_textbox, "value")
        if actual_ques1 == r_Ques1_withSplChar:
            return True
        else:
            return False

    def addQues_30(self):
        time.sleep(3)
        global r_Ques
        for i in range(1, 31):
            r_Ques = ''.join(
                secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10))
            self.click(self.new_TextBox)
            self.send_keys(self.new_TextBox, f"{r_Ques}")
            self.scroll_to_element(self.saveBtn)
            self.scroll_to_bottom()
            self.click(self.saveBtn)
            time.sleep(3)
            self.clickOnAddMore()
        return Questionnaires(self.driver)

    def verify30QuesAdded(self):
        ques_count = self.return_elements_count(self.addedQuesCount)
        if ques_count == 30:
            return True
        else:
            return False

    def verifyChartsPage(self):
        if self.get_element_text(self.chartPageTitle) == "Guest Feedback Analytics":
            return True
        else:
            return False

    def verifyAddedQuesOnChartsPage(self):
        addedQues = self.get_element_text(self.createdQues1)
        if r_Ques1 in addedQues:
            return True
        else:
            return False

    def totalGuestRatedLine(self):
        addedQues = self.get_element_text(self.createdQues1)
        if "Total 0 Guest rated" in addedQues:
            return True
        else:
            return False

    def verifyDataCountInFeedbackAnalyticsDD(self):
        c = self.return_elements_count(self.FA_DD_count)
        if c == 4:
            return True
        else:
            return False

    def verifyDeletedQuesOnChartsPage(self):
        r = self.return_elements_count(self.quesCountOnChartsPage)
        if r == 0:
            return True
        else:
            return False

    def verifyEditedQuesOnChartsPage(self):
        addedQues = self.get_element_text(self.createdQues1)
        if r_Edited_Ques1 in addedQues:
            return True
        else:
            return False

    def getDateOnChartsPage(self):
        return self.get_element_text(self.dateOnChartsPage)

    def verifyEditQuesPopup(self):
        time.sleep(3)
        self.click(self.editIconQues1)
        if self.return_elements_count(self.editQuesTextbox) == 1:
            r = self.find_element(self.updateBtn).is_enabled()
            if not r:
                return True
            else:
                return False
        else:
            return False

    def verifyDelete_X_Icon(self):
        self.click(self.editIconQues1)
        self.click(self.X_icon)
        r = self.return_elements_count(self.deletePopup)
        if r == 0:
            return True
        else:
            return False

    def verifyUpdateBtnAfterEdit(self):
        time.sleep(3)
        global r_Edited_Ques1
        r_Edited_Ques1 = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10))
        self.click(self.editIconQues1)
        self.find_element(self.editQuesTextbox).clear()
        self.send_keys(self.editQuesTextbox, f"{r_Edited_Ques1}")
        if self.return_elements_count(self.editQuesTextbox) == 1:
            r = self.find_element(self.updateBtn).is_enabled()
            if r:
                return True
            else:
                return False
        else:
            return False