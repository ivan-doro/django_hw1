import collections
from collections import defaultdict
from datetime import datetime

from django.core.paginator import Paginator
from django.shortcuts import render
from django.forms.models import model_to_dict
from books.models import Book


# View function that sends list of all the books in db to books_list.html
def books_view(request):
    template = 'books/books_list.html'
    books_list = list(Book.objects.all())
    books_list = sorted(books_list, key=lambda d: d.pub_date)
    context = {
        'books': books_list
    }
    return render(request, template, context)


# View function that sends all the books for the date to books_for_date.html
# It also has buttons for next and previous
def books_for_date_view(request, pub_date):
    print(pub_date)
    template = 'books/books_for_date.html'
    # Creating dictionary with lists of books for each date
    books_dict = defaultdict(list)
    for book in list(Book.objects.all()):
        books_dict[book.pub_date].append(model_to_dict(book))
    # Converting dictionary to list of dict elements, sorting them by date
    books_list = [{'date': date, 'books': books} for date, books in books_dict.items()]
    books_list = sorted(books_list, key=lambda d: d['date'])
    # Getting page number for the given pub_date
    i = 0
    page_num = 0
    for x in books_list:
        i += 1
        if x['date'] == datetime.strptime(pub_date, '%Y-%m-%d').date():
            page_num = i
    # Creating paginator
    paginator = Paginator(list(books_list), 1)
    page = paginator.get_page(page_num)
    # Finding next_date and previous_date to send to html file
    if page.has_next():
        next_page = paginator.get_page(page.next_page_number())
        next_date = next_page.object_list[0]['books'][0]['pub_date']
    else:
        next_date = ''

    if page.has_previous():
        previous_page = paginator.get_page(page.previous_page_number())
        previous_date = previous_page.object_list[0]['books'][0]['pub_date']
    else:
        previous_date = ''

    context = {
        'books': page.object_list[0]['books'],
        'page': page,
        'next_date': next_date,
        'previous_date': previous_date
    }
    return render(request, template, context)
