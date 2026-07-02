# Test Cases - Login System
## Test Case 1
* **ID** : EB_LOG_001
* **Title** : Successful user login with valid credentials
* **Description** : Verify that user succesfully logs in when valid credentials are used.
* **Pre-conditions** : 

    - The tester has a verified user account in the QA staging environment.

* **Test Steps** :

    1. Navigate to the Ebay login page (https://www.ebay.com/signin)

    2. Type 'sleepycat@gmail.com' in the 'Email or username' field

    3. Type 'secretspycat123' in the 'Password' field 

    4. Click on the 'Sign In' button

* **Expected Result** : System redirects the user to their account Dashboard and shows 'Hi, sleepycat' on top left corner.
* **Post-conditions** :

    - The user session remains active.

* **Actual Result** : As expected
* **Status** : PASSED

## Test Case 2
* **ID** : EB_LOG_002
* **Title** : Unsuccesful user login with invalid credentials
* **Description** : Verify that user does not log in when invalid credentials are used.
* **Pre-conditions** :

    - The credentials used for the test are not registered in the system database.

* **Test Steps** :

    1. Navigate to the Ebay login page (https://www.ebay.com/signin)

    2. Type 'hackercat@gmail.com' in the 'Email or username' field

    3. Type 'hackercat963' in the 'Password' field 

    4. Click on the 'Sign In' button

* **Expected Result** : The user remains on the login page. An error message is displayed stating: "We couldn't find this eBay account" and the field is highlighted in red.
* **Post-conditions** :

    - The user session remains inactive.

* **Actual Result** : As expected
* **Status** : PASSED

## Test Case 3
* **ID** : EB_LOG_003
* **Title** : Successful password reset request
* **Description** : Verify that the system successfully triggers a password reset email when a valid registered email is provided.
* **Pre-conditions** : 

    - The email 'sleepycat@gmail.com' belongs to a registered account in the system database.

* **Test Steps** :

    1. Navigate to the Ebay login page (https://www.ebay.com/signin)

    2. Click on 'Forgot password' button

    3. Type 'sleepycat@gmail.com' in the 'Email' field 

    4. Click on the 'Send link' button

* **Expected Result** : The system redirects the user to a confirmation page and displays a success message stating that a verification link has been sent to 'sleepycat@gmail.com'.
* **Post-conditions** :

    - A valid password reset token/email is generated and sent to the user's email address.

* **Actual Result** : As expected
* **Status** : PASSED
