Feature: Check that the Cookies Policy page contains a specified text

  @T4 @positiveTesting
  Scenario: I am on home page and I want to check that the Cookies Policy page contains a specified text
      Given I am on home page
      When  I click on Cookies Policy link
      When  I check that a specified text is shown
      Then  I return to home page

