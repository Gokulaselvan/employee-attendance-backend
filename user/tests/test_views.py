from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TestUserRegister(APITestCase):

    def setUp(self) -> None:

        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.change_password_url = reverse('change-password', args=[1])

        self.register_user_data = {
            "username": "test",
            "email": "test@gmail.com",
            "employee_id": "DT1001",
            "password": "wsxwsxwsx",
            "retype_password": "wsxwsxwsx",
        }

        self.login_user_data = {
            "username": "test@gmail.com",
            "password": "wsxwsxwsx",
        }

        self.re_login_user_data = {
            "username": "test@gmail.com",
            "password": "wsxwsx@123",
        }

        self.change_pass_data = {
            "old_password": "wsxwsxwsx",
            "password": "wsxwsx@123",
            "retype_password": "wsxwsx@123",
        }

        return super().setUp()

    def test_user_can_register(self) -> None:
        """User can register with post data"""

        response = self.client.post(
            self.register_url, self.register_user_data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {
            'response': "successfully registered a new user",
            "email": "test@gmail.com",
            "username": "test",
            "employee_id": "DT1001"
        })

    def test_user_cant_register_wo_postdata(self) -> None:
        """User cannot register without post data"""

        response = self.client.post(
            self.register_url, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_can_login(self) -> None:
        """user can login with post data"""

        self.client.post(
            self.register_url, self.register_user_data, format="json")
        response = self.client.post(self.login_url, self.login_user_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_login_wo_data(self) -> None:
        """user cannot login without post data"""

        self.client.post(
            self.register_url, self.register_user_data, format="json")
        response = self.client.post(self.login_url)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_can_change_password(self) -> None:
        """Test change password with token"""

        self.client.post(
            self.register_url, self.register_user_data, format="json")

        login_res = self.client.post(
            self.login_url, self.login_user_data, format="json")

        token = login_res.data['token']

        self.client.put(
            self.change_password_url, self.change_pass_data, format="json", **{"HTTP_AUTHORIZATION": "Token {}".format(token)})

        new_login_res = self.client.post(
            self.login_url, self.re_login_user_data, format="json")

        self.assertEqual(new_login_res.status_code, status.HTTP_200_OK)

    def test_user_cant_change_pass_wo_auth(self) -> None:
        """Test change password without token"""

        res = self.client.put(
            self.change_password_url, self.change_pass_data, format="json")

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)