__author__ = 'andrii.tiutiunnyk'

from resources import base_test_case
import time


class TestUserRegistration(base_test_case.BaseTestCase):
    def test_001_register_new_user(self):
        print(self.mobile.device_orientation)
        self.mobile.start_user_registration()
        print(self.mobile.device_orientation)
        self.mobile.set_orientation_landscape()
        print(self.mobile.device_orientation)
        """
        self.mobile.enter_username(username=self.mobile.selendroid_user.user_name)
        self.mobile.enter_email(email=self.mobile.selendroid_user.e_mail)
        self.mobile.enter_password(password=self.mobile.selendroid_user.password)
        self.assertEqual(self.mobile.get_default_name(), 'Mr. Burns')
        self.mobile.enter_name(name=self.mobile.selendroid_user.name)
        self.mobile.driver.hide_keyboard()
        self.mobile.set_programming_language(self.mobile.selendroid_user.programming_language[7])
        time.sleep(10)
        self.mobile.click_register_user_verify()
        """
        registration_parameters = self.mobile.full_user_registration(self.mobile.selendroid_user.user_name,
                                                                     self.mobile.selendroid_user.e_mail,
                                                                     self.mobile.selendroid_user.password,
                                                                     self.mobile.selendroid_user.name,
                                                                     self.mobile.selendroid_user.programming_language[7],
                                                                     accept_adds=True)
        self.mobile.click_register_user_verify()
        print(self.mobile.device_orientation)
        self.assertEqual('.VerifyUserActivity', self.mobile.driver.current_activity)
        verification_parameters = self.mobile.full_user_verification()
        self.assertListEqual(registration_parameters, verification_parameters)


if __name__ == "__main__":
    suite = base_test_case.unittest.TestLoader().loadTestsFromTestCase(TestUserRegistration)
    base_test_case.unittest.TextTestRunner(verbosity=2).run(suite)
