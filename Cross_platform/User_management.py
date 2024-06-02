import os
import platform
import subprocess

def add_user(username):
    system = platform.system()
    try:
        if system == "Linux" or system == "Darwin":  # Darwin is for macOS
            subprocess.run(["sudo", "useradd", username], check=True)
            print(f"User {username} added successfully.")
        elif system == "Windows":
            subprocess.run(["net", "user", username, "/add"], check=True)
            print(f"User {username} added successfully.")
        else:
            print(f"Unsupported operating system: {system}")
    except subprocess.CalledProcessError as e:
        print(f"Error adding user {username}: {e}")

def delete_user(username):
    system = platform.system()
    try:
        if system == "Linux" or system == "Darwin":
            subprocess.run(["sudo", "userdel", username], check=True)
            print(f"User {username} deleted successfully.")
        elif system == "Windows":
            subprocess.run(["net", "user", username, "/delete"], check=True)
            print(f"User {username} deleted successfully.")
        else:
            print(f"Unsupported operating system: {system}")
    except subprocess.CalledProcessError as e:
        print(f"Error deleting user {username}: {e}")

def list_users():
    system = platform.system()
    try:
        if system == "Linux" or system == "Darwin":
            subprocess.run(["cut", "-d:", "-f1", "/etc/passwd"])
        elif system == "Windows":
            subprocess.run(["net", "user"])
        else:
            print(f"Unsupported operating system: {system}")
    except subprocess.CalledProcessError as e:
        print(f"Error listing users: {e}")

def main():
    while True:
        print("User Management Script")
        print("1. Add User")
        print("2. Delete User")
        print("3. List Users")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            username = input("Enter the username to add: ")
            add_user(username)
        elif choice == '2':
            username = input("Enter the username to delete: ")
            delete_user(username)
        elif choice == '3':
            list_users()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
