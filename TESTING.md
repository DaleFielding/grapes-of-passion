# Testing

For this project, I started with Test Driven Development (TDD), writing tests before coding. Later, I switched to manual testing, which allowed me to find issues and improve usability that automated tests might miss. This also made it easier to adapt to changes and get quick feedback on the user experience. By using both TDD and manual testing, I ensured the application was well-tested and user-friendly.

## Validation

### WSC - Markup Validation Service

#### Homepage (including base and navigation)

[Check Validation Here](https://validator.w3.org/nu/?doc=https%3A%2F%2Fgrapes-of-passion-37a9373e50d5.herokuapp.com%2F)<br>

-   Some errors and warnings were displayed, which have all be corrected These are listed below:

| Warning/Error                                                             | Corrected by                                                                                 |
| ------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| Error: Element `li` not allowed as child of element `nav` in this context | Wrapping `<li>` elements inside `<ul>` elements.                                             |
| Error: Duplicate ID `user-options`                                        | Changed IDs to `user-options-desktop` and `user-options-mobile` to ensure uniqueness.        |
| Error: End tag `div` seen, but there were open elements                   | Ensured all opening tags have corresponding and properly nested closing tags.                |
| Error: Unclosed element `ul`                                              | Ensured all `<ul>` elements are properly closed.                                             |
| Error: No `li` element in scope but a `li` end tag seen                   | Ensured all `<li>` elements are properly nested within `<ul>`, `<ol>`, or `<menu>` elements. |
| Error: Stray end tag `ul`                                                 | Ensured all end tags match their corresponding opening tags.                                 |
| Error: Stray end tag `nav`                                                | Ensured all `<nav>` tags are properly opened and closed.                                     |
| Error: Stray end tag `div`                                                | Ensured all `<div>` tags are properly opened and closed.                                     |
| Error: Stray end tag `header`                                             | Ensured all `<header>` tags are properly opened and closed.                                  |
| Warning: The first occurrence of ID `user-options` was here               | Changed IDs to ensure each ID is unique within the document.                                 |
| Warning: The type attribute is unnecessary for JavaScript resources       | Removed the `type="text/javascript"` attribute from the `<script>` tags.                     |

#### Basket page

[Check Validation Here](https://validator.w3.org/nu/?doc=https%3A%2F%2Fgrapes-of-passion-37a9373e50d5.herokuapp.com%2Fbasket%2F)

-   One warning was displayed, which has been corrected. These are listed below:

| Warning/Error                                                             | Corrected by                                    |
| ------------------------------------------------------------------------- | ----------------------------------------------- |
| Error: Element `li` not allowed as child of element `nav` in this context | Wrapped `<li>` elements inside `<ul>` elements. |

#### Checkout page (including checkout success)

[Check Validation Here](https://validator.w3.org/nu/?doc=https%3A%2F%2Fgrapes-of-passion-37a9373e50d5.herokuapp.com%2Fcheckout%2F)

-   One error displayed, which has been corrected. Listed below:

| Warning/Error                                                          | Corrected by                                                                                                                                              |
| ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Warning: The `type` attribute is unnecessary for JavaScript resources. | Removed the `type="text/javascript"` attribute from the `<script>` tags. Noticed this was a recurring issue, so i have removed this from all other files. |

#### Products page (including checkout success)

[Check Validation Here](https://validator.w3.org/nu/?doc=https%3A%2F%2Fgrapes-of-passion-37a9373e50d5.herokuapp.com%2Fproducts%2F)

-   One error displayed, which has been corrected. Listed below:

| Warning/Error                                             | Corrected by                                                                  |
| --------------------------------------------------------- | ----------------------------------------------------------------------------- |
| Error: The `strike` element is obsolete. Use CSS instead. | Replaced the `<strike>` elements with CSS styling to achieve the same effect. |

#### Product detail page

[Check Validation Here](https://validator.w3.org/nu/?doc=https%3A%2F%2Fgrapes-of-passion-37a9373e50d5.herokuapp.com%2Fproducts%2F2%2F)<br>

-   No errors or warnings displayed.

#### Edit product page

[Check Validation Here](https://validator.w3.org/nu/?doc=https%3A%2F%2Fgrapes-of-passion-37a9373e50d5.herokuapp.com%2Fproducts%2Fedit%2F5%2F)

-   No errors or warnings displayed.

#### Add product page

[Check Validation Here](https://validator.w3.org/nu/?doc=https%3A%2F%2Fgrapes-of-passion-37a9373e50d5.herokuapp.com%2Fproducts%2Fadd%2F)

-   No errors or warnings displayed.

#### Profile page

[Check Validation Here](https://validator.w3.org/nu/?doc=https%3A%2F%2Fgrapes-of-passion-37a9373e50d5.herokuapp.com%2Fprofile%2F)

-   No errors or warnings displayed.

#### Register page

[Check Validation Here](https://validator.w3.org/nu/?doc=https%3A%2F%2Fgrapes-of-passion-37a9373e50d5.herokuapp.com%2Faccounts%2Fsignup%2F)

-   No errors or warnings displayed.

#### Login page

[Check Validation Here](https://validator.w3.org/nu/?doc=https%3A%2F%2Fgrapes-of-passion-37a9373e50d5.herokuapp.com%2Faccounts%2Flogin%2F)

-   No errors or warnings displayed.

#### Logout page

[Check Validation Here](https://validator.w3.org/nu/?doc=https%3A%2F%2Fgrapes-of-passion-37a9373e50d5.herokuapp.com%2Faccounts%2Flogout%2F)

-   No errors or warnings displayed.

#### Wine Tasting page

[Check Validation Here](https://validator.w3.org/nu/?doc=https%3A%2F%2Fgrapes-of-passion-37a9373e50d5.herokuapp.com%2Fwine_tasting%2F)

-   No errors or warnings displayed.

### WSC - CSS Validation Service

I have entered my external css file into the validator:

-   No errors found.
-   Some warnings have appeared in relation to using variables for the colours/fonts, using vendor extensions and setting the same colour for border and background. I have left these in as they were all taught in codeinstitute lessons.

![validator-css-results](resources/validator-css-results.png)
![validator-css-warnings](resources/validator-css-warnings.png)

### JSLint

A large amount of the functionality comes from script within the boutique_ado project. I have validated the additional js script/logic I have added as below:

#### Wine Tasting script

-   A few warnings/errors displayed, which have been corrected except one. Listed below:

| Warning/Error                              | Corrected by                                                                                                                                                                          |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Line is longer than 80 characters          | Split long lines into shorter ones                                                                                                                                                    |
| Use double quotes, not single quotes       | Changing the highlighted single quotes to double quotes                                                                                                                               |
| Expected an identifier and instead saw `{` | Not corrected, unsure why `const dates = {{ dates_json  \| safe }};` is flagging as the function works as expected, do not want to cause this to change so I have left this as it is. |

### CI Python Lynter

I have run each of my Python files through the linter, there were quite a few changes to make to most files in order for these to pass, all have been corrected now. The warnings that appeared throughout are listed below:

| Warning                                 | Corrected by                                                               |
| --------------------------------------- | -------------------------------------------------------------------------- |
| Lines over 80 characters                | Splitting into 2 or more lines, often including strings within parenthesis |
| Continuation line under indented        | Adjusting the indentation                                                  |
| Continuation line over indented         | Adjusting the indentation                                                  |
| Variables declared but never used       | Removing these where appropriate                                           |
| Handler404 has already been declared    | Removing import of handler404 as had a custom declaration for this         |
| Expected 2 blank lines, found 1         | Adding an additional line where appropriate                                |
| No newline at end of file               | Adding the newline at the end of the file                                  |
| Various Django imports that were unused | Removing these as unnecessary                                              |
| Do not use bare except                  | Importing Http404 to include after the except clause                       |
| Too many blank lines                    | Reducing the amount of blank lines                                         |
