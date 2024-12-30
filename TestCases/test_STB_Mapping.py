import time
import pytest
from datetime import datetime
from selenium.webdriver.common.by import By

from Pages.STB_Mapping import STB_Mapping
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


class Test_STB_Mapping(BaseTest):

    @pytest.fixture(autouse=True)
    def test_refreshBrowser(self):
        self.driver.refresh()

    def test_STB_MappingPage(self):
        with check:
            HomePage = STB_Mapping(self.driver)
            assert HomePage.goToSTB_Mapping().verifySTB_MappingPageTitle()
        with check:
            assert HomePage.goToSTB_Mapping().verifySTB_MappingPageTable()

    def test_bulkUpload_STB(self):
        with check:
            HomePage = STB_Mapping(self.driver)
            beforeStbCount = HomePage.goToSTB_Mapping().deleteAllStbFrom_AutomationGrp().getCurrantSTBCount_AutomationGrp()
            HomePage.bulkUpload_5Devices()
            # assert HomePage.getTextFromSuccessPopup() == "Uploaded Successfully"
        with check:
            afterStbCount = HomePage.getCurrantSTBCount_AutomationGrp()
            assert afterStbCount == beforeStbCount + 5
        HomePage.deleteAllStbFrom_AutomationGrp()

    def test_bulkUpload_STB_SerialNumberMissing(self):
        with check:
            HomePage = STB_Mapping(self.driver)
            beforeStbCount = HomePage.goToSTB_Mapping().deleteAllStbFrom_AutomationGrp().getCurrantSTBCount_AutomationGrp()
            HomePage.bulkUpload_SerialNumMissing()
            assert HomePage.verifyRejectedCount()
        with check:
            afterStbCount = HomePage.getCurrantSTBCount_AutomationGrp()
            assert afterStbCount == beforeStbCount

    def test_bulkUpload_STB_WithSerialNumRoomNumOnly(self):
        with check:
            HomePage = STB_Mapping(self.driver)
            beforeStbCount = HomePage.goToSTB_Mapping().deleteAllStb().getCurrantSTBCount()
            HomePage.bulkUpload_withSerialNumRoomNumOnly()
            # assert HomePage.getTextFromSuccessPopup() == "Uploaded Successfully"
        with check:
            afterStbCount = HomePage.getCurrantSTBCount()
            assert afterStbCount == beforeStbCount + 1
        HomePage.deleteAllStb()

    def test_bulkUpload_STB_DuplicateSerialNumber(self):
        with check:
            HomePage = STB_Mapping(self.driver)
            beforeStbCount = HomePage.goToSTB_Mapping().deleteAllStb().createSTB_Manually_User().getCurrantSTBCount()
            HomePage.bulkUpload_DuplicateSerialNum()
            assert HomePage.verifyRejectedCount()
        with check:
            afterStbCount = HomePage.getCurrantSTBCount()
            assert afterStbCount == beforeStbCount
        HomePage.deleteAllStb()

    def test_bulkUpload_STB_DuplicateSerialNumber_SameCsvFile(self):
        with check:
            HomePage = STB_Mapping(self.driver)
            beforeStbCount = HomePage.goToSTB_Mapping().deleteAllStb().getCurrantSTBCount()
            HomePage.bulkUpload_DuplicateSerialNum()
            afterStbCount = HomePage.getCurrantSTBCount()
            assert afterStbCount == beforeStbCount + 1
        with check:
            beforeStbCount = HomePage.getCurrantSTBCount()
            HomePage.bulkUpload_DuplicateSerialNum()
            assert HomePage.verifyRejectedCount()
        with check:
            afterStbCount = HomePage.getCurrantSTBCount()
            assert afterStbCount == beforeStbCount
        HomePage.deleteAllStb()

    def test_addRooms_ManualMapping(self):
        with check:
            HomePage = STB_Mapping(self.driver)
            assert HomePage.goToSTB_Mapping().verifyManualMappingPage()
        with check:
            assert HomePage.verifyAddRoomsPopup()

    def test_addRooms_SaveBtnWithoutDetails(self):
        with check:
            HomePage = STB_Mapping(self.driver)
            assert HomePage.goToSTB_Mapping().verifyManualMappingPage()
        with check:
            assert HomePage.verifyAddRoomsPopup()
        with check:
            assert HomePage.clickOnSaveBtn().getTextFromWarningPopup() == validDetails_popup

    def test_addRooms_SaveBtnWithRoomNumDetails(self):
        with check:
            HomePage = STB_Mapping(self.driver)
            assert HomePage.goToSTB_Mapping().verifySaveBtnWithRoomNumDetails().getTextFromWarningPopup() == validDetails_popup

    def test_addStb(self):
        with check:
            HomePage = STB_Mapping(self.driver)
            assert HomePage.goToSTB_Mapping().createGroup().goToSTB_Mapping().createSTB_Manually().getTextFromSuccessPopup() == addOneStb
        with check:
            assert HomePage.verifyAddedStb_roomNum()
        with check:
            assert HomePage.verifyAddedStb_serialNum()
        with check:
            assert HomePage.verifyAddedStb_grpName()
        HomePage.deleteStb().deleteGroup()

    def test_addStb_duplicateStb(self):
        with check:
            HomePage = STB_Mapping(self.driver)
            assert HomePage.goToSTB_Mapping().createGroup().goToSTB_Mapping().createSTB_Manually().getTextFromSuccessPopup() == addOneStb
        with check:
            assert HomePage.createSTB_Manually_duplicate().verifyWarnPopup_duplicateSerialNum()
        HomePage.deleteStb().deleteGroup()

    def test_addStb_SerialNumSequence(self):
        with check:
            HomePage = STB_Mapping(self.driver)
            assert HomePage.goToSTB_Mapping().createGroup().goToSTB_Mapping().createSTB_Manually_5devices_withoutSave().verifySequence5()
        self.driver.refresh()
        HomePage.deleteGroup()

    def test_addStb_SerialNumSequence_withDelete(self):
        with check:
            HomePage = STB_Mapping(self.driver)
            assert HomePage.goToSTB_Mapping().createGroup().goToSTB_Mapping().createSTB_Manually_5devices_withoutSave().delete2_3_STB().verifySequenceAfterDelete2_3()
        self.driver.refresh()
        HomePage.deleteGroup()

    def test_addStb_ResetBtn(self):
        with check:
            HomePage = STB_Mapping(self.driver)
            assert not HomePage.goToSTB_Mapping().createGroup().goToSTB_Mapping().createSTB_ResetBtn().verifyRoomNumTextbox()
        with check:
            assert not HomePage.verifySerialNumTextbox()
        with check:
            assert not HomePage.verifyGroupName()
        self.driver.refresh()
        HomePage.deleteGroup()

    def test_addStb_duplicateRoomNum(self):
        with check:
            HomePage = STB_Mapping(self.driver)
            assert HomePage.goToSTB_Mapping().createGroup().goToSTB_Mapping().createSTB_Manually().getTextFromSuccessPopup() == addOneStb
        with check:
            assert HomePage.createSTB_Manually_duplicate().verifyWarnPopup_duplicateSerialNum()
        with check:
            assert HomePage.createSTB_Manually_duplicateRoomNum().getTextFromSuccessPopup() == addOneStb
        HomePage.deleteAllStb().deleteGroup()

    def test_addStb_duplicateSerialNum(self):
        with check:
            HomePage = STB_Mapping(self.driver)
            assert HomePage.goToSTB_Mapping().createGroup().goToSTB_Mapping().createSTB_Manually().getTextFromSuccessPopup() == addOneStb
        with check:
            assert HomePage.createSTB_Manually_duplicate().verifyWarnPopup_duplicateSerialNum()
        HomePage.deleteStb().deleteGroup()

    def test_addStb_AlphabetInRoomNum(self):
        with check:
            HomePage = STB_Mapping(self.driver)
            assert HomePage.goToSTB_Mapping().createGroup().goToSTB_Mapping().createSTB_Manually_AlphabetRoomNum().getTextFromSuccessPopup() == addOneStb
        HomePage.deleteStb().deleteGroup()

    def test_addStb_NotMoreThan8(self):
        with check:
            HomePage = STB_Mapping(self.driver)
            assert HomePage.goToSTB_Mapping().createGroup().goToSTB_Mapping().createSTB_Manually_8devices_withoutSave() == deviceLimitWarnMsg
        with check:
            assert HomePage.clickOnSaveBtn().getTextFromSuccessPopup() == addEightStb
        HomePage.deleteAllStb().deleteGroup()

    def test_addStb_AutoRefreshedAfterSaveBtn(self):
        with check:
            HomePage = STB_Mapping(self.driver)
            assert HomePage.goToSTB_Mapping().createGroup().goToSTB_Mapping().createSTB_Manually_forRefresh()
        with check:
            assert HomePage.verifyAddedStb_roomNum()
        with check:
            assert HomePage.verifyAddedStb_serialNum()
        with check:
            assert HomePage.verifyAddedStb_grpName()
        HomePage.deleteAllStb().deleteGroup()

    def test_addStb_NotVisibleInOtherProperty(self):
        with check:
            HomePage = STB_Mapping(self.driver)
            assert HomePage.goToSTB_SubPropertyList().createSubProperty().goToSTB_Mapping().createGroup().goToSTB_Mapping().createSTB_Manually().getTextFromSuccessPopup() == addOneStb
        with check:
            assert HomePage.verifyAddedStb_roomNum()
        with check:
            assert HomePage.verifyAddedStb_serialNum()
        with check:
            assert HomePage.verifyAddedStb_grpName()
        with check:
            assert HomePage.goToCreatedSubProperty_StbMapping().verifyAddedStb_roomNum_notThere() == 0
        with check:
            assert HomePage.verifyAddedStb_serialNum_notThere() == 0
        with check:
            assert HomePage.verifyAddedStb_grpName_notThere() == 0
        self.driver.refresh()
        HomePage.deleteSubProperties().goToSTB_Mapping().deleteAllStb().deleteGroup()

    def test_addStb_8_devices(self):
        with check:
            HomePage = STB_Mapping(self.driver)
            beforeStbCount = HomePage.goToSTB_Mapping().createGroup().goToSTB_Mapping().getCurrantSTBCount()
            assert HomePage.createSTB_Manually_8devices().getTextFromSuccessPopup() == addEightStb
        with check:
            afterStbCount = HomePage.getCurrantSTBCount()
            assert afterStbCount == beforeStbCount + 8
        HomePage.deleteAllStb().deleteGroup()

    def test_addStb_8_devices_withDelete(self):
        with check:
            HomePage = STB_Mapping(self.driver)
            beforeStbCount = HomePage.goToSTB_Mapping().createGroup().goToSTB_Mapping().getCurrantSTBCount()
            assert HomePage.createSTB_Manually_8devices().getTextFromSuccessPopup() == addEightStb
        with check:
            afterStbCount = HomePage.getCurrantSTBCount()
            assert afterStbCount == beforeStbCount + 8
        with check:
            assert HomePage.deleteStb().getTextFromSuccessPopup() == deleteStb_popup
        with check:
            countAfterDelete = HomePage.getCurrantSTBCount()
            assert countAfterDelete == afterStbCount - 1
        HomePage.goToSTB_Mapping().deleteAllStb().deleteGroup()

    def test_addStb_8_devices_sequence(self):
        with check:
            HomePage = STB_Mapping(self.driver)
            beforeStbCount = HomePage.goToSTB_Mapping().deleteAllStb().goToSTB_Mapping().createGroup().goToSTB_Mapping().getCurrantSTBCount()
            assert HomePage.createSTB_Manually_8devices_sequence_().getTextFromSuccessPopup() == addEightStb
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

    def test_editStbWindow(self):
        with check:
            HomePage = STB_Mapping(self.driver)
            assert HomePage.goToSTB_Mapping().createGroup().goToSTB_Mapping().createSTB_Manually().getTextFromSuccessPopup() in addOneStb
        with check:
            assert HomePage.verifyAddedStb_roomNum()
        with check:
            assert HomePage.clickOnEditStbBtn().verifyEditStb_updateBtnDisabled()
        with check:
            assert HomePage.verifyEditStbPopup()
        self.driver.refresh()
        HomePage.goToSTB_Mapping().deleteAllStb().deleteGroup()

    def test_editStb_SerialRoomNum(self):
        with check:
            HomePage = STB_Mapping(self.driver)
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

    #This TC is removes from Test Plan
    # def test_editStb_Serial_SpecialChar(self):
    #     with check:
    #         HomePage = STB_Mapping(self.driver)
    #         assert HomePage.goToSTB_Mapping().createGroup().goToSTB_Mapping().createSTB_Manually().getTextFromSuccessPopup() in addOneStb
    #     with check:
    #         assert HomePage.verifyAddedStb_roomNum()
    #     with check:
    #         assert HomePage.verifyEditSerialNum_SpecialChar().getTextFromWarningPopup() in specialCharWarn
    #     with check:
    #         assert HomePage.clickOnUpdate().getTextFromWarningPopup() in validValues
    #     self.driver.refresh()
    #     HomePage.goToSTB_Mapping().deleteAllStb().deleteGroup()

    def test_deleteStb(self):
        with check:
            HomePage = STB_Mapping(self.driver)
            assert HomePage.goToSTB_Mapping().createGroup().goToSTB_Mapping().createSTB_Manually().getTextFromSuccessPopup() == addOneStb
        with check:
            assert HomePage.verifyAddedStb_roomNum()
        with check:
            assert HomePage.verifyAddedStb_serialNum()
        with check:
            assert HomePage.verifyAddedStb_grpName()
        with check:
            beforeCount = HomePage.getCurrantSTBCount()
            assert HomePage.deleteStb().getTextFromSuccessPopup() == deleteStb_popup
        with check:
            afterCount = HomePage.getCurrantSTBCount()
            assert afterCount == beforeCount - 1
        with check:
            assert HomePage.verifyAddedStb_serialNum_notThere() == 0
        with check:
            assert HomePage.verifyAddedStb_grpName_notThere() == 0
        HomePage.deleteGroup()

    def test_sort_Room_Serial_Num(self):
        with check:
            HomePage = STB_Mapping(self.driver)
            assert HomePage.goToSTB_SubPropertyList().createSubProperty().goToCreatedSubProperty_StbMapping().createGroup().goToCreatedSubProperty_StbMapping().createSTB_Manually_8devices_sequence().verifyInAscending_RoomNum()
        with check:
            assert HomePage.goToCreatedSubProperty_StbMapping().clickOnRoomNumCol().verifyIsDescending_RoomNum()
        with check:
            assert HomePage.goToCreatedSubProperty_StbMapping().verifyInAscending_SerialNum()
        with check:
            assert HomePage.goToCreatedSubProperty_StbMapping().clickOnSerialNumCol().verifyIsDescending_SerialNum()
        self.driver.refresh()
        HomePage.goToCreatedSubProperty_StbMapping().deleteAllStb().deleteGroup().deleteSubProperties()

    def test_downloadRecord_SuccessfulPopup(self):
        with check:
            HomePage = STB_Mapping(self.driver)
            assert HomePage.goToSTB_Mapping().createGroup().goToSTB_Mapping().createSTB_Manually().getTextFromSuccessPopup() == addOneStb
        with check:
            assert HomePage.verifyAddedStb_roomNum()
        with check:
            assert HomePage.downloadRecord().getTextFromSuccessPopup() in downloadRecordSuccessfulMsg
        HomePage.deleteAllStb().deleteGroup()

    def test_clearDataBtn_isDisabled(self):
        with check:
            HomePage = STB_Mapping(self.driver)
            assert HomePage.goToSTB_Mapping().createGroup().goToSTB_Mapping().createSTB_Manually().getTextFromSuccessPopup() == addOneStb
        with check:
            assert HomePage.verifyAddedStb_roomNum()
        with check:
            assert HomePage.is_Disabled_clearDataBtn()
        HomePage.deleteAllStb().deleteGroup()

    def test_bulkUpload_STB_DuplicateStb(self):
        with check:
            HomePage = STB_Mapping(self.driver)
            beforeStbCount = HomePage.goToSTB_Mapping().deleteAllStb().getCurrantSTBCount()
            HomePage.bulkUpload_DuplicateStb()
            assert HomePage.verifyCreatedRejectedCount_DuplicateSTB()
        with check:
            assert HomePage.verifyCancel_DownloadRejectedBtn()
        with check:
            afterStbCount = HomePage.clickOnCancel().getCurrantSTBCount()
            assert afterStbCount == beforeStbCount + 1
        HomePage.deleteAllStb()

    def test_bulkUpload_STB_ValidInvalidStb(self):
        with check:
            HomePage = STB_Mapping(self.driver)
            beforeStbCount = HomePage.goToSTB_Mapping().deleteAllStb().getCurrantSTBCount()
            HomePage.bulkUpload_DuplicateStb()
            assert HomePage.verifyCreatedRejectedCount_ValidInvalidStb()
        with check:
            afterStbCount = HomePage.getCurrantSTBCount()
            assert afterStbCount == beforeStbCount + 1
        HomePage.deleteAllStb()

    def test_bulkUpload_STB_CancelBtn(self):
        with check:
            HomePage = STB_Mapping(self.driver)
            HomePage.goToSTB_Mapping().deleteAllStb().bulkUpload_DuplicateStb()
            assert HomePage.verifyCreatedRejectedCount_DuplicateSTB()
        with check:
            HomePage.clickOnCancel().verifyPopup_NotThere()
        HomePage.deleteAllStb()

    def test_bulkUpload_STB_X_Btn(self):
        with check:
            HomePage = STB_Mapping(self.driver)
            HomePage.goToSTB_Mapping().deleteAllStb().bulkUpload_DuplicateStb()
            assert HomePage.verifyCreatedRejectedCount_DuplicateSTB()
        with check:
            HomePage.clickOnCancel().verifyPopup_NotThere()
        HomePage.deleteAllStb()

    def test_bulkUpload_ValidInvalidStbs(self):
        with check:
            HomePage = STB_Mapping(self.driver)
            beforeStbCount = HomePage.goToSTB_Mapping().deleteAllStb().getCurrantSTBCount()
            HomePage.bulkUpload_ValidInvalidStbs()
            assert HomePage.verifyCreatedRejectedCount_ValidInvalidStb()
        with check:
            afterStbCount = HomePage.getCurrantSTBCount()
            assert afterStbCount == beforeStbCount + 1
        with check:
            assert HomePage.verifyAddedStb_serialNum_AUTOMATION56789()
        HomePage.deleteAllStb()

    def test_bulkUpload_PopupNotTheir(self):
        with check:
            HomePage = STB_Mapping(self.driver)
            beforeStbCount = HomePage.goToSTB_Mapping().deleteAllStb().getCurrantSTBCount()
            HomePage.bulkUpload_1_ValidStb()
            assert HomePage.verifyAddRoomsPopup_NotTheir()
        with check:
            afterStbCount = HomePage.getCurrantSTBCount()
            assert afterStbCount == beforeStbCount + 1
        HomePage.deleteAllStb()
    


