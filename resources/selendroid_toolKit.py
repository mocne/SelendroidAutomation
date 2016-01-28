from .selendroid_resources import ApplicationObjects


# from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


class Selendroid(object):
    def __init__(self, driver=None):
        self.driver = driver
        self.desired_capabilities = dict()
        self.desired_capabilities['platformName'] = 'Android'
        self.desired_capabilities['deviceName'] = 'Nexus4'
        self.desired_capabilities['app-package'] = 'io.selendroid.testapp'
        self.desired_capabilities['app-activity'] = '.HomeScreenActivity'
        self.desired_capabilities['newCommandTimeout'] = 17200
        # self.desired_capabilities['automationName'] = "selendroid"
        # self.driver = webdriver.Remote()

    def is_installed(self):
        return self.driver.is_app_installed(bundle_id=self.desired_capabilities['app-package'])

    def wait_for_element_id(self, element_id, wait_time=10):
        # element = self.driver.find_element_by_id(element_id)
        wait = WebDriverWait(self.driver, wait_time, ignored_exceptions=NameError)
        return wait.until(lambda driver, elem_id=element_id: driver.find_element_by_id(elem_id))

    def wait_for_element_name(self, element_name, wait_time=10):
        wait = WebDriverWait(self.driver, wait_time, ignored_exceptions=NameError)
        return wait.until(lambda driver, elem_name=element_name: driver.find_element_by_name(elem_name))

    def click_logout_button(self):
        self.driver.find_element_by_id(ApplicationObjects.EN_Button_ID).click()

    def logout_from_application(self, logout=True):
        self.click_logout_button()
        if logout:
            self.wait_for_element_id(ApplicationObjects.i_agree_button_ID).click()
        else:
            self.wait_for_element_id(ApplicationObjects.no_button_ID).click()
