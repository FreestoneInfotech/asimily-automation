import unittest
from selenium import webdriver
from datetime import datetime
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from colorama import Fore
from selenium.common.exceptions import NoSuchElementException
from collections import OrderedDict
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager


base_url = "http://35.247.2.171:6868"
username = "admin"
password = "portal1_Asimily"
landingPage = base_url+"/index.html#/asset"


class AsimilyPortalTestCases(unittest.TestCase):

    # Utility function for login.
    def login(self):
        page_url = "login.html"
        url = f"{base_url}/{page_url}"

        driver = self.driver
        driver.maximize_window()
        driver.get(url)
        uname = driver.find_element_by_id("username")
        uname.clear()
        uname.send_keys(username)

        pwd = driver.find_element_by_id("password")
        pwd.clear()
        pwd.send_keys(password)

        driver.find_element_by_id("signIn").click()
        time.sleep(10)

    # Utility function for single filter search

    def singleFilterApply(self, filterName, value):
        driver = self.driver
        driver.find_element_by_xpath(
            "//span[@class='typeahead']//input").send_keys(filterName)
        driver.find_element_by_xpath(
            "//span[@class='typeahead']/input").send_keys(u'\ue007')
        time.sleep(5)
        driver.find_element_by_xpath(
            "//span[@class='typeahead']//input").send_keys(value)
        time.sleep(5)
        driver.find_element_by_xpath(
            "//span[@class='typeahead']/input").send_keys(u'\ue007')
        time.sleep(2)
        return

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        print("Executing {} ".format(self._testMethodName))

    # TEST CASE 1:To verify if user is able to login successfully.
    def test_login(self):
        self.login()
        self.assertEqual(self.driver.current_url, landingPage,
                         "Did not redirect to landing page!")

    # TEST CASE 2:To navigate to Anomaly tab.

    def test_navigate_anomaly_tab(self):
        self.login()
        time.sleep(5)
        driver = self.driver
        driver.find_element_by_id("noanim-tab-example-tab-2").click()
        time.sleep(5)
        tabName = driver.find_element_by_id("vulTabs-tab-2").text
        self.assertEqual(tabName, "Anomaly View",
                         "Did not navigate to the Anomaly tab")

    # TEST CASE 3:To verify on click of checkbox fix button getting enabled.
    def test_fix_button_enabled(self):
        self.login()
        time.sleep(5)
        driver = self.driver
        driver.find_element_by_id("noanim-tab-example-tab-2").click()
        time.sleep(5)
        checkbox_1 = driver.find_element_by_xpath(
            "//tbody[@class='reactable-data']//div[@class='am-checkbox checkbox']/label/label")
        checkbox_1.click()
        time.sleep(5)
        fixButton = driver.find_element_by_xpath("//button[text()='Fix']")
        print("fix button enabled:", fixButton.is_enabled())
        self.assertEqual(fixButton.is_enabled(), True,
                         "Fix button not getting enabled")

    # TEST CASE 4:To verify on click of fix button popup getting displayed in Anomaly-Device View.

    def test_fix_button_click(self):
        self.login()
        time.sleep(5)
        driver = self.driver
        driver.find_element_by_id("noanim-tab-example-tab-2").click()
        time.sleep(5)
        checkbox_1 = driver.find_element_by_xpath(
            "//tbody[@class='reactable-data']//div[@class='am-checkbox checkbox']/label/label")
        checkbox_1.click()
        time.sleep(3)
        fixButton = driver.find_element_by_xpath("//button[text()='Fix']")
        fixButton.click()
        time.sleep(3)
        title = driver.find_element_by_xpath("//b[text()='Integration']")
        self.assertEqual("Integration", title.text,
                         "Popup is not displayed on click of fix button")

    # TEST CASE 5:To verify cancel button functionality on fix button popup in Anomaly-Device View.

    def test_cancel_button(self):
        self.login()
        time.sleep(5)
        driver = self.driver
        driver.find_element_by_id("noanim-tab-example-tab-2").click()
        time.sleep(5)
        checkbox_1 = driver.find_element_by_xpath(
            "//tbody[@class='reactable-data']//div[@class='am-checkbox checkbox']/label/label")
        checkbox_1.click()
        time.sleep(3)
        fixButton = driver.find_element_by_xpath("//button[text()='Fix']")
        fixButton.click()
        time.sleep(3)
        cancelButton = driver.find_element_by_xpath(
            "//button[text()=' Cancel']")
        cancelButton.click()
        text_visible = driver.find_element_by_xpath(
            "//label[text()='Show Fixed Devices']")
        time.sleep(5)
        self.assertEqual(text_visible.text, "Show Fixed Devices",
                         "Cancel button is not working")

    # TEST CASE 6: To verify if 'fixed' getting displayed in checkbox column after device is marked as fixed.

    def test_fixed_displayed(self):
        self.login()
        time.sleep(5)
        driver = self.driver
        driver.find_element_by_id("noanim-tab-example-tab-2").click()
        time.sleep(5)
        checkboxSelect = driver.find_element_by_xpath(
            "//tbody[@class='reactable-data']//div[@class='am-checkbox checkbox']/label/label")
        checkboxSelect.click()
        ip = driver.find_element_by_xpath(
            "//tbody[@class='reactable-data']//td[2]")
        ipAddress = ip.text
        time.sleep(3)
        fixButton = driver.find_element_by_xpath("//button[text()='Fix']")
        fixButton.click()
        time.sleep(4)
        driver.find_element_by_xpath(
            "//div[@class='modal-body']//select[@class='form-control']").click()
        time.sleep(2)
        selectManual = driver.find_element_by_xpath(
            "//div[@class='FormInput']/select/option[@value=2]")
        selectManual.click()
        driver.find_element_by_xpath(
            "//textarea[@class='form-control']").send_keys("Test")
        time.sleep(3)
        confirm = driver.find_element_by_xpath(
            "//div[@class='button-popovering m-l-xs']/button[text()='Confirm']")
        confirm.click()
        time.sleep(3)
        driver.find_element_by_xpath(
            "//div[@class='am-checkbox inline adjust-device-checkbox']/label").click()
        time.sleep(2)
        driver.find_element_by_xpath("//span[@class='typeahead']").click()
        time.sleep(2)
        driver.find_element_by_xpath(
            "//ul[@class='typeahead-selector']//li[2]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//span[@class='typeahead']").click()
        time.sleep(4)
        print("Value to be entered:", ipAddress)
        driver.find_element_by_xpath(
            "//span[@class='typeahead']/input").send_keys(ipAddress)
        driver.find_element_by_xpath(
            "//span[@class='typeahead']/input").send_keys(u'\ue007')
        time.sleep(5)
        ipAddressValue = driver.find_element_by_xpath(
            "//tbody[@class='reactable-data']/tr//td[2]").text
        checkboxColumnText = driver.find_element_by_xpath(
            "//tbody[@class='reactable-data']/tr//td[1]").text
        time.sleep(2)
        if (ipAddressValue == ipAddress):
            # print("web element value:",driver.find_element_by_xpath("//tbody[@class='reactable-data']/tr//td[2]").text)
            self.assertEqual(checkboxColumnText, "Fixed",
                             "Device did not get marked as fixed")
            print("Device has been successfully marked as fixed")

    # TEST CASE 7:To verify if data getting displayed based on the filter Applied (Manufacturer)

    def test_manufacturer_filter_search(self):
        filter = 'Manufacturer'
        manufacturerVal = 'Alerton'
        self.login()
        time.sleep(5)
        driver = self.driver
        time.sleep(2)
        driver.find_element_by_xpath(
            "//div[@class='filter-input-group']").click()
        time.sleep(2)
        self.singleFilterApply(filter, manufacturerVal)
        time.sleep(5)
        resultSet = driver.find_elements_by_xpath(
            "//tbody[@class='reactable-data']/tr/td[2]")
        for element in resultSet:
            self.assertEqual(manufacturerVal, element.text,
                             "Manufacturer value is not equal to {}.".format(manufacturerVal))

    # TEST CASE 8:To verify if data getting displayed based on the combination of filters
    # (device type+device model) in Asset Details

    def test_device_type_device_model_filter_search(self):
        filter1 = 'Device Type'
        filter2 = 'Device Model'
        param1 = 'Logic controller'
        param2 = 'VLX'
        self.login()
        time.sleep(5)
        driver = self.driver
        driver.find_element_by_xpath(
            "//div[@class='filter-input-group']").click()
        time.sleep(2)
        self.singleFilterApply(filter1, param1)
        self.singleFilterApply(filter2, param2)
        time.sleep(2)
        resultSet = driver.find_elements_by_xpath(
            "//tbody[@class='reactable-data']//tr")
        for element in resultSet:
            deviceTypes = element.find_elements_by_xpath(".//td[3]")
            for deviceType in deviceTypes:
                self.assertEqual(
                    deviceType.text, param1, "Device Type value is not equal to {}.".format(param1))

            deviceModels = element.find_elements_by_xpath(".//td[4]")
            for deviceModel in deviceModels:
                self.assertEqual(
                    deviceModel.text, param2, "Device Model value is not equal to {}.".format(param2))

    # TEST CASE 9:Asset Details: To verify edit button functionality.

    def test_edit_button_asset_details(self):
        filter = 'IP Address'
        param = '10.19.19.120'
        manufacturerNewVal = 'G24 Power Limited'
        self.login()
        driver = self.driver
        time.sleep(5)
        driver.find_element_by_xpath(
            "//div[@class='filter-input-group']").click()
        time.sleep(2)
        self.singleFilterApply(filter, param)
        time.sleep(2)
        editSaveButton = driver.find_element_by_xpath(
            "//button[@class='btn btn-primary']")
        editSaveButton.click()
        time.sleep(2)
        driver.find_element_by_xpath(
            "//span[@class='Select-value-label']").click()
        time.sleep(2)
        driver.find_element_by_xpath(
            "//div[@class='Select-input']/input").send_keys(manufacturerNewVal)
        time.sleep(2)
        driver.find_element_by_xpath(
            "//div[@class='Select-input']/input").send_keys(u'\ue007')

        editSaveButton.click()
        time.sleep(2)
        manufacturerUpdatedVal = driver.find_element_by_xpath(
            "//tbody[@class='reactable-data']//td[2]").text
        self.assertEqual(manufacturerNewVal, manufacturerUpdatedVal,
                         "Failed to update Manufacturer.")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
