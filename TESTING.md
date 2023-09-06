# **Dublin EatsTesting**

## **Testing Overview**

A wide range of testing was carried out during development by myself,slack community, friends and family.

## **Contents**

1. [Testing Overview](#testing-overview)
2. [Automated Testing](#automated-testing)
    - [Unit Testing](#unit-testing)
3. [Manual Testing](#manual-testing)
    - [User Story Testing](#user-story-testing)
4. [Validators](#validators)
    - [CI Python Linter](#ci-python-linter)
    - [JSHint](#jshint)
    - [W3C CSS Validator](#w3c-css-validator)
    - [W3C Markup Validator](#w3c-markup-validator)
    - [Lighthouse](#lighthouse)
    - [Lighthouse Errors](#lighthouse-errors)
    - [Wave Accessibility Tests](#wave-accessibility-tests)
5. [Responsiveness](#responsiveness)
6. [Bugs & Fixes](#bugs--fixes)
7. [Unresolved Bugs/Issues](#unresolved-bugsissues)

## **Automated Testing**

### **Unit Testing**

Unit tests were created to test the functionality of the apps. These can be found in the tests.py files in the respective apps.

#### **Home**

**Home Views Test**

The unit test for home app is testing the functionality related to searching and viewing search results. It ensures that after performing a search, the user is redirected to the search results page, and that page is correctly rendered with the the template results.html. It also verifies the authentication and setup of the user, profile, restaurant, and review objects before testing the views.

![Home test_views](/documentation/unit-tests/home-test.png)

#### **Restaurants**

**Restaurants Views Test**

The unit test for Restaurants app views.py is testing the functionality related to restaurant categorization, pinning, and removal are working as expected in the Django application. It checks various scenarios, including rendering template categories.html, handling redirects, and updating user profiles based on their interactions with restaurants.

![Restaurant test_views](/documentation/unit-tests/restaurants-test_views.py.png)

**Restaurants Models Test**

This unit test case is verifying that the "Restaurant" model behaves as expected by creating a test instance of the model and checking if the attributes of that instance match the expected values.

![Restaurant test_models](/documentation/unit-tests/restaurants-test_models.py.png)

#### **Review**

**Review Views Test**

These tests cover various scenarios related to creating, editing, and deleting restaurant reviews.When user clicks on the rate button, 
 the site Ensures  GET request is sent to a URL named "review" with the restaurant ID as an argumentand checks if the response status code is 200 (OK) and if the "review_page.html" template is used. It then sends a POST request to the same URL with review data.
It checks if the response status code  redirects to the "allreviews" page for the same restaurant.
When user want to edit reviews site it sends a GET request to a URL named "edit_review" with the restaurant ID and review ID as arguments.
It checks if the "review_page.html" template is used.It retrieves the existing review's attributes and checks if they match the initial review data.It sends a POST request to the same URL with updated review data.It checks if if it redirects to the "allreviews" page for the same restaurant.When user wants to delete a review, The site  first checks the initial count of reviews in the database. It sends a POST request to a URL named "delete_review" with the restaurant ID and review ID as arguments.It checks if the response status code is 302 (a redirect) and if it redirects to the "allreviews" page for the same restaurant.It checks if the review no longer exists in the database by verifying that it cannot be retrieved.It checks the new count of reviews in the database, which should be zero.

![Review test_views](/documentation/unit-tests/review-test_views.py.png)

**Review Models Test**

The test case verifies that the "Review" model behaves as expected by creating a test instance of the model and checking if its attributes and string representation match the expected values. This is a basic unit test for the model's correctness and can help ensure that the model's fields and methods are defined and working correctly.

![Review test_models](/documentation/unit-tests/review-test_models.py.png)

**Review Forms Test**

This test cases ensure that the "RatingForm" form behaves correctly in terms of validation. The first test checks that the form is valid when provided with valid data, and the second test checks that the form correctly identifies and reports errors when ratings exceed the maximum allowed value of 5.

![Review test_forms](/documentation/unit-tests/review-test_forms.py.png)

#### **Users**

**Users Views Test**

This test cases ensure that the views related to user profiles, including viewing, editing, and deleting profiles, work as expected in the Django application.It tests that site logs in the test user using the client, then It sends a GET request to a URL named "profile" with the test user's username as a parameter.It checks if the response status code is 200 (OK) and if the "profile.html" template is used.When user wants to edit a profile,the site sends a POST request to a URL named "editprofile" with the test user's username as an argument and data for updating the user's first and last name.It checks if the response status code is 200 (OK) and if the "edit_profile.html" template is used.When user wants to delete their profile, the site sends a POST request to a URL named "deleteprofile" with the test user's username as an argument.It checks if the response status code is 302 (a redirect) and if the redirected URL is the home page.

![Review Views](/documentation/unit-tests/users-test_views.py.png)

**Users Models Test**

This unit test cases ensure that the "Profile" model behaves as expected by verifying attributes and relationships. The first test checks the attributes of the user's profile, and the second test checks the relationships between the profile and pinned restaurants and reviews.

![Review Models](/documentation/unit-tests/users-test_models.py.png)

**Users Forms Test**

The unit tests ensures that the UserUpdateForm and ProfileUpdateForm forms behave correctly in terms of validation. They cover scenarios involving valid data, invalid email formats, missing required fields, and fields exceeding character limits.

![Review Forms](/documentation/unit-tests/users-test_forms.py.png)



## **Manual Testing**

### **User Story Testing**

Manual testing for each userstory is documented in [Dublin Eats Userstory spreadsheet](https://docs.google.com/spreadsheets/d/11P1y7mkce_feJ34opPtlGRvyqhV4u9YRYWoxAketVkE/edit#gid=0)

After all the bugs were resolved, all manual testing has resulted in a pass result. 

In addition to manual testing, the site was continuously being tested throughout development of the website. 



## **Validators**


### **CI Python Linter**

The [CI Python Linter](https://pep8ci.herokuapp.com/) was used to validate the python code used throughout the project. The results are outlined in below:

|     **Files**      |     **Result**    |    **Pass**   |
|--------------------|-------------------|---------------|
|   **DUBLINEATS**   |                   |               |
| asgi.py            |returned no errors |     Pass      |
| settings.py        |returned no errors |     Pass      |
| urls.py            |returned no errors |     Pass      |
| wsgi.py            |returned no errors |     Pass      |
|--------------------|-------------------|---------------|
|     **HOME**       |                   |               |
| admin.py           |returned no errors |     Pass      |
| apps.py            |returned no errors |     Pass      |
| urls.py            |returned no errors |     Pass      |
| views.py           |returned no errors |     Pass      |
| test_views.py      |returned no errors |     Pass      |
|--------------------|-------------------|---------------|
|  **RESTAURANTS**   |                   |               |
| admin.py           |returned no errors |     Pass      |
| apps.py            |returned no errors |     Pass      |
| urls.py            |returned no errors |     Pass      |
| views.py           |returned no errors |     Pass      |
| models.py          |returned no errors |     Pass      |
| test_views.py      |returned no errors |     Pass      |
| test_models.py     |returned no errors |     Pass      |
|--------------------|-------------------|---------------|
|  **REVIEW**        |                   |               |
| admin.py           |returned no errors |     Pass      |
| apps.py            |returned no errors |     Pass      |
| urls.py            |returned no errors |     Pass      |
| views.py           |returned no errors |     Pass      |
| models.py          |returned no errors |     Pass      |
| forms.py           |returned no errors |     Pass      |
| test_forms.py      |returned no errors |     Pass      |
| test_models.py     |returned no errors |     Pass      |
| test_views.py      |returned no errors |     Pass      |
|--------------------|-------------------|---------------|
|    **USERS**       |                   |               |
| admin.py           |returned no errors |    Pass       |
| apps.py            |returned no errors |    Pass       |
| urls.py            |returned no errors |    Pass       |
| views.py           |returned no errors |    Pass       |
| models.py          |returned no errors |    Pass       |
| forms.py           |returned no errors |    Pass       |
| test_forms.py      |returned no errors |    Pass       |
| test_models.py     |returned no errors |    Pass       |
| test_views.py      |returned no errors |    Pass       |
|--------------------|-------------------|---------------|


### **JSHint**

JavaScript code in rate.js, blur.js, timeout.js for the project was passed through the [JSHint](https://jshint.com/)  validator. This detected error "i" is already defined. This was corrected by defining i outside of loop and not defining everytime i is changed.JavaScript now passes the validator with no problems. Note that JSHint flags an issue with an undefined bootstrap variable, however this is because JSHint does not have access to the Bootstrap CDN import defined within a script tag in the base.html template. There are no JavaScript errors with the deployed site when using google chrome dev tools.

**blur.js**
![blur.js JSHint Results](/documentation/validation/JSHint/blur.js%20validation.png)

**rate.js**
![rate.js JSHint Results](/documentation/validation/JSHint/rate.js%20validation.png)

**timeout.js**
![timeout.js JSHint Results](/documentation/validation/JSHint/timeout.js%20validation.png)


### **W3C CSS Validator**

base.css was passed through [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) with no errors.

![CSS](/documentation/validation/W3C%20css/no-css-errors.png)

### **W3C Markup Validator**

All pages were run through the [W3C Markup Validator](https://validator.w3.org/nu/). Initially, there were some errors but all these issues were corrected and all pages passed validation.

The errors shown below were all corrected accordingly:

1. Error 1

![Error 1](/documentation/validation/W3C%20html/home-onfocus-htmlerror.png)

2. Error 2

![Error 2](/documentation/validation/W3C%20html/review-duplicate-error.png)

3. Error 3

![Error 3](/documentation/validation/W3C%20html/profile-htmlerror.png)

4. Error 4

![Error 4](/documentation/validation/W3C%20html/profile-deletemodal-formerror.png)

### **Lighthouse**

A number of issues were found during lighthouse testing.
Namely :
- Incorrect image ratios
- Not setting fixed width and height for images
- Not having aria-labels for all links
- Performance was more on the lower side for rseataurant page and search results but that is mostly due to images being loaded from google API
- Profile pictures uploaded were taking in jpg which affected performance.

#### **Home Page**

***Mobile***

![Home page mobile](/documentation/validation/Lighthouse/homepage-mobile.png)

***Desktop***

![Home page desktop](/documentation/validation/Lighthouse/homepage-desktop.png)

#### **Results Page**

***Mobile***



***Desktop***

#### **Categories Page**

***Mobile***

![Categories page mobile](/documentation/validation/Lighthouse/restaurants-mobile.png)

***Desktop***

![Categories page mobile](/documentation/validation/Lighthouse/restaurants-desktop.png)

#### **Profile Page**

***Mobile***

***Desktop***

![Profile page mobile](/documentation/validation/Lighthouse/profile-desktop.png)

#### **Edit Profile Page**

***Mobile***

![Edit Profile mobile](/documentation/validation/Lighthouse/edit-profile-mobile.png)

***Desktop***

![Edit Profile desktop](/documentation/validation/Lighthouse/editprofile-desktop.png)

#### **Review/Rating Page**

***Mobile***

![Review page mobile](/documentation/validation/Lighthouse/review-mobile.png)

***Desktop***

![Review page desktop](/documentation/validation/Lighthouse/review-desktop.png)

#### **Allreviews Page**

***Mobile***

![Allreviews page mobile](/documentation/validation/Lighthouse/allreviews-mobile.png)

***Desktop***

![Allreviews page desktop](/documentation/validation/Lighthouse/allreviews-desktop.png)


### **Wave Accessibility Tests**

All pages were tested using [Wave Evaluation Tool](https://wave.webaim.org/) via the Chrome extension.
The following errors were found and corrrected : 

1. Contrast error for home page. The text overlying the home page was resulting in contrast error even though the text could be clearly seen. I corrected this by adding contrasting background color to the white overlying text.
2. Headings were not in sequential order, this was corrected on all pages
3. Profile images and hero image had alerted suspicious alt test which were also corrected.

**homepage**

![Home page wave](/documentation/validation/Wave%20Lighthouse/homepage-wave.png)

**restaurants**

![Restaurants page wave](/documentation/validation/Wave%20Lighthouse/restaurants-wave.png)

**review page**

![Review page wave](/documentation/validation/Wave%20Lighthouse/edit-reviews-wave.png)

**allreviews**

![Allreviews page wave](/documentation/validation/Wave%20Lighthouse/allreviews-wave.png)

**login**

![Login page wave](/documentation/validation/Wave%20Lighthouse/login-wave.png)

**logout**

![logout page wave](/documentation/validation/Wave%20Lighthouse/logout-wave.png)

**profile**

![Profile page wave](/documentation/validation/Wave%20Lighthouse/profile-wave.png)

**signup**

![signup page wave](/documentation/validation/Wave%20Lighthouse/signup-wave.png)

## **Responsiveness**


| **Browser Tested** | **Actual Result** | **Pass/Fail** |
|--------------------|-------------------|---------------|
|                    |                   |               |
|                    |                   |               |
|                    |                   |               |
|                    |                   |               |

| **Device Tested** | **Actual Result** | **Pass/Fail** |
|-------------------|-------------------|---------------|
|                   |                   |               |
|                   |                   |               |
|                   |                   |               |
|                   |                   |               |
|                   |                   |               |
|       |        |          |
|   |        |         |
|  |       |           |
|      |       |          |
|   |      |         |
|   |       |           |
|  |        |           |


## **Bugs & Fixes**

| **Bug** | **Resolution** |
|---------|----------------|
| Images in carousal were changing automatically and not when user clicks next button.  [View bug here](/documentation/bugs/bug-%20automatic%20carousal.gif) | By adding "data-bs-interval="false" to carousal, the automatic changing of images is disabled. The solution for this was found here. View solution [View solution here](https://stackoverflow.com/questions/14977392/bootstrap-carousel-remove-auto-slide) |
| Images that were being uploaded by user were getting cropped when displaying in profile page. [View bug here](/documentation/bugs/error-upload-image.png) | The images being uploaded were undergoing transformation through profile modal where i set the setting crop:crop, i just needed to change that to crop:fill. I learnt the differences and found the solution for this here. [View solution here](https://buildmedia.readthedocs.org/media/pdf/django-daguerre/2.3.1/django-daguerre.pdf) |
| Certain search query's were returning results from UK instead of Dublin. These were the case when search query was a very rare cuizine that would not be available in Dublin. [View bug here](/documentation/bugs/query-bringing-uk-restaurant.png) | The solution found for this was to set the longitude and latitude for the google places API to be that of Dublin, Ireland and also to limit the number of results being retrieved from API. [View suggestion here](https://towardsdatascience.com/how-to-use-the-google-places-api-for-location-analysis-and-more-17e48f8f25b1) [View my solution here](/documentation/bugs/location-solution.png) |
| For search results page, when user moves to next page using paginator, the results would not be from the search query anymore. The query became "None" | I solved this by indicating the query in the pagination code in the html. [View solution here](/documentation/bugs/query-pagination-solution.png) I found the solution among some suggestions here . [View suggestions](https://docs.guidewire.com/cloud/pc/202302/cloudapibf/cloudAPI/topics/101-Fund/03-query-parameters/c_the-pagination-query-parameters.html) |
| I had category saved in Restaurant model for Restaurants app. The search query restaurants were also being saved using restaurant model, but since one restaurant can be retrieved from google places API using different queries, i could not just save each query as category. When user wanted to move from allreviews page back to the results page, the user is redirected to a page with a different query because that particular restaurant from this query was already saved as a different category. | The solution i could implement was to update Restaurant.category  for each time whenever query is given. |
| Seach query were returning results for numbers, special charectors and blank spaces. | solution- using patterning matching in search input field. |
| Some Restaurants ddnt have website urls, so it returned blank and would just refresh the page for instances with no website.| I handled this bug in html where it would be indicated to user when a restaurant has no website. |

## **Unresolved Bugs/Issues**


-	Some queries are still retrieveing restaurants from uk, only very rarely but a future solution for this would be to 
-	Search query doesn’t have to make sense to return a result. If user types in “uherge” this will return some restaurants regardless of there is result for that exact query. This is due to the fact that restaurants names could have vary in terms of  languages.
