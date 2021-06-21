from django.db import models

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

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=50,blank=False, default='')
    image = models.CharField(max_length=500,blank=False, default='')
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