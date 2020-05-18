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


base_url="http://35.247.2.171:6868"
username="admin"
password="portal1_Asimily"
landingPage=base_url+"/index.html#/asset"

class AsimilyPortalTestCases(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
    
    #TEST CASE 1:To verify if user is able to login successfully.
    def test_login(self):
        page_url = "login.html"
        url= f"{base_url}/{page_url}"

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
        self.assertEqual(driver.current_url, landingPage, "Did not redirect to landing page!")
    
    def login(self):
        page_url = "login.html"
        url= f"{base_url}/{page_url}"

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

    # TEST CASE 2:To navigate to Anomaly tab.
    def test_navigate_anomaly_tab(self):
        self.login()
        time.sleep(5)
        driver = self.driver
        print ("clicking on anomaly tab")
        driver.find_element_by_id("noanim-tab-example-tab-2").click()
        time.sleep(5)
        tabName=driver.find_element_by_id("vulTabs-tab-2").text
        self.assertEqual(tabName,"Anomaly View","Did not navigate to the Anomaly tab") 
        
    # TEST CASE 3:To verify on click of checkbox fix button getting enabled. 
    def test_fix_button_enabled(self):
        self.login()
        time.sleep(5)
        driver = self.driver
        print ("clicking on anomaly tab")
        driver.find_element_by_id("noanim-tab-example-tab-2").click()
        time.sleep(5)
        checkbox_1 = driver.find_element_by_xpath("//tbody[@class='reactable-data']//div[@class='am-checkbox checkbox']/label/label")
        checkbox_1.click()
        time.sleep(5)
        fixButton=driver.find_element_by_xpath("//button[text()='Fix']")
        print ("fix button enabled:",fixButton.is_enabled())
        self.assertEqual(fixButton.is_enabled(),True,"Fix button not getting enabled")  
        

    # TEST CASE 4:To verify on click of fix button popup getting displayed in Anomaly-Device View.
    def test_fix_button_click(self):
        self.login()
        time.sleep(5)
        driver = self.driver
        print ("clicking on anomaly tab")
        driver.find_element_by_id("noanim-tab-example-tab-2").click()
        time.sleep(5)
        checkbox_1 = driver.find_element_by_xpath("//tbody[@class='reactable-data']//div[@class='am-checkbox checkbox']/label/label")
        checkbox_1.click()
        time.sleep(3)
        fixButton=driver.find_element_by_xpath("//button[text()='Fix']")
        fixButton.click()
        time.sleep(3)
        title=driver.find_element_by_xpath("//b[text()='Integration']")
        self.assertEqual("Integration" ,title.text, "Popup is not displayed on click of fix button")
       
    
    # TEST CASE 5:To verify cancel button functionality on fix button popup in Anomaly-Device View.
    def test_cancel_button(self):
        self.login()
        time.sleep(5)
        driver = self.driver
        driver.find_element_by_id("noanim-tab-example-tab-2").click()
        time.sleep(5)
        checkbox_1 = driver.find_element_by_xpath("//tbody[@class='reactable-data']//div[@class='am-checkbox checkbox']/label/label")
        checkbox_1.click()
        time.sleep(3)
        fixButton=driver.find_element_by_xpath("//button[text()='Fix']")
        fixButton.click()
        time.sleep(3)
        cancelButton=driver.find_element_by_xpath("//button[text()=' Cancel']")
        cancelButton.click()
        text_visible=driver.find_element_by_xpath("//label[text()='Show Fixed Devices']")
        time.sleep(5)
        self.assertEqual(text_visible.text,"Show Fixed Devices","Cancel button is not working") 


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
