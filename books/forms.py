from django import forms
from .models import Book, Category
from django.contrib.auth.models import User

class UserModelChoiceField(forms.ModelChoiceField):

    def label_from_instance(self, obj):
        return obj.email

class BookForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['author'].empty_label = '-- Select author --'
        self.fields['category'].empty_label = '-- Select category --'

    class Meta:
        model = Book
        fields = ('title','content','author','published','category')
        field_classes = {
            'author': UserModelChoiceField
        }

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'}),
            'author': forms.Select(attrs={'class':'form-control'}),
        }
