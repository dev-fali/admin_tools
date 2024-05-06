import subprocess

def is_admin():
    try:
        result = subprocess.run(['groups'], capture_output=True, text=True)
        groups = result.stdout.strip().split()
        return 'sudo' in groups
    except:
        return False

if is_admin():
    print("L'utilisateur a les droits d'administration sur Linux.")
else:
    print("L'utilisateur n'a pas les droits d'administration sur Linux.")
