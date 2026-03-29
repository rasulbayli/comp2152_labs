# ============================================================
#  WEEK 11 LAB — Q2: PASSWORD STRENGTH CHECKER CLASS
#  COMP2152 — Rasul Dadashbayli 101527648
# ============================================================


class PasswordChecker:
    def __init__(self):
        self.common_passwords = ["password", "123456", "admin", "root", "letmein", "qwerty", "abc123"]
        self.history = []

    def check_common(self, password):
        return password.lower() in self.common_passwords

    def check_strength(self, password):
        has_length  = len(password) >= 8
        has_digit   = any(c.isdigit() for c in password)
        has_special = any(c in "!@#$%^&*" for c in password)
        return {"length": has_length, "digit": has_digit, "special": has_special}

    def evaluate(self, password):
        if self.check_common(password):
            result = "WEAK (common password)"
        else:
            checks = self.check_strength(password)
            passed = sum(checks.values())
            if passed <= 1:
                result = "WEAK"
            elif passed == 2:
                result = "MEDIUM"
            else:
                result = "STRONG"

        self.history.append((password, result))
        return result


# --- Main ---
if __name__ == "__main__":
    print("=" * 60)
    print("  Q2: PASSWORD STRENGTH CHECKER")
    print("=" * 60)

    checker = PasswordChecker()

    test_passwords = ["admin", "hello", "hello123", "MyP@ss99", "p@ssw0rd!", "root"]

    print("\n--- Checking Passwords ---")
    for pw in test_passwords:
        result = checker.evaluate(pw)
        print(f"  {pw:<16}  {result}")

    print("\n--- Check History ---")
    for pw, result in checker.history:
        print(f"  {pw:<16}: {result}")

    print("\n" + "=" * 60)
