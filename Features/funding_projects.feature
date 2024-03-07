Feature: Check that clicking on an company name link (from the list) redirect me to an external website

  @T6 @positiveTesting
  Scenario: I am on Funding Projects page and I want to check redirecting to external websites
      Given I am on home page
      When  I click on Funding Projects link
      When  I click on an company name link, from the list
      Then  I am redirected to an external website
