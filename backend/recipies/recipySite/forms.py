from django import forms
from .models import Recipy, Category


class RecipyForm(forms.ModelForm):
   class Meta:
       model = Recipy
       fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
