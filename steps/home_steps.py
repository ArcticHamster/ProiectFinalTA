from behave import *


#  Background: Login with registered account

@when('I insert registered email and password')
def step_impl(context):
    context.login_page.set_email('only.laur@gmail.com')
    context.login_page.set_password("e&9]2&D3f^8%)CA")


@when('I click the Sign In button and then the store logo')
def step_impl(context):
    context.login_page.click_sign_in_button()
    context.home_page.click_logo_button()


# Scenario: Check Add to Cart option without entering details: size, colour
@when('I insert a "search term" in the search box and click search button')
def step_impl(context):
    context.home_page.set_search_term('pants')
    context.home_page.click_search_button()


@when('I click a product from the product grid')
def step_impl(context):
    context.home_page.click_random_product_from_search_result_list()


@when('I click Add to Cart button')
def step_impl(context):
    context.home_page.click_add_to_cart_button()


@then('A error message is displayed')
def step_impl(context):
    context.home_page.is_error_message_displayed()


@then('The error message contains "{text}"')
def step_impl(context, text):
    assert text in context.home_page.get_error_message_text(), 'Error message not displayed'


# Scenario: Check Add to Cart option when entering required details: size, colour
@when('I click on random size and color labels')
def step_impl(context):
    context.home_page.click_random_size_of_selected_product()
    context.home_page.click_random_color_of_selected_product()


@when('I click button Add to Cart')
def step_impl(context):
    context.home_page.click_add_to_cart_button()


@then('A confirmation message is displayed')
def step_impl(context):
    context.home_page.is_confirmation_message_displayed()


@then('The confirmation message contains "{text}"')
def step_impl(context, text):
    assert text in context.home_page.get_confirmation_message_text(), 'Error message not displayed'


# Scenario: Check subtotal calculation for existing items in cart

@when('I click on cart button')
def step_impl(context):
    context.home_page.click_show_cart_button()


@then('The list of cart items is displayed')
def step_impl(context):
    context.home_page.is_cart_items_list_displayed()


@then('I click on view and edit cart button')
def step_impl(context):
    context.home_page.click_view_and_edit_cart_button()


@then('The cart subtotal is displayed correctly')
def step_impl(context):
    val1 = context.home_page.calculate_cart_subtotal()
    val2 = context.home_page.get_subtotal_from_page()
    assert val1 == val2, f'calculated subtotal {val1} different from page subtotal {val2}'
