__author__ = 'andrii.tiutiunnyk'

from resources import base_test_case


class TestUserRegistration(base_test_case.BaseTestCase):
    def test_001_register_new_user(self):
        self.mobile.start_user_registration()
        self.mobile.enter_username(username=self.mobile.selendroid_user.user_name)
        self.mobile.enter_email(email=self.mobile.selendroid_user.e_mail)
        self.mobile.enter_password(password=self.mobile.selendroid_user.password)
        self.assertEqual(self.mobile.get_default_name(), 'Mr. Burns')
        self.mobile.enter_name(name=self.mobile.selendroid_user.name)
        self.mobile.driver.hide_keyboard()
        self.mobile.click_register_user_verify()

if __name__ == "__main__":
    suite = base_test_case.unittest.TestLoader().loadTestsFromTestCase(TestUserRegistration)
    base_test_case.unittest.TextTestRunner(verbosity=2).run(suite)
