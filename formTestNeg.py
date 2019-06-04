# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time
import os
from sauceclient import SauceClient

#driver.quit()

#username=os.environ.get("yoavikz")
#access_key=os.environ.get("b465e2dc-2485-4ed6-9ced-502738b61f61")

class Check(unittest.TestCase):    
    def setUp(self):
       # self.driver = webdriver.Firefox()
        self.sauce_client = SauceClient("yoavikz", 'b465e2dc-2485-4ed6-9ced-502738b61f61')
        SAUCE_USERNAME = 'yoavikz'
        SAUCE_ACCESS_KEY = 'b465e2dc-2485-4ed6-9ced-502738b61f61'
        self.driver = webdriver.Remote(
        desired_capabilities=webdriver.DesiredCapabilities.FIREFOX,
        command_executor='http://%s:%s@ondemand.saucelabs.com:80/wd/hub' %
        (SAUCE_USERNAME, SAUCE_ACCESS_KEY)
        )
        id = self.driver.session_id
        print 'Link to your job: https://saucelabs.com/jobs/%s' % id
        self.driver.implicitly_wait(30)
        self.base_url = "http://spectory-web.herokuapp.com"
        self.verificationErrors = []
        self.accept_next_alert = True

    
    def test_check(self):
        
        self.driver.get(self.base_url + "/en")
        self.sauce_client.jobs.update_job(self.driver.session_id, passed=True,name="Negative test")    
        self.driver.find_element_by_xpath("//input[@type='text']").clear()
        self.driver.find_element_by_xpath("//input[@type='text']").send_keys("yoav zaltsman")
        self.driver.find_element_by_xpath("(//input[@type='text'])[2]").clear()
        self.driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys("yoavzaltsmangmail.com") #Input invalid! no "@" in email address.
        self.driver.find_element_by_xpath("(//input[@type='text'])[3]").clear()
        self.driver.find_element_by_xpath("(//input[@type='text'])[3]").send_keys("0544756400")
        self.driver.find_element_by_xpath("//div[@id='contact-form']/div/textarea").clear()
        self.driver.find_element_by_xpath("//div[@id='contact-form']/div/textarea").send_keys("hey. this is an automation test.")
        self.driver.find_element_by_css_selector("div.send-btn.eng-variant").click()
        time.sleep(2) #Wait for greeting to appear
        p=self.driver.find_elements_by_class_name("nice-to-meet-you")     #gets html attribute of display of greeting
        print p[0].get_attribute('style')        
        
        if not (p[0].get_attribute('style')):   #checks if there is a style attribute in the greeting (if there is not, the test ends with failure )
            print "failed"
            self.sauce_client.jobs.update_job(self.driver.session_id, passed=False) 
        else:
            self.sauce_client.jobs.update_job(self.driver.session_id, passed=True)    # test ends with success if there is a style attribute for greeting
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
