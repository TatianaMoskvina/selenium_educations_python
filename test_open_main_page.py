# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_open_main_page(self):
        driver = self.driver
        driver.get("http://www.tsu.ru/")


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

