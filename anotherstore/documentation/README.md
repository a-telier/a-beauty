  A-telier Beauty
This is an e-commerce shop developped as part of my Full-Stack Software development
program at Code Institute. The purpose of the shop is to make it easy for consumers
to find and purchase beauty products from a selection of hand-picked items.

##  UX process
### Who is this site for?
This site is meant for users looking to buy beauty products.

### What does the user want to achieve in this site?
#####   User Stories - as a user I want to..:
* Explore different products:
- Browse through products.
- See information about the product I am interested in.
- Easily navigate throught the site.
- Filter products by category.
- Sort products by a certain metric.

* Pay for products:
- Add products to my cart.
- See the items in my cart.
- Remove or adjust items in my cart.
- Pay for my purchase quickly and safely.

* Store my information:
- Access a page where my information is stored.
- Easily adjust my information.
- View my purchases history.
- Use this information to complete my purchase quicker.


### How can the user achieve this?
#####   Home View
- The user is able to browse through different recommended categories through banners in the home page.
- The user is able to navigate through the site by using the navigation menu.
- The user is able to see products by category of interest via the navigation menu.

<!-- <div style="display: inline block;">
    <img width="400" height="300" src="/static/img/documentation/wireframe-home.png">
    <img width="400" height="300" src="/static/img/documentation/wireframe-home-2.png">
</div> -->

#####   Products View
* All Products Page:
- The user is able to access all the products in our inventory via the main navigation bar.
- The user is able to see an overview of product image, price, and name in this view.
- The user can access the detailed product view by clicking on the product image or product card.
- The user is able to add products to their cart from this view.
- The user is able to see that a product has been added to the cart via the product counter in the top right corner.
- The user is able to sort by different metrics ex. ratings, pricing, or brand name.

* Category Page:
- The user is able to see products sorted by category by selecting one of the subcategories from the navigation menu.
- The user has similar functionalities than in the home page ex. adding products to cart and accessing detailed views.

* Product Detail Page:
- The user is able to see product details such as product description in a separate view.
- The user is shown related products from the same category when scrolling down.
- If the user is not interested in related products, the user is given the option to browse through other categories by clicking on the visual banners at the end of the page.
- The user has similar functionalities than in the home page ex. adding products to cart.
- The user is able to specify the quantity of products they would like to add to their cart.

<!-- <div style="display: inline block;">
    <img width="400" height="300" src="/static/img/documentation/wireframe-category.png">
</div> -->

#####   Cart View
- The user is able to access their cart at any point by clicking on the top right shopping basket icon.
- Once in this view, the user is able to see the details of their cart such as product name, a thumnail picture and quantity of items added.
- The user is able to adjust the number of products per item in the cart by using the arrows down or up next to the quantity indicator.
- The user is able to remove items completely from the cart by clicking on the cross icon under each item in the cart.
- The user can see a summary per line including item price, quantity and price per line.
- The user is able to see a summary of the total order value.
- The user is able to see whether there is a delivery cost associated depending on whether the total order value is higher or lower than the delivery threshold.
- The user is able to see how much more they would need to spend to eliminate the delivery cost for their order.

#####   Checkout View
- The user is able to move to the checkout page by clicking on a visible red button in the cart view.
- The user is able to then complete their order by filling in their personal details, shipping information and payment details.
- The user knows the transaction was processed via a success_page which (s)he is redirected to, confirming the order and sharing an order number.

#####   Profile View
- The user is able to login by creating an account which requires a username and password.
- If the user is not logged in, the button displayed in navigator will say 'Login', if the 
user has already logged in the button will display 'Sign out'.
- The user is able to sign out of their account, which removes the cookie session by clicking on 
the Sign Out button.
- When logged in, the user is able to see a summary of their purchase history as well as the order number in their profile.


<!-- <div style="display: inline block;">
    <img width="400" height="300" src="/static/img/documentation/wireframe-profile.png">
    <img width="400" height="300" src="/static/img/documentation/wireframe-add.png">
</div> -->

##  UX Features
This project's ideation started from the Assignment's Mandatory Requirements, and therefore the 
features will be explained in the same order, showing how the project fullfills these requirements.

###### Data handling:
- The database is handled via Django's own database and admin interface.

###### Database structure:
* Product handling:
- Product model
- Category model

* Order handling:
- Order model
- OrderLineItem model

* Profile handling:
- UserProfile model

<!-- <div style="display: inline block;">
    <img width="250" height="300" src="/static/img/documentation/data/collections.png">
    <img width="250" height="300" src="/static/img/documentation/data/collection-examples.png">
</div>
<div style="display: inline block;">
    <img width="600" height="300" src="/static/img/documentation/data/collections-interactions.png">
</div> -->

###### User functionality:
- Users are able to create, edit and delete records that they have added to the database.
- The user can access these records via their profile page.
- If they have not placed their order, the user is able to modify the elements added to their cart via the buttons in both the detailed product view and the cart view.
- In addition, the user is able to search the database by looking at different category pages.
<!-- Need to add more here -->

###### Front-end:
<!-- - Created a navigation menu via templating in base.html that works both in desktop and mobile devices.
- Created Flask-based templates for the different pages needed for front-end, for example Recipe or Category pages.
- Used the Materialize library to speed up the design process.
- Used icons from both Materialize and Font Awesome libraries to make the interactions more intuitive.
- And added custom HTML and CSS to complete the options not available via the Materialize library. -->

###### Back-end:
- All of the libraries needed to run this project are stored in the requirements.txt file, which can be installed by running <em>pip install -r requirements.txt</em>.
- Defined the data types that should be collected in the database when the user is adding or editing the documents contained.
- Created authentication requirements, where a user can not access certain pages unless a username is in session.
<!-- Need to add more here  -->

<!-- <div style="display: inline block;">
    <img width="300" height="300" src="/static/img/documentation/data/configuration.png">
    <img width="300" height="300" src="/static/img/documentation/data/routing.png">
</div>
<div style="display: inline block;">
    <img width="650" height="300" src="/static/img/documentation/data/data-types.png">
</div> -->

### Existing Features
###### Navigation:
- Fixed desktop navigation menu - the user is able to navigate through the site via the navigation menu.
- The user is able to access filtered views of the product inventory by clicking on elements in the dropdown menu.
- Once in the All Products View or Category View the user is able to select one of the category tags to access a filtered view per category.
<!-- - Mobile navigation menu - when browsing from mobile devices, the user can access a side navigation menu that pops up when the user clicks on 
the burger icon on the top left. -->
- Sign In/Sign Out navigation - if a user is in session, the navigation button displays the 'Sign Out' option, if there is no username 
in session the option displayed is 'Sign In'. This is done via an if statement in the base.html file.

###### Viewing information:
- View existing records in the database - all users (without needing to log in) are able to view products in the site.
- View single products from the database such as Detailed Product Views.
- View products by category - all users (without needing to log in) are able to see products filtered by category.
- View purchase history - once logged in, the user is able to see the records of what they have inputted under their profile page.
- View items in cart -
- View profile information - 
<!-- Need to add more here -->

<!-- <div style="display: inline block;">
    <img width="250" height="300" src="/static/img/documentation/home-page.png">
    <img width="250" height="300" src="/static/img/documentation/home-browse-page.png">
</div> -->

###### Authentication of user:
- Register an account - the user is able to do so via the 'Register an Account'.
- Sign In function - if no username is in session, the user is redirected to an html Sign In page.
- Sign Out function - if the user clicks on the Sign Out button at the top right corner of the navigation menu in desktop or bottom option 
in the mobile menu, the user is automatically logged out. The username in session is removed.

### Features Left to Implement
###### Data Protection:
- Adding T&C including GDPR clause and how the data is stored and for what purposes.
<!-- More to be added here -->

##  Languages
### Programming languages:
- HTML: Combined with Jinja, HTML is used to create the backbone and structure of the site.
  [Learn more about HTML.](https://www.w3schools.com/html/default.asp)
- CSS: Used to customize the visual outcome of the site, as well as to ensure via @media queries that the content displays nicely 
in all devices.
  [Learn more about CSS.](https://www.w3schools.com/css/default.asp)
- Javascript: Combined with JQuery, Javascript is used to deploy triggers that the user interacts with for example the input form 
and the navigation dropdown and side mobile menus.
  [Learn more about Javascript.](https://www.w3schools.com/js/default.asp)
- Python: Used to communicate with the database, routing and displaying html templates and manipulating data via the user interface.
  [Learn more about Python.](https://www.w3schools.com/python/default.asp)
- SQL: Used to store the records from our database.
  [Learn more about SQLite.](https://sqlite.org/docs.html)

### Libraries:
###### Structural:
- Django: Used for setting up the different apps and models needed to run the project.
  [Learn more about Django.](https://docs.djangoproject.com/en/3.1/)
- Jinja: Used as the templating engine to be able to create HTML pre-made layouts that can be then can be rendered via Python.
  [Learn more about Jinja.](https://jinja..com/en/2.11.x/)

###### Styling and Interactions:
- JQuery: Used to be able to select elements in the HTML code based on their styling, and then modify them in Javascript.
  [Learn more about JQuery.](https://www.w3schools.com/jquery/jquery_intro.asp)
- Materialize: Used to speed up the development process by taking ready to use components and styling classes from the Materialize.
  [Learn more about Materialize.](https://materializecss.com/navbar.html)
- Bootstrap: Used to create all of the HTML structures and some of the styling such as padding and color classes.
  [Learn more about Bootstrap.](https://getbootstrap.com/docs/4.0/getting-started/introduction/)

###### Forms:
- Django-allauth: Used to render profiles and handle authentication.
  [Learn more about Django-allauth.](https://django-allauth.readthedocs.io/en/latest/installation.html)
- Django-countries: Used to display countries in forms in a dropdown list.
  [Learn more about Django-countries.](https://pypi.org/project/django-countries/)
- Django-crispy-forms: Used to display forms.
  [Learn more about Django-crispy-forms.](https://django-crispy-forms.readthedocs.io/en/latest/install.html)

###### File & Data Handling:
- Pillow: Provides extensive file support in several formats.
  [Learn more about Pillow.](https://pillow.readthedocs.io/en/stable/installation.html)
- Psycopg: Translates Python variables into SQL values.
  [Learn more about Psycopg.](https://www.psycopg.org/docs/)
- SQLParse: Provides support for parsing, splitting and formatting SQL statements.
  [Learn more about SQLParse.](https://pypi.org/project/sqlparse/)


### Tools:
###### Production Environment:
- Gitpod: Used as the coding environment for this project.
- Github: Used to store all repositories for this project, as well as to deploy the site via GitPages.

###### Closing knowledge gaps:
- W3schools: Used to clarify and solidify knowledge acquired during the course.
- Stack Overflow: Used as support when troubleshooting and fixing bugs.


##  Testing
Manual tests have been conducted via the Google Chrome Developer Tools to verify that all pages are working properly. The site 
functionalities have been tested in live/deployed version by 3 other users from Android and iOs devices.

###### Navigation menu:
1. Desktop:
- The user is able to navigate to and from all pages via the navigation menu.
- In the desktop menu, the user is able to see the categories set in the dropdown menu.
- Sign In / Sign Out button in the navigator toggles according to whether the user is in session or not.

2. Mobile:
- The mobile menu triggers when the hamburger icon is clicked on.
- All of the options and icons in the menu display correctly.
- The navigation functionality has been checked in different devices incl. mobile devices via the Google Chrome Developer Tools.
- Sign In / Sign Out button in the navigator toggles according to whether the user is in session or not.

###### Home Page:
- The correct information displays from database records.
- All users (without needing to log in) are able to view recipes that have been added to the database.
- The contents resize and are able to be seen properly in all different devices. This function has been testsed by using Google 
Chrome Developer Tools.

###### Product & Category Pages:
For all pages, the contents resize and are able to be seen properly in all different devices. This function has been testsed by using Google 
Chrome Developer Tools.
<!-- Add more information here -->

###### Profile Page:
For all pages, the contents resize and are able to be seen properly in all different devices. This function has been testsed by using Google 
Chrome Developer Tools.
- The user is able to see the records (s)he has added to the database.
- If a user is logged in, a welcome message displays, if a user is not logged in there is no message displaying.
<!-- Add more information here -->

###### Authentication & User Pages:
- If there is no username in session, the user is prompt to a Sign In form.
- If the user does not have an account, the Register link under the Sign In form works properly.
- A user that is not sign in can not access the Profile Page view.
<!-- Add more information here -->

## Deployment
This application is hosted in Heroku, which you would need an account for.
###### To deploy this project yourself:
1. Copy the repository from Github.
2. Open a Heroku account.
3. Create a new project under Heroku.
4. Go to the Settings tab in Heroku.
5. Scroll down and click on Config Var to reveal the Config Variables.
    Here we need to add the following variables:
    - IP - which IP you can access this app from.
    - MONGO_URI - which allows you to connect to the MongoDB database.
    - PORT - which is set by default by Heroku.
    - SECRET KEY 
5. Go to the Deploy tab in Heroku.
6. Connect Heroku to Github directly via API connector.
7. When propted, logged in to your Github account. If everything went well, the Github sub-tab should say Connected in green.
8. In the same tab, make sure that the right repository is connected.
9. Select automatic deployments to Master to make the updating of the site easier.


## Credits

###### Media:
- Unsplash: Used to get all the stock photo material. This is a library where amateur photographers around the world upload their 
pictures and make them available to other users for free.
  [Learn more about Unsplash.](https://unsplash.com/s/photos/vegetarian)
- Canva Online Editor: Used to do any graphic design used on this site such as resizing pictures or creating the logo.
  [Learn more about Canva.](https://www.canva.com/)
- Font Awesome: Used to get icons making it a more intuitive experience for the user such as for example having a User icon leading 
to the Profile page.
  [Learn more about Font Awesome.](https://fontawesome.com/icons?d=gallery)

###### Login System:
<!-- Add more information here -->

###### Documentation:
<!-- Add more information here -->

## Acknowledgements
<!-- Add more information here -->