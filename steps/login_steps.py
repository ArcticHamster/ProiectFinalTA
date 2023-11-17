import time

from behave import *


# Scenario 1 Check error message presence when providing wrong credentials
@given('I am on the login page')
def step_impl(context):
    context.login_page.navigate_to_login_page()


@given('I accepted cookies')
def step_impl(context):
    context.login_page.accept_cookies_ckeck()


@when('I insert an unregistered email in the email input field')
def step_impl(context):
    context.login_page.set_email('email@email.com')


@when('I insert a password in the password input field')
def step_impl(context):
    context.login_page.set_password('randompass')


@when('I click on Sign In button')
def step_impl(context):
    context.login_page.click_sign_in_button()


@then('The error message is displayed')
def step_impl(context):
    assert context.login_page.is_error_message_displayed(), "Error message not displayed"


@then('The error message contains "{text}" text')
def step_impl(context, text):
    assert text in context.login_page.get_error_message_text()


# Scenario 2 Check account information displayed when providing correct credentials
@when('I insert an registered email in the email input field')
def step_impl(context):
    context.login_page.set_email('only.laur@gmail.com')


@when('I insert a correct password in the password input field')
def step_impl(context):
    context.login_page.set_password("e&9]2&D3f^8%)CA")


@when('I click on Sign In button again')
def step_impl(context):
    context.login_page.click_sign_in_button()
    time.sleep(3)


@then('The account page "{expected_url}" is opened')
def step_impl(context, expected_url):
    assert context.login_page.is_url_as_expected(expected_url), f'Page URL is not {expected_url}'


@then('The account information for "{name}" is displayed')
def step_impl(context, name):
    assert name in context.login_page.get_user_name(), f'Account information for {name} NOT displayed'


# Scenario 3: Check that sign out option is successfully

@when('I login using valid credentials')
def step_impl(context):
    context.login_page.set_email('only.laur@gmail.com')
    context.login_page.set_password("e&9]2&D3f^8%)CA")
    context.login_page.click_sign_in_button()
    time.sleep(2)


@when('I select the Logged In dropdown menu')
def step_impl(context):
    context.login_page.click_logged_in_dropdown_menu()
    time.sleep(1)


@When('I select the Sign Out option')
def step_impl(context):
    context.login_page.click_sign_out_menu_option()
    time.sleep(3)


@Then('The Signed-Out Url is "{expected_url}"')
def step_impl(context, expected_url):
    assert context.login_page.is_url_as_expected(expected_url), f'Page URL is not {expected_url}'
    time.sleep(7)


@Then('After 5 seconds redirects to homepage URL "{expected_url}"')
def step_impl(context, expected_url):
    assert context.login_page.is_url_as_expected(expected_url), f'Page URL is not {expected_url}'


# Scenario: Verify Forgot Password functionality

@when('I click on the Forgot Your password link')
def step_impl(context):
    context.login_page.click_forgot_password_link()


@when('I insert a random email address in E-mail field')
def step_impl(context):
    context.login_page.set_forgot_pswd_email()


@when('I click Reset my Password button')
def step_impl(context):
    context.login_page.click_reset_pswd_button()


@then('Signup: A confirmation message is displayed')
def step_impl(context):
    context.login_page.is_success_message_displayed()


@then('The message contains "{text}"')
def step_impl(context, text):
    assert text in context.login_page.get_success_message_text(), 'Error message not displayed'
