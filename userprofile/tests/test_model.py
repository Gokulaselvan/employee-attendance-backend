from django.test import TestCase

from model_bakery import baker

from ..models import UserProfile


class TestUserProfileModel(TestCase):

    def setUp(self) -> None:

        self.userprofile = baker.make(UserProfile)
        self.userprofile1 = baker.make(UserProfile, experience=2)
        return super().setUp()

    def test_create_usercount(self) -> None:
        """Checks the User count as per baker"""

        user_count = UserProfile.objects.all().count()

        self.assertEqual(user_count, 2)

    def test_check_experience_is_postitve_num(self) -> None:
        """Checks the User experience is positive integer only"""

        user_exp = UserProfile.objects.get(id=self.userprofile.id)
        user_exp1 = UserProfile.objects.get(id=self.userprofile1.id)

        self.assertTrue(user_exp.experience == 0)
        self.assertTrue(user_exp1.experience > 0)
