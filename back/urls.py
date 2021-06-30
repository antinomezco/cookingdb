# class
from django.urls import path
from .views import RecipesFilterView, CourseView, CuisineView, FoodCategoryView
# function
from django.conf.urls import url
from back import views

urlpatterns = [
    path('filterrecipes/', RecipesFilterView.as_view(),
         name='filter_recipes_view'),
    url('edit/recipe/(?P<slug>.+)/', views.edit_recipe_view),
    url('recipe/(?P<slug>.+)', views.recipe_view),
    url('add_recipe/', views.add_recipe_view),
    path('allcourses/', CourseView.as_view(), name='all_courses_models_view'),
    path('allfoodcategories/', FoodCategoryView.as_view(), name='all_food_categories_models_view'),
    path('allcuisines/', CuisineView.as_view(), name='all_cuisines_view'),
]
