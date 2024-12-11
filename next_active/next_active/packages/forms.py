from django import forms

from next_active.packages.models import Package


class PackageBaseForm(forms.ModelForm):
    class Meta:
        model = Package
        exclude = ['user']


class PackageAddForm(PackageBaseForm):
    pass


class PackageEditForm(PackageBaseForm):
    pass
