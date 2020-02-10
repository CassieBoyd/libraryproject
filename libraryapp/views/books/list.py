import sqlite3
from django.shortcuts import render, redirect
from libraryapp.models import Book
from ..connection import Connection
from django.contrib.auth.decorators import login_required
from libraryapp.models import model_factory
from django.urls import reverse


# Note that the row factory being used for this connection to the database uses the built-in sqlite3.Row method. This allows developers to access columns in each row in the dataset by the column name instead of by index in the tuple.
@login_required
def book_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = model_factory(Book)
            # conn.row_factory = sqlite3.Row <-----Previous code
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                b.id,
                b.title,
                b.isbn,
                b.author,
                b.published,
                b.librarian_id,
                b.location_id
            from libraryapp_book b
            """)

            all_books = db_cursor.fetchall()

            # all_books = []
            # dataset = db_cursor.fetchall()

            # for row in dataset:
            #     book = Book()
            #     book.id = row['id']
            #     book.title = row['title']
            #     book.isbn = row['isbn']
            #     book.author = row['author']
            #     book.published = row['published']
            #     book.librarian_id = row['librarian_id']
            #     book.location_id = row['location_id']

            #     all_books.append(book)

        template = 'books/list.html'
        # Context is name of dictionary, gets passed to template
        context = {
            'all_books': all_books
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

    with sqlite3.connect(Connection.db_path) as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO libraryapp_book
        (
            title, author, isbn,
            published, location_id, librarian_id
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (form_data['title'], form_data['author'],
            form_data['isbn'], form_data['published'], form_data["location"], request.user.librarian.id))

    return redirect(reverse('libraryapp:books'))