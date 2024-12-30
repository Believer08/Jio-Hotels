import time
import pytest
from datetime import datetime
from Pages.IAU_SelectFeatureAccess import IAU_SelectFeatureAccess
from TestCases.BaseTest import BaseTest
from pytest_check import check

userAddedSuccessfully_popup = "User invited successfully"
userEditedSuccessfully_popup = "User detail added successfully"
userDeletedSuccessfully_popup = "User Deleted Successfully"
splCharWarnMsg = "special characters are not allowed"
invalidMobileNum = "Invalid Mobile Number"
invalidEmail = "Invalid Email Address"
enterValuesWarnMsg = "Please Enter Values"
enterUserTypeWarnMsg = "Please Select User Type"
enterFeatureAccessWarnMsg = "Please select Feature Access"
userAlreadyExistWarnMsg = "User already exists"


class Test_STB_Mapping(BaseTest):

    @pytest.fixture(autouse=True)
    def test_refreshBrowser(self):
        self.driver.refresh()

    def test_InviteUser_SFA_Window(self):
        with check:
            HomePage = IAU_SelectFeatureAccess(self.driver)
            HomePage.goTo_InviteUser_SFA().clickOnInviteUser().verifyInviteUserWindow()
        with check:
            HomePage.verifyDataOnIUWindow()
        with check:
            HomePage.verifyDisabledResetBtn()
        self.driver.refresh()

    def test_InviteUser_SFA_SelectUserDD(self):
        with check:
            HomePage = IAU_SelectFeatureAccess(self.driver)
            assert HomePage.goTo_InviteUser_SFA().clickOnInviteUser().verifySelectUserDDElements() == "true"
        self.driver.refresh()

    def test_selectFeatureAccessIsVisible(self):
        with check:
            HomePage = IAU_SelectFeatureAccess(self.driver)
            assert HomePage.goTo_InviteUser_SFA().createUser_PropertyAdmin_withoutAdd().verifySelectFeatureAccessDD()
        self.driver.refresh()

    def test_selectFeatureAccessDD(self):
        with check:
            HomePage = IAU_SelectFeatureAccess(self.driver)
            assert HomePage.goTo_InviteUser_SFA().createUser_PropertyAdmin_withoutAdd().verifySelectFeatureAccessDD()
        with check:
            assert HomePage.verifySelectFeatureAccessDDElements() == "true"
        self.driver.refresh()

    def test_selectFeatureAccess_NameWith_XIcon(self):
        with check:
            HomePage = IAU_SelectFeatureAccess(self.driver)
            assert HomePage.goTo_InviteUser_SFA().createUser_PropertyAdmin_STBMapping_withoutAdd().verifySTBMappingTextWith_XBtn()
        self.driver.refresh()

    def test_selectFeatureAccess_ClickOnXIcon_StbMapping(self):
        with check:
            HomePage = IAU_SelectFeatureAccess(self.driver)
            assert HomePage.goTo_InviteUser_SFA().createUser_PropertyAdmin_STBMapping_withoutAdd().clickOnStbMapping_X_Btn().verifySTBMappingTextWith_XBtn_NotThere()
        self.driver.refresh()

    def test_InviteUser_SFA_ResetBtn(self):
        with check:
            HomePage = IAU_SelectFeatureAccess(self.driver)
            assert HomePage.goTo_InviteUser_SFA().createUser_PropertyAdmin_STBMapping_withoutAdd().clickOnResetBtn().valueOfUserNameTB() == ""
        with check:
            assert HomePage.valueOfEmailTB() == ""
        with check:
            assert HomePage.valueOfMobileNumTB() == ""
        with check:
            assert HomePage.valueOfUserTypeDD() == "Select User Type"
        with check:
            assert HomePage.verifySelectFeatureAccessDD()
        self.driver.refresh()

    def test_InviteUser_SFA_EditUserWindow(self):
        with check:
            HomePage = IAU_SelectFeatureAccess(self.driver)
            assert HomePage.goTo_InviteUser_SFA().createUser_Admin().getTextFromSuccessPopup() == userAddedSuccessfully_popup
        with check:
            assert HomePage.clickOnEditBtnOfCreatedUser().verifyEditUserPopupIsDisplayed()
        with check:
            assert HomePage.verifyEditIUWindow()
        self.driver.refresh()
        HomePage.deleteAutoCreatedUser()

    def test_InviteUser_SFA_EditUserWindow_WithCorrectData(self):
        with check:
            HomePage = IAU_SelectFeatureAccess(self.driver)
            assert HomePage.goTo_InviteUser_SFA().createUser_Admin().getTextFromSuccessPopup() == userAddedSuccessfully_popup
        with check:
            assert HomePage.clickOnEditBtnOfCreatedUser().verifyEditUserPopupIsDisplayed()
        with check:
            assert HomePage.verifyUserNameOnEditUserWindow()
        with check:
            assert HomePage.verifyMobileNumOnEditUserWindow()
        with check:
            assert HomePage.verifyUserTypeOnEditUserWindow()
        self.driver.refresh()
        HomePage.deleteAutoCreatedUser()

    def test_InviteUser_SFA_EditUser(self):
        with check:
            HomePage = IAU_SelectFeatureAccess(self.driver)
            assert HomePage.goTo_InviteUser_SFA().createUser_Admin().getTextFromSuccessPopup() == userAddedSuccessfully_popup
        with check:
            assert HomePage.editUserNameOfCreatedUser().verifyTextFromSuccessPopupIfUpdateBtnIsEnabled()
        with check:
            assert HomePage.verifyEditedUserNameInSummary()
        self.driver.refresh()
        HomePage.deleteAutoCreatedUser()

    def test_InviteUser_SFA_X_Btn(self):
        with check:
            HomePage = IAU_SelectFeatureAccess(self.driver)
            assert HomePage.goTo_InviteUser_SFA().createUser_Admin_X_Btn().verifyInviteUserPopup_NotTheir()
        with check:
            assert HomePage.verifyUserNameInSummary_NotTheir()
        self.driver.refresh()

    def test_DeleteUser_CancelBtn(self):
        with check:
            HomePage = IAU_SelectFeatureAccess(self.driver)
            assert HomePage.goTo_InviteUser_SFA().createUser_Admin().getTextFromSuccessPopup() == userAddedSuccessfully_popup
        with check:
            assert HomePage.deleteCreatedUser_CancelBtn().verifyDeleteUserPopupInNotTheir()
        with check:
            assert HomePage.verifyUserNameInSummary()
        self.driver.refresh()
        HomePage.deleteAutoCreatedUser()

    def test_DeleteUser(self):
        with check:
            HomePage = IAU_SelectFeatureAccess(self.driver)
            assert HomePage.goTo_InviteUser_SFA().createUser_Admin().getTextFromSuccessPopup() == userAddedSuccessfully_popup
        with check:
            assert HomePage.deleteCreatedUser().getTextFromSuccessPopup() == userDeletedSuccessfully_popup
        with check:
            assert HomePage.verifyUserNameInSummary_NotTheir()

    def test_InviteUser_UserNameSplChar(self):
        with check:
            HomePage = IAU_SelectFeatureAccess(self.driver)
            assert HomePage.goTo_InviteUser_SFA().clickOnInviteUser().enterUserName_SplChar().getTextFromWarningPopup() == splCharWarnMsg
        with check:
            assert HomePage.valueOfUserNameTB() == ""
        self.driver.refresh()

    def test_InviteUser_MobileNumberSplCharAlphabets(self):
        with check:
            HomePage = IAU_SelectFeatureAccess(self.driver)
            assert HomePage.goTo_InviteUser_SFA().clickOnInviteUser().enterMobileNum_SplChar().getTextFromWarningPopup() == invalidMobileNum
        with check:
            assert HomePage.valueOfMobileNumTB() == ""
        with check:
            assert HomePage.enterMobileNum_Alphabets().getTextFromWarningPopup() == invalidMobileNum
        with check:
            assert HomePage.valueOfMobileNumTB() == ""
        self.driver.refresh()

    def test_InviteUser_AddBtnWithoutValues(self):
        with check:
            HomePage = IAU_SelectFeatureAccess(self.driver)
            assert HomePage.goTo_InviteUser_SFA().clickOnInviteUser().clickOnAddBtn().getTextFromWarningPopup() in enterValuesWarnMsg
        self.driver.refresh()

    def test_InviteUser_WithoutUserType(self):
        with check:
            HomePage = IAU_SelectFeatureAccess(self.driver)
            assert HomePage.goTo_InviteUser_SFA().createUser_Admin_WithoutUserType().getTextFromWarningPopup() in enterUserTypeWarnMsg
        self.driver.refresh()

    def test_InviteUser_WithoutSelectFeature(self):
        with check:
            HomePage = IAU_SelectFeatureAccess(self.driver)
            assert HomePage.goTo_InviteUser_SFA().createUser_PropertyAdmin_WithoutSelectFeatureAccess().getTextFromWarningPopup() in enterFeatureAccessWarnMsg
        self.driver.refresh()

    def test_SearchBar(self):
        with check:
            HomePage = IAU_SelectFeatureAccess(self.driver)
            assert HomePage.goTo_InviteUser_SFA().createUser_Admin().getTextFromSuccessPopup() == userAddedSuccessfully_popup
        with check:
            assert HomePage.searchCreatedUser().verifyUserNameInSummary()
        with check:
            assert HomePage.verifyOneRow()
        self.driver.refresh()
        HomePage.deleteAutoCreatedUser()

    def test_UserCountIncreaseDecrease(self):
        with check:
            HomePage = IAU_SelectFeatureAccess(self.driver)
            defaultUserCount = HomePage.goTo_InviteUser_SFA().getCurrantUserCount()
            assert HomePage.createUser_Admin().getTextFromSuccessPopup() == userAddedSuccessfully_popup
        with check:
            assert HomePage.getCurrantUserCount() == defaultUserCount + 1
        with check:
            assert HomePage.deleteCreatedUser().getCurrantUserCount() == defaultUserCount
        self.driver.refresh()

    def test_SerialNumSequence(self):
        with check:
            HomePage = IAU_SelectFeatureAccess(self.driver)
            assert HomePage.goTo_InviteUser_SFA().createUser_Admin().getTextFromSuccessPopup() == userAddedSuccessfully_popup
        with check:
            assert HomePage.verifySequenceIsAscending_SerialNum()
        with check:
            assert HomePage.deleteCreatedUser().verifySequenceIsAscending_SerialNum()
        self.driver.refresh()

    def test_InviteUser_5Users(self):
        with check:
            HomePage = IAU_SelectFeatureAccess(self.driver)
            defaultUserCount = HomePage.goTo_InviteUser_SFA().getCurrantUserCount()
            assert HomePage.verifyCreate5Users_Admin() == 5
        with check:
            assert HomePage.getCurrantUserCount() == defaultUserCount + 5
        self.driver.refresh()
        HomePage.deleteAutoCreatedUser()

    def test_InviteUser_IsRefreshedAfterReopen(self):
        with check:
            HomePage = IAU_SelectFeatureAccess(self.driver)
            assert HomePage.goTo_InviteUser_SFA().createUser_Admin_X_Btn().verifyInviteUserPopup_NotTheir()
        with check:
            assert HomePage.clickOnInviteUser().valueOfUserNameTB() == ""
        with check:
            assert HomePage.valueOfEmailTB() == ""
        with check:
            assert HomePage.valueOfMobileNumTB() == ""
        with check:
            assert HomePage.valueOfUserTypeDD() == "Select User Type"
        with check:
            assert HomePage.verifySelectFeatureAccessDD()
        self.driver.refresh()

    def test_InviteUser_existingEmail(self):
        with check:
            HomePage = IAU_SelectFeatureAccess(self.driver)
            assert HomePage.goTo_InviteUser_SFA().createUser_Admin().getTextFromSuccessPopup() == userAddedSuccessfully_popup
        with check:
            assert HomePage.createUser_Admin_existingEmail().getTextFromWarningPopup() == userAlreadyExistWarnMsg
        self.driver.refresh()
        HomePage.deleteAutoCreatedUser()

    def test_InviteUser_UserTypeInUserSummary(self):
        with check:
            HomePage = IAU_SelectFeatureAccess(self.driver)
            assert HomePage.goTo_InviteUser_SFA().createUser_PropertyAdmin().getTextFromSuccessPopup() == userAddedSuccessfully_popup
        with check:
            assert HomePage.verifyAddedUserRole_PropertyAdmin()
        self.driver.refresh()
        HomePage.deleteAutoCreatedUser()

    def test_InviteUser_InvalidMobileNum_9digit(self):
        with check:
            HomePage = IAU_SelectFeatureAccess(self.driver)
            assert HomePage.goTo_InviteUser_SFA().createUser_Admin_InvalidMobileNum().getTextFromWarningPopup() == invalidMobileNum
        self.driver.refresh()

    def test_InviteUser_UserNameMaxLength(self):
        with check:
            HomePage = IAU_SelectFeatureAccess(self.driver)
            assert HomePage.goTo_InviteUser_SFA().clickOnInviteUser().userName_MaxLength() == "20"
        with check:
            HomePage.enterUserName_50Char().verify20CharEntered()
        self.driver.refresh()

    def test_IAU_SelectFeatureAccessPage(self):
        with check:
            HomePage = IAU_SelectFeatureAccess(self.driver)
            actualDate = HomePage.goTo_InviteUser_SFA().clickOnInviteUser().dateOnIAU_SelectFeatureAccessPage()
            today = datetime.now()
            expectedDate = today.strftime("%d %B, %Y")
            assert actualDate == expectedDate

    def test_InviteUser_InvalidEmail_SplChar(self):
        with check:
            HomePage = IAU_SelectFeatureAccess(self.driver)
            assert HomePage.goTo_InviteUser_SFA().createUser_Admin_InvalidMail_SplChar().getTextFromWarningPopup() == invalidEmail
        self.driver.refresh()

    def test_InviteUser_InvalidEmail(self):
        with check:
            HomePage = IAU_SelectFeatureAccess(self.driver)
            assert HomePage.goTo_InviteUser_SFA().createUser_Admin_InvalidMail().getTextFromWarningPopup() == invalidEmail
        self.driver.refresh()

    def test_InviteUser_InvalidEmail_2EmailIDs(self):
        with check:
            HomePage = IAU_SelectFeatureAccess(self.driver)
            assert HomePage.goTo_InviteUser_SFA().createUser_Admin_InvalidMail_2EmailIDs().getTextFromWarningPopup() == invalidEmail
        self.driver.refresh()