# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        self.open_auth_page(driver)
        self.log_in(driver)
        #appearence
        driver.find_element_by_css_selector("span.name").click()

        #waiting
        wait = WebDriverWait(driver, 10)  # seconds
        element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

        #appearence->template
        driver.find_element_by_css_selector("#doc-template > a > span.name").click()
        # appearence->logotype
        driver.find_element_by_css_selector("#doc-logotype > a").click()

        #catalog
        driver.find_element_by_xpath("//li[2]/a/span[2]").click()
        driver.find_element_by_css_selector("#doc-catalog > a > span.name").click()
        driver.find_element_by_css_selector("#doc-product_groups > a > span.name").click()
        driver.find_element_by_css_selector("#doc-option_groups > a > span.name").click()
        driver.find_element_by_css_selector("#doc-manufacturers > a > span.name").click()
        driver.find_element_by_css_selector("#doc-suppliers > a > span.name").click()
        driver.find_element_by_css_selector("#doc-delivery_statuses > a > span.name").click()
        driver.find_element_by_css_selector("#doc-sold_out_statuses > a > span.name").click()
        driver.find_element_by_css_selector("#doc-quantity_units > a > span.name").click()
        driver.find_element_by_css_selector("#doc-csv > a > span.name").click()

        #countries
        driver.find_element_by_link_text("Countries").click()

        #currencies
        driver.find_element_by_xpath("//li[4]/a/span[2]").click()

        #customers
        driver.find_element_by_xpath("//li[5]/a/span[2]").click()
        driver.find_element_by_css_selector("#doc-csv > a > span.name").click()
        driver.find_element_by_css_selector("#doc-newsletter > a").click()

        #geo zones
        driver.find_element_by_xpath("//li[6]/a/span[2]").click()

        #languages
        driver.find_element_by_link_text("Languages").click()
        driver.find_element_by_css_selector("#doc-storage_encoding > a > span.name").click()

        #modules
        driver.find_element_by_link_text("Modules").click()
        driver.find_element_by_css_selector("#doc-customer > a").click()
        driver.find_element_by_css_selector("#doc-shipping > a").click()
        driver.find_element_by_css_selector("#doc-payment > a").click()
        driver.find_element_by_css_selector("#doc-order_total > a > span.name").click()
        driver.find_element_by_css_selector("#doc-order_success > a > span.name").click()
        driver.find_element_by_css_selector("#doc-order_action > a").click()

        #orders
        driver.find_element_by_link_text("Orders").click()
        driver.find_element_by_css_selector("#doc-order_statuses > a > span.name").click()

        #pages
        driver.find_element_by_link_text("Pages").click()

        #reports
        driver.find_element_by_link_text("Reports").click()
        driver.find_element_by_css_selector("#doc-most_sold_products > a > span.name").click()
        driver.find_element_by_css_selector("#doc-most_shopping_customers > a > span.name").click()

        #settings
        driver.find_element_by_link_text("Settings").click()
        driver.find_element_by_css_selector("#doc-store_info > a > span.name").click()
        driver.find_element_by_css_selector("#doc-defaults > a > span.name").click()
        driver.find_element_by_css_selector("#doc-general > a").click()
        driver.find_element_by_css_selector("#doc-listings > a").click()
        driver.find_element_by_css_selector("#doc-images > a").click()
        driver.find_element_by_css_selector("#doc-checkout > a > span.name").click()
        driver.find_element_by_css_selector("#doc-advanced > a > span.name").click()
        driver.find_element_by_css_selector("#doc-security > a").click()

        #slides
        driver.find_element_by_link_text("Slides").click()

        #tax
        driver.find_element_by_link_text("Tax").click()
        driver.find_element_by_css_selector("#doc-tax_rates > a").click()

        #translations
        driver.find_element_by_xpath("//li[15]/a/span[2]").click()
        driver.find_element_by_css_selector("#doc-scan > a > span.name").click()
        driver.find_element_by_css_selector("#doc-csv > a > span.name").click()

        #users
        driver.find_element_by_link_text("Users").click()

        #vQmods
        driver.find_element_by_link_text("vQmods").click()

    def open_auth_page(self, driver):
        driver.get("http://localhost/litecart/admin/login.php")

    def log_in(self, driver):
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("login").click()

    def tearDown(self):
        self.driver.quit()

