Feature: Check that the Cookies Policy page contains a specified text

  @T4 @positiveTesting
  Scenario: I am on home page and I want to check that the Cookies Policy page contains a specified text
      Given I am on home page
      When  I click on Cookies Policy link
      When  I check that a specified text is shown
      Then  I return to home page


  @T5 @positiveTesting
  Scenario: I am on Cookies Policy page and I want to check redirecting to an external application
      Given I am on Cookies Policy page
      When  I click on the email address specified
      Then  I am redirected to an external application (email client)

