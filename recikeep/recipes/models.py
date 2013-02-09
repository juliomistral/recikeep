from django.db import models

from recikeep.usermanagement.models import User
from django_extensions.db.models import ActivatorModel, TimeStampedModel
from django_extensions.db.fields import UUIDField


class Tag(TimeStampedModel):
    class Meta:
        unique_together = (
            ('name', 'user'),
        )

    id = UUIDField(primary_key=True)
    name = models.CharField(max_length=250, blank=False)
    user = models.ForeignKey(User, related_name='tags')


class Recipe(ActivatorModel, TimeStampedModel):
    id = UUIDField(primary_key=True)
    name = models.CharField(max_length=250, blank=False)
    user = models.ForeignKey(User, related_name='recipes')
    original_location = models.URLField(null=True)
    tags = models.ManyToManyField(Tag, db_table="recipes_recipe_to_tag")


class IngredientManager(models.Manager):
    def create_from_list_for_recipe(self, raw_ingredients, recipe):
        ingredients = []
        for raw_ingredient in raw_ingredients:
            ingredient = self.create(raw_text=raw_ingredient, recipe=recipe)
            ingredients.append(ingredient)
        return ingredients


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

    objects = IngredientManager()


class Step(TimeStampedModel):
    id = UUIDField(primary_key=True)
    instruction = models.TextField()
    sequence = models.PositiveIntegerField(blank=False)
