```python
import datetime

# =========================
# Configuration
# =========================

CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "password123"
MAX_FAILED_ATTEMPTS = 3
LOG_FILE = "login_log.txt"


# =========================
# Logging Function
# =========================

def log_attempt(username, status):
    """Save a login attempt with the current date and time."""

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_entry = (
        f"[{current_time}] "
        f"Username: '{username}' | "
        f"Status: {status}\n"
    )

    try:
        with open(LOG_FILE, "a", encoding="utf-8") as file:
            file.write(log_entry)

    except OSError as error:
        print(f"Warning: Unable to write to log file. {error}")


# =========================
# Report Function
# =========================

def display_report(total, successful, failed, locked):
    """Display the login attempt summary."""

    print("\n" + "=" * 45)
    print("          LOGIN ATTEMPT REPORT")
    print("=" * 45)

    print(f"Total Login Attempts:       {total}")
    print(f"Successful Login Attempts:  {successful}")
    print(f"Failed Login Attempts:      {failed}")

    account_status = (
        "LOCKED (Security Lockout)"
        if locked
        else "ACTIVE / OPEN"
    )

    print(f"Current Account Status:     {account_status}")
    print("=" * 45)


# =========================
# Login Function
# =========================

def login():
    """
    Handle the login process.

    Returns:
        tuple: total attempts, successful attempts,
               failed attempts, account lock status
    """

    total_attempts = 0
    successful_attempts = 0
    failed_attempts = 0
    consecutive_failures = 0
    account_locked = False

    print("\n=== Welcome to the Login Attempt Tracker ===")
    print("Enter 'exit' as the username to quit.\n")

    while not account_locked:

        username = input("Enter username: ").strip()

        # Allow the user to exit
        if username.lower() == "exit":
            print("\nExiting the application...")
            break

        password = input("Enter password: ")

        total_attempts += 1

        # Check credentials
        if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:

            successful_attempts += 1
            consecutive_failures = 0

            print("\nAccess Granted! Login Successful.\n")

            log_attempt(username, "SUCCESS")

        else:

            failed_attempts += 1
            consecutive_failures += 1

            print("\nAccess Denied! Incorrect username or password.")

            remaining_attempts = MAX_FAILED_ATTEMPTS - consecutive_failures

            if remaining_attempts > 0:
                print(
                    f"Warning: {remaining_attempts} "
                    f"attempt(s) remaining before lockout.\n"
                )

            log_attempt(username, "FAILED")

            # Lock account after maximum failures
            if consecutive_failures >= MAX_FAILED_ATTEMPTS:
                account_locked = True
                print("\nAccount locked due to too many failed attempts.")

    return (
        total_attempts,
        successful_attempts,
        failed_attempts,
        account_locked
    )


# =========================
# Main Program
# =========================

def main():

    (
        total,
        successful,
        failed,
        locked
    ) = login()

    display_report(
        total,
        successful,
        failed,
        locked
    )


# =========================
# Program Entry Point
# =========================

if __name__ == "__main__":
    main()
```
