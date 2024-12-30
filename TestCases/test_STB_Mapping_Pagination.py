import pytest
from Pages.STB_Mapping_Pagination import STB_Mapping_Pagination
from TestCases.BaseTest import BaseTest
from pytest_check import check

quesSuccessfulAdded_popup = "Questionnaire was successfully created"
quesSuccessfulUpdated_popup = "Question updated successfully"
validDetails_popup = "Please Enter Valid Values"
addOneStb = "Total Created STB 1, Total Rejected STB 0"
addEightStb = "Total Created STB 8, Total Rejected STB 0"
deviceLimitWarnMsg = "You can Insert 8 record at a time."
deleteStb_popup = "STB deleted successfully"
updateStb_popup = "STB Updated Successfully"
specialCharWarn = "Special Characters Are Not Allowed"
validValues = "Please Enter Values"
downloadRecordSuccessfulMsg = "Records downloaded successfully"

class Test_STB_Mapping_Pagination(BaseTest):

    @pytest.fixture(autouse=True)
    def test_refreshBrowser(self):
        self.driver.refresh()

    def test_bulkUpload_STB_Functionality(self):
        with check:
            HomePage = STB_Mapping_Pagination(self.driver)
            beforeStbCount = HomePage.goToSTB_Mapping().deleteAllStbFrom_AutomationGrp().getCurrantSTBCount_AutomationGrp()
            HomePage.bulkUpload_5Devices()
            # assert HomePage.getTextFromSuccessPopup() == "Uploaded Successfully"
        with check:
            afterStbCount = HomePage.getCurrantSTBCount_AutomationGrp()
            assert afterStbCount == beforeStbCount + 5
        HomePage.deleteAllStbFrom_AutomationGrp()

    def test_bulkUpload_25STBs(self):
        with check:
            HomePage = STB_Mapping_Pagination(self.driver)
            beforeStbCount = HomePage.goToSTB_Mapping().deleteAllStb().goToSTB_Mapping().deleteAllStb().getCurrantSTBCount()
            HomePage.bulkUpload_25Devices()
            # assert HomePage.getTextFromSuccessPopup() == "Uploaded Successfully"
        with check:
            assert HomePage.getRowCount() == 20
        with check:
            afterStbCount = HomePage.getCurrantSTBCount()
            assert afterStbCount == beforeStbCount + 25
        with check:
            assert HomePage.verifySerialNumbers1_20()
        with check:
            assert HomePage.clickOnNextArrow().verifySerialNumbers21_40()
        HomePage.goToSTB_Mapping().deleteAllStb().goToSTB_Mapping().deleteAllStb()

    def test_bulkUpload_NextPage(self):
        with check:
            HomePage = STB_Mapping_Pagination(self.driver)
            beforeStbCount = HomePage.goToSTB_Mapping().deleteAllStb().goToSTB_Mapping().deleteAllStb().getCurrantSTBCount()
            HomePage.bulkUpload_25Devices()
            # assert HomePage.getTextFromSuccessPopup() == "Uploaded Successfully"
        with check:
            assert HomePage.clickOnNextArrow().verifySerialNumbers21_40()
        with check:
            assert HomePage.verifyPage2()
        HomePage.goToSTB_Mapping().deleteAllStb().goToSTB_Mapping().deleteAllStb()

    def test_bulkUpload_PreviousPage(self):
        with check:
            HomePage = STB_Mapping_Pagination(self.driver)
            beforeStbCount = HomePage.goToSTB_Mapping().deleteAllStb().goToSTB_Mapping().deleteAllStb().getCurrantSTBCount()
            HomePage.bulkUpload_25Devices()
            # assert HomePage.getTextFromSuccessPopup() == "Uploaded Successfully"
        with check:
            assert HomePage.clickOnNextArrow().verifySerialNumbers21_40()
        with check:
            assert HomePage.verifyPage2()
        with check:
            assert HomePage.clickOnPreviousArrow().verifyPage1()
        HomePage.goToSTB_Mapping().deleteAllStb().goToSTB_Mapping().deleteAllStb()

    def test_bulkUpload_25STBs_WithGrpName(self):
        with check:
            HomePage = STB_Mapping_Pagination(self.driver)
            HomePage.goToSTB_Mapping().deleteAllStbFrom_AutomationGrp().goToSTB_Mapping().deleteAllStbFrom_AutomationGrp().goToSTB_Mapping().bulkUpload_25Devices_WithGrpName()
            # assert HomePage.getTextFromSuccessPopup() == "Uploaded Successfully"
        with check:
            assert HomePage.verifyAutomationTab()
        with check:
            assert HomePage.verifyAutomationGrpNames()
        HomePage.goToSTB_Mapping().deleteAllStbFrom_AutomationGrp().goToSTB_Mapping().deleteAllStbFrom_AutomationGrp()

    def test_bulkUpload_GroupTab(self):
        with check:
            HomePage = STB_Mapping_Pagination(self.driver)
            beforeCount = HomePage.goToSTB_Mapping().deleteAllStb().goToSTB_Mapping().deleteAllStb().goToSTB_Mapping().getCurrantSTBCount_AutomationGrp()
            HomePage.bulkUpload_25Devices_5DevicesFromAutomationGrp()
            # assert HomePage.getTextFromSuccessPopup() == "Uploaded Successfully"
        with check:
            assert HomePage.verifyAutomationTab()
        with check:
            assert HomePage.goToSTB_Mapping().getCurrantSTBCount_AutomationGrp() == beforeCount + 5
        HomePage.goToSTB_Mapping().deleteAllStb().goToSTB_Mapping().deleteAllStb()

    def test_bulkUpload_25STBs_VerifySerialNumbersSequence(self):
        with check:
            HomePage = STB_Mapping_Pagination(self.driver)
            HomePage.goToSTB_Mapping().deleteAllStb().goToSTB_Mapping().deleteAllStb().goToSTB_Mapping().bulkUpload_25Devices()
            # assert HomePage.getTextFromSuccessPopup() == "Uploaded Successfully"
        with check:
            assert HomePage.verifySerialNumbers1_20()
        with check:
            assert HomePage.clickOnNextArrow().verifySerialNumbers21_40()
        HomePage.goToSTB_Mapping().deleteAllStb().goToSTB_Mapping().deleteAllStb()

    def test_bulkUpload_25STBs_UserCount(self):
        with check:
            HomePage = STB_Mapping_Pagination(self.driver)
            beforeStbCount = HomePage.goToSTB_Mapping().deleteAllStb().goToSTB_Mapping().deleteAllStb().getCurrantSTBCount()
            HomePage.bulkUpload_25Devices()
            # assert HomePage.getTextFromSuccessPopup() == "Uploaded Successfully"
        with check:
            afterStbCount = HomePage.getCurrantSTBCount()
            assert afterStbCount == beforeStbCount + 25
        HomePage.goToSTB_Mapping().deleteAllStb().goToSTB_Mapping().deleteAllStb()

    def test_addStbDevices_sequence(self):
        with check:
            HomePage = STB_Mapping_Pagination(self.driver)
            beforeStbCount = HomePage.goToSTB_Mapping().deleteAllStb().goToSTB_Mapping().createGroup().goToSTB_Mapping().getCurrantSTBCount()
            assert HomePage.createSTB_Manually_8devices_sequence().getTextFromSuccessPopup() == addEightStb
        with check:
            afterStbCount = HomePage.getCurrantSTBCount()
            assert afterStbCount == beforeStbCount + 8
        with check:
            assert HomePage.verifySequenceOf8devices()
        HomePage.goToSTB_Mapping().deleteAllStb().deleteGroup()

    def test_addStbDevices_sequence_withDelete(self):
        with check:
            HomePage = STB_Mapping_Pagination(self.driver)
            beforeStbCount = HomePage.goToSTB_Mapping().deleteAllStb().goToSTB_Mapping().createGroup().goToSTB_Mapping().getCurrantSTBCount()
            assert HomePage.createSTB_Manually_8devices_sequence().getTextFromSuccessPopup() == addEightStb
        with check:
            afterStbCount = HomePage.getCurrantSTBCount()
            assert afterStbCount == beforeStbCount + 8
        with check:
            assert HomePage.verifySequenceOf8devices()
        with check:
            assert HomePage.verifySequenceOf7devices_afterDelete()
        with check:
            countAfterDelete = HomePage.getCurrantSTBCount()
            assert countAfterDelete == afterStbCount - 1
        HomePage.goToSTB_Mapping().deleteAllStb().deleteGroup()

    def test_downloadRecordWindow(self):
        with check:
            HomePage = STB_Mapping_Pagination(self.driver)
            assert HomePage.goToSTB_Mapping().createGroup().goToSTB_Mapping().createSTB_Manually().getTextFromSuccessPopup() == addOneStb
        with check:
            assert HomePage.verifyAddedStb_roomNum()
        with check:
            assert HomePage.ClickOnDownloadRecords().verifyDownloadRecordsPopup()
        self.driver.refresh()
        HomePage.deleteAllStb().deleteGroup()

    def test_downloadRecord_AllChecked(self):
        with check:
            HomePage = STB_Mapping_Pagination(self.driver)
            assert HomePage.goToSTB_Mapping().ClickOnDownloadRecords().clickOnAllCheckBox().verifyAllCheckBoxAreChecked() == "True"
        self.driver.refresh()

    def test_downloadRecord_ResetBtn(self):
        with check:
            HomePage = STB_Mapping_Pagination(self.driver)
            assert HomePage.goToSTB_Mapping().ClickOnDownloadRecords().clickOnAllCheckBox().verifyAllCheckBoxAreChecked() == "True"
        with check:
            assert HomePage.clickOnResetBtn().verifyAllCheckBoxAreUnchecked() == "True"
        self.driver.refresh()

    def test_downloadRecord_IsRefreshed(self):
        with check:
            HomePage = STB_Mapping_Pagination(self.driver)
            assert HomePage.goToSTB_Mapping().createGroup().goToSTB_Mapping().createSTB_Manually().getTextFromSuccessPopup() == addOneStb
        with check:
            assert HomePage.verifyAddedStb_roomNum()
        with check:
            assert HomePage.ClickOnDownloadRecords().verifyDownloadRecordsPopup()
        with check:
            assert HomePage.clickOnAllCheckBox().clickOnXBtn().ClickOnDownloadRecords_only().verifyAllCheckBoxAreUnchecked() == "True"
        self.driver.refresh()
        HomePage.deleteAllStb().deleteGroup()

    def test_downloadRecord_AllUnchecked(self):
        with check:
            HomePage = STB_Mapping_Pagination(self.driver)
            assert HomePage.goToSTB_Mapping().ClickOnDownloadRecords().clickOnAllCheckBox().verifyAllCheckBoxAreChecked() == "True"
        with check:
            assert HomePage.clickOnAllCheckBox().verifyAllCheckBoxAreUnchecked() == "True"
        self.driver.refresh()

    def test_searchBar(self):
        with check:
            HomePage = STB_Mapping_Pagination(self.driver)
            assert HomePage.goToSTB_Mapping().createGroup().goToSTB_Mapping().createSTB_Manually().verifyAddedStb_roomNum()
        with check:
            assert HomePage.verifySearchAddedDevice()
        with check:
            assert HomePage.verifySearch_DummySearch()
        HomePage.deleteStb().deleteGroup()

    def test_search_RemoveSearch(self):
        with check:
            HomePage = STB_Mapping_Pagination(self.driver)
            assert HomePage.goToSTB_Mapping().createGroup().goToSTB_Mapping().createSTB_Manually().verifyAddedStb_roomNum()
        with check:
            assert HomePage.verifySearchAddedDevice_DeleteText()
        HomePage.deleteStb().deleteGroup()

    def test_editStb_AllDataVisible(self):
        with check:
            HomePage = STB_Mapping_Pagination(self.driver)
            assert HomePage.goToSTB_Mapping().createGroup().goToSTB_Mapping().createSTB_Manually().getTextFromSuccessPopup() in addOneStb
        with check:
            assert HomePage.verifyAddedStb_roomNum()
        with check:
            assert HomePage.clickOnEditStbBtn().verifyEditStb_updateBtnDisabled()
        with check:
            assert HomePage.verifyEditStbPopup()
        with check:
            assert HomePage.verifyEditRoomNum()
        with check:
            assert HomePage.verifyEditSerialNum()
        self.driver.refresh()
        HomePage.goToSTB_Mapping().deleteAllStb().deleteGroup()

    def test_editStb_AllInformation(self):
        with check:
            HomePage = STB_Mapping_Pagination(self.driver)
            assert HomePage.goToSTB_Mapping().createGroup().goToSTB_Mapping().createSTB_Manually().getTextFromSuccessPopup() in addOneStb
        with check:
            assert HomePage.verifyAddedStb_roomNum()
        with check:
            assert HomePage.verifyEditRoomSerialNum().getTextFromSuccessPopup() in updateStb_popup
        with check:
            assert HomePage.verifyEditedStb_roomNum()
        with check:
            assert HomePage.verifyEditedStb_serialNum()
        self.driver.refresh()
        HomePage.goToSTB_Mapping().deleteAllStb().deleteGroup()
