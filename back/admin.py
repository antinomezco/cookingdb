from django.contrib import admin  
from .models import Course, Food_category, Cuisine, Recipe, User

# register models to use in admin site
admin.site.register(User)
admin.site.register(Course)
admin.site.register(Food_category)
admin.site.register(Cuisine)
admin.site.register(Recipe)
