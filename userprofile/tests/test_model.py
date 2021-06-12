from django.test import TestCase

from model_bakery import baker

from ..models import UserProfile


class TestUserProfileModel(TestCase):

    def setUp(self) -> None:

        self.userprofile = baker.make(UserProfile)
        print(vars(self.userprofile))
        return super().setUp()

    def test_create_usercount(self) -> None:

        user_count = UserProfile.objects.all().count()

        self.assertEqual(user_count, 1)
