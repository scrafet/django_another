from django.http import HttpResponse
from django.shortcuts import render

from core.erp.models import Category, Product


# Create your views here.
def myfirstview(request):
    data = {
        'name': 'William',
        'categories': Category.objects.all()
    }
    return render(request, 'home.html', data)


def mysecondview(request):
    data = {
        'name': 'William',
        'products': Product.objects.all()
    }
    return render(request, 'second.html', data)
