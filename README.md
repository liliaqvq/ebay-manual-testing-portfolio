# eBay E-Commerce Testing Portfolio

## 📌 Project Overview
This project serves as a professional Quality Assurance portfolio, focusing on the documentation and design of manual test cases for critical e-commerce functionalities. Using **eBay** as the target application, this repository demonstrates structural test case design, covering both positive (happy path) and negative scenarios.

## 🛠️ Skills & Concepts Applied
* **Test Case Design**: Documenting Pre-conditions, Test Steps, Expected Results, and Post-conditions.
* **Negative Testing**: Simulating system failures (e.g., declined payments) to verify error handling and state persistence.
* **Requirements Analysis**: Translating complex business logic into clear, executable testing documentation.
* **Markdown Standard**: Organizing documentation for high scannability and professional presentation.

## 📂 Repository Structure
The test cases are organized by functional modules:
* `/login-module.md` - Verification of user authentication, valid sessions, and invalid credential constraints.
* `/checkout-module.md` - Verification of the purchasing funnel, payment processing, and boundary behaviors like insufficient funds.

## 📝 Test Case Breakdown
A total of 5 high-priority test cases have been documented across the following areas:

### 1. Login System (`login-module.md`)
* **EB_LOG_001**: Successful user login with valid credentials (Positive).
* **EB_LOG_002**: Unsuccessful login attempt with unregistered email (Negative).
* **EB_LOG_003**: Successful password reset request (Positive).

### 2. Checkout & Payment System (`checkout-module.md`)
* **EB_CO_001**: Successful purchase using a saved, valid payment method (Positive).
* **EB_CO_002**: Unsuccessful purchase transaction due to insufficient funds (Negative).

## 🐛 Bug Reporting & Issue Tracking

To demonstrate my defect reporting skills and technical documentation criteria, I manage and track system bugs directly through GitHub Issues as my primary test management tool. 

Below is a live link to a high-severity bug report created for this portfolio:

* **[Checkout Module]** - [Bug #1: Application freezes when clicking 'Place Order' with an expired session token](https://github.com/liliaqvq/ebay-manual-testing-portfolio/issues/1)
  * **Key Skills Demonstrated:** Cross-browser verification, browser console log analysis, business impact evaluation (core conversion funnel validation), severity and priority assessment.


