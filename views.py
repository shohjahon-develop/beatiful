from django.shortcuts import render
from .models import Maxsulotlar, Client
# Create your views here.
def client(request):
    client=Client.objects.all()
    context = {
        "client": client,
    }
    return render(request,"client.html",context=context)
def contact(request):
    return render(request,"contact.html",context={})

def products(request):
    products = Maxsulotlar.objects.all()
    context = {
        "products": products,
    }
    return render(request,"products.html",context=context)

def about(request):
    return render(request,"about.html",context={})

def index(request):
    print("request")
    maxsulot = Maxsulotlar.objects.all()
    print("maxsulotlar -> ", maxsulot)
    context = {
        "products": maxsulot
    }
    return render(request, "index.html", context)