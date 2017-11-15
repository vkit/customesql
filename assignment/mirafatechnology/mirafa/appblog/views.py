from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView, View, DetailView
from .models import Book, BookComment
from .forms import BookForm, BookCommentForm, BookUpdateForm, RatingUpdateForm
from django.shortcuts import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

# To display all book information
from django.db.models import Count
class BookList(ListView):
    template_name = 'book_list.html'
    model = Book

    def get_context_data(self, **kwargs):
        context = super(BookList, self).get_context_data(**kwargs)
        context['form'] = BookForm()
        context['book_count'] = Book.objects.count()
        context['books'] = Book.objects.all().order_by('-created_at')
        return context

# To  add books, make sure only authenticated person can add the books.

class AddBook(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        try:
            form = BookForm(request.POST)
            if form.is_valid():
                instance = form.instance
                instance.save()
                form.save()
                messages.success(
                    request, 'Well done!Your book is Addded Succesfully.')
            else:
                print form.errors
            return HttpResponseRedirect('/appblog/book_list/')
        except Exception as e:
            print e

# Display the detail page of the each book

class BookDetailView(DetailView):
    template_name = 'book_detail.html'
    model = Book

    def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data(**kwargs)
        context['form'] = BookCommentForm()
        context['book'] = Book.objects.get(pk=self.kwargs.get('pk'))
        context['form1'] = BookUpdateForm(instance=context['book'])
        context['form2'] = RatingUpdateForm(instance=context['book'])
        return context

# Inside detail of each book, user can put comment on boooks
class BookCommentView(View):

    def post(self, request, *args, **kwargs):
        form = BookCommentForm(request.POST)
        if form.is_valid():
            instance = form.instance
            book = Book.objects.get(pk=self.kwargs.get('pk'))
            instance.book = book
            form.save()
            messages.success(
                request, 'Well done!Your Comment is Added Succesfully.')
        else:
            print form.errors
        return HttpResponseRedirect(
            '/appblog/{0}/detail/'.format(self.kwargs.get('pk')))

# Only authenticated user can change the status of the book,whether book is instock or out of stock
class BookupdateStatusView(LoginRequiredMixin,View):

    def post(self, request, *args, **kwargs):
        book = Book.objects.get(pk=self.kwargs.get('pk'))
        form1 = BookUpdateForm(request.POST, instance=book)
        if form1.is_valid():
            form1.save()
            messages.success(
                request, 'Well done!Your status is updated succesfully.')
        else:
            print form1.errors
        return HttpResponseRedirect(
            '/appblog/{0}/detail/'.format(book.id))


class BookUpdateRatingView(View):
    def post(self, request, *args, **kwargs):
        book = Book.objects.get(pk=self.kwargs.get('pk'))
        form2 = RatingUpdateForm(request.POST,instance=book)
        if form2.is_valid:
            form2.save()
            messages.success(
                request, 'Well done!Your status is updated succesfully.')
        else:
            print form1.errors
        return HttpResponseRedirect(
            '/appblog/{0}/detail/'.format(book.id))


class BookLikeView(View):
    def post(self, request, *args, **kwargs):
        book = Book.objects.get(pk=self.kwargs.get('pk'))
        book.bookcomment_set.update(like=1)
        book.save()
        messages.success(
            request, 'Well done!Your item is changed Succesfully.')
        return HttpResponseRedirect(
            '/appblog/{0}/detail/'.format(book.id))


class DeleteBook(View):
    def get(self, request, *args, **kwargs):
        try:
            book = Book.objects.get(pk=self.kwargs.get('pk'))
            book.delete()
            messages.success(
                request, 'Well done!Your deleted succesfully.')
            return HttpResponseRedirect(
                '/appblog/book_list/')
        except Book.DoesNotExists:
            print e


# SELECT COUNT(CustomerID), Country
# FROM Customers
# GROUP BY Country;


from django.db import connection


class Test(View):
    def get(self, request,*args, **kwargs):
        
        cursor = connection.cursor()
        cursor.execute('SELECT COUNT(price)FROM appblog_book')
        max_value = cursor.fetchone()[0]
        print max_value
        context = {"max_value":max_value}
        return render(request, "test.html", context)

# Group by, sum of all price in status=instock


class TestView(View):
    def get(self, request, *args, **kwargs):
        cursor = connection.cursor()
        cursor.execute("SELECT SUM(price),status='INSTOCK'FROM appblog_book GROUP BY status='INSTOCK'")
        value = cursor.fetchone()[0]
        context = {"value":value}
        return render(request,"test.html",context)


class Test2View(View):
    def get(self, request,*args, **kwargs):
        
        cursor = connection.cursor()
        cursor.execute("SELECT DISTINCT status='INSTOCK' FROM appblog_book")
        dif = cursor.fetchone()[0]
        print dif
        context = {"max_value":dif}
        return render(request, "test.html", context)


class TitleView(View):
    def get(self, request,*args, **kwargs):
        
        cursor = connection.cursor()
        cursor.execute("SELECT title FROM appblog_book")
        all_value = cursor.cursor.fetchall()

        print all_value
        context = {"all_value":all_value}
        return render(request, "test.html", context)

