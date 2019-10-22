Feature: Using behave and selenium together

    Scenario Outline: Asserting against input fields and the URL values they give you
        Given the user navigates to the URL <url>
        When the user fills in the string <first string> in the first-field
        And the user fills in the string <second string> in the second-field
        And the user submits the form
        Then The URL the user is on is <end url>

        Examples:
            | url                   | first string | second string | end url                       |
            | http://127.0.0.1:5000 | First        | Second        | http://127.0.0.1:5000/success |
            | http://127.0.0.1:5000 | garbage      | garbage       | http://127.0.0.1:5000/        |
