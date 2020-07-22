from django.shortcuts import render
from .models import BlogPost

# Create your views here.
def blog(request):
    blog_post_list = BlogPost.objects.all()
    context = {
        'blog_post_list': blog_post_list
    }
    return render(request, 'blog/blog-list.html', context)
