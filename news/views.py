from django.shortcuts import render
from .models import PostNew, Comment
from .forms import CommentForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseNotFound


# Create your views here.
def post_detail(request, id):
    post = get_object_or_404(PostNew, pk = id)
    # List of active comments for this post
    comments = post.comments.filter(active=True) #, year, month, day, post
    #post_detail_self = PostNew.objects.get(id)

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    context = {'comments': comments, 'comment_form': comment_form, 'post' : post}

    return render(request, 'news/new_single.html', context)


def edit_comment(request, id):
    edit_comment = get_object_or_404(Comment, id = id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance = edit_comment)
        if form.is_valid():
            CommentForm.name = request.POST.get("name")
            CommentForm.email = request.POST.get("email")
            CommentForm.body = request.POST.get("body")
            edit_comment.save()
            return HttpResponseRedirect('/news/')
    else:
        form = CommentForm(instance = edit_comment)
    return render(request, 'news/edit_comment.html', {'form' : form})


def delete_comment(request, id):
    try:
        delete_list = Comment.objects.get(id=id)
        delete_list.delete()
        return HttpResponseRedirect("/news/")
    except Comment.DoesNotExist:
        return HttpResponseNotFound("<h2>Item not found</h2>")
