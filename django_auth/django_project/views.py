from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django_project.models import Borrow, Book, Member
from django_project.forms import BookForm, MemberForm

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html', {'authors': authors})

def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'author_detail.html', {'author': author})

def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm()
    return render(request, 'author_form.html', {'form': form})

def author_update(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm(instance=author)
    return render(request, 'author_form.html', {'form': form})

def author_delete(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        author.delete()
        return redirect('author_list')
    return render(request, 'author_confirm_delete.html', {'author': author})

# Similarly, you can define views for books and members
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
            return redirect('members_list')  # Redirect to members list page after successful form submission
    else:
        form = MemberForm()
    return render(request, 'library/add_member.html', {'form': form})
