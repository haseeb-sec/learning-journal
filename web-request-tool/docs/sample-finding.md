# Sample Security Finding 

## Finding 1

## Title

Missing `Content-Security-Policy (CSP)` Header

## Severity

Medium

## Description

During a security assessment of `https://python.org` using a custom `Web Security Header Analyzer`, the HTTPS response was found to be missing the `Content-Security-Policy (CSP)` header.

The `Content-Security-Policy` header is a browser security mechanism that helps control which scripts, styles, and other resources are allowed to load and execute. It reduces the impact of several client-side attacks by restricting untrusted content.

## Evidence

Target: `https://python.org`

Web Security Header Analyzer Output:

`[MISSING] Content-Security-Policy`

## Impact

Without a `Content-Security-Policy` header, browsers have fewer restrictions on which resources can be loaded and executed. If another client-side vulnerability exists, such as Cross-Site scripting, the absence of CSP may increase its impact by allowing malicious scripts to execute more easily.

## Recommendation

Configure and deploy an appropriate `Content-Security-Policy` that allows scripts, styles, images, and other resources only from trusted sources. Test the policy carefully to ensure that legitimate website functionality continues to work after deployment.

---

## Finding 2

## Title

Missing `X-Content-Type-Options` Header

## Severity

Medium

## Description

During the security assessment of `https://python.org`, the `X-Content-Type-Options` header was not present in the HTTP response. This header instructs browsers not to perform MIME type sniffing and to respect the content type specified by the server.

## Evidence 

Target: `https://python.org`

Web Security Header Analyzer Output:

`[MISSING] X-Content-Type-Options`

## Impact

Without the `X-Content-Type-Options` header, browsers may perform `MIME type sniffing` and incorrectly interpret certain files. If an attacker is able to upload or manipulate content, this could increase the risk of malicious files being executed instead of treated as harmless content.

## Recommendation

Configure the web server to include the `X-Content-Type-Options: nosniff` HTTP response header for all applicable responses. After deployment, verify that browsers correctly respect the declared content types and that website functionality remains unaffected.

---

## Finding 3

## Title

Missing `X-XSS-Protection` Header 

## Severity

Low

## Description

During the security assessment of `https://python.org`, the `X-XSS-Protection` header was not present in the HTTP response. This header was historically used to enable built-in browser protection against some reflected `Cross-Site Scripting (XSS)` attacks. However, most modern browsers have deprecated or removed support for this header.

## Evidence

Target: `https://python.org`

Web Security Header Analyzer Output:

`[MISSING] X-XSS-Protection`

## Impact

The absence of the `X-XSS-Protection` header has limited security impact on modern browsers because support for the header has been deprecated. Websites should instead rely on stronger defenses such as `Content Security Policy (CSP)`, `secure coding` practices, and proper `input validation`.

## Recommendation

Focus on implementing and maintaining modern protections such as `Content Security Policy (CSP)`, `secure input validation`, and `output encoding`. The `X-XSS-Protection` header may be added for compatibility with older browsers if required, but it should not be relied upon as the primary defense against `Cross-Site Scripting` attacks.