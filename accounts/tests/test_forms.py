from django.test import TestCase
from accounts.forms import CustomUserCreationForm


class CustomUserCreationFormTest(TestCase):
    def test_fields_form_length(self):
        form = CustomUserCreationForm()
        self.assertEqual(len(form.fields), 6)
