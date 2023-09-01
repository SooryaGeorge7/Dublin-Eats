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



### **W3C Markup Validator**



### **Lighthouse**



### **Lighthouse Errors**



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


