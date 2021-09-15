from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """Custom user creation form"""
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'birth_date')

    def __init__(self, *args, **kwargs):
        """Display the labels in French instead of English"""
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = 'Prénom'
        self.fields['last_name'].label = 'Nom'
        self.fields['birth_date'].label = 'Date de naissance (AAAA-MM-JJ)'
        self.fields['password1'].label = 'Mot de passe'
        self.fields['password2'].label = 'Confirmation mot de passe'
