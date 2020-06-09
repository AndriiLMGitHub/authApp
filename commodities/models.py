from django.db import models

# Create your models here.


class CommodityItem(models.Model):
    name_good = models.CharField(max_length = 50)
    price_good = models.CharField(max_length = 10)
    description_good = models.TextField(max_length = 1000)
    date_published_good = models.DateTimeField(auto_now_add=True)
    image_good = models.ImageField(upload_to='images_goods/',)
    image_good_galery_1 = models.ImageField(upload_to='images_goods',)
    image_good_galery_2 = models.ImageField(upload_to='images_goods/',)
    image_good_galery_3 = models.ImageField(upload_to='images_goods/',)
    image_good_galery_4 = models.ImageField(upload_to='images_goods/',)
    image_good_galery_5 = models.ImageField(upload_to='images_goods/',)
    image_good_galery_6 = models.ImageField(upload_to='images_goods/',)
    image_good_galery_7 = models.ImageField(upload_to='images_goods/gallery',)

    def __str__(self):
        return self.name_good
