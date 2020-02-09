from django.urls import path
from .views import *
from django.urls import include, path


app_name = "libraryapp"

urlpatterns = [
    path('', home, name='home'),
    path('books/', book_list, name='books'),
    path('librarians/', librarian_list, name='librarians'),
    path('libraries/', library_list, name='libraries'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('book/form', book_form, name='book_form'),
    path('library/form', library_form, name='library_form'),
    path('books/<int:book_id>/', book_details, name='book'),
]