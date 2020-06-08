from django.urls import path, include, re_path
from django.views.generic import ListView, DetailView
from .models import CommodityItem
from . import views

urlpatterns = [
    path('add_good', views.add_good, name="add_good"),
    path('', views.commodities, name="commodities"),
    re_path(r'^(?P<pk>\d+)$', DetailView.as_view(model = CommodityItem, template_name = "commodities/single_commodity.html")),
    re_path(r'^(?P<id>[0-9]+)/delete_commodity$', views.delete_commodity, name="delete_commodity"),
    re_path(r'^(?P<id>[0-9]+)/edit_commodity$', views.edit_commodity, name="edit_commodity"),
]
