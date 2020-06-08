from .models import Comment
from django import forms



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Назва', 'class': 'form-control'}),
            'email': forms.TextInput(attrs={'placeholder': 'Ціна', 'class': 'form-control'}),
            'body': forms.Textarea(attrs={'placeholder': 'Текст', 'cols': 50, 'rows': 15, 'class':'form-control'})
        }
