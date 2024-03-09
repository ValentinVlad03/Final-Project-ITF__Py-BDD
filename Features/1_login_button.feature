Feature: Check that the authentication button on the Licentepc website is working properly and I can access my account

  @T1 @negativeTesting
  Scenario Outline: Trying to authenticate with an invalid password
    Given I am on the Licentepc website homepage
    When  I click on accept cookies button
    When  I click on My Account link
    When  I enter my valid email address
    When  I insert my invalid "<password>"
    When  I click on sign in account button
    Then  I receive an "<error_message>"
    Examples:
      | password  | error_message                                         |
      | asdasdsa  | Te rugam sa verifici daca ai introdus parola corecta. |
#

  @T2 @positiveTesting
  Scenario: I am on the Licentepc website homepage and I want to login on my account
      Given I am on the Licentepc website homepage
      When  I click on user icon
      When  I enter my valid email
      When  I enter my valid password
      When  I click on the sign in account button
      Then  I am redirected to my account page


