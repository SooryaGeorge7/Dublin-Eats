from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserUpdateForm(forms.ModelForm):
    """
    Form to Edit User
    """
    email = forms.EmailField

    class Meta:
        """
        Define model, fields
        """
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    """
    Form to Edit/Delete Profile
     and account
    """
    class Meta:
        """
        Define model, form fields, help texts and widgets
        """
        model = Profile
        fields = [
            "firstname",
            "surname",
            "about",
            "profile_image",
            "fav_food",
        ]
        widgets = {
            'firstname': forms.TextInput(
                attrs={'placeholder': 'Please type in your Firstname here'}
            ),
            'surname': forms.TextInput(
                attrs={'placeholder': 'Please type in your Surname here'}
            ),
            'about': forms.Textarea(
                attrs={'placeholder': 'Tell us more about you!'}
            ),
            'fav_food': forms.Textarea(
                attrs={'placeholder': 'What is your favourite cuizine?'}
            ),
            'profile_image': forms.FileInput(
                attrs={'class': 'profile-image-input', }
            ),
        }
        help_texts = {
            'about': 'Maximum 250 characters',
            'fav_food': 'Maximum 100 charectors',
        }
