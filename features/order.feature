Feature: Test functionality of serch field and order options

  Background: Login with registered account
    Given I am on the Login page
    Given I insert registered email and password
    Given I click the Sign In button and then the store logo

  Scenario: Check Add to Cart option without entering details: size, colour
    When I insert a "search term" in the search box
    When I click a product from the product grid
    When I click Add to Cart button
    Then A error message is displayed
    Then The message contains 'This is a required field'

  Scenario: Check Add to Cart option when entering required details: size, colour
    When I insert a different "search term" in the search box
    When I click a random product from the product grid
    When I click on size label "36"
    When I click on colour label "brown"
    When I click button Add to Cart
    Then A confirmation message is displayed
    Then The message contains "You added..."

#  Scenario: Check