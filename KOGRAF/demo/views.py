from django.shortcuts import render
from django.http import HttpResponseRedirect
from demo.models import Experiment, Wavemaker, Dambreak, Compositionofwater

def home(request):
    database = Experiment.objects.all()
    # print(Experiment.objects.get(idexperiment=1))
    # print(database[0].durationoftheexp)
    return render(request, "demo.html", {"database": database})


def search(request):
    req = request.POST
    # condition = []
    # condition.append(req.get("id"))
    # condition.append(req.get("datetime"))
    # condition.append(req.get("title"))
    # condition.append(req.get("bottom"))
    # condition.append(req.get("amplitude"))
    # condition.append(req.get("quantity"))
    # condition.append(req.get("frequency"))
    # condition.append(req.get("operatingtime"))
    # condition.append(req.get("difference"))
    # condition.append(req.get("density"))
    # condition.append(req.get("color"))
    # condition.append(req.get("wave"))
    # condition.append(req.get("duration"))
    # # print(condition)

    # может доделаю if (not req.get("id") and not req.get("datetime") and not req.get("title") and not req.get("bottom") and not req.get("amplitude") and not req.get("quantity") and not req.get("frequency") and not req.get("operatingtime") and not req.get("difference") and not req.get("density") and not req.get("color") and not req.get("wave") req.get("duration")):
    # print(req)
    database = Experiment.objects.filter(titleofexp__icontains=req.get("title"))
    # print(database)
    return render(request, "demo.html", {"database": database})