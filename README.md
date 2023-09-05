# **Dublin Eats**

## **Overview**

Dublin Eats is a website designed to allow a user to find and review Restaurants in Dublin. The site features a search function that allows users to search for any Restaurant in Dublin. The restaurants can be viewed according to cuizines. Users will be able to view Restaurant details such as location, price range, etc. Users will also be able to review Restaurants and pin some restaurants page onto their own customizable profile page. Each user needs to sign up to be able to review and search for restaurants. Each user will have a profile page that they would be able to edit once logged in.

## **Project Goals**

This is my fourth portfolio project for [Code Institute](https://codeinstitute.net/). In this project i aim to demonstrate my goal of showcasing my skills in django , bootstrap etc.

## **Contents**

1. [Overview](#overview)
2. [Project Goals](#project-goals)
3. [UX](#ux)
   - [The Strategy Plane](#the-strategy-plane)
     - [The Ideal User](#the-ideal-user)
     - [Site Goals](#site-goals)
   - [Agile Planning](#agile-planning)
     - [Epics](#epics)
     - [User Stories](#user-stories)
   - [The Skeleton Plane](#the-skeleton-plane)
     - [Wireframes](#wireframes)
     - [Database Schema](#database-schema)
     - [Security](#security)
   - [The Scope Plane](#the-scope-plane)
   - [The Structure Plane](#the-structure-plane)
     - [Features](#features)
     - [Future Features](#future-features)
   - [The Surface Plane](#the-surface-plane)
     - [Design](#future-features)
       - [Colour Scheme](#colour-scheme)
       - [Typography](#typography)
       - [Imagery](#Imagery)
4. [Technologies Used](#technologies-used)
   - [Languages Used](#languages-used)
   - [Frameworks and Tools Used](#frameworks-and-tools-used)
   - [Libraries Used](#libraries-used)
5. [Testing](#testing)
6. [Deployment](#deployment)
7. [Credits](#credits)
8. [Acknowledgements](#acknowledgements)

## **UX**

## **The Strategy Plane**

Dublin Eats websites intends to allow  foodies of Dublin or tourists to discover new restaurants in Dublin which are top rated. Users will be able to search restaurants according to categories and rate/review the ones they have been to. They should be able to create their own profile page where they can also pin the restaurants they would like to visit in the future.

### **The Ideal User**

- User who enjoys food and would like to discover new restaurants or cuizines.
- User resides in Dublin and would share the app to their socials to generate traffic.
- User who will create a list of restaurants that they still want to visit(pin the restaurants)
- User who would rate and review restaurants that they have been to.
- User who has customized their page to showcase their interests in any aspects of food.

### **Site Goals**

- To provide users with all the restaurants and discover new ones.
- To provide users with the ability to review/rate restaurants.
- To provide users with the ability to create their own Profile.
- To provide users with the ability to view other users reviews/ratings.
- To provide users with the ability to pin / favourite the restaurants they want to go to.

### **Agile Planning**

1.	User stories are implemented which identifies the necessary features and functions of the website.
2.	Prioritzie User stories from high importance to least important. This is done using labels such as “must-haves”, “should-haves”, “could-haves”
3.	Categorize user stories further my having labels such as documentations for README and TESTING user stories.
4.	Break userstories into smaller tasks .

The must-have user stories were prioritized first. Certain other user stories were implemented based on time and complexity. Kanan board for the project can be viewed here

### **Userstories**

## **The Skeleton Plane**

#### **Wireframes**

<details><summary>Desktop</summary>

- ![Desktop page 1](/documentation/wireframes/desktop/desktop-homepage.png)
- ![Desktop page 2](/documentation/wireframes/desktop/desktop-restaurants-page.png)
- ![Desktop page 3](/documentation/wireframes/desktop/desktop-restaurant-details.png)
- ![Desktop page 4](/documentation/wireframes/desktop/desktop-userprofile.png)
- ![Desktop page 5](/documentation/wireframes/desktop/desktop-loginpage.png)
- ![Desktop page 6](/documentation/wireframes/desktop/desktop-signup-page.png)

</details>

<details><summary>Tablet</summary>

- ![Tablet page 1](/documentation/wireframes/tablet/tablet-homepage.png)
- ![Tablet page 2](/documentation/wireframes/tablet/tablet-restaurant-page.png)
- ![Tablet page 3](/documentation/wireframes/tablet/tablet-restaurant-detail.png)
- ![Tablet page 4](/documentation/wireframes/tablet/tablet-userprofile.png)
- ![Tablet page 5](/documentation/wireframes/tablet/tablet-login-page.png)
- ![Tablet page 6](/documentation/wireframes/tablet/tablet-signuppage.png)

</details>

<details><summary>Mobile</summary>

- ![Mobile page 1](/documentation/wireframes/mobile/mobile-homepage.png)
- ![Mobile page 2](/documentation/wireframes/mobile/mobile-restaurantpage.png)
- ![Mobile page 3](/documentation/wireframes/mobile/mobile-restaurant-detail.png)
- ![Mobile page 4](/documentation/wireframes/mobile/mobile-user-profile.png)
- ![Mobile page 5](/documentation/wireframes/mobile/mobile-loginpage.png)
- ![Mobile page 6](/documentation/wireframes/mobile/mobile-signup-page.png)

</details>

#### *Flow Chart logic

- ![Flow chart of logic](/documentation/flow-diagram/flow-chart-dublineats.jpg)

#### **Database Scheme**

- ![Entity relationships](/documentation/entity-relationship/entity-relationship.png)

#### **Security**

## **The Scope Plane**

-	User should be able to create , read, update and delete their profiles, ratings and reviews.
-	The website should be responsive to devices from 320px and up.
-	Navbar menu should be shown in a hamburger toggler in smaller devices.
-	The user should be able to access the websites features once they are logged in.
-	User should have a clear understanding of site from home page.
-	Other functionalities available to user- pinning restaurants to their profile, clicking on each restaurant.

## **The Structure Plane**

### **Features**

1. **REGISTERED USER FEATURES**

Registered users for DublinEats would be able to access all features available.

**Across All Pages**

***Navbar***

Users would be able to naviagate the website so that they can find any information they are looking for.

<details><summary>Navbar in desktop</summary>

![Desktop navbar](/documentation/features/home-page/navbar-desktop.png)

![Desktop open navbar](/documentation/features/home-page/navbar-open-desktop.png)

</details>
<details><summary>Navbar in Mobile devices</summary>

![Mobile Navbar](/documentation/features/home-page/navbar-mobile.png)

![Mobile open navbar](/documentation/features/home-page/navbar-open-mobile.png)

</details>
<details><summary>Navbar logged out</summary>

Navbar will look different to users if they have logged out or havnt signed up for website yet. They will not have a profile lab and logout tab, instead they will have access to login tab and signup tab on navbar.

![LoggedOut navbar](/documentation/features/home-page/navbar-loggedout.png)

</details>
<details><summary>Dublin Eats logo</summary>

User can click on logo at any point, and the user will be redirected to the home page

![Dublin Eats Logo](/documentation/features/home-page/logo-feat.gif)

</details>


***Footer***

<details><summary>Footer on desktop</summary>

![Footer desktop](/documentation/features/home-page/footer-desktop.png)

</details>

<details><summary>Footer on mobiles</summary>

![Footer mobile](/documentation/features/home-page/footer-mobile.png)

</details>

**Home Page & features**

<details><summary>Home page desktop</summary>

![Home page desktop](/documentation/features/home-page/home-page-desktop.png)

</details>

<details><summary>Home page mobile</summary>

![Home page mobile](/documentation/features/home-page/home-page-mobile.png)

</details>

<details><summary>Search feature</summary>

Users who open the home page is immediately drawn to this text and search feature overlying the background image.

![Search feature](/documentation/features/home-page/search-feature.png)

</details>

<details><summary>Search validation</summary>

Users who adds input and clicks search button would not be able to seach with numbers, special charectors , no input or blank spaces. 

![Search number validation](/documentation/features/home-page/search-feature-number-validation.gif)
![Search blank validation](/documentation/features/home-page/search-feature-blank-validation.gif)
![Search special charectors validation](/documentation/features/home-page/search-feature-specialchar-feature.gif)

</details>

**Restaurants page & features**

When user clicks on a category from restaurants tab on navbar, a page is rendered which contains a few restaurants of the category you selected in Dublin. A maximum of 8 restaurants are rendered per page.

<details><summary>Restaurants page desktop</summary>

For desktop - User is shown 4 restaurants details displayed as cards in a row.

![Restaurants page desktop](/documentation/features/restaurants-page/restaurantspage-desktop.gif)

</details>

<details><summary>Restaurants page mobile</summary>

For mobile- User is shown 1 restaurant details displayed as a card in a row.

![Restaurants page mobile](/documentation/features/restaurants-page/restaurantspage-mobile.gif)

</details>

<details><summary>Restaurants page pin restaurants</summary>

Users are allowed to pin any restaurants to their profile. Once user pins a restaurant, the pin will change color to red. Users cant pin a restaurant twice unless they unpin the already pinned restaurant.A relevant success message is also shown.

![Pin restaurants](/documentation/features/restaurants-page/restaurants-pin-feature.gif)

</details>

<details><summary>Restaurants page unpin restaurants</summary>

Users may unpin restaurants from their profile. The pinned restaurants(red pin) will change their color back to its original color which would a shade of navy. A relevant message is shown to users when unpinning.

![Unpin restaurants](/documentation/features/restaurants-page/restaurants-unpin-feature.gif)

</details>

<details><summary>Restaurants page rate button</summary>

Users can click on rate button for a restaurant which will the redirect the user to another page which is the review/rate page

![Rate button](/documentation/features/restaurants-page/restaurants-rate-feature.gif)

</details>

<details><summary>Restaurants page rated feature</summary>

Once user has rated a restaurant already, the rate button will change color, and will loose ability to be clicked. This will prevent users from rating the same restaurant twice. Only once they have deleted their review, the button can change back to being original color and user will be able to review the restaurant again.

![Rated feature](/documentation/features/restaurants-page/restaurants-rated-feature.gif)

</details>

<details><summary>Restaurants page carousal feature</summary>

Users can have access to images of restaurants which are featured from google since we are using google places api to retrieve restaurant information.

![Carousal feature](/documentation/features/restaurants-page/restaurants-carousal-feature.gif)

</details>

<details><summary>Restaurants page visit website feature</summary>

Users would be able to visit restaurant websites when they click visit website button if a website is available to them.

![Visit website](/documentation/features/restaurants-page/restaurant-website-feature.gif)

</details>

<details><summary>Restaurants page all reviews button</summary>

Users will be able to access all reviews of a restaurant by clicking on all reviews button.

![All reviews](/documentation/features/restaurants-page/restaurants-allreviews-button.gif)

</details>

<details><summary>Restaurants page mobile go up button</summary>

When users access restaurants page on mobile or smaller devices, a go up button will appear which allow users to go to the top of the page by clicking on the button which will help user experience.

![Go up button restaurants](/documentation/features/restaurants-page/restaurantspage-go-up-button.gif)

</details>

<details><summary>Restaurants page no website feature</summary>

Users are shown when a website is not available for a restaurant, as the information are retrieved from googplaces api. Sometimes websites would not be able for some restaurants.

![No website feature](/documentation/features/restaurants-page/website-unavailable-feature.png)

</details>

<details><summary>Restaurants page no images feature</summary>

Users will be shown an appropriate image that matches with website theme incase there are no images to feature in a carousal from google places API.

![No images feature](/documentation/features/restaurants-page/no-images-available-feature.png)

</details>

<details><summary>Restaurants page pagination feature</summary>

Users will be able to move to next page by clicking the next arrow or 1, 2, 3 buttons. There is a limit of 20 restaurants all together for each category chosen as this is the limit with google places API. Each will have 8 restaurants or less.

![Restaurant pagination](/documentation/features/restaurants-page/restaurants-pagination-feature.gif)

</details>

**Profile page & features**

**Rate page & features**

**Allreview page & features**

**Edit review page features**

**Edit profile page features**

**Login page features**

**Logout page features**

**Signup page features**

**Superuser features**

2. **UNREGISTERED USER ACCESS**

**Can Access**

**Cant Access**

### **Future Features**

## **The Surface Plane**

### **Design**

#### **Colour Scheme**

- ![Dublin Eats color palette](/documentation/color-scheme/restaurant-color-palette.png)

#### **Typography**

#### **Imagery**

## **Technologies Used**

### **Languages Used**

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [Javascript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](<https://en.wikipedia.org/wiki/Python_(programming_language)>)

### **Frameworks and Tools Used**

1. [Django](https://www.djangoproject.com/)
2. [Bootstrap5](https://blog.getbootstrap.co#) 
3. [ElephantSQL](https://www.elephantsql.com/)
4. [Cloudinary](https://cloudinary.com/)
5. [GitHub:](https://github.com/)
6. [Balsamiq](https://balsa#)
7. [Stackoverflow](https://stackoverflow.com/)
7. [CI Python Linter](https://pep8ci.herokuapp.com/)
8. [Birme](https://www.birme.net/)
9. [Real Favicon Generator](https://realfavicongenerator.net/)
10. [FreePik](http://www.freepik.com/)

### **Libraries Used**

## **Testing**
Testing for the wesbite can be found here. [TESTING.md](TESTING.md)


## **Deployment**

### **GitHub**

This project was developed by forking a specialized [Code Institute template](https://github.com/Code-Institute-Org/python-essentials-template) which simulates a terminal in the web browser.

1. Click Use this template
2. Name the repository
3. Launch using the Gitpod web extension
4. Pin project in Gitpod workspaces

### **Version Control**

For version control the following steps were made:

For version control the following steps were made:

1. Changes made to files in Gitpod
2. Files made ready for commit with command - git add "filename", or git add . to add all files
3. For the commits the following command was run along with commit description - git commit -m "This is my commit etc"
4. To move the changes to Github the following command was run - git push
5. Alternatively files can be made ready for commit using the Source Control staging area in Gitpod
6. Files were staged and a message describing the commit was made before committing and pushing it to GitHub

### **Cloning the GitHub Repository**

Creating a clone enables you to make a copy of the repository at that point in time - this lets you run a copy of the project locally: This can be done by:

1. Navigating to
2. Clicking on the arrow on the green code button at the top of the list of files
3. Select Local then HTTPS copy the URL it provides to the clipboard
4. Navigate to your code editor of choice and within the terminal change the directory to the location you want to clone the repository to.
5. Type 'git clone' and paste the HTTPS link you copied from GitHub
6. Press enter and git will clone the repository to your local machine

### **Forking the GitHub Repository**

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the repository
2. At the top of the Repository (not the top of the page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### **Final Deployment with Heroku**

## **Credits**

### **Code Used**

### **Content**

### **Media**

## **Acknowledgements**