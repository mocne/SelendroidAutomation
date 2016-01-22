__author__ = 'andriy.tutunyk'

from resources import base_test_case


class TestTest(base_test_case.BaseTestCase):

    def test_001_test(self):
        print(self.driver.current_activity)

if __name__ == "__main__":
    suite = base_test_case.unittest.TestLoader().loadTestsFromTestCase(TestTest)
    base_test_case.unittest.TextTestRunner(verbosity=2).run(suite)