from django.test import TestCase
from accounts.models import CustomUser


class CustomUserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        CustomUser.objects.create(birth_date='1992-05-15', email='helloworld@hello.world', username='axel')

    def test_username_max_length(self):
        user = CustomUser.objects.get(id=1)
        max_length = user._meta.get_field('username').max_length
        self.assertEquals(max_length, 50)

    def test_birthdate_can_be_blank(self):
        user = CustomUser.objects.get(id=1)
        blank = user._meta.get_field('birth_date').blank
        self.assertTrue(blank)

    def test_email_is_unique(self):
        user = CustomUser.objects.get(id=1)
        email_is_unique = user._meta.get_field('email').unique
        self.assertTrue(email_is_unique)
