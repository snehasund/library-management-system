# models.py
from django.db import models
from django.utils import timezone

class Borrow(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    member = models.ForeignKey('Member', on_delete=models.CASCADE)
    borrow_date = models.DateField(default=timezone.now)
    return_date = models.DateField(null=True, blank=True)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13)
    quantity = models.IntegerField(default=0)

class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

# views.py
from django.shortcuts import get_object_or_404, redirect, render
from .models import Book, Member, Borrow

def borrow_book(request, book_id, member_id):
    book = get_object_or_404(Book, pk=book_id)
    member = get_object_or_404(Member, pk=member_id)
    if book.quantity > 0:
        Borrow.objects.create(book=book, member=member)
        book.quantity -= 1
        book.save()
        return redirect('book_detail', book_id=book_id)
    else:
        # Handle case when book is not available
        pass

def return_book(request, borrow_id):
    borrow = get_object_or_404(Borrow, pk=borrow_id)
    if borrow.return_date is None:
        borrow.return_date = timezone.now().date()
        borrow.save()
        borrow.book.quantity += 1
        borrow.book.save()
    return redirect('member_detail', member_id=borrow.member_id)
