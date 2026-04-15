## 📊 Real-World Audit Examples

### 1. Security Alert Found:
When the script detects loose permissions on `/etc/shadow`, it provides a clear warning and a remediation command:
`[!] WARNING: /etc/shadow has loose permissions!`
`Fix with: sudo chmod 600 /etc/shadow`

### 2. Passing Audit:
After hardening the system, the output confirms the secure state:
`[V] /etc/shadow is secure.`
`[V] Firewall is active.`
`[V] Only one Root user detected.`

## 🛡️ Remediation Steps (Hardening)
To achieve a 100% pass rate with this tool:
* **Firewall:** Run `sudo ufw enable`
* **File Permissions:** Run `sudo chmod 600 /etc/shadow`