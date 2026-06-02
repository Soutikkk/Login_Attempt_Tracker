# Login Attempt Tracker
(Vibecoded)

Welcome to the **Login Attempt Tracker**! This is a simple, beginner-friendly Python command-line application that simulates a secure user authentication system. It demonstrates fundamental programming concepts like functions, loops, conditional statements, file operations, and datetime manipulation.

---

## Features
- **User Authentication:** Validates inputs against stored credentials inside the program.
- **Login Tracking:** Keeps track of total attempts, successful attempts, and failed attempts.
- **Security Lockout:** Automatically locks the account after **3 consecutive failed attempts** to prevent brute-force attacks.
- **Event Logging (Optional feature implemented):** Writes a detailed history of all attempts with precise timestamps to a log file (`login_log.txt`).
- **Interactive Session:** Allows users to try multiple logins or exit cleanly by typing `exit`.
- **Final Session Report:** Displays a complete report showing performance statistics and the current account lock status.

---

## File Structure
- `tracker.py` - Contains the logic and implementation code.
- `login_log.txt` - Created automatically after the first login attempt to store chronological login logs.

---

## Prerequisites & Installation
You only need **Python 3.x** installed on your system to run this script. There are no external libraries or dependencies required.

### How to Run
1. Open your terminal or command prompt.
2. Navigate to the project folder.
3. Run the script using the following command:
   ```bash
   python tracker.py
   ```

---

## Step-by-Step Logic Explanation

Here is a breakdown of how the program handles the logic, structured for beginners:

### 1. Credentials Setup & Importing Modules
We start by importing Python's built-in `datetime` library to handle date and time capture. Then, we store a predefined set of credentials:
```python
CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "password123"
```
*Note: In production environments, credentials should never be stored in plain text, but this serves as a beginner simulation.*

### 2. File Logging Helper (`log_attempt`)
Every time a login is attempted:
- The script retrieves the current time: `datetime.datetime.now()`.
- It formats the time (e.g., `2026-06-03 00:25:00`).
- It opens/creates a text file called `login_log.txt` using the `"a"` (append) mode. This ensures new entries are added to the bottom of the file rather than erasing previous records.
- We wrap this in a `try-except` block to prevent crashes if files are locked or write permissions are restricted.

### 3. Reporting Helper (`display_report`)
When the user exits or the account is locked, this function prints a neat summary report detailing:
- The number of attempts made.
- The breakdown of successes and failures.
- Whether the account ended up in a `LOCKED` or `ACTIVE` state.

### 4. Running the Main Authentication Loop (`main`)
The core flow of the application operates inside a `while` loop that runs continuously until the account is locked or the user chooses to exit:
- **Input Gathering:** The program asks for a username and a password. It uses `.strip()` to clean trailing or leading spaces from the username.
- **Early Exit Check:** If the username entered is `exit`, the loop breaks immediately.
- **Validating Credentials:** 
  - If they match the predefined ones, access is granted. The consecutive failure counter is reset back to `0` (since a success breaks any failure streak).
  - If they don't match, access is denied. We increment the consecutive failure counter.
- **Lockout Mechanism:** If `consecutive_failed_attempts` reaches `3`, the program sets `account_locked` to `True`, displays the lockout message, and exits the loop immediately to protect the account.
