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
        self.selendroid_user = User('NAME', 'USERNAME', 'PASSWORD')

    def is_installed(self):
        return self.driver.is_app_installed(bundle_id=self.desired_capabilities['app-package'])

    def wait_for_element_id(self, element_id, wait_time=10):
        # element = self.driver.find_element_by_id(element_id)
        wait = WebDriverWait(self.driver, wait_time, ignored_exceptions=NameError)
        return wait.until(lambda driver, elem_id=element_id: driver.find_element_by_id(elem_id))

    def wait_for_not_element_id(self, element_id, wait_time=10):
        wait = WebDriverWait(self.driver, wait_time, ignored_exceptions=NameError)
        wait.until_not(lambda driver, elem_id=element_id: driver.find_element_by_id(elem_id))

    def wait_for_element_name(self, element_name, wait_time=10):
        wait = WebDriverWait(self.driver, wait_time, ignored_exceptions=NameError)
        return wait.until(lambda driver, elem_name=element_name: driver.find_element_by_name(elem_name))

    def is_check_box_checked(self, check_box_id):
        check_box = self.driver.find_element_by_id(check_box_id)
        if check_box.get_attribute('checked') == 'true':
            return True
        elif check_box.get_attribute('checked') == 'false':
            return False

    def click_on_check_box(self, check_box_id):
        self.driver.find_element_by_id(check_box_id).click()
    '''
    def clear_text_field(self, text_field_id):
        self.driver.find_element_by_id(text_field_id).clear()
    '''
    def click_logout_button(self):
        self.driver.find_element_by_id(ApplicationObjects.EN_Button_ID).click()

    def logout_from_application(self, logout=True):
        self.click_logout_button()
        if logout:
            self.wait_for_element_id(ApplicationObjects.i_agree_button_ID).click()
        else:
            self.wait_for_element_id(ApplicationObjects.no_button_ID).click()

    def start_web_view(self):
        self.driver.find_element_by_id(ApplicationObjects.start_web_view_button_ID).click()

    def start_user_registration(self):
        self.driver.find_element_by_id(ApplicationObjects.user_registration_button_ID).click()

    def start_user_registration_with_delay(self):
        self.driver.find_element_by_id(ApplicationObjects.show_progress_bar_button_ID).click()
        self.wait_for_not_element_id(ApplicationObjects.progress_bar_ID)

    def text_field_enter_text(self, text_field_id, text='some text'):
        text_field = self.driver.find_element_by_id(text_field_id)
        text_field.send_keys(text)
        self.driver.hide_keyboard()
        assert text_field.text == text

    def click_display_text_button(self):
        self.driver.find_element_by_id(ApplicationObjects.display_text_view_button_ID).click()

    def text_view_is_displayed(self):
        try:
            text_view = self.driver.find_element_by_id(ApplicationObjects.visible_text_view_ID)
            return text_view
        except NoSuchElementException:
            pass
        # else: return False

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

    def enter_username(self, username='default_username'):
        username_field = self.find_on_register_activity(ApplicationObjects.input_username_field_ID)
        username_field.send_keys(username)

    def enter_email(self, email='default_email'):
        email_field = self.find_on_register_activity(ApplicationObjects.input_email_field_ID)
        email_field.send_keys(email)

    def enter_password(self, password='default_password'):
        password_field = self.find_on_register_activity(ApplicationObjects.input_password_field_ID)
        password_field.send_keys(password)

    def get_default_name(self):
        name_field = self.find_on_register_activity(ApplicationObjects.input_name_field_ID)
        return name_field.text

    def enter_name(self, name='default_name'):
        name_field = self.find_on_register_activity(ApplicationObjects.input_name_field_ID)
        name_field.clear()
        name_field.send_keys(name)

    def set_programming_language(self, programming_language):
        pass

    def click_accept_adds(self):
        pass

    def accept_adds_is_clicked(self):
        pass

    def click_register_user_verify(self):
        self.driver.find_element_by_id(ApplicationObjects.register_user_verify_button_ID).click()
