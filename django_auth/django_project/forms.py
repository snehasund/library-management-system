# forms.py

from django import forms
from .models import Book, Member

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'isbn']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'book title'}),
            'author': forms.TextInput(attrs={'placeholder': 'author'}),
            'genre': forms.TextInput(attrs={'placeholder': 'genre'}),
            'isbn': forms.TextInput(attrs={'placeholder': 'ISBN number'}),
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
    
