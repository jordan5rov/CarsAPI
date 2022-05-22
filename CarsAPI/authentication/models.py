from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth import models as auth_models

from CarsAPI.authentication.manager import CarsUserManager


class CarsUser(auth_models.AbstractUser, auth_models.PermissionsMixin):
    username = None
    first_name = None
    last_name = None
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )
    is_staff = models.BooleanField(
        default=False,
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CarsUserManager()


class Profile(models.Model):
    PROFILE_FIRST_NAME_MAX_LEN = 30
    PROFILE_LAST_NAME_MAX_LEN = 30
    PROFILE_FIRST_NAME_MIN_LEN = 3
    PROFILE_LAST_NAME_MIN_LEN = 5

    PROFILE_GENDER_MALE = 'Male'
    PROFILE_GENDER_FEMALE = 'Female'
    PROFILE_GENDER_OTHER = 'Other'
    PROFILE_GENDER_CHOICES = [
        (x, x) for x in
        (
            PROFILE_GENDER_MALE,
            PROFILE_GENDER_FEMALE,
            PROFILE_GENDER_OTHER
        )
    ]

    first_name = models.CharField(
        max_length=PROFILE_FIRST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(PROFILE_FIRST_NAME_MIN_LEN),
        ),
    )

    last_name = models.CharField(
        max_length=PROFILE_LAST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(PROFILE_LAST_NAME_MIN_LEN),
        ),
    )

    gender = models.CharField(
        max_length=max(
            len(x) for x in (
                PROFILE_GENDER_MALE,
                PROFILE_GENDER_FEMALE,
                PROFILE_GENDER_OTHER
            )
        ),
        choices=PROFILE_GENDER_CHOICES,
    )

    user = models.OneToOneField(
        CarsUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )
