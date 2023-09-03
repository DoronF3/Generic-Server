import requests
import json
import unittest


class TestAppEndpoints(unittest.TestCase):

    base_url = "http://10.0.0.15:5000"
    cookie = ""

    def test_homepage(self):
        url = f"{self.base_url}/"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "You have reached the server.")

    def test_login(self):
        url = f"{self.base_url}/login"
        payload = json.dumps({
            "username": "user1",
            "password": "user1"
        })
        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.post(url, headers=headers, data=payload)
        print(response.content)
        self.assertEqual(response.status_code, 200)


    def test_admin_dashboard_failure(self):
        # Login as a non-admin user
        login_url = f"{self.base_url}/login"
        payload = json.dumps({
            "username": "user",
            "password": "user"
        })
        headers = {
            'Content-Type': 'application/json',
        }
        login_response = requests.post(login_url, headers=headers, data=payload)
        self.assertEqual(login_response.status_code, 200)

        # Attempt to access the admin dashboard
        url = f"{self.base_url}/admin_dashboard"
        response = requests.get(url)
        self.assertEqual(response.status_code, 401)

    def test_admin_dashboard_success(self):
        # Login as an admin user
        login_url = f"{self.base_url}/login"
        payload = json.dumps({
            "username": "admin",
            "password": "admin"
        })
        headers = {
            'Content-Type': 'application/json',
        }
        login_response = requests.post(login_url, headers=headers, data=payload)
        self.assertEqual(login_response.status_code, 200)

        # Access the admin dashboard
        url = f"{self.base_url}/admin_dashboard"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Admin Dashboard")

    def test_login(self):
        url = f"{self.base_url}/login"
        payload = json.dumps({
            "username": "admin",
            "password": "admin"
        })
        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.post(url, headers=headers, data=payload)
        self.assertEqual(response.status_code, 200)

    def test_admin_route(self):
        url = f"{self.base_url}/admin"
        response = requests.get(url)
        self.assertEqual(response.status_code, 401)

        # Login as an admin user before accessing the admin route
        login_url = f"{self.base_url}/login"
        payload = json.dumps({
            "username": "admin",
            "password": "admin"
        })
        headers = {
            'Content-Type': 'application/json',
        }
        login_response = requests.post(login_url, headers=headers, data=payload)
        self.assertEqual(login_response.status_code, 200)

        # Access the admin route after login as an admin user
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        # Login before logging out
        login_url = f"{self.base_url}/login"
        payload = json.dumps({
            "username": "admin",
            "password": "admin"
        })
        headers = {
            'Content-Type': 'application/json',
        }
        login_response = requests.post(login_url, headers=headers, data=payload)
        self.assertEqual(login_response.status_code, 200)

        # Logout
        logout_url = f"{self.base_url}/logout"
        logout_response = requests.get(logout_url)
        self.assertEqual(logout_response.status_code, 200)

if __name__ == '__main__':
    unittest.main()

