from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase


class TestUserProfileView(APITestCase):

    def setUp(self) -> None:

        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.profile_list_url = reverse('userprofile-list')
        self.profile_list_url_detail = reverse('userprofile-detail', args=[1])

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

        self.data = {
            "user": 1,
            "designation": "Manager",
            "department": "design",
            "date_of_birth": "1994-12-12",
            "joining_date": "2000-12-12",
            "experience": 23,
            "shift": "Morning",
            "about": "im a good manager"
        }

        self.wrong_data = {
            "user": 1,
            "designation": "Manager",
            "department": "design",
            "date_of_birth": "2000-12-12",
            "joining_date": "1994-12-12",
            "experience": 34,
            "shift": "Morning",
            "about": "im a good manager"
        }

        self.profile_patch_data = {
            "department": "Design",
            "shift": "Evening",
            "about": "Im a Great manager"
        }

        self.client.post(
            self.register_url, self.register_user_data, format="json")

        response = self.client.post(self.login_url, self.login_user_data)
        self.token_key = response.data['token']

        return super().setUp()

    def test_user_can_create_profile(self) -> None:

        res = self.client.post(self.profile_list_url, self.data, **
                               {"HTTP_AUTHORIZATION": "Token {}".format(self.token_key)})

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_user_cant_create_profile_wo_token(self) -> None:

        res = self.client.post(self.profile_list_url, self.data)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_cant_create_profile_wo_post_data(self) -> None:

        res = self.client.post(
            self.profile_list_url, **{"HTTP_AUTHORIZATION": "Token {}".format(self.token_key)})

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_check_users_only_auth_can_see_profile_list(self) -> None:

        self.client.post(self.profile_list_url, self.data, **
                         {"HTTP_AUTHORIZATION": "Token {}".format(self.token_key)})

        res = self.client.get(self.profile_list_url,
                              **{"HTTP_AUTHORIZATION": "Token {}".format(self.token_key)})

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_check_users_cant_see_profile_list_wo_token(self) -> None:

        self.client.post(self.profile_list_url, self.data)

        res = self.client.get(self.profile_list_url)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_check_users_can_get_detail(self) -> None:

        self.client.post(self.profile_list_url, self.data, **
                         {"HTTP_AUTHORIZATION": "Token {}".format(self.token_key)})

        res = self.client.get(self.profile_list_url_detail, **
                              {"HTTP_AUTHORIZATION": "Token {}".format(self.token_key)})

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['designation'], "Manager")

    def test_check_users_can_update_detail(self) -> None:

        self.client.post(self.profile_list_url, self.data, **
                         {"HTTP_AUTHORIZATION": "Token {}".format(self.token_key)})

        res = self.client.patch(self.profile_list_url_detail, self.profile_patch_data, **
                                {"HTTP_AUTHORIZATION": "Token {}".format(self.token_key)})

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['department'], "Design")
        self.assertEqual(res.data['shift'], "Evening")
        self.assertEqual(res.data['about'], "Im a Great manager")

    def test_check_auth_users_can_delete(self) -> None:

        self.client.post(self.profile_list_url, self.data, **
                         {"HTTP_AUTHORIZATION": "Token {}".format(self.token_key)})

        res = self.client.delete(self.profile_list_url_detail, **
                                 {"HTTP_AUTHORIZATION": "Token {}".format(self.token_key)})

        get_res = self.client.get(self.profile_list_url_detail, **
                                  {"HTTP_AUTHORIZATION": "Token {}".format(self.token_key)})

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertIsNone(res.data)
        self.assertEqual(get_res.status_code, status.HTTP_404_NOT_FOUND)

    # def test_create_user_dob_lt_jd(self) -> None:

    #     res = self.client.post(self.profile_list_url, self.wrong_data, **
    #                      {"HTTP_AUTHORIZATION": "Token {}".format(self.token_key)})

    #     import pdb
    #     pdb.set_trace()
