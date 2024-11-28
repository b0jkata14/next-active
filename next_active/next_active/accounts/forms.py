from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from next_active.accounts.models import UserProfile


UserModel = get_user_model()


class CustomerRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ['first_name', 'last_name', 'email', 'username']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'full_name', 'bio', 'phone_number']
