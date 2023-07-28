from django.shortcuts import render


# Create your views here.

def myfirstview(request):

    return render(request, 'index.html')
