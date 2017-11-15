from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone


CHOICE = (
    ('OUTOFSTOCK', 'OUTOFSTOCK'),
    ('INSTOCK', 'INSTOCK')
)
CATEGORY = (
    ('Science fiction','Science fiction'),
    ('Drama','Drama'),
    ('Romance','Romance'),
    ('Horror','Horror')
)


class Book(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User)
    author = models.CharField(max_length=50)
    publisher = models.CharField(max_length=60)
    description = models.TextField()
    price = models.IntegerField()
    category_books = models.CharField(
        max_length=40,
        choices=CATEGORY, default='Drama'
    )
    book_no = models.IntegerField(blank=True)
    status = models.CharField(
        max_length=40,
        choices=CHOICE, default='INSTOCK'
    )
    updated = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        book_no = Book.objects.count()
        if book_no == 0:
            self.book_no = 1
        else:
            self.book_no = book_no + 1
        return super(Book, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

# Cooment for each book
class BookComment(models.Model):

    book_comment = models.ForeignKey(Book, null=True, blank=True)
    user = models.ForeignKey(User, blank=True, null=True)
    person_name = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now)
    email = models.EmailField()
    body = models.TextField()
    rating = models.IntegerField(default=0)
    like = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(default=timezone.now)

    class Meta:
        def __str__(self):
            return self.name
