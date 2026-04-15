import os

def check_security():
    print("\n--- Starting Linux Security Audit ---")
    
    # 1. בדיקה אם ה-Firewall מותקן ופעיל
    print("[*] Checking Firewall (UFW) status...")
    check_ufw = os.popen('which ufw').read()
    if not check_ufw:
        print("[!] ALERT: UFW is not installed! Run 'sudo apt install ufw'")
    else:
        ufw_status = os.popen('sudo ufw status').read()
        if "inactive" in ufw_status:
            print("[!] ALERT: Firewall is INACTIVE!")
        else:
            print("[V] Firewall is active.")

    # 2. בדיקת הרשאות לקובץ הסיסמאות הרגיש
    print("[*] Checking /etc/shadow permissions...")
    shadow_perms = os.popen('ls -l /etc/shadow').read()
    # בשרת מאובטח ההרשאות צריכות להיות -rw------- (רק ל-root)
    if "rw-------" not in shadow_perms:
        print(f"[!] WARNING: /etc/shadow has loose permissions: {shadow_perms.strip()}")
        print("    Fix with: sudo chmod 600 /etc/shadow")
    else:
        print("[V] /etc/shadow is secure.")

    # 3. בדיקה אם יש יותר מדי משתמשי Root
    print("[*] Checking for UID 0 users...")
    # חילוץ כל המשתמשים שה-UID שלהם הוא 0
    users_with_root_privs = os.popen("cut -d: -f1,3 /etc/passwd | grep ':0'").read().strip()
    user_list = users_with_root_privs.split('\n')
    
    if len(user_list) > 1:
        print(f"[!] DANGER: Multiple Root-level users found: {', '.join(user_list)}")
    else:
        print(f"[V] Only one Root user detected: {user_list[0]}")

    print("--- Audit Complete ---\n")

if __name__ == "__main__":
    check_security()