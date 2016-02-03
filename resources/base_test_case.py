__author__ = 'andrii.tiutiunnyk'

import unittest
from appium import webdriver
from .selendroid_toolKit import Selendroid


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.mobile = Selendroid()
        """
        if self.mobile.driver is None:
            executor = 'http://localhost:4723/wd/hub'
            self.mobile.driver = webdriver.Remote(command_executor=executor,
                                                  desired_capabilities=self.mobile.desired_capabilities)
        """
        executor = 'http://localhost:4723/wd/hub'
        self.mobile.driver = webdriver.Remote(command_executor=executor,
                                              desired_capabilities=self.mobile.desired_capabilities)

    def tearDown(self):
        # self.test_case_count += 1

        # print(self.test_case_count)
        self.mobile.driver.quit()
        # print('>>> in tearDown method of ', self.__class__.__name__)
        # print(self.countTestCases())
