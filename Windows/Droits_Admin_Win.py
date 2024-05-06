import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    print("L'utilisateur a les droits d'administration sur Windows.")
else:
    print("L'utilisateur n'a pas les droits d'administration sur Windows.")
