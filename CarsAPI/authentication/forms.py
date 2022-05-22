from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms

from CarsAPI.authentication.models import Profile

UserModel = get_user_model()


class UserRegistrationForm(auth_forms.UserCreationForm):
    first_name = forms.CharField(
        max_length=Profile.PROFILE_FIRST_NAME_MAX_LEN
    )
    last_name = forms.CharField(
        max_length=Profile.PROFILE_LAST_NAME_MAX_LEN
    )
    gender = forms.ChoiceField(
        choices=Profile.PROFILE_GENDER_CHOICES
    )

    class Meta:
        model = UserModel
        fields = (
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
        )

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            gender=self.cleaned_data['gender'],
            user=user,
        )
        if commit:
            profile.save()

        return user
