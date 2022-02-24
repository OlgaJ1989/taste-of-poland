# Taste of Poland

Taste of Poland is a restaurant website designed to allow customers to make, edit and delete reservations. Users can also view the menu, gallery, and the venue's contact details.

TO UPDATE: The website can be accessed [here](https://olgaj1989.github.io/sussex-walks/).

![Mockup](https://github.com/OlgaJ1989/taste-of-poland/blob/main/docs/mockup.PNG)

## Features

### Existing features

* Navigation Bar 
    * Includes direct links to all parts of the website, allowing the user to easily navigate between them. 
        1. When logged OUT, the user can see the following links in the navbar: Home, Menu, Reservations (with a Reserve A Table dropdown), Gallery, Contact, Register, Login.

           ![Navigation Logged Out](https://github.com/OlgaJ1989/taste-of-poland/blob/main/docs/logged-out-new.PNG)

        2. When logged IN, the user can see the following links in the navbar: Home, Menu, Reservations (with Reserve A Table and My Reservations dropdowns), Gallery, Contact, Logout.  

           ![Navigation Logged In](https://github.com/OlgaJ1989/taste-of-poland/blob/main/docs/logged-in-new.PNG)

        3. On smaller devices the menu links scale down to a toggler, allowing for a cleaner design.

           ![Navigation Responsive](https://github.com/OlgaJ1989/taste-of-poland/blob/main/docs/responsive-menu.PNG)
      
* Landing page image with overlaying jumbotron
    * The index.html page (Home) includes a background picture inspired by Polish folk art, with a one-sentence description of the website and a button leading directly to a booking page (if logged in) or to the login page (if logged out).
    
      ![Jumbotron](https://github.com/OlgaJ1989/taste-of-poland/blob/main/docs/jumbotron.PNG)

* About Us section
    * A small section containing a short description of the restaurant. 

      ![About](https://github.com/OlgaJ1989/taste-of-poland/blob/main/docs/about-us.PNG)

* Cards section with links to Gallery and Menu pages
    * A section containing two cards with links to the two pages, catching the eye and allowing quick navigation. The design is responsive - users will see 2 cards next to each other on bigger screens and 1 card on top of the other on smaller devices. 

      ![Cards](https://github.com/OlgaJ1989/taste-of-poland/blob/main/docs/cards.PNG)

* Interactive footer across all pages
    * It consists of clickable icons linking the user to a choice of social media platforms (Facebook, Twitter, Instagram). All links open in new tabs so the user does not have to leave the Sussex Walks page.

      ![Footer](https://github.com/OlgaJ1989/taste-of-poland/blob/main/docs/footer.PNG)

* Menu page
    * The Menu located in menu.html will provide the user with a list of dishes that can be ordered at the restaurant along with their prices. It consists of 3 tabs (Soups, Mains, Desserts) that can be easily switched between. 

      ![Menu](https://github.com/OlgaJ1989/taste-of-poland/blob/main/docs/menu.PNG) 

* Gallery page
    * The Gallery located in gallery.html will provide the user with a collection of photographs showcasing some of the dishes served in the restaurant. The responsive design of the gallery means the images will still be viewed in a good resolution on a smaller screen.

      ![Gallery](https://github.com/OlgaJ1989/taste-of-poland/blob/main/docs/gallery.PNG)  

* Contact page
    * The contact.html page consists of restaurant contact info (phone, address, email) and an embedded Google map with the location. 
    
      ![Contact](https://github.com/OlgaJ1989/taste-of-poland/blob/main/docs/contact.PNG)

* Reservation / booking page
    * The 'Book' tab links with a page that consists of a reservation / booking form which allows the user to book a table for a chosen date and time up to a day before and for up to 6 guests.  
    
      ![Reservation](https://github.com/OlgaJ1989/taste-of-poland/blob/main/docs/booking-form.PNG)

* My Bookings page
    * The 'My Bookings' tab display all the bookings that the user has made. It only shows bookings made by the person who is currently logged in. From here the user can edit and delete existing bookings.      
    
      ![Bookings](https://github.com/OlgaJ1989/taste-of-poland/blob/main/docs/bookings.PNG)

* Deletion confirmation page
    * A template that renders after the user chooses to delete a booking, giving them a chance to confirm their choice or go back to safety.      
    
      ![Delete](https://github.com/OlgaJ1989/taste-of-poland/blob/main/docs/delete.PNG)

* Sign In / Login page
    * Allows the user to log in to an existing account in order to book a table and view existing bookings. It also provides the user with the link to register.      
    
      ![Sign In](https://github.com/OlgaJ1989/taste-of-poland/blob/main/docs/sign-in.PNG)

* Sign out / Logout confirmation page
    * A template that renders after the user chooses to log out, giving them a chance to confirm in case they clicked the link by mistake.       
    
      ![Sign Out](https://github.com/OlgaJ1989/taste-of-poland/blob/main/docs/sign-out-confirm.PNG)

*  404 page
    * A custom 404 page has been made to make it easy for the user to come back to the game page after they tried to move to a non-existent page.

      ![404](https://github.com/OlgaJ1989/taste-of-poland/blob/main/docs/404.PNG)

* A favicon
    * A favicon has been added to make it easier for users to find the Taste of Poland page if multiple tabs are open. 
    
      ![Favicon](https://github.com/OlgaJ1989/taste-of-poland/blob/main/docs/favicon.PNG)

### Features left to implement

TO UPDATE 

## User Experience Design

Taste of Poland is a responsive website of a non-existent Polish restaurant in Brighton. 

The aim of the website is: 
- to give users the possibility of viewing the restaurant's Menu and photo Gallery so that they can decide in advance of their visit whether the restaurant and its offering is something they would like to try out;
- to give users the possibility of registering for an account in order to be able to book a table so that the bookings are held in a secure environment where no one can access and tamper with them without login details;
- to give the site owners / authorised staff the possibility of viewing the bookings users made so they can be modified or deleted if needed;
- to give users the possibility of accessing the website and booking a table on any device;
- to give users the details necessary for them to be able to contact the venue.

### User Stories

User stories for this project can be viewed on [Trello](https://trello.com/b/OdCkLJxF/kanban-template).

![UX Epic](https://github.com/OlgaJ1989/taste-of-poland/blob/main/docs/ux_epic.PNG)

1. As a user, I want the main purpose of the website to be clear so that upon entering I immediately know what its purpose is.
    * Acceptance Criteria:
        - Restaurant logo ad information is displayed on the main page with clear information on what the site's purpose is.
    * Implementation:
        - The Home page will contain the main website title of "Taste of Poland", situated in the navbar section. 
        - It will also contain information about the site's general purpose and about the restaurant itself, to make what the site is intended for immediately clear to the user.
        
2. As a user, I want to be able to easily navigate between the different parts / pages of the website so that I can find content quickly and easily on any device.
    * Acceptance Criteria:
        - Navigation menu to allow users to navigate the site with ease.
        - Collapsible mobile menu to allow users to navigate the site from a mobile device. 
        - All navigation links should navigate to the correct pages.
        - The 'My Reservations' dropdown option should only appear for signed-in users.
    * Implementation:
        - A navigation menu will be created to allow users to navigate through the site. It will be collapsible on a mobile device, and positioned at the top right of the logo element.
        - When a user is not logged in, 'Home', 'Menu', 'Reservations' (with a 'Reserve a Table' dropdown), 'Gallery', 'Contact' 'Register' and 'Login' navigation items will be displayed.
        - When a user is logged in, an extra 'My Reservations' dropdown will appear under the 'Reservations' link, and 'Register' and 'Login' will disappear, with 'Logout' appearing in their place.

3. As a user, I want to be able to easily find links to any social media channels that the restaurant might be running.
    * Acceptance Criteria:
        - Social media links included to allow users to navigate to linked accounts with ease.
        - All links should navigate to the correct pages.
    * Implementation:
        - Social media links in the form of FontAwesome icons will be added to the footer and appear on each page.

4. As a user, I want to be able to view the menu so I can choose what I would like to order in advance of my visit.
    * Acceptance Criteria:
        - A list of dishes that the restaurant serves, along with their descriptions and pricing.
        - Clear division between types of dishes.
    * Implementation:
        - The 'Menu' tab will include an interactive menu consisting of three tabs: 'Soups', 'Mains' and 'Desserts'. Users will be able to easily and quickly switch between these tabs to reveal the list of relevant dishes.

5. As a user, I want to be able to contact the restaurant in case I have any questions regarding the venue or a reservation I made, or if I encounter any issues with the website. 
    * Acceptance Criteria:
        - A 'Contact' page which includes the venue's contact information.
    * Implementation:
        - A 'Contact' page will be created and it will include the venue's contact information (such as an address, email and phone number) as well as an embedded Google map showing the restaurant's location. This page will also include the Opening Hours.

6. As a user, I want to be able to view a photo gallery of dishes, so I can decide whether they look appealing enough for me to visit and try them out.
    * Acceptance Criteria:
        - A 'Gallery' page displaying photos of the dishes present on the restaurant's menu.
    * Implementation:
        - A 'Gallery' page will be created, using high-quality photos of the food the restaurant serves. It will be made responsive so that users can enjoy good resolution also on smaller devices. 
 
![Admin Profile Epic](https://github.com/OlgaJ1989/taste-of-poland/blob/main/docs/ap_epic.PNG)

7. As a site admin, I want to be able to view, modify or delete existing bookings.
    * Acceptance Criteria:
        - An 'Admin' page displaying all existing bookings for every user, where the restaurant's owners / authorised staff can view, modify and delete them.
    * Implementation:
        - A Django built-in admin panel will be utilised to create a page where staff authorised as Django 'superusers' can view the users that registered for an account, as well as view, modify, and delete their reservations if necessary.

8. As a site admin, I want to make the option of reserving a table available only to registered users.
    * Acceptance Criteria:
        - Booking / reservation form not available for unregistered users.
    * Implementation:
        - If a user that is not logged in clicks on the 'Reserve a table' link in the 'Reservations' dropdown, they will be redirected straight to the 'Login' page. If they do not have login details, the information on the 'Login' page will direct them to the 'Register' page. The 'Reserve a table' link will display the booking form only if they are logged in.   

![User Profile Epic](https://github.com/OlgaJ1989/taste-of-poland/blob/main/docs/up_epic.PNG)

9. As a user, I want to be able to create, view, edit and delete a table reservation.
    * Acceptance Criteria:
        - A custom booking form allowing the users to book a table for a chosen date and time.
        - A 'My reservations' page displaying all the reservations that they have so far created.
        - Functionality allowing the users to edit and delete the existing reservations.
    * Implementation:
        - A custom reservation form will be created (under 'Reserve a table' in the 'Reservations' dropdown), allowing registered users to book a table for a chosen date and time.
        - When the booking is submitted, the user will be redirected to 'My reservations' page that will display the reservation details, such as the first and last name of the main guest, date, time, table and number of guests.
        - 'Edit' and 'Delete' buttons will appear next to each created booking, allowing users to modify or cancel bookings easily.

10. As a user, I want to be able to register for an account to be able to make reservations and store them in a secure environment.
    * Acceptance Criteria:
        - A custom registration form / page allowing the users to register for an account.
    * Implementation:
        - A reservation form / page will be created using the allauth library, allowing users to register for an account. 
        

11. As a user, I want to be able to log into my account to make a reservation and view my bookings.
    * Acceptance Criteria:
        - A custom login form allowing the users to log in to the website.
    * Implementation:
        - A login form will be created using the allauth library, allowing users to log in to an existing account.

### Wireframes

* Home

    ![WireframeHome](https://github.com/OlgaJ1989/taste-of-poland/blob/main/docs/wireframe_home.PNG)

* Menu

    ![WireframeMenu](https://github.com/OlgaJ1989/taste-of-poland/blob/main/docs/wireframe_menu.PNG)

* Gallery

    ![WireframeGallery](https://github.com/OlgaJ1989/taste-of-poland/blob/main/docs/wireframe_gallery.PNG)

* Book a table

    ![WireframeReserve](https://github.com/OlgaJ1989/taste-of-poland/blob/main/docs/wireframe_booking_form.PNG)

* Existing reservations

    ![WireframeReservations](https://github.com/OlgaJ1989/taste-of-poland/blob/main/docs/wireframe_reservations.PNG)

* Contact Us

    ![WireframeContact](https://github.com/OlgaJ1989/taste-of-poland/blob/main/docs/wireframe_contact.PNG)

* Register

    ![WireframeRegister](https://github.com/OlgaJ1989/taste-of-poland/blob/main/docs/wireframe_register.PNG)

* Login

    ![WireframeLogin](https://github.com/OlgaJ1989/taste-of-poland/blob/main/docs/wireframe_login.PNG)


## Technologies

* [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) has been used to structure the website.
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) has been used to style the website.
* [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) was used to tweak the settings of login / logout notifications / messages.
* [Python](https://www.python.org/) was used as the main language in which this project was coded.
* [Django](https://www.djangoproject.com/) was the framework used to build this website.
* [Bootstrap](https://getbootstrap.com/docs/4.0/getting-started/introduction/) was used to create and style the front end of the website.
* [Font Awesome](https://fontawesome.com/) icons have been used for the social media links in the Footer and on the Contact page.    
* [Google Fonts](https://fonts.google.com/) have been used to import Tangerine and Roboto Slab fonts. 
* [Favicon](https://favicon.io/) was used to create the favicon for the website.
* [Techsini](http://techsini.com/multi-mockup/index.php) mockup generator was used to create the mockup image for the README.md file. 
* [Google Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools) were used to inspect elements of the website and test different styles. 
* [GitHub](https://github.com/) has been used to store the code, images, and other contents of the website. 
* [Heroku](https://dashboard.heroku.com/apps) was used to deploy the game to the web.
* [Git](https://git-scm.com/) was used to track changes made to the project and to commit and push code to the repository.
* [Wave Web Accessibility Evaluation Tool](https://wave.webaim.org) was used to test the website's accessibility.
* [Lighthouse](https://developers.google.com/web/tools/lighthouse#devtools) was used to run an audit of the website. 
* [Grammarly](https://www.grammarly.com) was used to check for typos in Readme.md.


## Testing

* Check the responsiveness of the website on different screen sizes across different browsers (Chrome, Firefox, Opera).
    * Test:
        1. Open the website in each of the aforementioned browsers.
        1. Right-click on the screen and choose 'Inspect' ('Inspect element' on Opera).
        1. Grab and drag the responsive window slowly down to 300px and then back again, checking that everything is displayed correctly in each size / breakpoint.
    * Result:
        * All elements are responsive and display correctly in each of the browsers and each of the window sizes.
    * Additionally, I also had a chance to check the responsiveness on several 'real' devices, such as Samsung Galaxy S8, Samsung Galaxy A42, Xiaomi POCO X Pro, iPhone X, iPhone 13 Pro, Samsung Galaxy Tab A. All elements are responsive and display correctly on each of these devices.

* Check that the links in the navigation bar navigate to the correct pages. 
    * Test:
        1. Open the website in a browser.
        1. Click on all navigation items one by one to make sure the attached links are correct and that they lead the user to the correct parts of the website.
    * Result:
        * All links working and directing users to the correct pages.

* Check that the 'My reservations' tab in the 'Reservations' dropdown appears only if a user is signed in.

* Check that the 'Reserve a table' tab in the 'Reservations' dropdown redirects to the 'Login' page if a user is signed out.

* Check that the 'Reserve a table' tab in the 'Reservations' dropdown displays a table reservation form if a user is signed in.

* Check that when user clicks 'Logout' they are redirected to a confirmation page ('Are you sure you want to sign out?')

* Check that user is correctly notified when they have logged in. 

* Check that user is correctly notified when they have logged out.

* Make sure that unauthorised users cannot view, edit or delete someone else's reservations.

* Check that the links to social media pages in the Footer work and open in new tabs.
    * Test:
        1. Open the website in a browser.
        1. Click on all social media links (Facebook, Twitter, YouTube, Instagram) one by one to make sure that the links are in working order and that they all open in a separate tab.
    * Result:
        * All links are working and all of them open in separate / new tabs.

* Check that the links included in the 'Gallery' and 'Menu' cards in the Home page work and redirect correctly to the 'Gallery' and 'Menu' pages.
    * Test:
        1. Open the website in a browser.
        1. Scroll down the Home page to the cards section.
        1. Click on the 'View Menu' button in the 'Menu' card to make sure that the link works and redirects to the 'Menu' page.
        1. Then click on the 'View Gallery' button in the 'Gallery' card to make sure that the link works and redirects to the 'Gallery' page.        
    * Result:
        * All links are working and all of them redirect to correct pages.

* Check validation of the Reservation form.
    * Test:
        1. Open the website in a browser and navigate to the Contact Us page.
        1. Fill in the form leaving different input areas empty each time to make sure there is a warning message displayed each time you leave any of the fields empty. 
    * Result: 
        * The form cannot be submitted until each of the input fields has been filled in correctly so the validation is working.

### Validator testing

* HTML - when the code was passed through the official [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcode-institute-org.github.io%2Flove-running-2.0%2Findex.html) 
    * I have received a few errors referring to the validator not recognising jinja. To avoid this, I have taken the HTML code straight from each page by clicking on each navbar element in turn, right-clicking and choosing 'View page source' to get clean HTML. 
    * Across all pages (inheriting from base.html): 'Error: Stray end tag div. From line 86, column 5; to line 86, column 10'. After checking the code in my repository I did not find this to be true as all the tags were present. I believe there was a glitch in the code taken from 'View page source' (possibly due to jinja not displaying there). There is actually no problem with the code.

    ![Error](https://github.com/OlgaJ1989/taste-of-poland/blob/main/docs/html-error.PNG) 

    * In contact.html: 'Bad value 100% for attribute width on element iframe: Expected a digit but saw % instead.' I have fixed this by moving the 'width' attribute from the 'iframe' tag in the template to style.css.    
    
* CSS - no errors were found when code was passed through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator)

    ![CSS](https://github.com/OlgaJ1989/taste-of-poland/blob/main/docs/css-validator.PNG)


* JavaScript - when running the code through [JSHint linter](https://jshint.com/) I received the following error message referring to the two 'let' variables: "'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).". I copied /*jshint esversion: 6 */ into the linter window to override this. I have also used /*globals bootstrap */ to stop JSHint from treating 'bootstrap' in let alert = new bootstrap.Alert(messages) as an undefined variable. After I did this, no more errors appeared.

    ![jShint](https://github.com/OlgaJ1989/taste-of-poland/blob/main/docs/jshint.PNG)


* Python - when running the code through [PEP8 linter](http://pep8online.com/) I received a few 'line too long' errors referring to the automatically generated code in settings.py. As the code was auto-generated and there was not an easy fix to shorten the lines, I have left this error in. There were no errors in any other files that have been coded and customised by me.  


* Accessibility - when using the [Wave Web Accessibility Evaluation Tool](https://wave.webaim.org) to test the site's accessibility, I have encountered the following errors and/or warnings:
    * I skipped a heading level on the menu.html page (I used h1 and h3, leaving out h2). I fixed this by changing the h3 elements to h2. No further errors have been found after I applied this fix and passed the site through the validator again. 
    * There was not enough contrast between the navbar background and the font of its elements. I have corrected this by changing the basic background color of 'red' to a slightly deeper #d40b0b. 
    * Aria-labels in the Gallery page were missing. I have added them to all images. 
    * No further errors have been found after I applied the above fixes and passed the site through the validator again.
    
    ![Wave](https://github.com/OlgaJ1989/taste-of-poland/blob/main/docs/wave.PNG)

### Unfixed bugs

No other bugs found.

## Deployment

TO UPDATE BEFORE FINAL DEPLOYMENT!

The below steps were followed to deploy this project to Heroku:
1. Go to [Heroku](https://dashboard.heroku.com/apps) and click 'New' to create a new app.
2. After choosing the app name and setting the region, press 'Create app'.
3. Go to 'Resources' to add a database and scroll down to 'Add-ons'. Search for 'Postgres' and choose 'Heroku Postgres' from available options.
4. Go to 'Settings' and navigate to 'Config Vars'. As the Postgres database has been connected, the DATABASE_URL is already there. Add the remaining config vars: CLOUDINARY_URL, SECRET_KEY, (the values for these variables depend on your own personal set up and will not be added here for security reasons). 
5. Leave 'Settings' and go to 'Deploy'. Scroll down and set 'Deployment Method' to GitHub. Once GitHub is chosen, find your repository and connect it to Heroku.
6. Scroll down to Manual Deploy, make sure the 'main' branch is selected and click 'Deploy Branch'.

TO UPDATE 
7. The deployed app can be found TO UPDATE [here](https://stranded.herokuapp.com/).

## Credits

### Content 

All the general 'blurb' across the website has been written by me, apart from the names and descriptions of the dishes in the Menu. These have been taken and adapted from [StayPoland](https://www.staypoland.com/poland/polish-food/).

### Media 

All photos / images have been taken from [ShutterStock](https://www.shutterstock.com/.)

### Code

I have used this code snippet from [Bootdey](https://www.bootdey.com/snippets/view/bs4-Food-Menu) to create the Menu page.

### Acknowledgements

As always, I'd like to thank my mentor Daisy McGirr for her guidance throughout this project. 
