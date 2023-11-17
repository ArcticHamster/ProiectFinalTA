Feature: Test functionality of the signup page

  Background: Open Signup Page
    Given I am on the signup page


  Scenario: Verify special characters acceptance in Personal Information fields
    When I enter special characters in first name input field
    When I enter special characters in last name input field
    When I insert an unregistered "email" in the email input field
    When I insert a random password in the password input and confirm password fields
    When I click on the create account button
    Then The account is NOT created and URL is still "https://magento.softwaretestingboard.com/customer/account/create"
#unaccepted symbols: ^=


  Scenario: Verify numbers acceptance in Personal Information fields
    When I enter numbers in first name input field
    When I enter numbers in last name input field
    When I insert another unregistered "email" in the email input field
    When I insert a random password in the password input and in confirm password fields
    When I click on the create account button again
    Then The account is NOT created, and URL is still "https://magento.softwaretestingboard.com/customer/account/create"

  Scenario: Check posibility to create new account using already registered email
    When I enter random first and last name in corresponding fields
    When I insert an registered "email" in the email input field
    When I insert a random password in the password and confirm password input fields
    When I click create account button
    Then Signup: A error message is displayed
    Then Signup: The error message contains "There is already an account"
