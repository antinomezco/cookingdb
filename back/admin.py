from django.contrib import admin
# from admin_auto_filters.filters import AutocompleteFilter   
from .models import Course, Food_category, Cuisine, Recipe, User#, Ingredients, Recipe_steps#, Measurements, Quantity, 

# register models to use in admin site
admin.site.register(User)
admin.site.register(Course)
admin.site.register(Food_category)
admin.site.register(Cuisine)
# admin.site.register(Ingredients)
# admin.site.register(Measurements)
admin.site.register(Recipe)
# admin.site.register(Quantity)
# admin.site.register(Recipe_steps)
