# models.py
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Author(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length = 250)
    
class Borrow(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    member = models.ForeignKey('Member', on_delete=models.CASCADE)
    borrow_date = models.DateField(default=timezone.now)
    return_date = models.DateField(null=True, blank=True)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    isbn = models.CharField(max_length=13)
    
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_favorited = models.DateTimeField(auto_now_add=True)

class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    favorite_genre = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='templates/library/media/profile_pictures/')
