# Taste of Poland

Taste of Poland is a restaurant website designed to allow customers to book, edit and delete tables through a custom booking form. Users can also view the menu, gallery and the venue's contact details.

The website can be accessed [here](https://olgaj1989.github.io/sussex-walks/).

![Mockup](https://github.com/OlgaJ1989/taste-of-poland/blob/main/static/images/readme/mockup.jpg)

## Features

### Existing features

* Navigation Bar 
    * Includes direct links to all parts of the website, allowing the user to easily navigate between them. 
        1. When clicked, the logo leads to the home page.
        
        2. When logged OUT, the user can see the following links in the navbar: Home, Menu, Book, Gallery, Contact, Register, Login.

        ![Navigation1](https://github.com/OlgaJ1989/taste-of-poland/blob/main/static/images/readme/logged-out.PNG)

        3. When logged IN, the user can see the following links in the navbar: Home, Menu, Book, My Bookings, Gallery, Contact, Logout.  

        ![Navigation2](https://github.com/OlgaJ1989/taste-of-poland/blob/main/static/images/readme/logged-in.PNG)

        4. On smaller devices the menu links scale down to a toggler, allowing for a cleaner design.

        ![Navigation3](https://github.com/OlgaJ1989/taste-of-poland/blob/main/static/images/readme/responsive-menu.PNG)
       

* Landing page image with overlaying jumbotron
    * The index.html page (Home) includes a background picture inspired by Polish folk art, with a one-sentence description of the website and a button leading directly to a booking page (if logged in) or to the login page (if logged out).
    
    ![Jumbotron](https://github.com/OlgaJ1989/taste-of-poland/blob/main/static/images/readme/jumbotron.PNG)

* About Us section
    * A small section containing a short description of the restaurant. 

    ![About](https://github.com/OlgaJ1989/taste-of-poland/blob/main/static/images/readme/about-us.PNG)

* Cards section with links to Gallery and Menu pages
    * A section containing of two cards with links to the two pages, catching the eye and allowing quick navigation. The design is responsive - users will see 2 cards next to each other on bigger screens and 1 card on top of the other on smaller devices. 

    ![Cards](https://github.com/OlgaJ1989/taste-of-poland/blob/main/static/images/readme/cards.PNG)

* Interactive footer across all pages
    * It consists of clickable icons linking the user to a choice of social media platforms (Facebook, Twitter, Instagram). All links open in new tabs so the user does not have to leave the Sussex Walks page.

    ![Footer](https://github.com/OlgaJ1989/taste-of-poland/blob/main/static/images/readme/footer.PNG)

* Gallery
    * The Gallery located in gallery.html will provide the user with a collection of photographs showcasing some of the dishes served in the restaurant. Responsive design of the gallery means the images will still be viewed in a good reolution on a smaller screen.

    ![Gallery](https://github.com/OlgaJ1989/taste-of-poland/blob/main/static/images/readme/gallery.PNG)  

* Contact Us form
    * The contact.html page consists of a form which users can use in order to contact the admin with any questions / queries. 
    
    ![Form](https://github.com/OlgaJ1989/sussex-walks/blob/master/docs/form.png)

* A favicon
    * A favicon has been added to make it easier for users to find the Sussex Walks page if multiple tabs are open. 
    
    ![Favicon](https://github.com/OlgaJ1989/sussex-walks/blob/master/docs/favicon.png)

### Features left to implement

I would like to include another page consisting of a form and called Design Your Walk or similar. The form would consist of a short survey, covering areas such as difficulty, length, and type of a walk. Radio buttons and checkboxes would be provided for the user to be able to make their choices, which they could then submit to the admin to receive personalised walk ideas tailored to their choices.  

## Technologies

* HTML has been used to structure the website.
* CSS has been used to style the website.
* [Font Awesome](https://fontawesome.com/) icons have been used on the Walking Tips page and for social media links in the Footer.    
* [Google Fonts](https://fonts.google.com/) have been used to import Amatic SC and Josefin Slab fonts. 
* [Colormind](http://colormind.io) was used to determine the color pallette for the website.
* [Hex Color Tool](https://www.hexcolortool.com/) was used to convert Hex to RGBA.
* [Favicon](https://favicon.io/) was used to create the favicon for the website.
* [Techsini](http://techsini.com/multi-mockup/index.php) mockup generator was used to create the mockup image for the readme.md file. 
* [Google Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools) were used to inspect elements of the website and test different styles. 
* [GitHub](https://github.com/) has been used to store the code, images, and other contents of the website. 
* [Git Pages](https://pages.github.com/) was used to deploy the website to the web.
* [Git](https://git-scm.com/) was used to track changes made to the project and to commit and push code to the repository.
* [Wave Web Accessibility Evaluation Tool](https://wave.webaim.org) was used to test the website's accessibility.
* [Lighthouse](https://developers.google.com/web/tools/lighthouse#devtools) was used to run an audit of the website. 

## Testing

* Check the responsiveness of the website on different screen sizes across different browsers (Chrome, Firefox, Opera).
    * Test:
        1. Open the website in each of the aforementioned browsers.
        1. Right-click on the screen and choose 'Inspect' ('Inspect element' on Opera).
        1. Grab and drag the responsive window slowly down to 300px and then back again, checking that everything is displayed correctly in each size / breakpoint.
    * Result:
        * All elements are responsive and display correctly in each of the browsers and in each of the window sizes.

* Check that the links in the navigation bar navigate to correct pages. 
    * Test:
        1. Open the website in a browser.
        1. Click on all navigation items (Home, Walking Tips, Gallery, Contact Us) one by one to make sure the attached links are correct and that they lead the user to the correct parts of the website.
    * Result:
        * All links working and directing user to the correct pages.

* Check that the links to social media pages in the Footer work and open in new tabs.
    * Test:
        1. Open the website in a browser.
        1. Click on all social media links (Facebook, Twitter, YouTube, Instagram) one by one to make sure that the links are in working order and that they all open in a separate tab.
    * Result:
        * All links are working and all of them open in separate / new tabs.

* Check that the name of the page user is currently on is highlighted (underlined) in the navigation bar.
    * Test:
        1. Open the website.
        1. Open each of the pages in the navigation bar to see whether the active page is underlined in the menu.
    * Result:
        * Each of the navigation bar elements becomes underlined when the page is active.
    
* Check that each of the navigation bar elements displays as underlined when hovered over.
    * Test:
        1. Open the website.
        1. Hover over each of the navigation bar elements with the cursor to make sure that they display and underline when hovered over. 
    * Result:
        * Each element becomes udenrlined when hovered over with a mouse cursor.
                
* Check validation of the Contact Us form.
    * Test:
        1. Open the website in a browser and navigate to the Contact Us page.
        1. Fill in the form leaving different input areas empty each time to make sure there is a warning message displayed each time you leave any of the fields empty. 
    * Result: 
        * The form cannot be submitted until each of the input fields has been filled in correctly so the validation is working.

### Validator testing

* HTML - when the code was passed through the official [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcode-institute-org.github.io%2Flove-running-2.0%2Findex.html) I have received the following error notification: "Element h3 not allowed as child of element label in this context." referring to all input labels in the Contact Us form. To fix this, I have changed all h3 elements to span elements as per the advice found in [this Stackoverflow post](https://stackoverflow.com/questions/50068995/element-h3-not-allowed-as-child-of-element-label-in-this-context-html). No further errors have been found after I applied this fix and passed the code through the validator again.
* CSS - no errors were found when code was passed through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fvalidator.w3.org%2Fnu%2F%3Fdoc%3Dhttps%253A%252F%252Fcode-institute-org.github.io%252Flove-running-2.0%252Findex.html&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en#css)
* Accessibility - when using the [Wave Web Accessibility Evaluation Tool](https://wave.webaim.org) to test the site's accessibility, I received 2 errors:
    * There was not enough contrast between the background and font of the 'Submit' button in the Contact Us form. I have corrected this by changing the background color #559e79 to #32644b. No further errors have been found after I applied this fix and passed the site through the validator again.
    * Two of the aria-labels in the Gallery page were identical. I have corrected this by changing the name of one of them. No further errors have been found after I applied thise fix and passed the site through the validator again.

### Unfixed bugs

No other bugs found.

## Deployment

Sussex Walks was deployed to GitHub Pages by following the below steps:
1. Navigate to the ['sussex-walks' repository](https://github.com/OlgaJ1989/sussex-walks) on GitHub.
1. Navigate to the 'Settings' tab.
1. Navigate to 'Pages' from the menu on the left. 
1. Select 'master' branch in the source drop-down.
1. Click 'Save'.
1. A link to the live deployed page is generated and can be found here: https://olgaj1989.github.io/sussex-walks/

## Credits

### Content 

The written content has been developed by me, Olga Jasinska, using my past experience of walking in and around of Brighton. 

### Media 

All photos have been taken from my private collection or provided by my partner Ben Butler with his permission. 

### Code

When creating flexbox and media queries I used tutorials and some base code from [W3Schools](https://www.w3schools.com/css/css3_flexbox.asp) modules on CSS Flexbox and CSS Flex Responsive.  

### Acknowledgements

I'd like to thank my mentor Daisy McGirr for her guidance throughout this project.
