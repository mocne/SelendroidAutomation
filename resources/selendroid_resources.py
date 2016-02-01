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
    display_text_view_button_ID = 'io.selendroid.testapp:id/visibleButtonTest'
    display_toast_button_ID = 'io.selendroid.testapp:id/showToastButton'
    display_popup_window_button_ID = 'io.selendroid.testapp:id/showPopupWindowButton'
    unhandled_exception_button_ID = 'io.selendroid.testapp:id/exceptionTestButton'

    i_agree_button_ID = 'android:id/button1'
    no_button_ID = 'android:id/button2'
    message_ID = 'android:id/message'
    message_text = 'This will end the activity'


    visible_text = {'resource-id': 'io.selendroid.testapp:id/visibleTextView',
                    'text': ''}

    encoding_text_viewID = 'io.selendroid.testapp:id/encodingTextview'

# ======================================================================================

# User registration screen elements
    input_username_fieldID = 'io.selendroid.testapp:id/inputUsername'
    input_email_fieldID = 'io.selendroid.testapp:id/inputEmail'
    input_password_fieldID = 'io.selendroid.testapp:id/inputPassword'
    input_name_field = {'default_text': 'Mr. Burns',
                        'id': 'io.selendroid.testapp:id/inputName'}
    adds_check_boxID = 'io.selendroid.testapp:id/input_adds'
    register_user_buttonID = 'io.selendroid.testapp:id/btnRegisterUser'