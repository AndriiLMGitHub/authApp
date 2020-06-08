from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .forms import AddCommidityItem
from .models import CommodityItem

# Create your views here.

def add_good(request):
    form = AddCommidityItem()
    if request.method == "POST":
        form = AddCommidityItem(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return HttpResponseRedirect('/commodities/')
        else:
            form = AddCommidityItem()
    return render(request, 'commodities/add_good.html', {'form' : form })


def commodities(request):
    post_commodities = CommodityItem.objects.all()
    return render(request, 'commodities/commodities.html', {'post_commodities' : post_commodities})

def edit_commodity(request, id):
    edit_form = get_object_or_404(CommodityItem, id=id)
    if request.method == "POST":
        form = AddCommidityItem(request.POST, request.FILES, instance = edit_form)
        if form.is_valid():
            AddCommidityItem.name_good = request.POST.get("name_good")
            AddCommidityItem.price_good = request.POST.get("price_good")
            AddCommidityItem.description_good = request.POST.get("description_good")
            edit_form.save()
            return HttpResponseRedirect('/commodities/')
    else:
        form = AddCommidityItem(instance=edit_form)
    return render(request, 'commodities/edit_commodity.html', {'form': form })

def delete_commodity(request, id):
    post_commodities = CommodityItem.objects.all()
    try:
        delete_list = CommodityItem.objects.get(id=id)
        delete_list.delete()
        return HttpResponseRedirect("/commodities/")
    except Add_item.DoesNotExist:
        return HttpResponseNotFound("<h2>Item not found</h2>")
