# forms.py

from django import forms
from .models import Author, Book, Member

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'book title'}),
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
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'name'}),
            'email': forms.TextInput(attrs={'placeholder': 'email'}),
            'favorite_genre': forms.TextInput(attrs={'placeholder': 'favorite genre'}),
        }
        fields = '__all__'  # Specify the fields you want to include in the form
    
