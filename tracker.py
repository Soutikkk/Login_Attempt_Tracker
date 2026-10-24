
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
    """Record a login attempt with its date and time."""

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] Username: '{username}' | Status: {status}\n"

    try:
        with open(LOG_FILE, "a", encoding="utf-8") as file:
            file.write(log_entry)
    except OSError as error:
        print(f"Warning: Could not write to log file: {error}")


# =========================
# Report Function
# =========================

def display_report(total, successful, failed, locked):
    """Display a summary of login activity."""

    print("\n" + "=" * 45)
    print("           LOGIN ATTEMPT REPORT")
    print("=" * 45)
    print(f"Total Login Attempts     : {total}")
    print(f"Successful Attempts      : {successful}")
    print(f"Failed Attempts          : {failed}")
    print(f"Maximum Failed Attempts  : {MAX_FAILED_ATTEMPTS}")
    print(f"Account Status           : {'LOCKED' if locked else 'ACTIVE / OPEN'}")
    print("=" * 45)


# =========================
# Login Function
# =========================

def login():
    """Manage login attempts and return a summary."""

    total_attempts = 0
    successful_attempts = 0
    failed_attempts = 0
    consecutive_failures = 0
    account_locked = False

    print("\n=== LOGIN ATTEMPT TRACKER ===")
    print("Enter 'exit' as the username to quit.\n")

    while not account_locked:
        username = input("Enter username: ").strip()

        if username.lower() == "exit":
            print("\nExiting application...")
            break

        password = input("Enter password: ")
        total_attempts += 1

        if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
            successful_attempts += 1
            consecutive_failures = 0

            print("\nAccess Granted! Login Successful.\n")
            log_attempt(username, "SUCCESS")

        else:
            failed_attempts += 1
            consecutive_failures += 1

            print("\nAccess Denied! Invalid username or password.")
            log_attempt(username, "FAILED")

            remaining = MAX_FAILED_ATTEMPTS - consecutive_failures

            if remaining > 0:
                print(f"Warning: {remaining} attempt(s) remaining before lockout.\n")
            else:
                account_locked = True
                print("\nAccount locked due to too many failed attempts.")

    return (
        total_attempts,
        successful_attempts,
        failed_attempts,
        account_locked
    )


# =========================
# Main Function
# =========================

def main():
    total, successful, failed, locked = login()

    display_report(total, successful, failed, locked)


# =========================
# Program Entry Point
# =========================

if __name__ == "__main__":
    main()
