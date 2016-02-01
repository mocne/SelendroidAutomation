from .selendroid_resources import ApplicationObjects
from appium import webdriver
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
        else:
            return False

    def click_display_toast_button(self):
        self.driver.find_element_by_id(ApplicationObjects.display_toast_button_ID).click()

    def click_display_popup(self):
        self.driver.find_element_by_id(ApplicationObjects.display_popup_window_button_ID).click()

    def click_throw_exception(self):
        self.driver.find_element_by_id(ApplicationObjects.unhandled_exception_button_ID).click()

    def get_encoding_text_view(self):
        return self.driver.find_element_by_id(ApplicationObjects.encoding_text_viewID)


# ========================================================================================================================
# user registration helpers
# ========================================================================================================================

    def find_on_register_activity(self, element_id):
        element = self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().resourceId("{}"))'.format(element_id))
        return element

    def enter_username(self):
        username_field = self.find_on_register_activity(ApplicationObjects.input_username_fieldID)
        username_field.send_keys(self.selendroid_user.user_name)

    def enter_email(self):
        email_field = self.find_on_register_activity(ApplicationObjects.input_email_fieldID)
        email_field.send_keys(self.selendroid_user.e_mail)

    def enter_password(self):
        password_field = self.find_on_register_activity(ApplicationObjects.input_password_fieldID)
        password_field.send_keys(self.selendroid_user.password)

    def get_default_name(self):
        name_field = self.find_on_register_activity(ApplicationObjects.input_name_field['id'])
        return name_field.text

    def enter_name(self):
        name_field = self.find_on_register_activity(ApplicationObjects.input_name_field['id'])
        name_field.send_keys(self.selendroid_user.name)

    def set_programming_language(self, programming_language):
        pass

    def click_accept_adds(self):
        pass

    def accept_adds_is_clicked(self):
        pass

    def click_register_user(self):
        self.driver.find_element_by_id(ApplicationObjects.register_user_buttonID).click()
