from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.food, name="food"),
    path('<int:id>', views.food_detail, name="food_detail"),

]
