from .selendroid_resources import ApplicationObjects

# from appium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

from .user import User


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
        self.selendroid_user = User('selen_name', 'selen_username', 'selen_password')

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

    def text_field_enter_text(self, text='some text'):
        text_field = self.driver.find_element_by_id(ApplicationObjects.text_field_ID)
        text_field.send_keys(text)
        self.driver.hide_keyboard()
        assert text_field.text == text

    def click_display_text_button(self):
        self.driver.find_element_by_id(ApplicationObjects.display_text_view_button_ID).click()

    def text_view_is_displayed(self):
        try:
            text_view = self.driver.find_element_by_id(ApplicationObjects.visible_text['resource-id'])
            return text_view
        except NoSuchElementException:
            pass
        else: return False

    def click_display_toast_button(self):
        self.driver.find_element_by_id(ApplicationObjects.display_toast_button_ID).click()

    def click_display_popup(self):
        self.driver.find_element_by_id(ApplicationObjects.display_popup_window_button_ID).click()

    def click_throw_exception(self):
        self.driver.find_element_by_id(ApplicationObjects.unhandled_exception_button_ID).click()

    def get_encoding_text_view(self):
        return self.driver.find_element_by_id(ApplicationObjects.encoding_text_viewID)
