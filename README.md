# WiFi Password Security Auditor

## 📌 Project Overview

The WiFi Password Security Auditor is a Python-based cybersecurity project designed to help users evaluate the strength of saved WiFi passwords on their own computer. It analyzes password complexity based on factors such as length and character variety, then provides security recommendations to encourage stronger passwords.

**Note:** This project is intended only for auditing WiFi profiles that belong to the user or for which the user has permission.

---

## 🎯 Objectives

- Analyze the strength of saved WiFi passwords.
- Promote good password security practices.
- Demonstrate Python programming and basic cybersecurity concepts.
- Generate a simple password security report.

---

## ✨ Features

- View saved WiFi profile names.
- Analyze password strength.
- Check password length and complexity.
- Detect weak passwords.
- Display security recommendations.
- Generate a text-based audit report.
- User-friendly command-line interface.
- Error handling for unsupported systems.

---

## 🛠️ Technologies Used

- Python 3.14
- Standard Python Libraries
  - `subprocess`
  - `re`
  - `os`
  - `datetime`

---

## 📂 Project Structure

```
WiFi-Password-Security-Auditor/
│
├── wifi_auditor.py
├── requirements.txt
├── README.md
└── audit_report.txt
```

---

## ▶️ Requirements

- Python 3.14 or later
- Windows operating system (for accessing saved WiFi profiles)
- Administrator privileges may be required for some operations.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/WiFi-Password-Security-Auditor.git
```

### 2. Open the project folder

```bash
cd WiFi-Password-Security-Auditor
```

### 3. Install dependencies (if required)

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

Run the project using:

```bash
python wifi_auditor.py
```

or

```bash
python3 wifi_auditor.py
```

---

## 📊 Example Output

```
=========================================
WiFi Password Security Auditor
=========================================

Saved WiFi Profiles Found: 5

Profile: Home_WiFi
Password Strength: Strong
Recommendation: Password meets basic security guidelines.

Profile: Office_WiFi
Password Strength: Medium
Recommendation: Consider using a longer password with special characters.

Audit completed successfully.
Report saved to audit_report.txt
```

---

## 📚 Learning Outcomes

- Python programming
- Password strength evaluation
- Basic cybersecurity principles
- File handling
- Command-line application development
- Report generation

---

## ⚠️ Disclaimer

This project is intended **only for educational purposes and for auditing WiFi profiles that you own or are authorized to access**. It should not be used to obtain or attempt to access WiFi passwords or networks without permission.

---

## 👩‍💻 Author

**Shruti Chanoria**

B.Tech Information Technology

Cybersecurity Mini Project
