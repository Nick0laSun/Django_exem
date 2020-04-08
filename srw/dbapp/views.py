from django.shortcuts import render
from django.http import HttpResponseRedirect
from dbapp.models import Experiment

def home(request):
    return render(request, "dbapp/home.html")
    # return HttpResponse("Hello World!")
    
def index(request):
    database = Experiment.objects.all()
    return render(request, "index.html", {"database": database})
    # header = "Personal Data"
    # langs = ["English", "German", "Spanish"]
    # user = {"name": "Tom", "age": 23}
    # addr = ("Абрикосовая", 23, 45)

    # data = { "header": header, "langs": langs, "user": user, "address": addr }
    # return render(request, "index.html", context=data)
    # # return render(request, "index.html")

def create(request):
    if (request.method == "POST"):
        example = Experiment()
        example.title_of_exp = request.POST.get("title")
        example.type_of_bottom = request.POST.get("bottom")
        example.video_reference = request.POST.get("video")
        example.type_of_wave = request.POST.get("wave")
        example.save()
    return HttpResponseRedirect("index")

def search(request):
    req = request.POST
    # print(req)
    if (not req.get("id") and not req.get("title") and not req.get("wave")) or not req:
        database = Experiment.objects.all()
    else:
        # database = Experiment.objects.filter(id=id).filter(title_of_exp__icontains=req.get("title"))
        if not req.get("id") and not req.get("wave"):
            database = Experiment.objects.filter(title_of_exp__icontains=req.get("title"))

        if not req.get("title") and not req.get("wave"):
            id = int(req.get("id"))
            if (id == 0):
                database = Experiment.objects.all()
            else:
                database = Experiment.objects.filter(id=id)

        if not req.get("id") and not req.get("title"):
            database = Experiment.objects.filter(type_of_wave__icontains=req.get("wave"))


    # if not request.POST.get("id"):
    #     database = Experiment.objects.all()
    # else:
    #     id = int(request.POST.get("id"))
    #     if (id == 0):
    #         database = Experiment.objects.all()
    #     else:
    #         database = Experiment.objects.filter(id=id)
    return render(request, "index.html", {"database": database})
