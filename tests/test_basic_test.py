__author__ = 'andrii.tiutiunnyk'

from resources import base_test_case


class BasicTests(base_test_case.BaseTestCase):

    def test_001_installation_test(self):
        self.assertTrue(self.mobile.is_installed())
        # print(self.mobile.driver.current_activity)

    def test_002_logout(self):
        current_activity_1 = self.mobile.driver.current_activity
        self.mobile.logout_from_application()
        current_activity_2 = self.mobile.driver.current_activity
        self.assertNotEqual(current_activity_1, current_activity_2)

    def test_003_logout_refuse(self):
        current_activity_1 = self.mobile.driver.current_activity
        self.mobile.logout_from_application(logout=False)
        self.assertEqual(self.mobile.driver.current_activity, current_activity_1)

if __name__ == "__main__":
    suite = base_test_case.unittest.TestLoader().loadTestsFromTestCase(BasicTests)
    base_test_case.unittest.TextTestRunner(verbosity=2).run(suite)
