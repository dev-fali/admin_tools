import os
import platform
import subprocess
from admin_check import is_user_admin  

def is_user_exist(username):
  system = platform.system()
  try:
    if system == "Linux" or system == "Darwin":
      result = subprocess.run(["grep", username, "/etc/passwd"], capture_output=True, check=True)
      return len(result.stdout) > 0
    elif system == "Windows":
      result = subprocess.run(["net", "user", username], capture_output=True, check=True)
      return "user account does not exist" not in result.stdout.decode()
    else:
      print(f"Unsupported operating system: {system}")
      return False
  except subprocess.CalledProcessError:
    print(f"Error checking user {username}")
    return False

if not is_user_exist(username):
  print(f"User {username} does not exist.")
  return


def add_user(username):
    system = platform.system()
    try:
        if system == "Linux" or system == "Darwin":  # Darwin : macOS
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

def change_password(username):
    system = platform.system()
    try:
        if system == "Linux" or system == "Darwin":
            subprocess.run(["sudo", "passwd", username], check=True)
            print(f"Password for user {username} changed successfully.")
        elif system == "Windows":
            new_password = input("Enter the new password: ")
            subprocess.run(["net", "user", username, new_password], check=True)
            print(f"Password for user {username} changed successfully.")
        else:
            print(f"Unsupported operating system: {system}")
    except subprocess.CalledProcessError as e:
        print(f"Error changing password for user {username}: {e}")

def is_group_exist(group):
  system = platform.system()
  try:
    if system == "Linux" or system == "Darwin":
      # Use grep to search for group in /etc/group
      result = subprocess.run(["grep", group, "/etc/group"], capture_output=True, check=True)
      return len(result.stdout) > 0
    elif system == "Windows":
      # Use net localgroup to query group information
      result = subprocess.run(["net", "localgroup", group], capture_output=True, check=True)
      return "The group name is not found" not in result.stdout.decode()
    else:
      print(f"Unsupported operating system: {system}")
      return False
  except subprocess.CalledProcessError:
    print(f"Error checking group {group}")
    return False

if not is_group_exist(group):
  print(f"Group {group} does not exist.")
  return


def change_user_group(username, group):
    system = platform.system()
    try:
        if system == "Linux" or system == "Darwin":
            subprocess.run(["sudo", "usermod", "-aG", group, username], check=True)
            print(f"User {username} added to group {group} successfully.")
        elif system == "Windows":
            subprocess.run(["net", "localgroup", group, username, "/add"], check=True)
            print(f"User {username} added to group {group} successfully.")
        else:
            print(f"Unsupported operating system: {system}")
    except subprocess.CalledProcessError as e:
        print(f"Error changing group for user {username}: {e}")

def main():
    if not is_user_admin():
        print("This script must be run with administrative privileges.")
        return

    while True:
        print("User Management Script")
        print("1. Add User")
        print("2. Delete User")
        print("3. List Users")
        print("4. Change User Password")
        print("5. Change User Group")
        print("6. Exit")
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
            username = input("Enter the username to change password: ")
            change_password(username)
        elif choice == '5':
            username = input("Enter the username to change group: ")
            group = input("Enter the group to add the user to: ")
            change_user_group(username, group)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
