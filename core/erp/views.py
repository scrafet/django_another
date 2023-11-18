from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def myfirstview(request):
    data={
        'name' : 'William'
    }
    return render(request, 'index.html',data)
