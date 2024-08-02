from django.urls import path
from .views import FoodApiView

app_name = 'food'

urlpatterns = [
    path('api/v1/foods', FoodApiView.as_view()),
]
