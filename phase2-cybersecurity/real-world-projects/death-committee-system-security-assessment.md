# Death Committee System — Security Assessment

**Project:** Death Committee System<br>
**Application repository:** https://github.com/haseeb-sec/death-committee-system<br>
**Assessment repository:** https://github.com/haseeb-sec/learning-journal<br>
**Assessment type:** Security assessment of a self-developed web application<br>
**Status:** Completed<br>
**Final regression result:** 81/81 backend tests passed

---

## 1. Overview

The Death Committee System is a real web application developed to manage committee membership, contributions, dues, goods, assets, death assistance, settlements, and related accounting operations.

After implementing the application's core functionality, a dedicated security assessment was performed against the running application.

The assessment treated the application as an attacker would and focused on:

- Authentication boundaries
- Role and committee isolation
- Unauthorized object access
- Privilege escalation
- Business-logic restrictions
- Financial-operation integrity
- API input validation
- Session/token behavior
- Frontend/API authorization
- Reproduction and remediation of confirmed weaknesses
- Retesting and regression testing

The assessment identified one confirmed session-security vulnerability and several authorization/business-logic weaknesses that were corrected during the assessment.

---

## 2. Security Assessment Scope

The assessment covered:

- Authentication
- JWT/session handling
- Role-based access control
- Committee-level authorization
- IDOR / BOLA
- Privilege escalation
- Member-management permissions
- Business-logic controls
- Contributions
- Dues
- Settlements
- Accounting integrity
- API input validation
- Error handling
- Information disclosure
- Frontend/API interaction
- Logout/session invalidation
- Regression testing

The assessment focused on the application's own running environment and source code.

---

## 3. Security Assessment Tools

The following tools were used during the assessment.

### Burp Suite Community Edition

Used as the primary HTTP security testing tool for:

- Intercepting application requests
- Inspecting authenticated API requests
- Sending requests to Repeater
- Modifying object identifiers
- Testing authorization boundaries
- Replaying authenticated requests
- Testing cross-user and cross-committee access
- Verifying the session-token vulnerability

### curl

Used for direct API testing, including:

- Authentication requests
- Protected endpoint requests
- Invalid authentication
- Authorization testing
- Logout requests
- Token replay
- Malformed parameters
- HTTP status and response verification

### Chrome DevTools

Used for:

- Inspecting browser localStorage
- Verifying the frontend authentication-token lifecycle
- Testing frontend logout
- Controlled replay of a previously issued token
- Confirming backend rejection of the old token

### WSL / Linux Terminal

Used throughout the assessment for:

- Running the backend and frontend
- Executing API tests
- Inspecting source code and configuration
- Inspecting database state
- Running migrations
- Running regression tests
- Reviewing Git changes

### pytest

Used for backend regression testing.

Final result:

81 passed

### Git and GitHub

Used to isolate, review, commit, push, and merge security changes.

Security branch:

security/session-revocation-and-hardening

Security remediation commit:

4d636f1 security: revoke sessions on logout and harden access controls

### Alembic

Used for the database migration required for server-side session revocation.

### SQLite / Database Inspection

Used to verify application state including:

- User roles
- Committee access
- Administrator privileges
- Token versions
- Settlement state
- Accounting state

### Source Code Review

Backend and frontend source code was reviewed to understand and verify:

- JWT creation and validation
- Authentication dependencies
- RBAC checks
- Committee access controls
- Member access controls
- Administrative checks
- Contribution logic
- Settlement logic
- Accounting logic
- Frontend API calls
- Frontend logout behavior


---

## 4. Methodology

The assessment followed a practical application-security workflow rather than relying only on source-code inspection.

The main approach was:

1. Identify the security boundary being tested.
2. Establish the expected behavior for an authorized user.
3. Repeat the request with an unauthorized user, role, object ID, committee ID, or modified input.
4. Compare the response with the expected authorization boundary.
5. Determine whether the behavior represented a real security weakness or expected application behavior.
6. Reproduce confirmed weaknesses.
7. Implement a targeted remediation.
8. Retest the original attack path.
9. Run the broader backend regression suite to ensure the fix did not introduce regressions.

Testing was performed across the application's three main authorization roles:

- Super Admin
- Committee Admin
- Member

Where relevant, testing also considered committee-level isolation so that access to one committee could not be used to access another committee's data or administrative functions.

The assessment deliberately avoided treating every unusual response as a vulnerability. Findings were classified according to their actual security impact and whether unauthorized access or modification could be demonstrated.

---

## 5. Authentication Testing

Authentication testing focused on whether protected API functionality could be accessed without valid authentication and whether invalid or revoked credentials were rejected.

### Tests performed

- Unauthenticated requests to protected endpoints
- Invalid bearer tokens
- Invalid or expired JWT handling
- Inactive-user authentication behavior
- JWT validation
- Existing-token behavior after logout

### Results

Unauthenticated requests were rejected with HTTP 401.

Invalid authentication tokens were rejected with HTTP 401 and an appropriate authentication error.

Inactive or nonexistent users were not allowed to authenticate through an existing token.

JWT validation was reviewed to ensure that the authenticated user was resolved from the token and validated against the current database state.

Authentication controls were therefore considered effective after remediation of the session-revocation issue described later in this report.

---

## 6. Authorization and RBAC Testing

The application uses role-based access control combined with committee-level access restrictions.

Testing focused on whether users could perform actions outside their assigned role or committee.

### Role boundaries tested

#### Super Admin

The Super Admin has global administrative authority over committees and users.

#### Committee Admin

The Committee Admin is restricted to committees for which they have active administrative access.

#### Member

Members are restricted to their own permitted member data and cannot perform administrative operations.

### Tests performed

- Member access to administrative endpoints
- Committee Admin access to another committee
- Member access to another committee
- Administrative endpoint access without sufficient privileges
- Committee-level authorization checks
- Cross-role access attempts

### Results

Unauthorized administrative requests were rejected.

Committee Admin access was restricted to the committee where the user had active administrative authority.

Member requests attempting to access administrative functionality were denied.

Cross-committee access attempts were denied.

The authorization model was therefore considered effective after the identified access-control weaknesses were corrected.

---


---

## 7. IDOR / BOLA Testing

IDOR (Insecure Direct Object Reference), also commonly discussed as BOLA (Broken Object Level Authorization), was tested by changing object identifiers in authenticated requests.

The main question was whether an authenticated Member could replace their own member ID with another member's ID and access that member's private information.

### Endpoints tested

Cross-user access was tested against:

- /members/{member_id}/financial-summary
- /members/{member_id}/goods
- /members/{member_id}/dues
- /members/{member_id}/statement
- /members/{member_id}/settlement
- /members/{member_id}/contributions
- /members/{member_id}/contributions/total
- /members/{member_id}/dues/outstanding

### Testing approach

A request belonging to an authorized Member was first established.

The member identifier was then changed to another member's identifier while keeping the same authenticated session.

Cross-committee identifiers were also tested where applicable.

### Results

Unauthorized member records were rejected.

Attempts to access another member's financial information, goods, dues, statements, settlements, and contribution information returned an access-denied response rather than the target member's data.

Cross-committee access was also rejected.

No confirmed IDOR/BOLA vulnerability remained after the authorization controls were verified.

---

## 8. Privilege Escalation and Business-Logic Testing

Privilege escalation testing focused on whether a lower-privileged user could obtain administrative capabilities or perform operations reserved for a higher-privileged role.

### Tests performed

- Member attempting administrative operations
- Committee Admin attempting to assign administrator privileges
- Committee Admin attempting access outside the administered committee
- Unauthorized committee administration
- Deactivation of the last active Committee Admin
- Committee creation and administrator assignment
- Member-management permission boundaries

### Findings and remediation

The assessment identified several authorization and business-logic weaknesses that were corrected.

#### Administrative privilege assignment

Committee Admin users were not intended to assign administrator privileges to other users.

The application was reviewed and corrected so that administrator privilege assignment remains restricted to the Super Admin role.

#### Last active Committee Admin

The application originally allowed the last active Committee Admin of a committee to be deactivated.

This could leave a committee without an active administrative user.

The application was changed to reject deactivation when the target user is the last active Committee Admin.

#### Committee creator administrator access

Committee creation was reviewed to ensure that the Super Admin creating a committee receives the expected administrative access to the new committee.

The access assignment was corrected so the creator receives active administrator access.

### Results

Privilege-escalation attempts were denied.

The identified business-logic weaknesses were remediated and subsequently covered by regression testing.

---


---

## 9. Financial and Accounting Integrity Testing

Because the application manages contributions, dues, assets, settlements, and cash accounting, financial integrity was treated as a separate security-testing area.

The objective was to determine whether an unauthorized user could create or manipulate financial records, bypass amount validation, duplicate transactions, or cause an inconsistent settlement or accounting state.

### Contribution testing

The contribution functionality was tested for:

- Authorization requirements
- Committee-level access
- Positive amount validation
- Duplicate same-day contribution handling
- Unauthorized Member attempts
- Cross-committee administrative attempts

### Results

Contribution creation requires appropriate Committee Admin access.

Members were not permitted to create contributions through the administrative contribution endpoint.

Cross-committee administrative attempts were rejected.

Contribution amounts are required to be greater than zero.

Duplicate same-day contributions for the same applicable record are prevented by the application logic.

No confirmed contribution-integrity vulnerability was identified.

### Settlement testing

Settlement creation and payment logic were reviewed and tested.

The assessment verified controls for:

- Authorized settlement creation
- Member and committee association
- Outstanding dues
- Settlement amount consistency
- Negative settlement amounts
- Settlement status
- Cash availability
- Accounting entries
- Duplicate settlement prevention
- Settlement payment authorization

The payment logic verifies that the settlement is pending, the member and required accounts exist, the outstanding dues are satisfied, the stored settlement components match the final amount, and sufficient committee cash is available.

The resulting accounting entry is balanced before the settlement is marked as paid.

A unique member association also prevents multiple settlement records for the same member.

### Results

No confirmed financial or accounting-integrity vulnerability was identified.

The financial controls were therefore considered effective within the tested application scope.

---

## 10. API and Input Security Testing

API input security was tested to determine whether malformed, unexpected, or unauthorized input could bypass application controls or cause unintended behavior.

### Tests performed

- Invalid authentication input
- Invalid bearer tokens
- Malformed path parameters
- Unauthorized object identifiers
- Cross-committee identifiers
- Invalid financial amounts
- Requests made with insufficient privileges
- Validation behavior for protected endpoints

### Results

Invalid authentication was rejected with HTTP 401.

Malformed integer path parameters were rejected with HTTP 422 rather than reaching application logic as an invalid value.

Unauthorized object and committee identifiers were rejected by authorization checks.

Financial amount validation rejected non-positive contribution values.

No confirmed API input-validation vulnerability was identified during the assessment.

This area remains documented as reviewed with no confirmed issue.

---


---

## 11. Error Handling and Information Disclosure

Error responses were reviewed to determine whether malformed requests or unauthorized access could expose sensitive implementation details, database information, stack traces, or other internal data.

### Tests performed

- Invalid authentication
- Unauthorized administrative access
- Unauthorized committee access
- Unauthorized member access
- Invalid member identifiers
- Malformed path parameters
- Error responses from protected endpoints

### Results

Authentication failures returned controlled HTTP 401 responses.

Authorization failures returned controlled access-denied responses.

Malformed integer path parameters returned structured HTTP 422 validation errors.

No application stack traces, database queries, passwords, JWT signing secrets, or other sensitive implementation details were exposed through the tested error responses.

During the assessment, one administrative endpoint initially produced an HTTP 500 response when an unauthorized Member accessed it because an application-level authorization exception was not being handled correctly.

The endpoint was corrected so that unauthorized access now returns a controlled HTTP 403 response instead of an internal server error.

After remediation, no remaining information-disclosure issue was identified.

---


---

## 12. Confirmed Session Security Vulnerability

### Finding

The assessment identified a confirmed session-management vulnerability in the original implementation.

Before remediation, logging out through the frontend only removed the JWT from browser localStorage.

The backend did not invalidate the token.

### Attack scenario

An authenticated user obtains a valid access token.

The user then logs out through the application.

Because the original logout process only removed the token from the browser, a previously captured copy of the token remained usable until its normal expiration.

An attacker who obtained that token could therefore replay it against protected API endpoints even after the legitimate user had logged out.

### Proof of vulnerability

The behavior was reproduced by:

1. Authenticating successfully.
2. Capturing the issued authentication token.
3. Confirming that the token provided access to a protected endpoint.
4. Logging out through the application.
5. Replaying the previously issued token against the protected API.
6. Observing that the old token was still accepted before remediation.

This confirmed that frontend logout did not provide server-side session invalidation.

### Security impact

An attacker possessing a valid but previously captured token could continue accessing protected API resources after the legitimate user had logged out.

The vulnerability therefore affected session revocation and could extend the useful lifetime of a compromised authentication token.

### Remediation

A server-side token-version mechanism was implemented.

A token version was added to the user record.

New JWTs now contain the user's current token version.

During authentication, the token version is compared with the current database value.

A new logout endpoint increments the user's token version.

This invalidates previously issued tokens while allowing a newly authenticated session to receive the current version.

The frontend logout flow was also updated to call the backend logout endpoint before clearing the local token.

### Database change

An Alembic migration added the user token-version field with an initial value of zero.

### Verification

The vulnerability was retested after remediation.

The exact previously issued token was replayed after frontend logout.

The protected API returned:

HTTP 401 Unauthorized

The old token was therefore successfully rejected after logout.

The session-revocation vulnerability was considered fixed and verified end-to-end.

---


---

## 13. Frontend and API Interaction Testing

The frontend was tested together with the backend API to verify that security controls were not dependent only on the user interface.

The assessment specifically considered whether a user could bypass frontend restrictions by directly calling the API.

### Tests performed

- Member access through the normal frontend
- Direct API access using the Member session
- Modification of member identifiers in API requests
- Direct access to administrative endpoints
- Cross-committee API requests
- Frontend logout behavior
- Replay of a previously issued authentication token after logout

### Results

The backend consistently enforced authorization independently of the frontend.

Changing identifiers in API requests did not bypass the backend access controls.

Administrative endpoints remained protected even when called directly rather than through the frontend.

Cross-committee access remained denied.

The frontend logout flow was updated to perform server-side session revocation before removing the local token.

No confirmed frontend/API authorization bypass was identified.

---

## 14. Member-Management Permission and UI Gap

During the assessment, a permission-related usability gap was identified in member management.

Committee Admin users could create members through the application, and the backend already enforced the appropriate member-management authorization. However, the frontend did not provide the Committee Admin with an action to deactivate an ordinary member.

This was treated as a functional permission/UI gap rather than a confirmed authorization vulnerability.

### Remediation

The frontend was updated to:

- Add the member leave/deactivation API action.
- Add a Leave action for active members.
- Restrict the action to users with the appropriate write permission.

The backend authorization remained the final security boundary.

### Verification

The frontend was rebuilt successfully.

A Committee Admin logged into the application and verified that the Leave action was available for an active ordinary member.

The member was successfully deactivated through the frontend and subsequently appeared as inactive.

The member-management gap was therefore considered fixed and verified.

---


---

## 15. Regression Testing

After the security fixes were implemented, the backend test suite was executed to verify that the changes did not break existing functionality.

The first regression run identified one test failure because the authentication token-generation function had been changed to require the new token-version parameter.

The affected test was updated to use the user's current token version.

The complete backend test suite was then executed again.

### Final result

81/81 backend tests passed.

This confirmed that the implemented security changes were compatible with the existing tested application behavior.

---

## 16. Remediation Summary

The following security-related changes were implemented during the assessment.

### Authentication and session security

- Added server-side session revocation using a token-version mechanism.
- Added token-version validation during authentication.
- Added a backend logout endpoint.
- Updated frontend logout to call the backend logout endpoint.
- Verified that a previously issued token is rejected after logout.

### Authorization and RBAC

- Enforced committee-level administrative access.
- Restricted administrator privilege assignment to the Super Admin.
- Prevented unauthorized Member access to administrative functionality.
- Corrected an administrative endpoint that previously returned an internal server error for unauthorized access.

### Business logic

- Prevented deactivation of the last active Committee Admin.
- Ensured the creator of a new committee receives the expected administrator access.

### Member management

- Added the missing frontend Leave action for authorized Committee Admin users.
- Verified successful member deactivation through the frontend.

### Database

- Added the user token-version field through an Alembic migration.
- Verified token-version state in the database.

### Verification

- Replayed the previously issued authentication token after logout and confirmed HTTP 401.
- Rebuilt the frontend successfully.
- Executed the complete backend regression suite.
- Final result: 81/81 tests passed.

---


---


---

## 17. Git and Change Management

Security remediation work was isolated on a dedicated Git branch:

security/session-revocation-and-hardening

The security changes were reviewed, committed, pushed to GitHub, and merged into the main development branch.

Security remediation commit:

4d636f1 security: revoke sessions on logout and harden access controls

The changes included authentication/session hardening, authorization corrections, business-logic protections, database migration changes, frontend logout handling, and the member-management UI correction.

Git was used to keep the security changes traceable and separated from unrelated application development work.

---

## 18. Final Security Status

The status below records the result of the original focused security assessment described in Sections 1–17.

| Area | Assessment Status |
|---|---|
| Authentication | Pass after remediation |
| Authorization / RBAC | Pass after remediation |
| IDOR / BOLA | No confirmed issue |
| Privilege escalation | Pass after remediation |
| Business logic | Pass after remediation |
| Financial/accounting integrity | No confirmed issue |
| API/input security | No confirmed issue |
| Error handling/information disclosure | Pass after remediation |
| Session/token security | Fixed and verified |
| Frontend/API interaction | No confirmed issue |
| Member-management permissions | Fixed and verified |
| Backend regression testing | 81/81 passed |

The main confirmed security vulnerability identified during the original assessment was the ability to replay a previously issued authentication token after frontend logout.

That vulnerability was remediated through server-side session revocation and verified by replaying the old token after logout and receiving HTTP 401 Unauthorized.

Several additional authorization, business-logic, and application-behavior weaknesses were identified and corrected during the assessment.

No confirmed financial-accounting, IDOR/BOLA, or API-input vulnerability remained at the completion of that assessment.

The 81/81 result is intentionally preserved because it records the regression-suite result at that historical assessment stage. Subsequent security hardening and additional regression coverage are documented in Section 20.

---

## 19. Conclusion

The Death Committee System underwent a focused application-security assessment covering authentication, authorization, object-level access control, privilege escalation, business logic, financial operations, API behavior, session management, frontend/API interaction, and regression testing.

The assessment successfully demonstrated that security testing could be performed against the application's real authorization boundaries rather than relying only on theoretical review.

The most significant confirmed issue was the lack of server-side session invalidation after logout. The issue was reproduced, its security impact was established, a targeted remediation was implemented, and the original attack path was retested successfully.

Additional access-control and business-logic weaknesses were also corrected.

Following the original remediation, the backend regression suite completed with 81/81 tests passing.

After the original assessment, the project underwent additional security hardening and regression testing. Those changes are documented separately in Section 21 rather than being mixed into the historical assessment record.

The current project state therefore represents a later security baseline than the 81/81 assessment result recorded above.

This assessment and the subsequent hardening provide a documented example of a complete security workflow:

**Test → Identify → Reproduce → Assess impact → Remediate → Retest → Regression test → Document**

---

---

## 20. Post-Assessment Security Hardening

After the original assessment documented in Sections 1–19, additional security review and hardening were performed against the project.

These changes are recorded separately so that the original assessment results remain historically accurate.

### Authentication and session security

Additional verification and hardening included:

- JWT signature, expiry, subject, and required-claim validation.
- Token-version validation for server-side session revocation.
- Regression coverage for expired, tampered, incomplete, and revoked JWTs.
- Password-reset token expiry and single-use verification.
- Password-length policy enforcement.
- Login rate limiting for repeated failed authentication attempts.

### Authorization and access control

The authorization model was reviewed across the registered API routers and resource boundaries.

Additional work included:

- Explicit separation of authorization failures from resource-level accounting errors.
- Correct HTTP 403 handling for permission failures where appropriate.
- Continued committee-level isolation and member/resource ownership checks.
- Review of cross-committee and cross-member authorization coverage.
- Verification that administrative operations remain restricted to the appropriate roles.

### Financial and business-logic integrity

Additional integrity controls were reviewed and tested for:

- Committee asset valuation chronology.
- Member good valuation chronology.
- Settlement and death-support date ordering.
- Settlement snapshot consistency.
- Inactive-member financial operations.
- Contribution-rate effective-date uniqueness.
- Committee asset valuation-date uniqueness.
- Member good valuation-date uniqueness.

For valuation history, uniqueness is enforced at both the application/model level and the database schema level where appropriate.

### Security configuration and HTTP protections

Additional application hardening included:

- Configurable CORS origins.
- Production configuration validation for the JWT secret and token expiry.
- Security response headers including `X-Content-Type-Options`, `X-Frame-Options`, and `Referrer-Policy`.
- Verification that real environment files and local development artifacts are excluded from source control.

### Dependency and repository security

The project was additionally checked for:

- Backend dependency vulnerabilities using `pip-audit`.
- Frontend dependency vulnerabilities using `npm audit`.
- Dependency consistency with `pip check`.
- Accidental tracking of databases, environment files, build artifacts, caches, backups, and temporary development files.
- Automated CI checks for backend tests, frontend checks, and dependency security scanning.

### Current verification baseline

The current backend regression suite contains **103 passing tests**.

The original assessment's 81/81 result should therefore be understood as a historical checkpoint, while 103/103 represents the later verified baseline after additional security hardening and regression coverage.

The current project remains an active portfolio/development application and is not presented as a production security certification or guarantee.

---

---

## 21. Related Resources


### Application Repository

https://github.com/haseeb-sec/death-committee-system

### Security Assessment Documentation

https://github.com/haseeb-sec/learning-journal

### Cybersecurity Write-ups

https://github.com/haseeb-sec/learning-journal/tree/main/phase2-cybersecurity/write-ups

### Security Assessment Directory

phase2-cybersecurity/real-world-projects/

---
