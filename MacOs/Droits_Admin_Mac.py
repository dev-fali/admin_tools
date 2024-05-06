import subprocess

def is_admin():
    try:
        result = subprocess.run(['osascript', '-e', 'do shell script "id -Gn | grep -q admin"'], capture_output=True)
        return result.returncode == 0
    except:
        return False

if is_admin():
    print("L'utilisateur a les droits d'administration sur macOS.")
else:
    print("L'utilisateur n'a pas les droits d'administration sur macOS.")
