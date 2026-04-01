# 🛡️ Security Policy

## ⚠️ Ethical Use Warning
ShadowGuard is developed strictly for **educational and research purposes** as part of the [CEH repository](https://github.com). 
*   **Do not** use this tool on any systems or networks without explicit, written permission from the owner.
*   The author is not responsible for any misuse or damage caused by this application.

## 🚀 Supported Versions
We actively provide security updates for the following versions:


| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | ✅ Yes             |
| < 1.0   | ❌ No              |

## 🛠️ Reporting a Vulnerability
We take the security of this tool seriously. If you discover a vulnerability, please do not report it via public GitHub issues. Instead, follow this process:

1.  **Private Disclosure:** Please report the issue privately by [opening a Draft Security Advisory](https://github.com/security/advisories/new) on GitHub.
2.  **Details to Include:**
    *   Description of the vulnerability.
    *   Steps to reproduce (PoC).
    *   Potential impact (e.g., bypass of monitoring).
3.  **Response Timeline:** You can expect an initial acknowledgement within **48 hours**.

## 🌐 External Threat Reporting (AbuseIPDB)
If ShadowGuard detects malicious activity or unauthorized access attempts originating from a public IP address that falls under the purview of reporting:

*   **Reporting:** We encourage users to report these IPs to [AbuseIPDB.com](https://abuseipdb.com) to help the global security community.
*   **Automation:** Future versions of ShadowGuard may include a module to automate this reporting via the AbuseIPDB API (API key required).
*   **Verification:** Ensure the IP is not a false positive (e.g., local network testing) before reporting.

## 🛡️ Our Security Standards
To maintain the integrity of this repository, we utilize:
*   **Dependency Scanning:** Monitoring for vulnerable third-party libraries via GitHub alerts.
*   **Manual Review:** All PRs and code changes are manually audited for security flaws to ensure the tool remains a reliable part of the CEH lab environment.
