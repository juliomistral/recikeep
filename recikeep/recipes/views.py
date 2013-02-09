from rest_framework import serializers, generics

from recikeep.recipes.models import Recipe, Ingredient


class RecipeDisplaySerializer(serializers.ModelSerializer):
    tags = serializers.CharField(source="tag_list", required=False)
    ingredients = serializers.ManyPrimaryKeyRelatedField()

    class Meta:
        model = Recipe
        fields = ('id', 'user', 'name', 'tags', 'ingredients')


class IngredientDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ("id", "raw_text")


class RecipeList(generics.ListAPIView):
    model = Recipe
    serializer_class = RecipeDisplaySerializer
