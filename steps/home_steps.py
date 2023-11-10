import time

from behave import *


#  Background: Login with registered account
@given('I am on the Login page')
def step_impl(context):
    context.login_page.navigate_to_login_page()


@given('I insert registered email and password')
def step_impl(context):
    context.login_page.set_email('only.laur@gmail.com')
    context.login_page.set_password("e&9]2&D3f^8%)CA")


@given('I click the Sign In button and then the store logo')
def step_impl(context):
    context.login_page.click_sign_in_button()
    time.sleep(1)
    context.home_page.click_logo_button()


# Scenario: Check Add to Cart option without entering details: size, colour
@when('I insert a "search term" in the search box')
def step_impl(context):
    context.home_page.set_search_term('pants')


@when('I click a product from the product grid')
def step_impl(context):
    context.home_page.click_random_product_from_search_result_list()


@when('I click Add to Cart button')
def step_impl(context):
    context.home_page.click_add_to_cart_button()
