from django.core.validators import MinLengthValidator
from django.db import models
from MyPlantApp.plant.validators import letter_validator

class Plant(models.Model):
    PLANT_TYPES = (
        ("Outdoor Plants", "Outdoor Plants"),
        ("Indoor Plants", "Indoor Plants"),
    )
    plant_type = models.CharField(max_length=14, choices=PLANT_TYPES)
    name = models.CharField(max_length=20, validators=(MinLengthValidator(2), letter_validator,))
    image_url = models.URLField()
    description = models.TextField()
    price = models.FloatField()

