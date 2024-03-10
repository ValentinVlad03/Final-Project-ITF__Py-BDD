## Final project for the Manual and Automated Testing Course

### Project description:
-   Framework used: BDD  (Behaviour Driven Development - Page Object Model)
-   Feature files that contain different scenarios (simple, outline)
-   Tags that separate different tests (@T1, @T2, etc)
-   Use of multiple selectors
-   The code is structured in folders for **features, pages** and **steps**
-   The tests were made on the www.licentepc.ro website and consists of:\
        - @T1 - Scenario outline that tests the login with different invalid passwords\
        - @T2 - Scenario that tests the login with valid password\
        - @T3 - Scenario that tests changing the user's account data (the address used for invoicing)\
        - @T4 - Scenario that tests that the Cookies Policy page contains a specified text\
        - @T5 - Scenario that test redirecting to an external website\
        - @T6 - Scenario outline that test searching for an invalid product\
        - @T7 - Scenario that test searching for a product in the search bar\
        - @T8 - Scenario that tests the sorting options for products listed as a search result\
        - @T9 - Scenario that test that one product from the list can be added to Favorites list\
        - @T10 - Scenario that test that a product can be removed from the Favorites list\
        - @T11 - Scenario that test the sign out option and returning to home page


---
### Installing/cloning the project:
* Open Git Bash
* Change the current working directory to the location where you want to be the cloned directory using the `cd` command
* Type `git clone` and paste the URL link of the repository
```
git clone https://github.com/ValentinVlad03/Final-Project-ITF__Py-BDD
```
* Press **Enter** to create your local clone
---
### Installing dependencies:
* Open the terminal and type the following command:
```
pip install -r requirements.txt
```
* Press **Enter** to install
---
### Running the tests:
All commands to be entered in the terminal
1. **Running tests:**
```
behave
```
2. **Running specific tests:**
```
behave --tags=tag_value (E.g. T1)
```
3. **Running tests with report:**
```
behave -f behave_html_formatter:HTMLFormatter -o behave-report.html
```
4. **Running specific tests with report:**
```
behave -f html-o behave-report --tags=tag_value
```
