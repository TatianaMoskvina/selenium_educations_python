# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)


    def test_litecarte(self):
        driver = self.driver
        driver.get("http://localhost/litecart/admin/login.php")
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("login").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Appearence'])[1]/following::span[2]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Customers'])[1]/preceding::span[4]").click()
        driver.find_element_by_link_text("Pages").click()
        driver.find_element_by_link_text("Slides").click()
        driver.find_element_by_xpath("//td[@id='sidebar']/div[2]/a[5]/i").click()



    def tearDown(self):
        self.driver.quit()


