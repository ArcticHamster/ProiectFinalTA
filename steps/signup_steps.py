import time

from behave import *


@given('I am on the signup page')
def step_impl(context):
    context.signup_page.navigate_to_signup_page()


# Scenario 1: Verify special characters acceptance in Personal Information fields
@when('I enter special characters in first name input field')
def step_impl(context):
    context.signup_page.set_first_name(context.base_page.randomtext('special', 8))


@when('I enter special characters in last name input field')
def step_impl(context):
    context.signup_page.set_last_name(context.base_page.randomtext('special', 8))


@when('I insert an unregistered "{email}" in the email input field')
def step_impl(context, email):
    context.signup_page.set_random_email(email)


@when('I insert a random password in the password input and confirm password fields')
def step_impl(context):
    context.signup_page.set_password_and_confirm(context.base_page.randomtext('super_strong', 10))


@when('I click on the create account button')
def step_impl(context):
    context.signup_page.click_create_account_button()
    time.sleep(3)


@Then('The account is NOT created and URL is still "{expected_url}"')
def step_impl(context, expected_url):
    assert context.signup_page.is_url_as_expected(expected_url), f'Page URL is not {expected_url}'


# Scenario 2: Verify numbers acceptance in Personal Information fields

@when('I enter numbers in first name input field')
def step_impl(context):
    context.signup_page.set_first_name(context.base_page.randomtext('numbers', 8))


@when('I enter numbers in last name input field')
def step_impl(context):
    context.signup_page.set_last_name(context.base_page.randomtext('numbers', 8))


@when('I insert another unregistered "{email}" in the email input field')
def step_impl(context, email):
    context.signup_page.set_random_email(email)


@when('I insert a random password in the password input and in confirm password fields')
def step_impl(context):
    context.signup_page.set_password_and_confirm(context.base_page.randomtext('super_strong', 10))


@when('I click on the create account button again')
def step_impl(context):
    context.signup_page.click_create_account_button()
    time.sleep(3)


@then('The account is NOT created, and URL is still "{expected_url}"')
def step_impl(context, expected_url):
    assert context.signup_page.is_url_as_expected(expected_url), f'Page URL is not {expected_url}'


# Scenario 3: Check posibility to create new account using already registered email

@when('I enter random first and last name in corresponding fields')
def step_impl(context):
    context.signup_page.set_first_name(context.base_page.randomtext('medium', 10))
    context.signup_page.set_last_name(context.base_page.randomtext('medium', 10))


@when('I insert an registered "email" in the email input field')
def step_impl(context):
    context.signup_page.set_email('only.laur@gmail.com')


@when('I insert a random password in the password and confirm password input fields')
def step_impl(context):
    context.signup_page.set_password_and_confirm(context.base_page.randomtext('super_strong', 10))


@when('I click create account button')
def step_impl(context):
    context.signup_page.click_create_account_button()
    time.sleep(3)


@then('Signup: A error message is displayed')
def step_impl(context):
    context.signup_page.is_error_message_displayed()


@then('Signup: The error message contains "{text}"')
def step_impl(context, text):
    assert text in context.home_page.get_error_message_text(), 'Error message not displayed'
