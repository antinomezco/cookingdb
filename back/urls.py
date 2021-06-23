# class
from django.urls import path
from .views import RecipesFilterView
# function
from django.conf.urls import url
from back import views

urlpatterns = [
    path('filterrecipes/', RecipesFilterView.as_view(),
         name='filter_recipes_view'),
    url('edit/recipe/(?P<slug>.+)/', views.edit_recipe_view),
    url('recipe/(?P<slug>.+)', views.recipe_view),
    url('add_recipe/', views.add_recipe_view),
    url('user_add/', views.add_user_view),
    url('edit/user/(?P<sub>.+)/', views.edit_user_view),
]
