Feature: Check that I can sign out from my account


    @T11 @positiveTesting
    Scenario: I can sign out and return to home page
      Given I am on my account page
      When  I click sign out link
      Then  I am redirected to home page