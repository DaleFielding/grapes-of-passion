# Grapes of Passion

Website to be created for a fictional independent wine seller focused on enhancing the wine-buying experience with a user-friendly online platform. The website will offer easy navigation, detailed product listings, and secure shopping capabilities, ensuring an easy browsing and purchasing experience. Aiming to create a seamless and enjoyable way for consumers to explore and buy a selection of wines or book relevant experiences.

### [View the live project here...To be added](https://sitetobeadded/)

![Mockup for grapes of passion site...To be added]()

## User Experience (UX)

### User Stories

#### _Viewing/Navigation and Searching_

| #   | As a User I want to be able to...                         |
| --- | --------------------------------------------------------- |
| 1   | Navigate around the site by scrolling.                    |
| 2   | Navigate through categories and subcategories.            |
| 3   | View products.                                            |
| 4   | View available offers.                                    |
| 5   | Search for specific queries relating to products.         |
| 6   | View imagery and relevant information about each product. |
| 7   | See the total amount of products in my cart.              |
| 8   | Filter to refine results for product/query.               |
| 9   | Sort products depending on preference.                    |
| 10  | View contact information and social media links.          |
| 11  | Book dates for events and specify any requirements.       |

#### _Checkout/Payment Processing_

| #   | As a User I want to be able to...                                         |
| --- | ------------------------------------------------------------------------- |
| 12  | View the grand total and list of the products to check before purchasing. |
| 13  | Remove/or adjust quantity of items in the bag.                            |
| 14  | Trust my personal and payment information kept secret and secure.         |
| 15  | Receive an email confirmation if checkout is succesful.                   |

#### _Managing Accounts_

| #   | As a User I want to be able to...               |
| --- | ----------------------------------------------- |
| 16  | Register for an account.                        |
| 17  | Receive an email confirmation.                  |
| 18  | Login and logout of my account.                 |
| 19  | Recover password if forgotten.                  |
| 20  | Add default delivery information in my profile. |
| 21  | View my order history.                          |

#### _Site Owners/Admins_

| #   | As a Site Owner/Admin I want to be able to...                                 |
| --- | ----------------------------------------------------------------------------- |
| 22  | Create products to including relevant details to be stored within a database. |
| 23  | View products displayed throughout the site.                                  |
| 24  | Manage these products so I can update and delete.                             |
| 25  | View a warning if deleting an item to prevent accidental deletions.           |

## Design

### Strategy

The strategy for this site is to include a wide range of features that users would expect for this type of website, as identified in the research below. I will also incorporate a darker, more passionate design to capture the company's essence and help it stand out from competitors.

#### Sites Researched:

-   [Averys](https://averys.com/)
-   [Laithwaites](https://www.laithwaites.co.uk/)
-   [The Great Wine Co.](https://greatwine.co.uk/)
-   [Kask](https://www.kaskwine.co.uk/)
-   [Cave Bristol](https://www.cavebristol.co.uk/)

#### General Findings:

-   Logos are typically in the top left, with a search function and cart icon in the top right.
-   Navigation includes dropdown menus for categories such as; Offers, Wine, Mixed Cases, Champagne & Sparkling, Subscriptions/Clubs, Gifts, About/About Us, Contact info, Events, and Reservations. These expand into subcategories.
-   Eye-catching background images or videos are common.
-   Incentives/offers are frequently displayed.
-   Products and categories are presented in grids and buttons further down the pages.
-   Clicking on the products will direct to a product details page, providing more information and option to add to cart/basket.
-   Viewing basket/checking out contains total, subtotal, delivery information and payment options.
-   When searching or selecting categories, further options are presented to filter/organise the displayed products.
-   Selecting events/reservations will inform users of dates and/or allow them to select available dates through a calendar/booking system.
-   Some sites display ratings, awards, and offer features such as chat support, newsletters, and blogs.
-   Footers include FAQs, delivery info, contact details, T&Cs, copyright, social links, and privacy policies.
-   Site styles are mostly bright/white with contrasting colours for emphasis.

Need to sort scope, have only copy and pasted it from Bonsay Bay, so far.

### Scope

I have listed the possible features below and ranked 1-5 in level of importance/relevance to user/business needs (1 being most important and viable/feasible):

| Possible Feature                                                   | Rank |
| ------------------------------------------------------------------ | ---- |
| Relational database                                                | 1    |
| Form/database validation                                           | 1    |
| Site navigation                                                    | 1    |
| Accessibility                                                      | 1    |
| Device/resolution responsivity                                     | 1    |
| Responses to user actions                                          | 1    |
| Account login/registration and account/profile management          | 1    |
| Authorisation, authentication and permission functionalities       | 1    |
| Ability to create, update and delete listings (owners/superusers)  | 1    |
| Available products                                                 | 1    |
| Available Wine Tasting Events                                      | 1    |
| Details of products for sale including images                      | 1    |
| Contact details                                                    | 1    |
| Search function                                                    | 1    |
| 404 page                                                           | 1    |
| Logo                                                               | 1    |
| Ability to choose delivery address                                 | 1    |
| Ability to add, edit and remove items from the shopping bag/cart   | 1    |
| Method to process payments (test functionality only)               | 1    |
| Email confirmation of order                                        | 1    |
| Various forms to pass information to the database                  | 1    |
| Ability to sort products by price, name etc                        | 1    |
| Ability to navigate by categories and subcategories                | 1    |
| Ability to view previous orders                                    | 2    |
| Filters to refine search; such as price, style, country, grape etc | 2    |
| Advertisements                                                     | 2    |
| Background image(s)                                                | 2    |
| Social links                                                       | 2    |
| Datepicker to select wine tasting products                         | 2    |
| Footer                                                             | 2    |
| Location finding                                                   | 3    |
| Breadcrumb Navigation                                              | 3    |
| Ability to save items as favourites/wish list                      | 4    |
| Ability to view/rate products                                      | 4    |
| Subscriptions/loyalty points                                       | 4    |
| Contact form                                                       | 4    |
| Blog                                                               | 5    |

As some of these features extend beyond the necessary requirements for the project and may take more time than appropriate, I will not currently be implementing:

-   Location Finding.
-   Breadcrumb Navigation.
-   Ability to view/rate products.
-   Ability to save items as favourites/wish list.
-   Subscriptions/loyalty points.
-   Contact form.
-   Blog.

### Structure

I have listed the pages below including the features they will contain.

#### All pages:

-   Navbar:
    -   Logo, clicking on this will reload the home page.
    -   Search button that opens search bar below allowing users to search products.
    -   Login/register/account button.
    -   Cart button allowing users to view items in their cart.
    -   Navigation by categories and sub categories:
        -   Offers:
        -   Wine:
            -   Style.
            -   Country.
            -   Region.
            -   Grape.
        -   Fortified Wine:
            -   Port.
            -   Sherry.
            -   Madiera.
            -   Vermouth.
        -   Wine Tasting
-   Banner displaying free delivery criteria.
-   Footer:
    -   Social media links.
    -   Contact information.
    -   Categories for navigation (as above).
    -   Logo.

#### Homepage:

-   Background image.
-   Company name displayed on top of image (offset).
-   Recommended wines section.
-   Wine tasting section.
-   Various offers section.

#### Product/Query Page

-   Product/Query displays as the title.
-   Button to filter, with a link to clear these filters also.
-   Button to sort by certain criteria.
-   Products displayed:
    -   Image.
    -   A few product details.
    -   Price.
    -   Button to add to cart.
    -   Ability to select quantity.
-   Pagination with arrows to navigate next and previous.

#### Product Details Page

-   Product name displayed.
-   Product image.
-   More details displayed.
-   Description of product.
-   Price.
-   Button to add to cart.
-   Ability to select quantity.

#### Wine Tasting Page

-   Title = Wine Tasting Experience.
-   Wine tasting products displayed:
    -   Image.
    -   Product Name.
    -   Description.
    -   Price.
-   Form and datepicker, allowing user to book and experience.

#### Cart Page

-   Title = Cart.
-   Display products that are in the cart.
-   Include; product images, names, individual price and total price for the product.
-   Functionality to amend quantity or remove product.
-   Cart total, delivery costs and grandtotal.
-   Button to proceed to secure check out.

#### Checkout page

-   Title = Checkout.
-   Form for user to enter their name, email, delivery address, and card details for payment.
-   Order summary; product name, image, qty and subtotal.
-   Cart total, delivery costs and grand total.
-   Button to complete order.
-   Button to adjust bag.

#### Register Page

-   Title = Register.
-   Form for user to enter; email address, confirm email, username, password, confirm password.
-   Button to complete registration.
-   Button to go back to login.

#### Sign In Page

-   Title = Sign in.
-   Form for user to enter their; username/email and password.
-   Link for 'Forgot password'.
-   Remember Me checkbox.
-   Button to sign in.
-   Button to return to Home.

#### Profile Page

-   Title = Your Profile.
-   Form to add default delivery information.
-   Order History; Order no, date, order total, items.
-   Button to update information.

#### Product Management Page

-   Title = Product management.
-   Form including all necessary fields to complete relating to the product being added/edited.
-   Button to add/edit product.
-   Button to cancel.

#### 404 Page

-   Message displayed confirming user has tried to visit a page in the domain that does not exist.
-   Link/button within the page content that will direct the user to the home page.

### Skeleton

#### Table Schema...To be added

![Table Schema]("")<br>

#### Wireframes...To be added

  <details><summary>Homepage</summary>
    <img src="">
  </details>

  <details><summary>Product/Query Page</summary>
    <img src="">
  </details>
  
  <details><summary>Product Details Page</summary>
    <img src="">
  </details>

  <details><summary>Wine Tasting Page</summary>
    <img src="">
  </details>

  <details><summary>Cart Page</summary>
    <img src="">
  </details>

  <details><summary>Checkout page</summary>
    <img src="">
  </details>

  <details><summary>Register Page</summary>
    <img src="">
  </details>

  <details><summary>Sign In Page</summary>
    <img src="">
  </details>

  <details><summary>Profile Page</summary>
    <img src="">
  </details>

  <details><summary>Product Management Page</summary>
    <img src="">
  </details>

  <details><summary>404 Page</summary>
    <img src="">
  </details>
