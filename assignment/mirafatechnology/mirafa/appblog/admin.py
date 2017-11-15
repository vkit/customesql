from django.contrib import admin

from .models import Book,BookComment
admin.site.register(Book)
admin.site.register(BookComment)
