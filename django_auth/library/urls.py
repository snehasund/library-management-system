from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('books/', views.book_list, name='book_list'),  # List all books
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),  # Book detail page
    path('books/add/', views.add_book, name='add_book'),  # Add a new book
    path('books/<int:book_id>/edit/', views.edit_book, name='edit_book'),  # Edit book details
    path('books/<int:book_id>/delete/', views.delete_book, name='delete_book'),  # Delete a book
    path('authors/', views.author_list, name='author_list'),  # List all authors
    path('authors/<int:author_id>/', views.author_detail, name='author_detail'),  # Author detail page
    path('authors/add/', views.add_author, name='add_author'),  # Add a new author
    path('authors/<int:author_id>/edit/', views.edit_author, name='edit_author'),  # Edit author details
    path('authors/<int:author_id>/delete/', views.delete_author, name='delete_author'),  # Delete an author
    path('members/', views.member_list, name='member_list'),  # List all members
    path('members/<int:member_id>/', views.member_detail, name='member_detail'),  # Member detail page
    path('members/add/', views.add_member, name='add_member'),  # Add a new member
    path('members/<int:member_id>/edit/', views.edit_member, name='edit_member'),  # Edit member details
    path('members/<int:member_id>/delete/', views.delete_member, name='delete_member'),  # Delete a member
]
