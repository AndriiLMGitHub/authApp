from django import forms

# Create your views here.


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    sender = forms.EmailField()
    message = forms.CharField()
    copy = forms.BooleanField(required=False)
    name = forms.CharField(max_length=100)

    def __str__(self):
        return self.name
