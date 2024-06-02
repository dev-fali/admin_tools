import unittest
import platform as pl
from unittest.mock import patch, call
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../User_management')))

from User_management import add_user, delete_user, list_users, change_password, change_user_group

class TestUserManagement(unittest.TestCase):

    @patch('subprocess.run')
    @patch('platform.system', return_value='Linux')
    def test_add_user_linux(self, mock_platform, mock_subprocess):
        add_user('testuser')
        mock_subprocess.assert_called_with(['sudo', 'useradd', 'testuser'], check=True)

    @patch('subprocess.run')
    @patch('platform.system', return_value='Windows')
    def test_add_user_windows(self, mock_platform, mock_subprocess):
        add_user('testuser')
        mock_subprocess.assert_called_with(['net', 'user', 'testuser', '/add'], check=True)

    @patch('subprocess.run')
    @patch('platform.system', return_value='Linux')
    def test_delete_user_linux(self, mock_platform, mock_subprocess):
        delete_user('testuser')
        mock_subprocess.assert_called_with(['sudo', 'userdel', 'testuser'], check=True)

    @patch('subprocess.run')
    @patch('platform.system', return_value='Windows')
    def test_delete_user_windows(self, mock_platform, mock_subprocess):
        delete_user('testuser')
        mock_subprocess.assert_called_with(['net', 'user', 'testuser', '/delete'], check=True)

    @patch('subprocess.run')
    @patch('platform.system', return_value='Linux')
    def test_list_users_linux(self, mock_platform, mock_subprocess):
        list_users()
        mock_subprocess.assert_called_with(['cut', '-d:', '-f1', '/etc/passwd'])

    @patch('subprocess.run')
    @patch('platform.system', return_value='Windows')
    def test_list_users_windows(self, mock_platform, mock_subprocess):
        list_users()
        mock_subprocess.assert_called_with(['net', 'user'])

    @patch('subprocess.run')
    @patch('platform.system', return_value='Linux')
    def test_change_password_linux(self, mock_platform, mock_subprocess):
        change_password('testuser')
        mock_subprocess.assert_called_with(['sudo', 'passwd', 'testuser'], check=True)

    @patch('subprocess.run')
    @patch('platform.system', return_value='Windows')
    def test_change_password_windows(self, mock_platform, mock_subprocess):
        with patch('builtins.input', return_value='newpassword'):
            change_password('testuser')
            mock_subprocess.assert_called_with(['net', 'user', 'testuser', 'newpassword'], check=True)

    @patch('subprocess.run')
    @patch('platform.system', return_value='Linux')
    def test_change_user_group_linux(self, mock_platform, mock_subprocess):
        change_user_group('testuser', 'testgroup')
        mock_subprocess.assert_called_with(['sudo', 'usermod', '-aG', 'testgroup', 'testuser'], check=True)

    @patch('subprocess.run')
    @patch('platform.system', return_value='Windows')
    def test_change_user_group_windows(self, mock_platform, mock_subprocess):
        change_user_group('testuser', 'testgroup')
        mock_subprocess.assert_called_with(['net', 'localgroup', 'testgroup', 'testuser', '/add'], check=True)

if __name__ == '__main__':
    unittest.main()
