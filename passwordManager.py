import hashlib

password_manager = {}  # Stores the key-value pairs of usernames and passwords

def create_account():
    print("Creating an account...")
    username = input("Enter your desired username: ")
    print(f"Username entered: {username}")
    password = input("Enter your desired password: ")  # Using input() instead of getpass() for testing
    print(f"Password entered: {password}")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()  # Hash the password
    password_manager[username] = hashed_password
    print("Account created successfully!")

def login():
    print("Logging in...")
    username = input("Enter your username: ")
    print(f"Username entered: {username}")
    password = input("Enter your password: ")  # Using input() instead of getpass() for testing
    print(f"Password entered: {password}")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()  # Call hexdigest()
    print(f"Hashed password: {hashed_password}")
    if username in password_manager.keys() and password_manager[username] == hashed_password:
        print("Login Successful!")
    else:
        print("Invalid username or password.")

def main():
    while True:
        try:
            choice = int(input("Enter 1 to create an account, 2 to login, or 0 to exit: "))  # Convert input to int
            print(f"Choice entered: {choice}")
            if choice == 1:
                create_account()
            elif choice == 2:
                login()
            elif choice == 0:
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 0.")
        except ValueError as e:
            print(f"Invalid input. Please enter a number. Error: {e}")

if __name__ == "__main__":
    main()

#Note: The code doesn't run with powershell. Use CMD or BAsh to run the script
