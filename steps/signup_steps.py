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
    context.signup_page.set_password(context.base_page.randomtext('super_strong', 10))


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
    context.signup_page.set_password(context.base_page.randomtext('super_strong', 10))


@when('I click on the create account button again')
def step_impl(context):
    context.signup_page.click_create_account_button()
    time.sleep(3)


@Then('The account is NOT created, and URL is still "{expected_url}"')
def step_impl(context, expected_url):
    assert context.signup_page.is_url_as_expected(expected_url), f'Page URL is not {expected_url}'
