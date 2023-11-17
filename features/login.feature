Feature: Test functionality of the login page

    Background: Open Login Page
      Given I am on the login page
#      Given I accepted cookies

# Check redirect active field to required empty input field

  Scenario: Check error message presence when providing wrong credentials
    When I insert an unregistered email in the email input field
    When I insert a password in the password input field
    When I click on Sign In button
    Then The error message is displayed
    Then The error message contains "account sign-in was incorrect" text

  Scenario: Check account information displayed when providing correct credentials
    When I insert an registered email in the email input field
    When I insert a correct password in the password input field
    When I click on Sign In button again
    Then The account page "https://magento.softwaretestingboard.com/customer/account/" is opened
    Then The account information for "Cosa Laurentiu" is displayed


  Scenario: Check that sign out option is successfully
    When I login using valid credentials
    When I select the Logged In dropdown menu
    When I select the Sign Out option
    Then The Signed-Out Url is "https://magento.softwaretestingboard.com/customer/account/logoutSuccess/"
    Then After 5 seconds redirects to homepage URL "https://magento.softwaretestingboard.com/"

@wip
#  Scenario: Verify Forgot Password functionality
#    When I click on the Forgot Your password link
#    When I insert a random email address in E-mail field
#    When I click Reset my Password button
#    Then A confirmation message is displayed
#    Then The message contains 'you will receive an email with a link to reset your password'