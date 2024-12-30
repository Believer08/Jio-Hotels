import time
import pytest
from datetime import datetime

from Pages.GuestServices import GuestServices
from TestCases.BaseTest import BaseTest
from pytest_check import check

quesSuccessfulAdded_popup = "Questionnaire was successfully created"
quesSuccessfulUpdated_popup = "Question updated successfully"
addOneStb = "Total Created STB 1, Total Rejected STB 0"
fillGuestName = "Please Fill the Guest Name"
splCharWarnMsg = "Special Characters Are Not Allowed."
guestAdded = "Guest data updated successfully"
checkoutGuest = "Guest has been checkout"

class Test_GuestServices(BaseTest):

    @pytest.fixture(autouse=True)
    def test_refreshBrowser(self):
        self.driver.refresh()

    def test_GuestServicesDD(self):
        with check:
            HomePage = GuestServices(self.driver)
            assert HomePage.clickOnGuestServicesDD().verifyGuestServicesDD() == "true"

    def test_GuestAdministrationPage_withCreatedSTB(self):
        with check:
            HomePage = GuestServices(self.driver)
            assert HomePage.createSTB().getTextFromSuccessPopup() == addOneStb
        with check:
            assert HomePage.goToGuestAdministration().verifyGuestAdTitle()
        with check:
            assert HomePage.verifyCreatedSTBSerialNumOnGuestAdPage()
        with check:
            assert HomePage.verifyEditBtnForCreatedSTBOnGuestAdPage()
        HomePage.goToSTB_Mapping().deleteAllStb().deleteGroup()

    def test_AddGuestName(self):
        with check:
            HomePage = GuestServices(self.driver)
            assert HomePage.createSTB().getTextFromSuccessPopup() == addOneStb
        with check:
            self.driver.refresh()
            time.sleep(0.6)
            assert HomePage.goToGuestAdministration().AddGuestNameToCreatedSTB().getTextFromSuccessPopup() == guestAdded
        with check:
            assert HomePage.verifyAddedGuestName()
        HomePage.goToSTB_Mapping().deleteAllStb().deleteGroup()

    def test_AddGuestName_withOutGuestName(self):
        with check:
            HomePage = GuestServices(self.driver)
            assert HomePage.createSTB().getTextFromSuccessPopup() == addOneStb
        with check:
            self.driver.refresh()
            assert HomePage.goToGuestAdministration().clickOnSaveBtn().getTextFromWarningPopup() == fillGuestName
        self.driver.refresh()
        HomePage.goToSTB_Mapping().deleteAllStb().deleteGroup()

    def test_AddGuestName_SplChar(self):
        with check:
            HomePage = GuestServices(self.driver)
            assert HomePage.createSTB().getTextFromSuccessPopup() == addOneStb
        with check:
            self.driver.refresh()
            assert HomePage.goToGuestAdministration().AddGuestNameToCreatedSTB_SplChar().getTextFromWarningPopup() == splCharWarnMsg
        with check:
            assert HomePage.verifyGuestNameTB_IsEmpty()
        self.driver.refresh()
        HomePage.goToSTB_Mapping().deleteAllStb().deleteGroup()

    def test_EditGuestName(self):
        with check:
            HomePage = GuestServices(self.driver)
            assert HomePage.createSTB().getTextFromSuccessPopup() == addOneStb
        with check:
            self.driver.refresh()
            assert HomePage.goToGuestAdministration().AddGuestNameToCreatedSTB().getTextFromSuccessPopup() == guestAdded
        with check:
            assert HomePage.verifyAddedGuestName()
        with check:
            assert HomePage.EditGuestNameToCreatedSTB().getTextFromSuccessPopup() == guestAdded
        with check:
            assert HomePage.verifyEditedGuestName()
        HomePage.goToSTB_Mapping().deleteAllStb().deleteGroup()

    def test_CheckOutGuest(self):
        with check:
            HomePage = GuestServices(self.driver)
            assert HomePage.createSTB().getTextFromSuccessPopup() == addOneStb
        with check:
            self.driver.refresh()
            assert HomePage.goToGuestAdministration().AddGuestNameToCreatedSTB().getTextFromSuccessPopup() == guestAdded
        with check:
            assert HomePage.checkOutCreatedGuest().getTextFromSuccessPopup() == checkoutGuest
        HomePage.goToSTB_Mapping().deleteAllStb().deleteGroup()

    def test_CheckOutGuest_CancelBtn(self):
        with check:
            HomePage = GuestServices(self.driver)
            assert HomePage.createSTB().getTextFromSuccessPopup() == addOneStb
        with check:
            self.driver.refresh()
            assert HomePage.goToGuestAdministration().AddGuestNameToCreatedSTB().getTextFromSuccessPopup() == guestAdded
        with check:
            assert HomePage.checkOutCreatedGuest_CancelBtn().verifyCheckoutPopupWindowNotTheir()
        with check:
            assert HomePage.verifyAddedGuestName()
        HomePage.goToSTB_Mapping().deleteAllStb().deleteGroup()

    def test_CheckOutGuest_X_Btn(self):
        with check:
            HomePage = GuestServices(self.driver)
            assert HomePage.createSTB().getTextFromSuccessPopup() == addOneStb
        with check:
            self.driver.refresh()
            assert HomePage.goToGuestAdministration().AddGuestNameToCreatedSTB().getTextFromSuccessPopup() == guestAdded
        with check:
            assert HomePage.checkOutCreatedGuest_X_Btn().verifyCheckoutPopupWindowNotTheir()
        with check:
            assert HomePage.verifyAddedGuestName()
        HomePage.goToSTB_Mapping().deleteAllStb().deleteGroup()

    def test_guestAdd_SearchBar(self):
        with check:
            HomePage = GuestServices(self.driver)
            assert HomePage.createSTB().getTextFromSuccessPopup() == addOneStb
        with check:
            self.driver.refresh()
            assert HomePage.goToGuestAdministration().AddGuestNameToCreatedSTB().getTextFromSuccessPopup() == guestAdded
        with check:
            assert HomePage.searchAddedGuest_SerialNum().verifyAddedGuestName()
        with check:
            self.driver.refresh()
            assert HomePage.searchAddedGuest_RoomNum().verifyAddedGuestName()
        with check:
            self.driver.refresh()
            assert HomePage.searchAddedGuest_GuestName().verifyAddedGuestName()
        HomePage.goToSTB_Mapping().deleteAllStb().deleteAllGroups()

    def test_guestAdd_SearchBar_withRemoveText(self):
        with check:
            HomePage = GuestServices(self.driver)
            assert HomePage.createSTB().getTextFromSuccessPopup() == addOneStb
        with check:
            self.driver.refresh()
            assert HomePage.goToGuestAdministration().AddGuestNameToCreatedSTB().getTextFromSuccessPopup() == guestAdded
        with check:
            assert HomePage.searchAddedGuest_SerialNum().verifyAddedGuestName()
        with check:
            self.driver.refresh()
            assert HomePage.searchAddedGuest_randomText().verifyAddedGuestName_NotTheir()
        with check:
            self.driver.refresh()
            assert HomePage.searchAddedGuest_ClearText().verifyAddedGuestName()
        HomePage.goToSTB_Mapping().deleteAllStb().deleteAllGroups()

    def test_guestAdd_SearchBar_NoData(self):
        with check:
            HomePage = GuestServices(self.driver)
            assert HomePage.createSTB().getTextFromSuccessPopup() == addOneStb
        with check:
            self.driver.refresh()
            assert HomePage.goToGuestAdministration().AddGuestNameToCreatedSTB().getTextFromSuccessPopup() == guestAdded
        with check:
            self.driver.refresh()
            assert HomePage.searchAddedGuest_randomText().verifyNoDataText()
        HomePage.goToSTB_Mapping().deleteAllStb().deleteAllGroups()



