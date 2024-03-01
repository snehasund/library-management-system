# models.py
from django.db import models
from django.utils import timezone

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
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13)
class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()