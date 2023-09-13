# **Dublin Eats**

## **Overview**

Dublin Eats is a website designed to allow users to find and review Restaurants in Dublin. The site features a search feature that allows users to search for any Restaurant in Dublin. This is implemented with Google Places API. The user can also view restaurants according to categories or cuiznes such as african, american, european, asian or irish. Users will be able to view Restaurant details such as their address and has access to their websites etc. Users will also be able to review  Restaurants and pin some restaurants page onto their own customizable profile page. Each user needs to sign up to be able to review and look at other reviews for restaurants.Each user will have a profile page that they would be able to edit once they have logged in.

## **Project Goals**

This is my fourth portfolio project for [Code Institute](https://codeinstitute.net/). In this project i aim to demonstrate my goal of showcasing my skills in django , bootstrap, html, javascript, python & css.

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

Dublin Eats websites intends to allow  foodies of Dublin or tourists to discover new restaurants in Dublin according to what they are feeling for /craving for in the moment. Users will be able to search restaurants according to categories or cravings and rate/review the ones they have been to. Each Registered user has a profile page where they can also pin the restaurants they would like to visit in the future.

### **The Ideal User**

- User who enjoys food and would like to discover new restaurants or cuizines.
- User resides in Dublin and would share the app to their socials to generate traffic.
- User who will create a list of restaurants that they still want to visit(pin the restaurants).
- User who would rate and review restaurants that they have been to.
- User who has customized their page to showcase their interests in any aspects of food.

### **Site Goals**

- To provide users with all the restaurants and discover new ones.
- To provide users with the ability to review/rate restaurants.
- To provide users with the ability to view other users reviews/ratings.
- To provide users with the ability to pin / favourite the restaurants they want to go to.

### **Agile Planning**

Agile development or planning were implemented using Github issues, milestones and project.Issue weres created for User stories which are implemented to identify the necessary features and functions of the website.

Since this was the first time using story points and it was not really explained in the walk-through videos, it was challenging to identify which userstories to allocate more story points and how much story points to provide for each user story.Story points were allocated according to complexity or how time consuming the user story was.The should-have user story points did not exceed 60% of user story points total.
The must-have user stories were prioritized first. Certain other user stories were implemented based on time and complexity. 
Project Kanan board was used to track progress with user stories moving between Todo, In Progress and Done columns.The kanan board can be located [here](https://github.com/users/SooryaGeorge7/projects/3/views/1). All user stories have acceptance critera and tasks that needs to be ticked off on the go as this will mark the story as complete.

The user stories for email confirmation and password reset is left as backlog as these were not able to be implemented due to time constraints and they were not part of MVP or must-have tags.

![Project kanban screenshot](/documentation/agile.png)

### **Epics**

Each epic created had a few user stories linked to it. The acceptance criteria, with tasks associated with each user story can be found in project kanban board linked [Here](https://github.com/users/SooryaGeorge7/projects/3/views/1)

#### **EPIC: Project Setup**

***As a developer i can set up project so that i can start working on my project***

This was done by installing the necessary framworks and libraries. Adding env.py to gitignore and deploying the site early to Heroku. Further development of the website could only be implemented after this step.

#### **EPIC: Home**

***As a developer i can implement home page so that users know exactly what to do and what the website is about when they enter the website***

 The Base template which consistes of header and footer was created first so I could extend within further templates and then the homepage(index.html) was built using bootstrap and styled. The home page also has the search functionality which is progressed under seperate user stories.

#### **EPIC: User authentication**

***As a developer i can **implement user authentication** so that only signed up users can use restaurant features***

This epic is associated with user stories of signup , login and logout functionality. These were implemented using django allauth.At first this was not implemented using django allauth because i had learnt how to implement signup, login, logout functionality with a [youtube video taught by Corey](https://www.youtube.com/watch?v=3aVqWaLjqS4&t=1324s), but i later realized that it would be django allauth for user registration and login because this was taught in the walk through video.

#### **EPIC: Restaurant**

***As a developer i can implement restaurant app in my project so that so that users may view, rate or pin restaurants.***

The user stories associated were Restaurant categories, websites, pinning restaurants to Profile. Retrieving restaurants information were implemented with google Places API.

#### **EPIC: Reviews & Ratings**

***As a developer i can implement reviews app so that users can review , view reviews, rate, edit reviews or delete reviews***

The user stories associated with this epic are the ones to review/rate restaurants, see all reviews, edit reviews and delete reviews. 

#### **EPIC: Profile**

***As a developer i can implement a profile for each user so that they can update profile , see reviewed restaurants, pinned restaurant or delete profile/account.***

The user stories associated with this epic are the ones where user can have access their profile, update and delete their profile.


#### **EPIC: Error pages**

***As a developer i can implement the necessary error pages so that that users are redirected to these pages incases of errors.***

The error pages to implement are 404, 403, 500 error pages

#### **EPIC: Documentation**

***As a developer i can implement a detailed readme so that other developers can see the process of how the website came to be as well as view all the necessary testings done***.

The Readme and Testing documents are part of this epic.

### **Userstories**

These userstories associated with each of these EPICs were implemented throughout development of the website.

#### **EPIC: Project Setup** 

* As a Developer I can set up Django and install the necessary libraries so that the necessities are there to start project development. 
* As a Developer I can deploy site to Heroku early so that I can start testing site early on before further development of application. 
* As a Developer I need to add env.py to .gitignore so that I can deploy the site without exposing sensitive information.

#### **EPIC: Home**

* As a developer I can implement search functionality, so that user can easily search for restaurants using key words.
* As a User I can see home page of website so that so that i can immediately know what the website is about and can see how to navigate to other pages
* As a User I can **use header with navigation bar and footer ** so that i can find all the necessary information i am looking for with ease in every page of the website

#### **EPIC: User authentication** 

* As a site admin i can review comments left for restaurant reviews so that i can filter out any offensive language. 
* As a User I want to Login and Logout so that I can use the features available to registered users.
* As a User I want to sign up / register once so that i can have access to all features available on site

The userstories below were not implemented due to time constraints.They were not part of the MVP milestone.

* As a user i can signup with email verification so that noone else would be able to signup using my email.
* As a User i can reset password so that i can still have my account if i forget my password

#### **EPIC: Restaurant**

* As a User I want to pin a restaurant so that I can see the restaurants i want to visit in my profile.
* As a User I can click the next page button so that that one page is not overflowing with results.
* As a User I can can choose restaurants according to categories so that that i can view all the restaurants that is available in Dublin according to that category.
* As a User I would like to to see the websites of each restaurant so that I can find menus and find other necessary about the restaurant .

#### **EPIC: Reviews & Ratings**

* As a User I can see all reviews so that users can find other user's reviews and and can find top rated restaurants.
* As a User I want to rate and review restaurants so that I can share my experience after visiting restaurant
* As a User i can edit the reviews so that i can change my mind about the restaurant if i want to.
* As a user I can delete a review I made so that create a new one in the future.

#### **EPIC: Profile**

* As a User I can see my profile so that **i can update information about myself, see or delete reviews already made, and see all the pinned restaurants i want to go visit **
* As a user i can delete profile so that remove my account from the website.

#### **EPIC: Error pages**

* As a developer, I can implement 403 error page so that users are redirected to these pages when there is insufficient permission to access the page. 
* As a developer, I can implement 500 error pages so that users are redirected to these pages when there is an internal server error.
* As a developer, I can implement 404 error page so that users are redirected to these pages when a page is not found.


#### **EPIC: Documentation**

* As a Developer I have to write extensive documentation on the development of my site so that other developers can have access to relevant information needed.
* As a Developer I have to *test website extensively so that **there would be no code, logical, accessibility errors **

## **The Skeleton Plane**

#### **Wireframes**

Although care was taken to implement as many of the features as the wireframes created, some features had to be changed or adjusted due to complexity and time constraints.

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

#### **Flow Chart logic**

A basic flowchart was used to plan the logic of this website. The logic was altered slightly during development of website to adapt to the project's needs.
The website now allows unregistered users to use the search field and view restaurant categories but they are unable to pin,rate or see any reviews of any restaurants until they have signed up for the website.

- ![Flow chart of logic](/documentation/flow-diagram/flow-chart-dublineats.jpg)

#### **Database Scheme**

The models for this project are Profile model, Review model and Restaurant model.

The profile model is linked directly with Django Allauth UserModel with the profile being created as the user signs up for website.
The review model is linked to restaurant model and user model via a foreign key. This allows for ratings/reviews to be linked to a specific user profile and a restaurant.The restaurant model is linked to the profile model via many to many relationship allowing the user to pin restaurants to their profile as well as to review as many restaurants as they want.

You can see the entity relationship diagram that was created for each model and how they are related.
- ![Entity relationships](/documentation/entity-relationship/entity-relationship.png)

#### **Security**

Security for this website was implemented  the following ways :

- Enivornmental variables were added to gitignore file as they contain API keys and sensitive information.
- These variables were added to Heroku config vars for production and deployment. 

## **The Scope Plane**

-	User should be able to create , read, update and delete their profiles and ratings/reviews.
-	The website should be responsive to devices from 320px and up.
-	Navbar menu should be shown in a hamburger toggler in smaller devices.
-	The user should be able to access the websites features once they are logged in.
-	User should have a clear understanding of site from home page.
-	Other functionalities available to user- pinning restaurants to their profile, clicking on each restaurant websites, having access to google images and address for each restaurant..

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

Once users sign up for the website, they will have access to a profile page which they would be able to customize.

<details><summary>Profile page desktop</summary>

![Profile page desktop](/documentation/features/profile-page/profilepage-desktop.gif)

</details>

<details><summary>Profile page mobile</summary>

![Profile page mobile](/documentation/features/profile-page/profilepage-mobile.gif)

</details>

<details><summary>Profile edit button</summary>

When user clicks on edit button on profile page, they are redirected to edit profile page.

![Profile page edit button](/documentation/features/profile-page/profile-editbutton.gif)

</details>

<details><summary>Profile my reviews</summary>

In user's profile page , users will be able to access the reviews they have already submitted for various restaurants. They would also be able to access the specific restaurant's website.

![Profile reviews feature](/documentation/features/profile-page/profile-myreviews-feat.gif)

</details>

<details><summary>Profile Open review button</summary>

If user clicks on the icon to open review, the user will be redirected to edit review page.

![Profile open review feature](/documentation/features/profile-page/profile-openreview-feat.gif)

</details>

<details><summary>Profile pinned restaurants feature</summary>

Users would be able to see all restaurants that they have pinned from Restaurant pages or search results page. 

![Profile pinned restaurants feature](/documentation/features/profile-page/profile-pinnedrestaurants-feat.gif)

</details>

<details><summary>Profile remove pinned restaurants feature</summary>

Users would be able unpin these restaurants from profile page by click on the remove button.

![Profile Remove restaurant feature](/documentation/features/profile-page/profile-remove-pinned-feat.gif)

</details>

**Rate page & features**

When user clicks on rate button in restaurant's page, user is redirected to page that contains the review or rating form. User would need to rate the restaurants 5 criterias before submiting a rating. Leaving a review or comment is optional.

<details><summary>Rate page</summary>

![Rate page](/documentation/features/rate-page/rate-restaurants-page.gif)

</details>

<details><summary>Rate stars feature</summary>

User would be able to click stars and depending on location of click, javascript code handles the event and changes the value of the rating for that particular criteria and also changes the color of the stars accordingly

![Rate stars feature](/documentation/features/rate-page/rate-stars-feature.gif)

</details>

<details><summary>Rate exit button</summary>

User would be able to exit the review page if they dont want to review anymore. They will be warned that any changes made will not be saved.

![Rate exit feature](/documentation/features/rate-page/rate-exitbutton.gif)

</details>

<details><summary>Rate submit success</summary>

User is shown appropriate success message after submitting a review and is redirected to all reviews page where they can see their review.

![Rate submit success](/documentation/features/rate-page/rate-submit-success.gif)

</details>

<details><summary>Rate all citeria validation</summary>

User is shown an error message if they try to submit the form without choosing all criterias.

![Rate all criteria validation](/documentation/features/rate-page/rate-allcriteria-feature.gif)

</details>

**Allreview page & features**

Users are redirected to all reviews page when user clicks on allreviews button.

<details><summary>All reviews page desktop</summary>

![All reviews desktop](/documentation/features/allreviews-page/allreviews-desktop.png)

</details>

<details><summary>All reviews page mobile</summary>

![All reviews mobile](/documentation/features/allreviews-page/allreviews-mobile.gif)

</details>

<details><summary>All reviews go back button</summary>

User has access to a go back button which allows user to go back to restaurant page of that particular restaurant

![All reviews go back button](/documentation/features/allreviews-page/allreviews-goback-button.gif)

</details>

<details><summary>All reviews go up button</summary>

User has access to go up the all reviews page incase when there are too many reviews, It was implemented to enhance user experience.

![All reviews go up button](/documentation/features/allreviews-page/allreviews-goup-button.gif)

</details>

<details><summary>All reviews edit button feature</summary>

User has access to edit button for their review in the all reviews page.

![All reviews edit button feature](/documentation/features/allreviews-page/allreviews-editbutton-feat.gif)

</details>

<details><summary>All reviews edit button redirect</summary>

If user clicks on edit button , user will be redirected to edit review page where user can make changes to their review.

![All reviews edit button redirect](/documentation/features/allreviews-page/allreviews-editbutton.gif)

</details>

<details><summary>All reviews profile link feature</summary>

Users have access to other user's profile page or their own profile page in allreviews page. 

![All reviews profile link feature](/documentation/features/allreviews-page/allreviews-profilelink.gif)

</details>

<details><summary>All reviews other user profile</summary>

When user A clicks on User B profile link, user A is redirected to user B profile where user A will be able to see User B's details, pinned restaurants and reviews made by user B.

![All reviews other user's profile](/documentation/features/allreviews-page/allreviews-otheruserprofile.gif)

</details>

<details><summary>All reviews other user's profile reviews</summary>

User can see other users reviews when viewing their profiles.

![All reviews other user's profile reviews](/documentation/features/allreviews-page/otheruser-profilereviews.gif)

</details>

<details><summary>All reviews other user's profile pinned restaurants</summary>

User can see which restaurants other user's have pinned to their profile.

![All reviews page other user's pinned restaurants features](/documentation/features/allreviews-page/otheruser-pinnedrestaurants.png)

</details>

**Edit review page features**

Users would be able to edit their own reviews from all reviews page and also their profile page. The edit button and open review button will both be redirected to edit reviews page.

<details><summary>Edit review feature</summary>

![Edit review feature](/documentation/features/rate-page/exit-review-feat.png)

</details>

<details><summary>Delete review feature</summary>

users can delete their review if they want to. The users are asked twice to be sure so that they dont delete review by mistake.

![Delete review feature](/documentation/features/rate-page/delete-review-feat.png)

</details>

<details><summary> Exit review feature</summary>

Users can exit out of this page if they want to incase they dont want to edit the review anymore.User will be asked twice and warned that any changes will not be saved.

![Exit review feature](/documentation/features/rate-page/exit-review-feat.png)

</details>

<details><summary>Exit review redirect page</summary>

Users are redirected to allreviews page after they exit the edit review page.

![Exit review redirect](/documentation/features/rate-page/exit-review-redirect.gif)

</details>

<details><summary>Review delete success message</summary>

Users will be shown appropriate message after deleting their review.

![Review delete success message](/documentation/features/rate-page/review-delete-success.gif)

</details>

<details><summary>Review update success message</summary>

Users will be shown appropriate message after updating their review.

![Review update success message](/documentation/features/rate-page/review-update-success.gif)

</details>

**Edit profile page features**

Once user clicks on edit button on profile page, they will be redirected to edit profile page where they will able able to updates names, any information and profile images.

<details><summary>Edit profile page</summary>

![Edit profile page](/documentation/features/profile-page/profile-editbutton.gif)

</details>

<details><summary>Edit profile update success</summary>

Once user clicks on update, then user is redirected back to profile page and is given an appropriate success message for updating profile.

![Update profile success message](/documentation/features/profile-page/update-profile-success.gif)

</details>

<details><summary>Delete profile feature</summary>

User would be able to delete their profile if they wanted to. In this case, their account will be deleted to. They will have to sign up again if they want access to all DublinEats features.

![Delete profile feature](/documentation/features/profile-page/delete-profile-feat.png)

</details>

<details><summary>Exit from editing profile feature</summary>

Users can exit the edit profile page if they dont want to change anything. Any changes made will not be saved and they will be redirected back to profile page.

![Exit from editing profile](/documentation/features/profile-page/exit-editprofile-feat.png)

</details>

<details><summary>Edit profile placeholders.</summary>

Once user signs up for website, and accesses the edit profile page. They are able to see placeholders which would help them in the information that they have to fill out for their profile.

![edit profile placeholders](/documentation/features/profile-page/edit-profile-placeholders.png)

</details>

**Login page features**

<details><summary>Login feature</summary>

![log in form](/documentation/features/login-page/login-page.png)

</details>

<details><summary>Login Success message</summary>

![login success](/documentation/features/login-page/loginpage-success.gif)

</details>

**Logout page features**

<details><summary>logout page</summary>

![Logout page](/documentation/features/logout-page/logout-feat.png)

</details>

<details><summary>logout message</summary>

![logout message](/documentation/features/logout-page/logout-message.gif)

</details>


**Signup page features**

<details><summary>Sign up page</summary>

![Sign up page](/documentation/features/signin-page/signup-form.png)

</details>

<details><summary>Sign up success message</summary>

![Sign up success](/documentation/features/signin-page/signup-success-message.gif)

</details>

**Search page**

Users can access search result page when entering a valid entry in search field.The search query will retrieve a maximum of 10 restaurants using google places API

<details><summary>Search results page</summary>

Search results page looks identical to restaurants category page. Users would be able to pin, review, view reviews of these restaurants just like they can in restaurants page featured on navbar.

![Search results page](/documentation/features/searchresults-page/search-results.gif)

</details>

<details><summary>Search results pagination</summary>

Search results will retrieve a maximum of 10 restaurant details, therefore pagination will allow for 2 pages only for each search query.

![Search results pagination](/documentation/features/searchresults-page/search-results-pagination.gif)

</details>

**Superuser features**

I have included front end superuser features which would allow superusers to delete other user's reviews or profiles. This is implemented to remove reviews with offensive language, or remove unwanted profiles if necessary.

<details><summary>Superuser all reviews page</summary>

Superusers would have access to edit button for all reviews found in allreviews page.

![Superuser allreviews access](/documentation/features/superuser/superuser-allreviewspage.gif)

</details>

<details><summary>Superuser delete other's reviewes feature</summary>

Superusers would be able to delete other user's reviews if they wanted to.

![Superuser delete other's review](/documentation/features/superuser/superuser-deleteotherreview.gif)

</details>

<details><summary>Superuser edit other's reviews</summary>

Superusers would be able to click on edit button for other's reviews. They will not have access to update button however.

![Superuser edit other's review](/documentation/features/superuser/superuser-editotherreview.gif)

</details>

<details><summary>Superuser delete other's profile feature</summary>

Superusers would be able to delete another person's profile for incase the particular user is not using their profile for the intended usage of the website.

![Superuser delete other's review](/documentation/features/superuser/superuser-otheruser-profile-delete.gif)

</details>

<details><summary>Superuser edit other's profiles</summary>

Super user's have access to edit profile button on other user's profile. The edit profile page will be accessible to the superuser without the update button.

![Superuser edit other's profile](/documentation/features/superuser/superuser-otheruser-profile-edit.gif)

</details>


**Error pages**

I have included 403,404 and 500 error pages

<details><summary>403 error page</summary>

This page appears when an action is forbidden.

![Superuser allreviews access](/documentation/features/error-pages/403.png)

</details>

<details><summary>404 error page</summary>

This page appears when a page is not found.

![Superuser allreviews access](/documentation/features/error-pages/404.png)

</details>

<details><summary>500 error page</summary>

This page appears when there is an error with the internal server.

![Superuser allreviews access](/documentation/features/error-pages/500.png)

</details>

2. **UNREGISTERED USER ACCESS**

**Can Access**

Unregistered users can access restaurants pages according to categories. They are able to access websites of each restaurant too.

Unregistered users have access to search feature. They can search for what they want but features such as rating, pinning and viewing reviews and profiles are restricted to registered users.

**Cant Access**

<details><summary>Unable to pin restaurants without loging in.</summary>

![unable to pin](/documentation/features/unregistered-users/unregistered-pin.gif)


</details>

<details><summary>Unable to rate restaurants without loging in</summary>

![Unable to rate](/documentation/features/unregistered-users/unregistered-rate-feature.gif)

</details>

<details><summary>Unable to access all reviews page</summary>

![Unable to access allreviews page](/documentation/features/unregistered-users/unregistered-allreviews-feat.gif)

</details>

### **Future Features**

- I would implement email confirmation to verify account when user initally signs up for website.
- I would implement password reset functionality for the instances the user forgets their password.
- I would add google maps directions for each restaurant being rendered from google places API , allowing user to access directions.
- I would want to implement sorting of restaurants according to highly rated, cheapest, etc
- I would want to implement even more categories in restaurants tabs as currently i only have 5 options for restaurants tab on navbar.
- Implementation Automatic reduction of profile image size on upload as this affects performance on lighthouse testing.
- Allowing of Automatic deletion of images from cloudinary storage when users change their profile images or delete their profile.
- Ability to register and login with social media accounts.
- Allow for users to report other users to the site admin incases of inappropraite comments or reviews.
- Mechanism for users to easily contact the site admin.

## **The Surface Plane**

### **Design**

Design of website was thought out through colorscheme, typography and imagery and was carried out through the entirety of the website.

#### **Colour Scheme**

- ![Dublin Eats color palette](/documentation/color-scheme/restaurant-color-palette.png)

- #2C3E50 was chosen as the primary color to be fitted throughout website as this color brings a more modern look to a website. 
- #F9BF3B was chosen as the secondary color which were mainly used for action buttons such as search, submit, updated, edit, or when user selected stars, the stars turn this color. This color works great with the primary color to enhance user experience.
- #F2F2F2 and #FFFFF was used as the background colors as the other colors were quite bold and daunting, a more neutral color would compliment well against the primary and secondary colors

The colors above were implemented via rgba format instead of hex formatting inorder to use the various colours with transparency.

#C0392B was a color that was implemented for delete buttons or remove buttons.

#### **Typography**

The font family Poppins were imported from google fonts and was implemented throughout website.

#### **Imagery**

The hero image used in home page,the default profile pictures, the background image used throughout the website and the default images in restaurants were all downloaded from [Pexels](). Their format was also changed to webp to improve performance during lighthouse testing.

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

1. Cloudinary 
2. dj-database-url
3. dj3-cloudinary-storage
4. Django
5. django-allauth
6. django-crispy-forms
7. Psychopg 2
8. Gunicorn
9. Crispy bootstrap5

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

The below steps were followed to deploy this project to Heroku:

1. Go to Heroku and click "New" to create a new app.
2. After choosing the app name and setting the region, press "Create app".
3. Go to "Settings" and navigate to Config Vars, enter the below:
        - SECRET_KEY: (Enter your secret key)
        - DATABASE_URL: (Enter the database URL from ElephantSQL)
        - CLOUNDINARY_URL: (Enter Cloudinary API URL)
        - PORT: 8000
        - API_KEY: (An API key will need to be retrieved from the google places API)
4. Leave "Settings" and go to "Deploy". Scroll down and set Deployment Method to GitHub. Once GitHub is chosen, find your repository and connect it to Heroku.
5. Scroll down to Manual Deploy, make sure the "main" branch is selected, and click "Deploy Branch".

## **Credits**

### **Code Used**

* The steps to connect to a Heroku Postgres database and deploy were adapted from the Code Institute 'I think therefore I blog' tutorial. This includes defining DATABASE_URL and SECRET_KEY environment variables in an env.py file in the local environment and adding corresponding config variables in the Heroku dashboard, using dj_database_url to create a URL from the database URL in settings.py, updating ALLOWED_HOSTS in settings.py with the deployed Heroku URL and adding the templates path to a TEMPLATES_DIR variable in settings.py
* The Bootstrap 5 documentation was extensively referenced for guidance on implementing navbars and modal dialogs.
* This repository was created using the template provided by Code Institute.
* Thanks to the Django docs which were also used as a step-by-step while going through the project to ensure everything was set up correctly.
* Corey Schafer for the tutorial to get automatic profile creation for my project.
* [Learnt how to implement search functionality in django here.](https://www.makeuseof.com/add-search-functionality-to-django-apps/#:~:text=Create%20a%20View%20for%20the%20Search&text=%23%20Check%20if%20the%20request%20is%20a%20post%20request.&text=In%20request.,your%20search%20bar's%20input%20field.&text=Finally%2C%20the%20function%20renders%20a,and%20filtered%20model%20as%20context.)
*[Learnt how to implement blurred background here](https://www.w3schools.com/howto/howto_css_blurred_background.asp)
* [Learnt how to implement star rating using javascript here](https://www.codingnepalweb.com/star-rating-html-css-javascript-2/)
* [Learnt how to retrieve images from google places API here](https://stackoverflow.com/questions/13524834/google-place-api-placedetails-photo-reference)
* Google places api documentation and youtube videos were used extensively to implement google places API to retrieve restaurant details from Dublin.


### **Content**

* Default profile image was found in pixabay.com [See here](https://pixabay.com/illustrations/profile-icon-symbol-male-profile-728591/)
* Background home page image was found in Pexels.come [See here](https://www.pexels.com/photo/cooked-food-in-white-and-brown-ceramic-bowl-close-up-photography-2741458/)
* Backdrop image which is also used for default image in restaurant cards were found in freepik.com [See here](https://toppng.com/free-image/attern-for-italian-restaurant-la-casata-in-prague-PNG-free-PNG-Images_179428)
* All icons used were from [Bootstrap icons](https://icons.getbootstrap.com/?q=globe)
* The logo image was created Realfavicon generator to fit the theme of the website.

## **Acknowledgements**

I would like to acknowledge the following people in helping with my project one way or another:

* My husband for supporting me through my decision to do this course and through all the late nights and meltdowns so far especially knowing that 
  this will only get worse through the course of the year. :D
* My friends ,family and colleagues who have tested my site on their devices to make sure all looks and works well.
* My Mentor Brian O'Hare for guiding me and giving constructive criticism in our 6 mentor sessions so far.
* UCD academy november private group in slack for our almost weekly facilitator sessions that have helped me in getting some our doubts cleared with regards to the project.
* Chris Quinn for delivering our facilitator and master classes so far which has helped me to not feel completely alone in this journey.