from .models import Course, Food_category, Recipe, Cuisine
from .serializers import RecipeSerializer, OneRecipeSerializer, CourseSerializer, CuisineSerializer, FoodCategorySerializer, OneRecipeSerializer
from rest_framework.generics import ListAPIView
from .pagination import StandardResultsSetPagination
# function
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.contrib.postgres.search import SearchVector

# Create your views here.


class RecipesFilterView(ListAPIView):
    """
    Return a list of all the existing recipes plus its course, food_category 
    and cuisine Foreign Keys.
    """
    serializer_class = RecipeSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        recipe_name = self.request.query_params.get('recipe_name', "")
        return Recipe.objects.annotate(search=SearchVector(
            'recipe_name', 'ingredients_text', 'course__course_name'
        )).filter(search__icontains=recipe_name).order_by('-created_at')


@api_view(['GET'])
def recipe_view(request, slug):
    """
    Return single recipe plus its course, food_category and cuisine Foreign Keys.
    """
    try:
        recipe = Recipe.objects.get(slug=slug)
    except Recipe.DoesNotExist:
        return JsonResponse({'message': 'The recipe does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        one_recipe_serializer = OneRecipeSerializer(recipe)
        return JsonResponse(one_recipe_serializer.data)


@api_view(['POST'])
def add_recipe_view(request):
    """
    Post a single recipe plus its course, food_category and cuisine Foreign Keys.
    """
    if request.method == 'POST':
        one_recipe_data = JSONParser().parse(request)
        one_recipe_serializer = OneRecipeSerializer(data=one_recipe_data)
        if one_recipe_serializer.is_valid():
            one_recipe_serializer.save()
            return JsonResponse(one_recipe_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(one_recipe_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def edit_recipe_view(request, slug):
    """
    GET:
    Return a single recipe.

    PUT:
    Edit a single recipe.

    DELETE: 
    Delete a single recipe.
    """
    try:
        recipe = Recipe.objects.get(slug=slug)
    except Recipe.DoesNotExist:
        return JsonResponse({'message': 'The recipe does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        one_recipe_serializer = OneRecipeSerializer(recipe)
        return JsonResponse(one_recipe_serializer.data)

    elif request.method == 'PUT':
        one_recipe_data = JSONParser().parse(request)
        one_recipe_serializer = OneRecipeSerializer(
            recipe, data=one_recipe_data)
        if one_recipe_serializer.is_valid():
            one_recipe_serializer.save()
            return JsonResponse(one_recipe_serializer.data)
        return JsonResponse(one_recipe_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        recipe.delete()
        return JsonResponse({'message': 'Recipe was deleted successfully!'},
                            status=status.HTTP_204_NO_CONTENT)

class CourseView(ListAPIView):
    """
    GET:
    Return all courses.
    """
    serializer_class = CourseSerializer

    def get_queryset(self):
        return Course.objects.order_by('course_name').all()


class CuisineView(ListAPIView):
    """
    GET:
    Return all cuisines.
    """
    serializer_class = CuisineSerializer

    def get_queryset(self):
        return Cuisine.objects.order_by('cuisine_name').all()


class FoodCategoryView(ListAPIView):
    """
    GET:
    Return all food categories.
    """
    serializer_class = FoodCategorySerializer

    def get_queryset(self):
        return Food_category.objects.order_by('food_category_name').all()
