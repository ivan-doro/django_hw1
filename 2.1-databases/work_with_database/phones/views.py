from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


# function that sends phones list from db to html file, filtered if required
def show_catalog(request):
    sort = request.GET.get("sort", None)
    if sort:
        if  sort == 'min_price':
            sort = 'price'
        elif sort == 'max_price':
            sort = '-price'
        phones = Phone.objects.all().order_by(sort)
    else:
        phones = Phone.objects.all()
    template = 'catalog.html'
    context = {
        'phones': phones
    }
    return render(request, template, context)


# function that sends particular phone info from db to html file based on slug
def show_product(request, slug):
    template = 'product.html'
    context = {
        'phone': Phone.objects.filter(slug__exact=slug)[0]
    }
    return render(request, template, context)
