from django.db import models
from djfractions.models import DecimalFractionField

class Course(models.Model):
    course_name = models.CharField(max_length=50,blank=False, default='')

    def __str__(self):
        return f"{self.course_name}"

class Food_category(models.Model):
    food_category_name  = models.CharField(max_length=50,blank=False, default='')

    class Meta:
        verbose_name_plural = "Food categories"
    
    def __str__(self):
        return f"{self.food_category_name}"

class Cuisine(models.Model):
    cuisine_name = models.CharField(max_length=50,blank=False, default='')

    def __str__(self):
        return f"{self.cuisine_name}"

class User(models.Model):
    username = models.CharField(max_length=50,blank=True, default='')
    email = models.CharField(max_length=50,blank=False, unique=True, default='')
    sub = models.CharField(max_length=70,blank=False, unique=True, default='')

    def __str__(self):
        return f"{self.username}, {self.email}"

# class Measurements(models.Model):
#     measurement_name = models.CharField(max_length=50,  default='')

#     class Meta:
#         verbose_name_plural = "Measurements"

#     def __str__(self):
#         return f"{self.measurement_name}"

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=50,blank=False, default='')
    image = models.CharField(max_length=150,blank=False, default='')
    prep_time = models.CharField(max_length=40, blank=False, default='')
    cook_time = models.CharField(max_length=40, blank=False, default='')
    servings = models.CharField(max_length=3, blank=False, default='')
    recipe_description = models.CharField(max_length=500,blank=True, default='')
    ingredients_text = models.TextField(blank=False, default='')
    recipe_steps = models.TextField(blank=False, default='')
    recipe_notes = models.TextField(blank=True, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    food_category = models.ForeignKey(Food_category, on_delete=models.CASCADE)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE)
    slug = models.CharField(max_length=150,blank=False, unique=True,default='')
    approval = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.recipe_name}"

    class Meta:
        verbose_name_plural = "Recipes"

# class Quantity(models.Model):
#     ingredient_id = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
#     recipe_id = models.ForeignKey(Recipe, related_name='q_recipe_id', on_delete=models.CASCADE)
#     measurement_id = models.ForeignKey(Measurements, blank=True, null=True, on_delete=models.CASCADE)
#     ingredient_quantity = DecimalFractionField(max_digits=5, decimal_places=2)
#     note = models.CharField(max_length=40, blank=True, default='')
#     note_addendum = models.BooleanField(default=False)

#     def __str__(self):
#         return f"{self.ingredient_quantity} {self.measurement_id} {self.ingredient_id}, {self.note}"

#     class Meta:
#         verbose_name_plural = "Quantities"

# class Recipe_steps(models.Model):
#     recipe_steps = models.TextField(blank=False, default='')
#     recipe_notes = models.TextField(blank=True, default='')
#     recipe_id = models.ForeignKey(Recipe, related_name='rs_recipe_id', on_delete=models.CASCADE)
#     # step_number = models.IntegerField(blank=False, default='')
#     # step_description = models.CharField(max_length=500,blank=False, default='')
#     # step_type = models.BooleanField(default=True)

#     def __str__(self):
#         return f"From: {self.recipe_id}, {self.recipe_steps}"

#     class Meta:
#         verbose_name_plural = "Recipe steps"

# class Ingredients(models.Model):
#     ingredients_text = models.TextField(blank=False, default='')
#     recipe_id = models.ForeignKey(Recipe, related_name='ing_recipe_id', on_delete=models.CASCADE)

#     def __str__(self):
#         return f"From: {self.recipe_id}, {self.ingredients_text}"

#     class Meta:
#         verbose_name_plural = "Ingredients"