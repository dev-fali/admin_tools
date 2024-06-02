import os
import platform
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def is_user_admin():
    if platform.system() == "Windows":
        return is_admin()
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        return os.geteuid() == 0
    else:
        return False
