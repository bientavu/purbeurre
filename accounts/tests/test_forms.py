from django.test import TestCase
from accounts.forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserCreationFormTest(TestCase):
    def test_fields_form_length(self):
        form = CustomUserCreationForm()
        self.assertEqual(len(form.fields), 6)


class CustomUserChangeFormTest(TestCase):
    def test_fields_form_length(self):
        form = CustomUserChangeForm()
        self.assertEqual(len(form.fields), 5)
