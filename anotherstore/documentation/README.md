 A-telier Beauty
This is an e-commerce shop developped as part of my Full-Stack Software development
program at Code Institute. The purpose of the shop is to make it easy for consumers
to find and purchase beauty products from a selection of hand-picked items. The site
also contains a blog, to attract potential customers via SEO keywords.

##  UX process
### Who is this site for?
This site is meant for customers looking to buy beauty products or find inspiration and advice.

### What does the user want to achieve in this site?
#####   User Stories - as a user I want to..:
* Explore different products:
- Browse through products.
- See information about the product I am interested in.
- Easily navigate throught the site.
- Filter/see products by category.
- Sort products by a certain metric ex. price or ratings.

* Pay for products:
- Add products to my cart.
- See the items in my cart.
- Remove or adjust number of items in my cart.
- Be notified when an item is added or removed from my cart.
- Pay for my purchase quickly and safely.

* Store my information:
- Access a page where my profile and order information is stored.
- Easily adjust my information.
- View my purchases history.
- Save my delivery information for a future purchase.
- Use this information to complete my purchase quicker.


### How can the user achieve this?
#####   Home View
- The user is able to browse through different recommended categories through banners in the home page.
- The user is able to navigate through the site by using the navigation menu.
- The user is able to see products by category of interest via the navigation menu.

<div style="display: inline block; background-size:contain;">
    <img width="420" height="600" src="/anotherstore/documentation/img/home/screenshot_home1.png">
    <img width="400" height="600" src="/anotherstore/documentation/img/home/screenshot_home2.png">
</div>

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

<div style="display: inline block; background-size:contain;">
    <img width="600" height="400" src="/anotherstore/documentation/img/categories/screenshot_category1.png">
    <img width="200" height="400" src="/anotherstore/documentation/img/categories/screenshot_category2.png">
</div>

#####   Profile View
- The user is able to login by creating an account which requires a username and password.
- If the user is not logged in, the button displayed in navigator will say 'Login', if the 
user has already logged in the button will display 'Sign out'.
- The user is able to sign out of their account, which removes the cookie session by clicking on 
the Sign Out button.
- When logged in, the user is able to see a summary of their purchase history as well as the order number in their profile.

<div style="display: inline block; background-size:contain;">
    <img width="400" height="600" src="/anotherstore/documentation/img/profile/screenshot_profile.png">
</div>

#####   Blog View
- The user can access the category 'blog' via the sidenav navigation menu.
- The user is able to see an overview of all posted articles.
- The user is able to filter by category by clicking on the tags above the articles.
- The user is able to see each single article.
- The user is able to browse through other categories or other articles after having read the single article.

<div style="display: inline block; background-size:contain;">
    <img width="600" height="700" src="/anotherstore/documentation/img/articles/screenshot_article1.png">
    <img width="600" height="700" src="/anotherstore/documentation/img/articles/screenshot_article2.png">
    <img width="200" height="400" src="/anotherstore/documentation/img/articles/screenshot_article3.png">
</div>

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

<div style="display: inline block; background-size:contain;">
    <img width="200" height="400" src="/anotherstore/documentation/img/cart/screenshot_cart1.png">
    <img width="200" height="400" src="/anotherstore/documentation/img/cart/screenshot_cart2.png">
</div>

##  UX Features
This project's ideation started from the Assignment's Mandatory Requirements, and therefore the 
features will be explained in the same order, showing how the project fullfills these requirements.

###### Data handling:
- The data in this site is handled based on different models and classes created specifically for each
application we created under the main project.

###### Database structure:
* Product handling:
- Product model ---> stores information about the products.
- Category model ---> stores the different categories, which allows us to sort the products.

* Order handling:
- Order model ---> collects the information in each order.
- OrderLineItem model

* Profile handling:
- UserProfile model

* Blog handling:
- Article model ---> stores the information in each single article.
- Blog_category model ---> stores the different categories, which allows us to sort the articles.

###### User functionality:
* Products:
- Products display dynamically from the database, as well as the URLS.
- The user is able to view products by category by either clicking on a category in the submenu, or by selecting one of the category tags over products.
- The user is able to see each individual product and their details.
- The user is then able to see items within the same category as they were browsing.
- The user is able to scroll further down the page and go to a filtered view of products per category.
- The user is able to add products directly from the all_products view.

* Categories:
- Categories are added dynamically from the database.
- Same as for products, one can see filtered views by using the category tags.
- Category banners are displayed dynamically in several pages of the site, to provide the user with a continuation of their shopping experience.
- The user is able to add products directly from the categories view.

* Profile:
- The user is able to login and logout of their profile.
- The user gets a notification when they have sign in to their profile.
- The user is able to access a profile page, where (s)he can see their saved profile details, and purchasing history.
- The user is able to update their delivery information via their profile page.

* Blog:
- The user is able to browse through articles posted on our site, to find inspiration, tips and tricks.
- For the owner of the site, the blog is a posibility to attract potential new shoppers interested in the topics discussed in the blog.
- THe user is able to see single articles.
- Simmilar than to the product and category pages, the user is able to filter the articles by category by using the clickable tags.

* Cart:
- The user is able to edit and remove items from their cart.
- The user can access these records via their profile page.
- If they have not placed their order, the user is able to modify the elements added to their cart via the buttons in both the detailed product view and the cart view.
- In addition, the user is able to search the database by looking at different category pages.

* Checkout:
- The user is able to review their purchase before entering their credit details.
- The user is able to save their delivery information when they create a purchase.
- If their information is already saved, the form is auto-filled.
- If the payment process goes as expected, the user gets redirected to a success_page.
- The payment are processed by using Stripe's API connection including the forms for inputting payment information.

###### Front-end:
Below are the wireframes that I created based on the purpose that we defined from the user stories.
The final result, the deploy site, does not necessarily look like the wireframes in terms of esthetics and branding,
but they were part of the process of defining which functions and data points would be needed to create this site.

<div style="display: inline block; background-size:contain;">
    <img width="500" height="500" src="/anotherstore/documentation/img/wireframe/screenshot-wireframe1.png">
    <img width="500" height="500" src="/anotherstore/documentation/img/wireframe/screenshot-wireframe2.png">
    <img width="500" height="500" src="/anotherstore/documentation/img/wireframe/screenshot-wireframe3.png">
    <img width="500" height="500" src="/anotherstore/documentation/img/wireframe/screenshot-wireframe4.png">
</div>

###### Back-end:
- All of the libraries needed to run this project are stored in the requirements.txt file, which can be installed by running <em>pip install -r requirements.txt</em>.
- Defined the data types that should be collected in the database to both display and store new information.
- Created authentication requirements, where a user can not access certain pages unless a username is in session.

Some libraries used to display information from backend to front-end: crispy forms, stripe and allauth forms.

### Existing Features
###### Navigation:
- Fixed desktop navigation menu - the user is able to navigate through the site via the sidenav menu.
- The user can open the navigation menu that opens on the left side of the screen by clicking on the bars icons.
- The sidenav menu looks and functions the same in both mobile and desktop, however a search bar is displayed in the mobile version.
- To browse through categories, the sidenav offers an accordion compoenent displaying the cateogries in the site.
- The Sign In or Sign Out option changes in the navigation menu depending whether you are logged in or not.
- The shopping cart always displays in the top right corner of the site.
- WHen an item is added, the user can easily see this in the shopping cart as there is a badge notification which displays the current product counter.

###### Viewing information:
- View existing records in the database - all users (without needing to log in) are able to view products in the site.
- View single products from the database such as Detailed Product Views.
- View products by category - all users (without needing to log in) are able to see products filtered by category.
- View purchase history - once logged in, the user is able to see the records of what they have inputted under their profile page.
- View items in cart.
- View profile information including both the saved information, or the purchase history.

###### Authentication of user:
- Register an account - the user is able to do so via the 'Register an Account'.
- Sign In function - if no username is in session, the user is redirected to an html Sign In page.
- Sign Out function - if the user clicks on the Sign Out button at the top right corner of the navigation menu in desktop or bottom option 
in the mobile menu, the user is automatically logged out. The username in session is removed.

### Features Left to Implement
1. Ratings - implement an option for users to rate products that they have purchased. This would ideally be averaged, and then update on the 'Product' model.
2. Sub product categories - be able to include more sub categories under the main categories.
3. Profile details - be able to display and store a profile picture. Maybe this picture could be displayed in the sidenav once the user is logged in.
4. Product details - be able to see additional pictures under the single product view.
5. Article images - display images inbetween the different paragraphs of the single article views.
6. Animations - I would have liked to add more JS animations and effects to give a more dynamic experience to the site.

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
- Font Awesome: Used the icons from this library.
  [Learn more about Font Awesome.](https://fontawesome.com/icons?d=gallery)

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

Please see a detailed view of all of the libraries included in this project in [requiements.txt](/workspace/a-telier-beauty/requirements.txt).

### Tools:
###### Production Environment:
- Gitpod: Used as the coding environment for this project.
- Github: Used to store all repositories for this project, as well as to deploy the site via GitPages.
- Heroku: Used to host the public/production version of the app

###### Closing knowledge gaps:
- W3schools: Used to clarify and solidify knowledge acquired during the course.
- Stack Overflow: Used as support when troubleshooting and fixing bugs.

Please see a detailed view of all of the different blogs and ressorces I have used in [credits.md](anotherstore/documentation/credits.md).

##  Testing
Manual tests have been conducted via the Google Chrome Developer Tools to verify that all pages are working properly. The site 
functionalities have been tested in live/deployed version by 3 other users from Android and iOs devices.

I have tested:
* Products & Category:
- Sorting products by different attributes.
- Filtering products by using menu categories, and by clicking on the tag categories.
- Navigating through the site by clicking on category banners and suggested product banners.

Articles:
- Similar as above, tested viewing single articles.
- Tested the tags by category filters.
- Tested navigating to other areas of the site via the banners in the Article pages.

* Profile:
- Creating a new accounts.
- Login in to the account.
- Registering a new account.
- Checking if information was saved to my profile.

* Cart:
- Adding a product and removing a product.
- Adjusting the quantities in the cart.
- Removing products completely from the cart.

* Checkout:
- Proceeding with payment with a test card.
- Checking that the order appears in my profile page.
- Tested that the webhooks were working properly.

###### Navigation menu:
The navigation menu is mobile-first, so it looks the same both in mobile and in desktop. You are able to open it by clicking on
 the bars icon, and then close it by clicking on the cross at the top of the open sidemenu var.
 So essentially the functionalities are the same.

1. Desktop:
- The user is able to navigate to and from all pages via the navigation menu.
- In the desktop menu, the user is able to see the categories set in the dropdown menu.
- Sign In / Sign Out button in the navigator toggles according to whether the user is in session or not.
- The Search bar displays in the middle of the top navigation bar, but does not display in small screens.

2. Mobile:
- The mobile menu triggers when the hamburger/bars icon is clicked.
- The menu closes when you click on the cross on the top left of the menu.
- All of the options and icons in the menu display correctly.
- The navigation functionality has been checked in different devices incl. mobile devices via the Google Chrome Developer Tools.
- Sign In / Sign Out button in the navigator toggles according to whether the user is in session or not.
- The Search bar appears in the side navbar menu instead of in the topnav menu.

###### Home Page:
- The correct information displays from database records.
- All users (without needing to log in) are able to view different banners redirecting to product categories and articles.
- The contents resize and are able to be seen properly in all different devices. This function has been testsed by using Google 
Chrome Developer Tools.

###### Product & Category Pages:
For all pages, the contents resize and are able to be seen properly in all different devices. This function has been testsed by using Google 
Chrome Developer Tools.

###### Profile Page:
For all pages, the contents resize and are able to be seen properly in all different devices. This function has been testsed by using Google 
Chrome Developer Tools.
- The user is able to see the records (s)he has added to the database.
- If a user is logged in, a welcome message displays, if a user is not logged in there is no message displaying.

###### Authentication & User Pages:
- If there is no username in session, the user is prompt to a Sign In form.
- If the user does not have an account, the Register link under the Sign In form works properly.
- A user that is not sign in can not access the Profile Page view.

## Deployment
This application is hosted in Heroku, which you would need an account for.
###### To deploy this project yourself:
1. Copy the repository from Github.
2. Open a Heroku account.
3. Create a new project under Heroku.
4. Go to the Settings tab in Heroku.
5. Scroll down and click on Config Var to reveal the Config Variables.
    Here we need to add the following variables:
    - Secret keywords
    - Stripe variables
    - AWS variables ---> this needs to be set-up separately, in order to store images via custom_storage.py
    - Postgres database
5. Go to the Deploy tab in Heroku.
6. Connect Heroku to Github directly via API connector.
7. When propted, logged in to your Github account. If everything went well, the Github sub-tab should say Connected in green.
8. In the same tab, make sure that the right repository is connected.
9. Select automatic deployments to Master to make the updating of the site easier.

To deploy locally, you may run python3 manage.py runserver.

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

###### Structure:
* Set-up
- [Python Django Web Framework - Full Course for Beginners at FreeCodeCamp.org](https://www.youtube.com/watch?v=F5mRW0jo-U4&feature=share)
- [Django Documentation](https://docs.djangoproject.com/en/3.1/)
- [How to structure Django project - Stack Overflow](https://stackoverflow.com/questions/22841764/best-practice-for-django-project-working-directory-structure)

* Paths
- [What is init used for & modifying default path](http://effbot.org/pyfaq/what-is-init-py-used-for.htm)
- [Search Path in Python](https://docs.python.org/3/install/index.html#modifying-python-s-search-path)

* Blog
- [How to build a Django blog](https://djangocentral.com/building-a-blog-application-with-django/)
- [Slugfield in Django](https://www.geeksforgeeks.org/slugfield-django-models/)

###### Navbar:
* Sidenav
- [Materialize sidenav](https://materializecss.com/sidenav.html)
- [Collapsible dropdown submenu](https://jsfiddle.net/zmgxz3o1/)

###### Authentication:
- [Allaut](https://django-allauth.readthedocs.io/en/latest/configuration.html)

###### Styling:
- [Git Commit Emojis](https://gist.github.com/parmentf/035de27d6ed1dce0b36a)

* Overlay spinner
- [Spinner](https://codepen.io/umng/pen/wZzbbQ)

* Cart badge
- [Shoppig cart badge](https://stackoverflow.com/questions/29313879/shopping-cart-number-of-items-in-cart-css)
- [Badges](https://www.w3schools.com/bootstrap4/bootstrap_badges.asp)

###### Forms:
- [Form fields (Crispy forms and Django fields)](https://www.geeksforgeeks.org/autofield-django-models/)
- [Advanced Crispy Forms](https://simpleisbetterthancomplex.com/tutorial/2018/11/28/advanced-form-rendering-with-django-crispy-forms.html)

###### Payment:
- [Stripe documentation](https://stripe.com/docs/payments)
- [Accept a card payment](https://github.com/stripe-samples/accept-a-card-payment)
- [Testing Stripe payments](https://stripe.com/docs/testing)

- [Mandatory Stripe fields](https://stripe.com/docs/api/payment_methods/create#create_payment_method-billing_details)
- [Payment Intent Shipping](https://stripe.com/docs/api/payment_intents/confirm#confirm_payment_intent-shipping)

###### Footer:
- [Materialize footer](https://materializecss.com/footer.html)

###### Debugging:
- [Diffchecker](https://www.diffchecker.com/)

## Acknowledgements
I would like to thank the code institute tutors Scott, Igor and Michael who supported me in debugging, and overcoming the different challenges I encountered.
I would also like to thank my fiancé, Jonatan, for his unconditional support.