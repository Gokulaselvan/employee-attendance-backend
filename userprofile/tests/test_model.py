from django.test import TestCase
from django.core.exceptions import ValidationError

from model_bakery import baker

from ..models import UserProfile


class TestUserProfileModel(TestCase):

    def setUp(self) -> None:

        self.userprofile = baker.make(UserProfile)
        self.userprofile1 = baker.make(UserProfile, experience=2)
        self.userprofile2 = baker.make(
            UserProfile, date_of_birth="2000-12-12", joining_date="1999-12-12")
        return super().setUp()

    def test_create_usercount(self) -> None:
        """Checks the User count as per baker"""

        user_count = UserProfile.objects.all().count()

        self.assertEqual(user_count, 3)

    def test_check_experience_is_postitve_num(self) -> None:
        """Checks the User experience is positive integer only"""

        user_exp = UserProfile.objects.get(id=self.userprofile.id)
        user_exp1 = UserProfile.objects.get(id=self.userprofile1.id)

        self.assertTrue(user_exp.experience == 0)
        self.assertTrue(user_exp1.experience > 0)

    def test_str_repr_model(self) -> None:
        """Checks for the Str method"""

        user_str = UserProfile.objects.get(id=self.userprofile.id)

        self.assertEqual(str(user_str), self.userprofile.user.email)

    def test_create_user_dob_lt_jd(self) -> None:
        """Checks for DOB less than Joining Date"""

        with self.assertRaises(ValidationError):
            self.userprofile2.full_clean()
