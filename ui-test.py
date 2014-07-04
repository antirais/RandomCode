#!/usr/bin/env python
# coding: utf-8
from selenium import webdriver
import unittest

class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        
    def tearDown(self):
    	self.browser.close()

    def testPageTitle(self):
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)

if __name__ == '__main__':
    unittest.main(verbosity=2)