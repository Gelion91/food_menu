from rest_framework import generics

from food.models import FoodCategory
from food.serializers import FoodListSerializer


# Class for displaying a list of food categories
class FoodApiView(generics.ListAPIView):
    queryset = FoodCategory.objects.filter(food__is_publish=True)
    serializer_class = FoodListSerializer
