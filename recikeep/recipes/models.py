from django.db import models

from django.contrib.auth.models import User
from django_extensions.db.models import ActivatorModel, TimeStampedModel
from django_extensions.db.fields import UUIDField


class Recipe(ActivatorModel, TimeStampedModel):
    id = UUIDField(primary_key=True)
    name = models.CharField(max_length=250, null=True, blank=False)
    user = models.ForeignKey(User, related_name='recipes')
    original_location = models.URLField(null=True)


class Ingredient(TimeStampedModel):
    MEASUREMENT_TYPE_CHOICES = (
        ('BY_VOLUME', 'By volume (i.e., tablespoons, cups)'),
        ('BY_WEIGHT', 'By weight (i.e., ounces, pounds)'),
        ('BY_COUNT', 'By count (1 each, 1 dozen)'),
    )

    WEIGHT_MEASUREMENT_CHOICES = (
        ('ONCE', 'Ounce'),
        ('POUND', 'Pound'),
    )

    VOLUME_MEASUREMENT_CHOICES = (
        ('CUP', 'Cup'),
        ('TABLE_SPOON', 'Tbsp.'),
        ('TEA_SPOON', 'Tsp.'),
    )

    MEASUREMENT_CHOICES = (
        WEIGHT_MEASUREMENT_CHOICES + VOLUME_MEASUREMENT_CHOICES
    )

    id = UUIDField(primary_key=True)
    raw_text = models.TextField()
    recipe = models.ForeignKey(Recipe, related_name='ingredients')
    units = models.DecimalField(max_digits=4, decimal_places=1)
    unit_of_measurement = models.TextField(choices=MEASUREMENT_CHOICES)
    measurement_type = models.TextField(choices=MEASUREMENT_TYPE_CHOICES)


class Step(TimeStampedModel):
    id = UUIDField(primary_key=True)
    instruction = models.TextField()
    sequence = models.PositiveIntegerField(blank=False)
