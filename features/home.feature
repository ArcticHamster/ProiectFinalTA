Feature: Test functionality of serch field and order options


  Background: Login with registered account
    Given I am on the Login page
    When I insert registered email and password
    When I click the Sign In button and then the store logo
    When I insert a "search term" in the search box and click search button
    When I click a product from the product grid

  Scenario: Check Add to Cart option without entering details: size, colour
    When I click Add to Cart button
    Then A error message is displayed
    Then The error message contains "This is a required field"

  Scenario: Check Add to Cart option when entering required details: size, colour
    When I click on random size and color labels
    When I click button Add to Cart
    Then A confirmation message is displayed
    Then The confirmation message contains "You added"
@wip
  Scenario: Check subtotal calculation for existing items in cart
    When I click on cart button
    Then The list of cart items is displayed
    Then I click on view and edit cart button
    Then The cart subtotal is displayed correctly

