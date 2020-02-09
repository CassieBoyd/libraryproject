import sqlite3
from django.shortcuts import render, redirect
from libraryapp.models import Library
from ..connection import Connection
from django.contrib.auth.decorators import login_required
from libraryapp.models import model_factory
from django.urls import reverse


@login_required
def library_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = model_factory(Library)

            # conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                l.id,
                l.title,
                l.address
            from libraryapp_library l
            """)

            all_libraries = db_cursor.fetchall()
            # all_libraries = []
            # dataset = db_cursor.fetchall()

            # for row in dataset:
            #     lib = Library()
            #     lib.title = row["title"]
            #     lib.address = row["address"]

            #     all_libraries.append(lib)

        template_name = 'libraries/list.html'

        context = {
            'all_libraries': all_libraries
        }

        return render(request, template_name, context)

    elif request.method == 'POST':
        form_data = request.POST

    with sqlite3.connect(Connection.db_path) as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO libraryapp_library
        (
            title, address
        )
        VALUES (?, ?)
        """,
        (form_data['title'], form_data['address']))

    return redirect(reverse('libraryapp:libraries'))