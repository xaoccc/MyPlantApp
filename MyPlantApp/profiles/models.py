from django.core.validators import MinLengthValidator
from django.db import models
from MyPlantApp.profiles.validators import capital_letter_validator


class Profile(models.Model):
    username = models.CharField(max_length=10, validators=(MinLengthValidator(2),))
    first_name = models.CharField(max_length=20, validators=(capital_letter_validator,), verbose_name="First Name")
    last_name = models.CharField(max_length=20, validators=(capital_letter_validator,), verbose_name="Last Name")
    profile_picture = models.URLField(blank=True, null=True)
