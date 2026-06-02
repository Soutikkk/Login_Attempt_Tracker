import datetime

# Predefined username and password stored inside the code
CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "password123"

def log_attempt(username, status):
    """
    Saves the login attempt details to a text file called 'login_log.txt'.
    Includes the current date and time.
    """
    # Get the current date and time formatted nicely
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Format the log line
    log_line = f"[{current_time}] Username: '{username}' | Status: {status}\n"
    
    try:
        # Open the file in 'append' mode ('a') so we don't overwrite previous attempts
        with open("login_log.txt", "a") as log_file:
            log_file.write(log_line)
    except IOError as e:
        print(f"Warning: Could not save log entry. Error: {e}")

def display_report(total, success, failed, is_locked):
    """
    Displays the summary report at the end of the program execution.
    """
    print("\n" + "=" * 40)
    print("           LOGIN ATTEMPT REPORT          ")
    print("=" * 40)
    print(f"Total Login Attempts:       {total}")
    print(f"Successful Login Attempts:  {success}")
    print(f"Failed Login Attempts:      {failed}")
    
    # Determine the status representation
    if is_locked:
        status = "LOCKED (Security Lockout)"
    else:
        status = "ACTIVE / open"
        
    print(f"Current Account Status:     {status}")
    print("=" * 40 + "\n")

def main():
    # Tracking variables initialized to 0
    total_attempts = 0
    successful_attempts = 0
    failed_attempts = 0
    consecutive_failed_attempts = 0  # Tracks consecutive fails to handle lockout
    
    account_locked = False

    print("=== Welcome to the Login Attempt Tracker ===")
    print("Instructions: Enter credentials. Enter 'exit' as username to quit.\n")

    # The loop runs as long as the account is not locked
    while not account_locked:
        # Prompt user for their username
        username_input = input("Enter username: ").strip()
        
        # Check if the user wants to exit early
        if username_input.lower() == "exit":
            print("Exiting the application...")
            break
            
        # Prompt user for their password
        password_input = input("Enter password: ")

        # Increment total attempts
        total_attempts += 1

        # Check if the credentials match the predefined username and password
        if username_input == CORRECT_USERNAME and password_input == CORRECT_PASSWORD:
            print("Access Granted! Login Successful.\n")
            successful_attempts += 1
            consecutive_failed_attempts = 0  # Reset consecutive failures upon successful login
            
            # Log the successful attempt
            log_attempt(username_input, "SUCCESS")
        else:
            print("Access Denied! Incorrect username or password.\n")
            failed_attempts += 1
            consecutive_failed_attempts += 1
            
            # Log the failed attempt
            log_attempt(username_input, "FAILED")

            # Lock account after 3 consecutive failed attempts
            if consecutive_failed_attempts >= 3:
                account_locked = True
                print("Account locked due to too many failed attempts.")
                break

    # Once the loop terminates, display the summary report
    display_report(total_attempts, successful_attempts, failed_attempts, account_locked)

# Run the program
if __name__ == "__main__":
    main()
