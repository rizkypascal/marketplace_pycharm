from django import forms

class ProductForm(forms.Form):
    link = forms.URLField(label='Your link', max_length=255)