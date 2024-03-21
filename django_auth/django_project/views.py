from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django_project.models import Borrow, Book, Member, Favorite
from django_project.forms import BookForm, MemberForm

from django.contrib.auth.decorators import user_passes_test

def user_is_admin(user):
    return user.is_superuser  # Assuming only superusers have admin privileges

# you can define views for books and members
def books_list_view(request):
    # Here you can include any logic or data retrieval you need
    # For example, if you want to pass some books data to the template
    books = Book.objects.all()
    context = {
        'books': books,  # Pass the books data to the template
    }
    return render(request, 'library/books_list.html', context)

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            # Optionally, you can redirect to a different URL after saving the form
            return redirect('books_list')  # Redirect to the books list page
    else:
        form = BookForm()
    return render(request, 'library/book_form.html', {'form': form})

def members_list(request):
    members = Member.objects.all()  # Retrieve all members from the database
    return render(request, 'library/members_list.html', {'members': members})

def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('members_list')  # Redirect to members list page after successful form submission
    else:
        form = MemberForm()
    return render(request, 'library/add_member.html', {'form': form})

@login_required
def favorites(request):
    user = request.user
    favorite_books = user.favorite_set.all()  # Assuming 'Favorite' model has a related_name of 'favorite'
    return render(request, 'favorites.html', {'favorite_books': favorite_books})

@login_required
def library_page(request):
    user = request.user
    favorites = Favorite.objects.filter(user=user)
    friend_name = request.GET.get('friend_name')
    return render(request, 'library/library_page.html', {'favorites': favorites, 'friend_name': friend_name})

@login_required
def favorite_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    user = request.user
    favorite, created = Favorite.objects.get_or_create(user=user, book=book)
    if not created:
        favorite.delete()
        status = 'unfavorited'
    else:
        status = 'favorited'
    return JsonResponse({'status': status})

@login_required
def rate_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    user = request.user
    favorite, created = Favorite.objects.get_or_create(user=user, book=book)
    favorite.rating = request.POST["rating"]
    favorite.save()
    print(request.POST["rating"])
    return JsonResponse({'status': request.POST["rating"]})

@login_required
def get_book_rating(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    user = request.user
    favorite, created = Favorite.objects.get_or_create(user=user, book=book)
    return JsonResponse({'rating': favorite.rating})

@user_passes_test(user_is_admin)
def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books_list')  # Redirect to the books list page
    else:
        form = BookForm(instance=book)
    return render(request, 'library/edit_form.html', {'form': form})
  
def edit_member(request, member_id):
    member = Member.objects.get(id=member_id)
    if request.method == 'POST':
        member_form = MemberForm(request.POST, instance=member)
        if member_form.is_valid():
            member_form.save()
            return redirect('members_list')  # Redirect to the books list page
    else:
        member_form = MemberForm(instance=member)
    return render(request, 'library/edit_member.html', {'member_form': member_form})