from rest_framework import serializers
from .models import Course, Food_category, Cuisine, Recipe


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'


class FoodCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Food_category
        fields = '__all__'


class CuisineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cuisine
        fields = '__all__'


class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = ['course', 'food_category', 'cuisine', 'recipe_name', 'slug',
                  'image', 'approval', 'ingredients_text', 'created_at']
        depth = 1


class RelatedFieldAlternative(serializers.PrimaryKeyRelatedField):
    def __init__(self, **kwargs):
        self.serializer = kwargs.pop('serializer', None)
        if self.serializer is not None and not issubclass(
                self.serializer, serializers.Serializer):
            raise TypeError('"serializer" is not a valid serializer class')

        super().__init__(**kwargs)

    def use_pk_only_optimization(self):
        return False if self.serializer else True

    def to_representation(self, instance):
        if self.serializer:
            return self.serializer(instance, context=self.context).data
        return super().to_representation(instance)


class OneRecipeSerializer(serializers.ModelSerializer):
    cuisine = RelatedFieldAlternative(
        queryset=Cuisine.objects.all(), serializer=CuisineSerializer)
    course = RelatedFieldAlternative(
        queryset=Course.objects.all(), serializer=CourseSerializer)
    food_category = RelatedFieldAlternative(
        queryset=Food_category.objects.all(), serializer=FoodCategorySerializer)

    class Meta:
        model = Recipe
        fields = '__all__'
        depth = 1
