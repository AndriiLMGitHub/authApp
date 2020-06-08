from django.db import models

# Create your models here.\
class PostNew(models.Model):
    name_post = models.CharField(max_length=120)
    description_post = models.TextField(max_length=400)
    date_time_post = models.DateTimeField()
    image_post = models.ImageField(upload_to = 'image_folder/')

    def __str__(self):
        return self.name_post


        
class Comment(models.Model):
    post = models.ForeignKey(PostNew, related_name='comments', on_delete = models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
