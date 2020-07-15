from django.db import models

# Create your models here.
class BlogPost(models.Model):

    labels_of_blog_post = [
        ('Ukraine', 'UA'),
        ('Russia','RU'),
        ('Poland', 'PL'),
        ('Belarus','BE'),
        ('Slovakia', 'SK'),
    ]

    name_blog_post = models.CharField(max_length=20)
    description_blog_post = models.CharField(max_length=50)
    date_time_blog_post = models.DateTimeField()
    label_blog_post = models.CharField(max_length=10, choices=labels_of_blog_post, default='1')
    image_blog_post = models.FileField(upload_to='blog_folder/',)

    def __str__(self):
        return self.name_blog_post
