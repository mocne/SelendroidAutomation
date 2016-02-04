__author__ = 'andrii.tiutiunnyk'


class ApplicationObjects(object):
    """
    selendroid-test-app elements
    """

# ======================================================================================================================
# .HomeScreenActivity elements
# ======================================================================================================================
    EN_Button_ID = 'io.selendroid.testapp:id/buttonTest'
    start_web_view_button_ID = 'io.selendroid.testapp:id/buttonStartWebview'
    user_registration_button_ID = 'io.selendroid.testapp:id/startUserRegistration'
    text_field_ID = 'io.selendroid.testapp:id/my_text_field'
    show_progress_bar_button_ID = 'io.selendroid.testapp:id/waitingButtonTest'
    accept_adds_check_box_ID = 'io.selendroid.testapp:id/input_adds_check_box'
    display_text_view_button_ID = 'io.selendroid.testapp:id/visibleButtonTest'
    visible_text_view_ID = 'io.selendroid.testapp:id/visibleTextView'
    display_toast_button_ID = 'io.selendroid.testapp:id/showToastButton'
    display_popup_window_button_ID = 'io.selendroid.testapp:id/showPopupWindowButton'
    unhandled_exception_button_ID = 'io.selendroid.testapp:id/exceptionTestButton'
    exception_text_field_ID = 'io.selendroid.testapp:id/exceptionTestField'
    encoding_text_viewID = 'io.selendroid.testapp:id/encodingTextview'

    # logout dialog
    i_agree_button_ID = 'android:id/button1'
    no_button_ID = 'android:id/button2'
    message_ID = 'android:id/message'

    # waiting dialog
    progress_bar_ID = 'android:id/progress'

# ======================================================================================================================
# .RegisterUserActivity elements
# ======================================================================================================================
    input_username_field_ID = 'io.selendroid.testapp:id/inputUsername'
    input_email_field_ID = 'io.selendroid.testapp:id/inputEmail'
    input_password_field_ID = 'io.selendroid.testapp:id/inputPassword'
    input_name_field_ID = 'io.selendroid.testapp:id/inputName'
    programming_language_spinner_ID = 'io.selendroid.testapp:id/input_preferedProgrammingLanguage'
    programming_language_spinner_text_ID = 'android:id/text1'
    adds_check_box_ID = 'io.selendroid.testapp:id/input_adds'
    register_user_verify_button_ID = 'io.selendroid.testapp:id/btnRegisterUser'

    # Programming Language selection
    select_language_list_ID = 'android:id/select_dialog_listview'

# ======================================================================================================================
# .VerifyUserActivity elements
# ======================================================================================================================
    name_data_ID = 'io.selendroid.testapp:id/label_name_data'
    username_data_ID = 'io.selendroid.testapp:id/label_username_data'
    password_data_ID = 'io.selendroid.testapp:id/label_password_data'
    email_data_ID = 'io.selendroid.testapp:id/label_email_data'
    programming_language_data_ID = 'io.selendroid.testapp:id/label_preferedProgrammingLanguage_data'
    accept_adds_data_ID = 'io.selendroid.testapp:id/label_acceptAdds_data'
    register_user_button_ID = 'io.selendroid.testapp:id/buttonRegisterUser'