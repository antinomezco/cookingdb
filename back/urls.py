#class
from django.urls import path, re_path
from .views import RecipesFilterView, CourseView, CuisineView, FoodCategoryView#, OneRecipeView
#, IngredientsView 
#function
from django.conf.urls import url
from back import views 

urlpatterns = [
    path('filterrecipes/', RecipesFilterView.as_view(), name='filter_recipes_view'),
    # re_path('^recipe/(?P<slug>.+)', OneRecipeView.as_view(), name='filter_one_recipe_view'),
    url('edit/recipe/(?P<slug>.+)/', views.edit_recipe_view),
    url('recipe/(?P<slug>.+)', views.recipe_view),
    path('allcourses/', CourseView.as_view(), name='all_courses_models_view'),
    path('allfoodcategories/', FoodCategoryView.as_view(), name='all_food_categories_models_view'),
    path('allcuisines/', CuisineView.as_view(), name='all_cuisines_view'),
    # url('allcuisines/', views.cuisine_list),
    url('add_recipe/', views.add_recipe_view),
    url('user_add/', views.add_user_view),
    url('edit/user/(?P<sub>.+)/', views.edit_user_view),
    # url('edit_recipe/(?P<slug>.+)', views.edit_recipe_view),
    # path('allingredients/', IngredientsView.as_view(), name='all_ingredients_models_view'),
]