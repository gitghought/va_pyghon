import sys
import os
from time import sleep
import unittest
from appium import webdriver
#I/ActivityManager( 2318): Start proc com.can.appstore for activity com.can.appstore/.index.IndexActivity

class AppiumTest (unittest.TestCase):
    desired_caps = {} 
    desired_caps['platformName'] = 'Android' 
    desired_caps['platformVersion'] = '4.4.2' 
    desired_caps['appPackage'] = 'com.can.appstore' 
    desired_caps['appActivity'] = '.index.IndexActivity' 
    desired_caps['deviceName'] = '192.168.1.102:5555'

    def test_Message (self):
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.desired_caps)
        msgBtn = driver.find_element_by_id("com.can.appstore:id/iv_message")
        msgBtn.click()
    
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(AppiumTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
