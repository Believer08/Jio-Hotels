import time
import pytest
from datetime import datetime
from Pages.Questionnaires import Questionnaires
from TestCases.BaseTest import BaseTest
from pytest_check import check

quesSuccessfulAdded_popup = "Questionnaire was successfully created"
quesSuccessfulUpdated_popup = "Question updated successfully"


class Test_Questionnaires(BaseTest):

    @pytest.fixture(autouse=True)
    def test_refreshBrowser(self):
        self.driver.refresh()

    def test_QuestionnairesDropdownOptions(self):
        with check:
            HomePage = Questionnaires(self.driver)
            assert HomePage.goToQuestionnaires().verifyQuesDD()

    def test_QuestionnairesPage(self):
        with check:
            HomePage = Questionnaires(self.driver)
            assert HomePage.goToQuestionnaires().goToQuestionnairesPage().verifyQuesTitle()
        with check:
            assert HomePage.verifyElementsFromQuesPage()

    def test_createNewQuestion(self):
        with check:
            HomePage = Questionnaires(self.driver)
            assert HomePage.goToQuestionnaires().goToQuestionnairesPage().deleteAddedQuestions().addQues1().getTextFromSuccessPopup() == quesSuccessfulAdded_popup
        with check:
            assert HomePage.verifyAddedQues1()
        HomePage.deleteAddedQuestions()

    def test_addMore(self):
        with check:
            HomePage = Questionnaires(self.driver)
            assert HomePage.goToQuestionnaires().goToQuestionnairesPage().deleteAddedQuestions().clickOnAddMore().verifyQues2Textbox()

    def test_X_icon(self):
        with check:
            HomePage = Questionnaires(self.driver)
            assert HomePage.goToQuestionnaires().goToQuestionnairesPage().deleteAddedQuestions().clickOnAddMore().verifyClickOn_X_icon()

    def test_editCreateQuestion(self):
        with check:
            HomePage = Questionnaires(self.driver)
            assert HomePage.goToQuestionnaires().goToQuestionnairesPage().deleteAddedQuestions().addQues1().getTextFromSuccessPopup() == quesSuccessfulAdded_popup
        with check:
            assert HomePage.verifyAddedQues1()
        with check:
            assert HomePage.editQues1().getTextFromSuccessPopup() == quesSuccessfulUpdated_popup
        with check:
            assert HomePage.verifyUpdatedQues1()
        HomePage.deleteAddedQuestions()

    def test_deleteQues_CancelBtn(self):
        with check:
            HomePage = Questionnaires(self.driver)
            assert HomePage.goToQuestionnaires().goToQuestionnairesPage().deleteAddedQuestions().addQues1().getTextFromSuccessPopup() == quesSuccessfulAdded_popup
        with check:
            assert HomePage.verifyAddedQues1()
        with check:
            assert HomePage.verifyDelete_CancelBtn()
        HomePage.deleteAddedQuestions()

    def test_deleteQues(self):
        with check:
            HomePage = Questionnaires(self.driver)
            assert HomePage.goToQuestionnaires().goToQuestionnairesPage().deleteAddedQuestions().addQues1().getTextFromSuccessPopup() == quesSuccessfulAdded_popup
        with check:
            assert HomePage.verifyAddedQues1()
        with check:
            assert HomePage.deleteAddedQuestions().verifyDeleteQues()

    def test_noMaxLength(self):
        with check:
            HomePage = Questionnaires(self.driver)
            assert HomePage.goToQuestionnaires().goToQuestionnairesPage().verifyNoMaxLength()

    def test_createNewQuestion_withSplChar(self):
        with check:
            HomePage = Questionnaires(self.driver)
            assert HomePage.goToQuestionnaires().goToQuestionnairesPage().deleteAddedQuestions().addQues1_withSplChar().getTextFromSuccessPopup() == quesSuccessfulAdded_popup
        with check:
            assert HomePage.verifyAddedQues1_withSplChar()
        HomePage.deleteAddedQuestions()

    def test_chartsPage(self):
        with check:
            HomePage = Questionnaires(self.driver)
            assert HomePage.goToQuestionnaires().goToChartsPage().verifyChartsPage()

    def test_createdQuesOnChartsPage(self):
        with check:
            HomePage = Questionnaires(self.driver)
            assert HomePage.goToQuestionnaires().goToQuestionnairesPage().deleteAddedQuestions().addQues1().getTextFromSuccessPopup() == quesSuccessfulAdded_popup
        with check:
            assert HomePage.verifyAddedQues1()
        with check:
            self.driver.refresh()
            assert HomePage.goToQuestionnaires().goToChartsPage().verifyChartsPage()
        with check:
            assert HomePage.verifyAddedQuesOnChartsPage()
        HomePage.goToQuestionnaires().goToQuestionnairesPage().deleteAddedQuestions()

    def test_feedbackAnalyticsDropdown(self):
        with check:
            HomePage = Questionnaires(self.driver)
            assert HomePage.goToQuestionnaires().goToQuestionnairesPage().deleteAddedQuestions().addQues1().getTextFromSuccessPopup() == quesSuccessfulAdded_popup
        with check:
            assert HomePage.verifyAddedQues1()
        with check:
            self.driver.refresh()
            assert HomePage.goToQuestionnaires().goToChartsPage().verifyDataCountInFeedbackAnalyticsDD()
        HomePage.goToQuestionnaires().goToQuestionnairesPage().deleteAddedQuestions()

    def test_totalGuestRatedLine(self):
        with check:
            HomePage = Questionnaires(self.driver)
            assert HomePage.goToQuestionnaires().goToQuestionnairesPage().deleteAddedQuestions().addQues1().getTextFromSuccessPopup() == quesSuccessfulAdded_popup
        with check:
            assert HomePage.verifyAddedQues1()
        with check:
            self.driver.refresh()
            assert HomePage.goToQuestionnaires().goToChartsPage().totalGuestRatedLine()
        HomePage.goToQuestionnaires().goToQuestionnairesPage().deleteAddedQuestions()

    def test_deleteQuesOnChartsPage(self):
        with check:
            HomePage = Questionnaires(self.driver)
            assert HomePage.goToQuestionnaires().goToQuestionnairesPage().deleteAddedQuestions().addQues1().getTextFromSuccessPopup() == quesSuccessfulAdded_popup
        with check:
            assert HomePage.verifyAddedQues1()
        with check:
            assert HomePage.deleteAddedQuestions().verifyDeleteQues()
        with check:
            self.driver.refresh()
            assert HomePage.goToQuestionnaires().goToChartsPage().verifyDeletedQuesOnChartsPage()

    def test_editQuestionOnChartsPage(self):
        with check:
            HomePage = Questionnaires(self.driver)
            assert HomePage.goToQuestionnaires().goToQuestionnairesPage().deleteAddedQuestions().addQues1().getTextFromSuccessPopup() == quesSuccessfulAdded_popup
        with check:
            assert HomePage.verifyAddedQues1()
        with check:
            assert HomePage.editQues1().verifyUpdatedQues1()
        with check:
            assert HomePage.goToQuestionnaires().goToChartsPage().verifyEditedQuesOnChartsPage()
        HomePage.goToQuestionnaires().goToQuestionnairesPage().deleteAddedQuestions()

    def test_dateOnChartsPage(self):
        with check:
            HomePage = Questionnaires(self.driver)
            actualDate = HomePage.goToQuestionnaires().goToChartsPage().getDateOnChartsPage()
            today = datetime.now()
            expectedDate = today.strftime("%d %B, %Y")
            assert actualDate in expectedDate

    def test_editQuestionPopup(self):
        with check:
            HomePage = Questionnaires(self.driver)
            assert HomePage.goToQuestionnaires().goToQuestionnairesPage().deleteAddedQuestions().addQues1().getTextFromSuccessPopup() == quesSuccessfulAdded_popup
        with check:
            assert HomePage.verifyAddedQues1()
        with check:
            assert HomePage.verifyEditQuesPopup()
        self.driver.refresh()
        HomePage.goToQuestionnaires().goToQuestionnairesPage().deleteAddedQuestions()

    def test_editQuestion_X_Button(self):
        with check:
            HomePage = Questionnaires(self.driver)
            assert HomePage.goToQuestionnaires().goToQuestionnairesPage().deleteAddedQuestions().addQues1().getTextFromSuccessPopup() == quesSuccessfulAdded_popup
        with check:
            assert HomePage.verifyAddedQues1()
        with check:
            assert HomePage.verifyDelete_X_Icon()
        self.driver.refresh()
        HomePage.goToQuestionnaires().goToQuestionnairesPage().deleteAddedQuestions()

    def test_editQuestionPopup_EnableUpdateBtn(self):
        with check:
            HomePage = Questionnaires(self.driver)
            assert HomePage.goToQuestionnaires().goToQuestionnairesPage().deleteAddedQuestions().addQues1().getTextFromSuccessPopup() == quesSuccessfulAdded_popup
        with check:
            assert HomePage.verifyAddedQues1()
        with check:
            assert HomePage.verifyUpdateBtnAfterEdit()
        self.driver.refresh()
        HomePage.goToQuestionnaires().goToQuestionnairesPage().deleteAddedQuestions()




