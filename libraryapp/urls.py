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
]