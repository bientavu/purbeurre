
# Create your views here.

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    """View that shows the custom user creation form"""
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
