from django import forms
from .models import CommodityItem



class AddCommidityItem(forms.ModelForm):

     class Meta():
         model = CommodityItem
         fields = (
         'name_good',
         'price_good',
         'description_good',
         'image_good',
         'image_good_galery_1',
         'image_good_galery_2',
         'image_good_galery_3',
         'image_good_galery_4',
         'image_good_galery_5',
         'image_good_galery_6',
         'image_good_galery_7',
         )
         widgets = {
             'name_good': forms.TextInput(attrs={'placeholder': 'Назва', 'class': 'form-control'}),
             'price_good': forms.TextInput(attrs={'placeholder': 'Ціна', 'class': 'form-control'}),
             'description_good': forms.Textarea(attrs={'placeholder': 'Текст', 'cols': 50, 'rows': 15, 'class':'form-control'}),
             #'image_good': forms.ImageField(attrs={'class': 'form-control'}),
         }
