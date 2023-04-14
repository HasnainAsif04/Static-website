from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def about_me(request):
    test = {'name': 'Hasnain',
            }
    return render(request, "about_me.html", test)

def portfolio(request):
    return render(request, "portfolio.html")

def contact(request):
    return render(request, "contact.html")