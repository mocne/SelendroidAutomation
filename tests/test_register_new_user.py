__author__ = 'andrii.tiutiunnyk'

from resources import base_test_case


class TestUserRegistration(base_test_case.BaseTestCase):
    def test_001_register_new_user(self):
        self.mobile.click_register_user()
        self.mobile.enter_username()
        self.mobile.enter_email()
        self.mobile.enter_password()
        self.assertEqual(self.mobile.get_default_name(), 'Mr. Burns')
        self.mobile.enter_name()
        self.mobile.click_register_user()

if __name__ == "__main__":
    suite = base_test_case.unittest.TestLoader().loadTestsFromTestCase(TestUserRegistration)
    base_test_case.unittest.TextTestRunner(verbosity=2).run(suite)
