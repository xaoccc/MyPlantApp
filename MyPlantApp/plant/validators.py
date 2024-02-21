from django.core.exceptions import ValidationError


def letter_validator(value):
    if not value.isalpha():
        raise ValidationError("Plant name should contain only letters!")