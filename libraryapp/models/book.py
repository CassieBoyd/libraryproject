from django.db import models
from .librarian import Librarian
from .library import Library


class Book (models.Model):

    title = models.CharField(max_length=50)
    isbn = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    published = models.IntegerField()
    librarian = models.ForeignKey(Librarian, on_delete=models.CASCADE)
    location = models.ForeignKey(
        Library, related_name="books",
        null=True,
        blank=True,
        on_delete=models.CASCADE)