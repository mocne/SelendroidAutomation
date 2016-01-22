__author__ = 'andriy.tutunyk'

import unittest
from appium import webdriver
from resources import desired_capabilities


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        application = 'selendroid-test-app.apk'
        executor = 'http://localhost:4723/wd/hub'

        desired_capabs = desired_capabilities.get_desired_capabilities(application)
        self.driver = webdriver.Remote(executor, desired_capabs)

    def tearDown(self):
        # self.driver.quit()
        print('>>> in tearDown method of ', self.__class__.__name__)