from django.conf.urls import patterns
from recikeep.recipes.views import RecipeList

urlpatterns = patterns('',
    (r'^$', RecipeList.as_view()),
)