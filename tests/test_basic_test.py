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

    def test_004_enter_text(self):
        self.mobile.text_field_enter_text()

    def test_005_display_text_view(self):
        if not self.mobile.text_view_is_displayed():
            self.mobile.click_display_text_button()
            self.assertTrue(self.mobile.text_view_is_displayed())
            self.assertEqual(self.mobile.text_view_is_displayed().text, 'Text is sometimes displayed')
            self.mobile.click_display_text_button()
            self.assertFalse(self.mobile.text_view_is_displayed())
        else:
            self.mobile.click_display_text_button()
            self.assertFalse(self.mobile.text_view_is_displayed())

    def test_006_display_toast(self):
        activity_before_click = self.mobile.driver.current_activity
        self.mobile.click_display_toast_button()
        activity_after_click = self.mobile.driver.current_activity
        self.assertEqual(activity_before_click, activity_after_click)

    def test_007_display_popup(self):
        self.mobile.click_display_popup()

    def test_008_press_to_throw_exception(self):
        activity_before_click = self.mobile.driver.current_activity
        self.mobile.click_throw_exception()
        self.assertEqual(activity_before_click, self.mobile.driver.current_activity, msg='Application crashed')

    def test_009_type_to_throw_exception(self):
        pass

    def test_010_encoding(self):
        china_string = b'\xe3\x83\x91\xe3\x82\xbd\xe3\x82\xb3\xe3\x83\xb3\xe7\x89\x88\xe3\x81\xab\xe3\x81\x99\xe3\x82\x8b'
        encoding_text_view = self.mobile.get_encoding_text_view()
        self.assertEqual(encoding_text_view.text.encode(), china_string)


if __name__ == "__main__":
    suite = base_test_case.unittest.TestLoader().loadTestsFromTestCase(BasicTests)
    base_test_case.unittest.TextTestRunner(verbosity=2).run(suite)
