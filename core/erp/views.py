from django.http import HttpResponse
from django.shortcuts import render

from core.erp.models import Category


# Create your views here.
def myfirstview(request):
    data = {
        'name': 'William',
        'categories': Category.objects.all()
    }
    return render(request, 'index.html', data)


def mysecondview(request):
    data = {
        'name': 'William',
        'categories': Products.objects.all()
    }
    return render(request, 'index.html', data)
