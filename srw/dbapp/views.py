from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "dbapp/home.html")
    # return HttpResponse("Hello World!")
    
def index(request):
    header = "Personal Data"
    langs = ["English", "German", "Spanish"]
    user = {"name": "Tom", "age": 23}
    addr = ("Абрикосовая", 23, 45)

    data = { "header": header, "langs": langs, "user": user, "address": addr }
    return render(request, "index.html", context=data)
    # return render(request, "index.html")