# forms.py

from django import forms
from .models import Book, Member

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'isbn']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'book title', 'style': "height: 40px; border-radius: 8px; text-align: center; background-color: rgb(207, 207, 241); margin-bottom: 10px;" }),
            'author': forms.TextInput(attrs={'placeholder': 'author', 'style': "height: 40px; border-radius: 8px; text-align: center; background-color: rgb(207, 207, 241); margin-bottom: 10px;"}),
            'genre': forms.TextInput(attrs={'placeholder': 'genre', 'style': "height: 40px; border-radius: 8px; text-align: center; background-color: rgb(207, 207, 241); margin-bottom: 10px;"}),
            'isbn': forms.TextInput(attrs={'placeholder': 'ISBN number', 'style': "height: 40px; border-radius: 8px; text-align: center; background-color: rgb(207, 207, 241); margin-bottom: 10px;"}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add to_field_name for the author field
        self.fields['author'].to_field_name = 'name'
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5:  # Just an example validation
            raise forms.ValidationError("Title should be at least 5 characters long.")
        return title
    
class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'email', 'favorite_genre']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Full Name', 'style': "height: 40px; border-radius: 8px; text-align: center; background-color: rgb(207, 207, 241); margin-bottom: 10px;" }),
            'email': forms.TextInput(attrs={'placeholder': 'Email', 'style': "height: 40px; border-radius: 8px; text-align: center; background-color: rgb(207, 207, 241); margin-bottom: 10px;"}),
            'favorite_genre': forms.TextInput(attrs={'placeholder': 'Favorite Genre', 'style': "height: 40px; border-radius: 8px; text-align: center; background-color: rgb(207, 207, 241); margin-bottom: 10px;"}),
        }
    
