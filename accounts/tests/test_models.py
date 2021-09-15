from django.test import TestCase
from accounts.models import CustomUser


class CustomUserModelTest(TestCase):
    """
    Multiple test for the accounts models
    """
    @classmethod
    def setUpTestData(cls):
        """User creation setup"""
        CustomUser.objects.create(
            birth_date='1992-05-15',
            email='helloworld@hello.world',
            username='axel'
        )

    def test_username_max_length(self):
        """Test the max length of the username"""
        user = CustomUser.objects.get(id=1)
        max_length = user._meta.get_field('username').max_length
        self.assertEqual(max_length, 50)

    def test_birthdate_can_be_blank(self):
        """Test that birth_date can be blank"""
        user = CustomUser.objects.get(id=1)
        blank = user._meta.get_field('birth_date').blank
        self.assertTrue(blank)

    def test_email_is_unique(self):
        """Test if email is unique"""
        user = CustomUser.objects.get(id=1)
        email_is_unique = user._meta.get_field('email').unique
        self.assertTrue(email_is_unique)
