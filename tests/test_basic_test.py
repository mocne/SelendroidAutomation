__author__ = 'andrii.tiutiunnyk'

from resources import base_test_case


class BasicTests(base_test_case.BaseTestCase):
    def test_001_installation_test(self):
        self.assertTrue(self.mobile.is_installed())
        # print(self.mobile.driver.current_activity)


if __name__ == "__main__":
    suite = base_test_case.unittest.TestLoader().loadTestsFromTestCase(BasicTests)
    base_test_case.unittest.TextTestRunner(verbosity=2).run(suite)
