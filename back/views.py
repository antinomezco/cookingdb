from .models import Course, Food_category, Recipe, Cuisine, User#, Ingredients, Measurements, Quantity, Recipe_steps
from .serializers import RecipeSerializer, OneRecipeSerializer, CourseSerializer, CuisineSerializer, FoodCategorySerializer, OneRecipeSerializer, UserSerializer#, IngredientsSerializer
from rest_framework.generics import ListAPIView
from .pagination import StandardResultsSetPagination
# function
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

# Create your views here.
class RecipesFilterView(ListAPIView):
    serializer_class = RecipeSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        recipe_name = self.request.query_params.get('recipe_name', "")
        # q_recipe_id = self.request.query_params.get('q_recipe_id', "")#"0")
        # if q_recipe_id:
        #     return Recipe.objects.filter(recipe_name__icontains=recipe_name).filter(q_recipe_id__exact=q_recipe_id)
        # #region = self.request.query_params.get('region', "")
        approval = self.request.query_params.get('approval', "")
        # sortBy = self.request.query_params.get('sortBy', "")
        return Recipe.objects.filter(recipe_name__icontains=recipe_name).filter(approval__exact=True)#.filter(category__icontains=category).order_by(sortBy).reverse()

# class OneRecipeView(ListAPIView):
#     serializer_class = OneRecipeSerializer
#     # pagination_class = StandardResultsSetPagination

#     def get_queryset(self):
#         slug= self.kwargs['slug']
#         # city = self.request.query_params.get('city', "")
#         # #region = self.request.query_params.get('region', "")
#         # category = self.request.query_params.get('category', "")
#         # sortBy = self.request.query_params.get('sortBy', "")
#         return Recipe.objects.filter(slug__exact=slug)#.filter(city__icontains=city).filter(category__icontains=category).order_by(sortBy).reverse()
@api_view(['GET', 'DELETE'])
def recipe_view(request, slug):
    try: 
        recipe = Recipe.objects.get(slug=slug) 
    except Recipe.DoesNotExist: 
        return JsonResponse({'message': 'The recipe does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        one_recipe_serializer = OneRecipeSerializer(recipe) 
        return JsonResponse(one_recipe_serializer.data)
    
    # elif request.method == 'PUT':
    #     one_recipe_data = JSONParser().parse(request)
    #     one_recipe_serializer = OneRecipeSerializer(recipe, data=one_recipe_data)
    #     if one_recipe_serializer.is_valid():
    #         one_recipe_serializer.save()
    #         return JsonResponse(one_recipe_serializer.data) 
    #     return JsonResponse(one_recipe_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseView(ListAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        return Course.objects.order_by('course_name').all()

class CuisineView(ListAPIView):
    serializer_class = CuisineSerializer

    def get_queryset(self):
        return Cuisine.objects.order_by('cuisine_name').all()

class FoodCategoryView(ListAPIView):
    serializer_class = FoodCategorySerializer

    def get_queryset(self):
        return Food_category.objects.order_by('food_category_name').all()

# class IngredientsView(ListAPIView):
#     serializer_class = IngredientsSerializer

#     def get_queryset(self):
#         return Ingredients.objects.order_by('ingredient_name').all()
@api_view(['POST'])
def add_recipe_view(request):
    # if request.method == 'GET':
    #     cuisine = Cuisine.objects.all()
    #     cuisine_serializer = CuisineSerializer(cuisine, many=True)
    #     return JsonResponse(cuisine_serializer.data, safe=False)
    if request.method == 'POST':
        one_recipe_data = JSONParser().parse(request)
        one_recipe_serializer = OneRecipeSerializer(data=one_recipe_data)
        if one_recipe_serializer.is_valid():
            one_recipe_serializer.save()
            return JsonResponse(one_recipe_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(one_recipe_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def edit_recipe_view(request, slug):
    try: 
        recipe = Recipe.objects.get(slug=slug) 
    except Recipe.DoesNotExist: 
        return JsonResponse({'message': 'The recipe does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        one_recipe_serializer = OneRecipeSerializer(recipe) 
        return JsonResponse(one_recipe_serializer.data)
    
    elif request.method == 'PUT':
        one_recipe_data = JSONParser().parse(request)
        one_recipe_serializer = OneRecipeSerializer(recipe, data=one_recipe_data)
        if one_recipe_serializer.is_valid():
            one_recipe_serializer.save()
            return JsonResponse(one_recipe_serializer.data) 
        return JsonResponse(one_recipe_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE': 
        recipe.delete() 
        return JsonResponse({'message': 'Recipe was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def add_user_view(request): 
    
    if request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def edit_user_view(request, sub): 
    try: 
        user = User.objects.get(sub=sub) 
    except Recipe.DoesNotExist: 
        return JsonResponse({'message': 'This user does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        user_serializer = UserSerializer(user) 
        return JsonResponse(user_serializer.data)
    
    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(user, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data) 
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)