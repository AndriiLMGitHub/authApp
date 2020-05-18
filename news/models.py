from django.db import models

# Create your models here.
class PostNews(models.Model):
    name_post = models.CharField(max_length=120)
    description_post = models.TextField(max_length=400)
    date_time_post = models.DateTimeField()
    image_post = models.ImageField(upload_to = 'image_folder/')
