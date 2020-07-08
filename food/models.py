from django.db import models

# Create your models here.
class FoodItem(models.Model):
    titleFood = models.CharField(max_length=30)
    textFood = models.TextField()
    date_published = models.DateTimeField()
    imageFood = models.FileField(upload_to='FoodImages')


    def __str_(self):
        return self.titleFood
