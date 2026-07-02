# Test Cases - Checkout & Payment System
## Test Case 1
* **ID** : EB_CO_001
* **Title** : Succesful purchase with saved payment method
* **Description**: Verify that a registered user can successfully complete a purchase using a valid, previously saved payment method.
* **Pre-conditions** : 
    - The user is logged into a verified account.
    - The user has at least one item added to the shopping cart.
    - The user has a valid, non-expired payment method saved with sufficient funds.

* **Test Steps** :

    1. Navigate to the eBay Shopping Cart page (https://cart.ebay.com/)

    2. Click on the 'Go to Checkout' button

    3. Verify that the saved payment method and shipping address are correctly selected.

    4. Click on the 'Place your order' button

* **Expected Result** : The system redirects the user to the order confirmation page, displaying a success message stating "Thank you for your purchase!" along with an order number.
* **Post-conditions** :

    - The total order amount is charged to the user's payment method.
    - An order confirmation email is generated and sent to the user.
    - The shopping cart is cleared of the purchased items.

* **Actual Result** : As expected
* **Status** : PASSED

## Test Case 2
* **ID**: EB_CO_002
* **Title**: Unsuccessful purchase due to declined payment
* **Description**: Verify system handling of a declined transaction due to insufficient payment funds.
* **Pre-conditions** : 
    - The user is logged into a verified account.
    - The user has at least one item added to the shopping cart.
    - The user has a valid payment method saved with insufficient funds.

* **Test Steps** :

    1. Navigate to the eBay Shopping Cart page (https://cart.ebay.com/)

    2. Click on the 'Go to Checkout' button

    3. Verify that the saved payment method and shipping address are correctly selected.

    4. Click on the 'Place your order' button

* **Expected Result** : The user remains on the checkout page. The system displays a prominent error message stating "Your payment was declined. Please try again or select another payment method."
* **Post-conditions** :

    - No charges are applied to the user's payment method.
    - The items remain in the user's shopping cart.
    - The user session remains active.
    - No order confirmation email is generated.

* **Actual Result** : As expected
* **Status** : PASSED