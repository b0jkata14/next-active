from django import forms

from next_active.applications.models import TrainerApplication


class TrainerApplicationBaseForm(forms.ModelForm):
    class Meta:
        model = TrainerApplication
        fields = ['sport', 'certifications']


class TrainerApplicationRegisterForm(TrainerApplicationBaseForm):
    pass


class TrainerApplicationEditForm(TrainerApplicationBaseForm):
    class Meta:
        model = TrainerApplication
        fields = ['sport', 'certifications', 'message']
