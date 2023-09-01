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

![Home test_views]()

#### **Restaurants**

**Restaurants Views Test**

![Restaurant test_views]()

**Restaurants Models Test**

![Restaurant test_models]()

#### **Review**

**Review Views Test**

![Review test_views]()

**Review Models Test**

![Review test_models]()

**Review Forms Test**

![Review test_forms]()

#### **Users**

**Users Views Test**

![Review Views]()

**Users Models Test**

![Review Models]()

**Users Forms Test**

![Review Forms]()



## **Manual Testing**

### **User Story Testing**


#### **Homepage**


#### **Navbar**



#### **Profile**


#### **Authentication**

#### **Error Pages**






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

| **Bug**                                                     | **Issue**                                                                                                                                                                                           | **Resolution**                                                                                                                                                                                                                                                            

## **Unresolved Bugs/Issues**


