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
        fields = '__all__'  # Specify the fields you want to include in the form

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'  # Specify the fields you want to include in the form
