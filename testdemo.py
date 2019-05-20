#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://release.keepwork.com/")
        self.assertIn("release", driver.title)
        elem = driver.find_element_by_name("wd")
        elem.send_keys("china")
        elem.send_keys(Keys.RETURN)
        # assert "No results found." not in driver.page_source

    def tearDown(self):
        pass
        # self.driver.close()


if __name__ == "__main__":
    unittest.main()

