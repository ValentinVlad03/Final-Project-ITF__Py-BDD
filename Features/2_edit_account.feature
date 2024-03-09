Feature: Check that I can edit data in my account

  @T3 @positiveTesting
  Scenario: I am on my account home page and I want to change my address used for invoicing
#      Given I am on my account home page
      When  I click on Update account link
      When  I delete the current address
      When  I enter my new address
      When  I click on the Update button
      Then  I am redirected to my account home page


