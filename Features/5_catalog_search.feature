Feature: Check that the product search is working properly

  @T7 @positiveTesting
    Scenario Outline: Trying to search for an invalid product that is not listed on the website
      Given I am on the Licentepc homepage and I want to search for an invalid product
      When  I enter the "<invalid_product>" name in the search box
      When  I click on the search button
      Then  I am redirected to a new page with the following message displayed : "<no_results>"
      Examples:
      | invalid_product   | no_results              |
      | ^%#$bb#@$#@       | Incearca o noua cautare |
      | surubelnita       | Incearca o noua cautare |
      | legume gratinate  | Incearca o noua cautare |


  @T8 @positiveTesting
    Scenario Outline: Trying to search for a valid product that is listed on the website
      Given I am on the Licentepc homepage and I want to search for a valid product
      When  I enter the "<product_name>" in the search box
      When  I click the search button
      Then  I am redirected to a new page that contains the "<results_title>"
      Examples:
      | product_name      | results_title          |
      | Autodesk          | Autodesk               |
      | Corel             | Corel                  |
      | PDF               | PDF                    |



  @T9 @positiveTesting
    Scenario: I am on the search result page on "PDF" and I want to sort the list
      Given I am on PDF search result page
      When  I click on sorting options checklist box
      When  I click on Ascending Price option
      Then  The list is shown sorted in ascending order by price



  @T10 @positiveTesting
    Scenario: I am on the search result page on "PDF" and I want to add one product to Favorites
      Given I am on PDF search result page
      When  I click on Favorite link of Corel PDF
      Then  I go on Favorite section of my account and check that the product is listed

