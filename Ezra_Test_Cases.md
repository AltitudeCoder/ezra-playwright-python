# Ezra Manual Test Cases

---

### TC001 - New Member Account Creation

**Description**  
Verify a new user can create an Ezra member account from the Join page using valid information.

**Preconditions**  
User is on [https://myezra-staging.ezra.com/join](https://myezra-staging.ezra.com/join)

**Steps**  
1. Enter valid First Name, Last Name, Email, Phone, and Password.  
2. Agree to required Terms of Use, Telehealth Policy, and Privacy Policy.  
3. Click “Submit”.  

**Expected Result**  
Account is successfully created, and the user is redirected to the booking (Select Scan) page.

**Priority:** P1 – Critical  
**Type:** Functional  
**Status:** Not Executed  
**Description of Importance:**  
If a new user is unable to create an account, no further steps in the flow can proceed.

---

### TC002 - Verify Member Can Select from Available Scan Options

**Description**  
Ensure a Member can view all available scan plans and select one to proceed.

**Preconditions**  
Member is logged in and on the "Select Scan" page.

**Steps**  
1. Verify that all plans are displayed correctly (MRI Scan, MRI Scan with Spine, MRI Scan with Skeletal and Neurological Assessment, and Heart & Lungs CT Scan).  
2. Select a valid plan option (e.g., "MRI Scan with Spine").  
3. Click the "Continue" button.  

**Expected Result**  
Plan selection is saved and the health questions popover is displayed.

**Priority:** P1 – Critical  
**Type:** Functional  
**Status:** Not Executed  
**Description of Importance:**  
This step defines user engagement with Ezra’s core offering. If users cannot select a plan, the flow breaks and conversion halts.

---

### TC003 - Verify Member Can Enter Valid Payment Information

**Description**  
Confirm that all required payment fields accept valid inputs and enforce proper validation.

**Preconditions**  
Member is on the "Reserve Your Appointment" page.

**Steps**  
1. Enter a valid credit card number, expiration date, CVV, and ZIP code.  
2. Select a country from the dropdown.  
3. Verify that reservation details (selected plan, add-ons, location, date, and time) are correct.  
4. Click the "Continue" button to submit payment.  

**Expected Result**  
All inputs accept valid values. Country defaults to "United States". No validation errors occur.

**Priority:** P1 – Critical  
**Type:** Functional  
**Status:** Not Executed  
**Description of Importance:**  
If users cannot complete payment, the transaction fails. This validates the entire booking pipeline.

---

### TC004 - Verify Account Creation Validation for Required Fields

**Description**  
Confirm that required fields (First Name, Last Name, Email, Password) enforce validation and display error messages for missing or invalid inputs.

**Preconditions**  
User is on the Join Page.

**Steps**  
1. Attempt to proceed without entering a first name.  
2. Attempt to proceed without entering a last name.  
3. Enter an invalid email (e.g., “user@”) and submit.  
4. Enter a password that does not meet requirements.  

**Expected Result**  
Appropriate validation messages appear for each field (e.g., “The Email field is invalid”).  

**Priority:** P2 – High  
**Type:** Validation  
**Status:** Not Executed  

---

### TC005 - Verify “Continue” Button Activation After Selecting a Scan

**Description**  
Confirm that a scan must be selected to activate the "Continue" button.

**Preconditions**  
Member is logged in and on the Select Scan page.

**Steps**  
1. Attempt to continue without selecting a scan.  
2. Select a scan and observe the button state.

**Expected Result**  
The “Continue” button activates only after a scan is selected.

**Priority:** P3 – Medium  
**Type:** Functional / Validation  
**Status:** Not Executed  

---

### TC006 - Verify Health Questions Questionnaire Popover Displays

**Description**  
Verify that selecting the “Heart & Lungs CT Scan” add-on triggers the health questions popover after clicking “Continue”.

**Preconditions**  
Member is logged in, age ≥ 35, and has selected the Heart & Lungs CT Scan add-on.

**Steps**  
1. Select a scan.  
2. Enable the Heart & Lungs CT Scan add-on.  
3. Click the “Continue” button.

**Expected Result**  
Health questionnaire popover with five questions appears.

**Priority:** P2 – High  
**Type:** Functional  
**Status:** Not Executed  

---

### TC007 - Verify “Submit” Button Activation After Completing Questions

**Description**  
Ensure that all questions must be answered before the “Submit” button becomes active.

**Preconditions**  
Member is viewing the health questionnaire popover after selecting the Heart & Lungs CT Scan add-on.

**Steps**  
1. Answer each required question.  
2. Observe the “Submit” button state.

**Expected Result**  
The “Submit” button activates once all mandatory questions are completed.

**Priority:** P2 – High  
**Type:** Functional / Validation  
**Status:** Not Executed  

---

### TC008 - Verify Conditional Add-On Option for Heart & Lungs CT Scan

**Description**  
Confirm that only Members aged 35+ can select the Heart & Lungs CT Scan add-on.

**Preconditions**  
Member is on the Select Scan page.

**Steps**  
1. Enter DOB 01/01/1990.  
2. Enter DOB 01/01/1991.

**Expected Result**  
Add-on is available for DOB 01/01/1990 and unavailable for DOB 01/01/1991.

**Priority:** P3 – Medium  
**Type:** Functional  
**Status:** Not Executed  

---

### TC009 - Verify State-Based Location Filtering

**Description**  
Ensure that selecting a state displays only locations within that state.

**Preconditions**  
Member is on the "Schedule Your Scan" page.

**Steps**  
1. Open the State dropdown.  
2. Select a valid state (e.g., California).  

**Expected Result**  
Only locations in the selected state are displayed.

**Priority:** P3 – Medium  
**Type:** Functional  
**Status:** Not Executed  

---

### TC010 - Verify Date and Time Selection Flow

**Description**  
Confirm that selecting a location displays scheduling fields and allows date/time selection.

**Preconditions**  
Member is on the "Schedule Your Scan" page and has selected a state.

**Steps**  
1. Select a location.  
2. Verify calendar and time options appear.  
3. Select a date and time.

**Expected Result**  
Calendar and time pickers display and store selected values.

**Priority:** P2 – High  
**Type:** Functional  
**Status:** Not Executed  

---

### TC011 - Verify Navigation to “Reserve Your Appointment” Page

**Description**  
Confirm that after scheduling, the user navigates to the payment (“Reserve Your Appointment”) page.

**Preconditions**  
Valid location, date, and time have been selected.

**Steps**  
1. Click “Continue” on the Scheduling page.

**Expected Result**  
The “Reserve Your Appointment” page is displayed.

**Priority:** P2 – High  
**Type:** Functional  
**Status:** Not Executed  

---

### TC012 - Verify Transition to “Begin Medical Questionnaire” After Payment

**Description**  
Ensure successful payment redirects the Member to the Medical Questionnaire page.

**Preconditions**  
All payment fields are valid and accepted.

**Steps**  
1. Click “Continue” on the Payment page.

**Expected Result**  
Payment is processed and user is redirected to the “Begin Medical Questionnaire” page.

**Priority:** P2 – High  
**Type:** End-to-End Functional  
**Status:** Not Executed  

---

### TC013 - Verify “3 Times Available” Popover Functionality

**Description**  
Validate that the “3 Times Available” popover appears and can be acknowledged.

**Preconditions**  
Member selects a date/time combination that triggers the popover.

**Steps**  
1. Observe the popover.  
2. Click “I Understand”.

**Expected Result**  
Popover closes and scheduling flow continues.

**Priority:** P3 – Medium  
**Type:** Functional  
**Status:** Not Executed  

---

### TC014 - Verify Password Strength Validation

**Description**  
Validate that password requirements display correctly and strength meter updates dynamically.

**Preconditions**  
User is on the Join page.

**Steps**  
1. Enter characters into the Password field.  
2. Observe checklist and strength meter behavior.

**Expected Result**  
Checklist updates dynamically. Strength meter turns green when all requirements are met.

**Priority:** P2 – High  
**Type:** UI / Functional  
**Status:** Not Executed  

---

### TC015 - Verify Tooltip Content Accuracy

**Description**  
Validate that hovering over tooltip icons displays correct informational copy.

**Preconditions**  
Member is on the Select Scan page.

**Steps**  
1. Hover over each tooltip icon (“i”) next to feature descriptions.  
2. Verify displayed text matches expected content.

**Expected Result**  
Each tooltip displays accurate and complete copy.

**Priority:** P4 – Low  
**Type:** UI / Content Verification  
**Status:** Not Executed  

---
