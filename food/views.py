from django.shortcuts import render, get_object_or_404
import random
from home.views import context_password
from .models import FoodItem
# Create your views here



def food(request):
    all_post_food = FoodItem.objects.all()
    new_context = {'all_post_food': all_post_food }
    new_context.update(context_password())
    return render(request, 'food/food-items.html', new_context)


def food_detail(request, id):
    food_single_post = get_object_or_404(FoodItem, pk = id)
    food_detail = {
        'food_single_post' : food_single_post,
    }
    return render(request, 'food/food_detail.html', food_detail)
