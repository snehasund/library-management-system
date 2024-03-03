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
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'book title'}),
            'author': forms.TextInput(attrs={'placeholder': 'author name'}),
            'isbn': forms.TextInput(attrs={'placeholder': 'ISBN number'}),
        }
        fields = '__all__'  # Specify the fields you want to include in the form
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
    
