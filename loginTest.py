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


base_url="http://35.247.2.171:6868/"
username="admin"
password="portal1_Asimily"
landingPage=base_url+"/index.html#/asset"

class AsimilyPortalTestCases(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()

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


 

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
