## Question 2
### Part 1
Please devise an integration test case that prevents members from accessing other’s medical data.

### TC-IN-100 – Verify Members Cannot Access Other Members’ Medical Data

**Description:** 
Ensures the each logged-in Member can only access their own medical questionnaire and data, even if attempting to modify the URL encounterId value
**Preconditions:** 
Member A and Member B have valid accounts.
 * Both have started or completed a medical questionnaire.
 * Member A is logged in through an authenticated session.

**Test Steps:**
1. Log in as Member A and begin the Medical Questionnaire.

2. Capture the "encounterId" (for test tracking purposes).

3. Attempt to access Member B’s questionnaire by:
	>Directly modifying the URL  (e.g., /medical-questionnaire?direct=true&clearData=true&extraData={"encounterId":"##########"})

4. Observe the system’s response. Member A and B are logged out, and returned to the login page.

**Expected Result:**
* The system exits the Medical Questionnaire.
* Member A’s session is scoped only to their own data.
* No Personally Identifiable Information (PII) or medical data from Member B is exposed.

**Priority:** P0 – Critical

**Type:** Integration / Security

**Status:** Not Executed

---

### Part 2
Submit a written HTTP requisitions:

1. Authenticate as Member A
POST https://myezra-staging.ezra.com/api/auth/login
Headers:
  Content-Type: application/json
Body:
{
  "email": "memberA@test.com",
  "password": "FakePassword123!"
}
Expected Response:
  200 OK
  {
    "userId": "A12345",
    "token": "FAKEtoken123456789"
  }
2. Access Member A’s Own Medical Questionnaire
GET https://myezra-staging.ezra.com/api/medical-questionnaire?encounterId=ENC-001
Headers:
  Authorization: Bearer FAKEtoken123456789
  Content-Type: application/json
Expected Response:
  200 OK
  {
    "encounterId": "ENC-001",
    "memberId": "A12345",
    "questionnaireData": { ... }
  }
3. Attempt Unauthorized Access (Member B’s Questionnaire)
GET https://myezra-staging.ezra.com/api/medical-questionnaire?encounterId=ENC-002

Headers:
Authorization: Bearer FAKEtoken123456789
Content-Type: application/json
Expected Response:
403 Forbidden
{
"error": "Access denied. You are not authorized to view this questionnaire."
}

### Description of Importance
Protecting medical data privacy is critical. This test confirms that cross-user access is impossible, ensuring compliance and user trust in Ezra’s booking and questionnaire system.

---

### Part 3 
What is your thought process around managing the security quality of these endpoints? What are the tradeoffs and potential risks of your solution?

My approach would be to first classify and prioritize endpoints by sensitivity, making sure the most critical ones, like those handling medical or payment data get the highest focus. I’d combine automated tests, integration checks, and continuous monitoring to catch any misses, while enforcing strict authentication and authorization at every step. Like with most thing there are tradeoffs, for example extra setup time and maintenance and potential performance impact, but protecting member data is far more important. The goal is a process that’s reliable, repeatable, and keeps sensitive data safe across the board.
