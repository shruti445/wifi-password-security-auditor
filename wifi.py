import re

def check_password_strength(password):
    score = 0
    remarks = []

    # Length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        remarks.append("Password is too short.")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        remarks.append("Add uppercase letters.")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        remarks.append("Add lowercase letters.")

    # Numbers
    if re.search(r"\d", password):
        score += 1
    else:
        remarks.append("Add numbers.")

    # Special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 2
    else:
        remarks.append("Add special characters.")

    # Common passwords
    common_passwords = [
        "password",
        "12345678",
        "admin123",
        "qwerty",
        "password123",
        "welcome",
        "letmein"
    ]

    if password.lower() in common_passwords:
        remarks.append("Password is commonly used.")
        score = 0

    if score >= 7:
        strength = "Very Strong"
    elif score >= 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, remarks


print("========== Wi-Fi Password Security Auditor ==========")

wifi_name = input("Enter Wi-Fi Name (SSID): ")
password = input("Enter Wi-Fi Password: ")

strength, suggestions = check_password_strength(password)

print("\n------ Audit Report ------")
print("Wi-Fi Name :", wifi_name)
print("Password Strength :", strength)

if suggestions:
    print("\nSuggestions:")
    for s in suggestions:
        print("-", s)
else:
    print("\nExcellent! Your password follows good security practices.")
