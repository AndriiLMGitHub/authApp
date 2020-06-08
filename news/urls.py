from django.urls import path, include, re_path
from django.views.generic import ListView, DetailView
from . import views
from news.models import PostNew


urlpatterns = [
    path('', ListView.as_view(queryset = PostNew.objects.all().order_by("-date_time_post")[:10] ,
    template_name = "news/news.html" )),
    #re_path(r'^(?P<pk>\d+)$', DetailView.as_view(model = PostNew, template_name = "news/new_single.html")),

    path('<int:id>/', views.post_detail, name="post_detail"),

    path('<int:id>/edit_comment', views.edit_comment, name="edit_comment"),
    path('<int:id>/delete_comment', views.delete_comment, name="delete_comment"),
]
