from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "profile_photo",
            "first_name",
            "last_name",
            "city",
            "birth_date",
            "bio",
        ]