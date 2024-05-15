"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView 
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path('books/', views.books_list_view, name='books_list'),
    path('add_book/', views.add_book, name='add_book'),
    path('members/', views.members_list, name='members_list'),
    path('add_member/', views.add_member, name='add_member'),
    path('favorite/<int:book_id>/', views.favorite_book, name='favorite_book'),  # URL pattern for favoriting/unfavoriting
    path('rate/<int:book_id>/', views.rate_book, name='rate_book'),  
    path('rating/<int:book_id>/', views.get_book_rating, name='get_book_rating'), 
    path('library/', views.library_page, name='library_page'),     
    path('edit-form/<int:book_id>/', views.edit_book, name='edit_book'),
    path('edit_member/<int:member_id>/', views.edit_member, name='edit_member'),
    path('delete_member/<int:member_id>/', views.delete_member, name='delete_member'),
    path('delete-book/<int:book_id>/', views.delete_book, name='delete_book'),
]
