from cloudinary.models import CloudinaryField
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from next_active.accounts.models import UserProfile, TrainerProfile

UserModel = get_user_model()


class CustomerRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ['first_name', 'last_name', 'email']


class ProfileEditForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)

    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'bio', 'phone_number']

    def __init__(self, *args, **kwargs):
        user = kwargs.get('instance').user
        super().__init__(*args, **kwargs)

        self.fields['first_name'].initial = user.first_name
        self.fields['last_name'].initial = user.last_name

    def save(self, commit=True):
        instance = super().save(commit=False)
        user = instance.user

        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
            instance.save()

        return instance



class TrainerEditForm(forms.ModelForm):
    class Meta:
        model = TrainerProfile
        fields = ['location', 'experience', 'certifications']