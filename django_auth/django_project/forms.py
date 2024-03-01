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

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'  # Specify the fields you want to include in the form
