from django.shortcuts import render
from django.http import HttpResponseRedirect
from dbapp.models import Experiment

def home(request):
    return render(request, "dbapp/home.html")
    # return HttpResponse("Hello World!")
    
def index(request):
    database = Experiment.objects.all()
    return render(request, "dbapp/index.html", {"database": database})
    # header = "Personal Data"
    # langs = ["English", "German", "Spanish"]
    # user = {"name": "Tom", "age": 23}
    # addr = ("Абрикосовая", 23, 45)

    # data = { "header": header, "langs": langs, "user": user, "address": addr }
    # return render(request, "index.html", context=data)
    # # return render(request, "index.html")

def create(request):
    if (request.method == "POST"):
        req = request.POST
        example = Experiment()
        example.date_and_time = req.get("")
        example.title_of_exp = req.get("title")
        example.type_of_bottom = req.get("bottom")
        example.video_reference = req.get("video")
        
        if (req.get("wave") == "Внутренняя"):
            example.result.bottom_sensors.results = req.get("bottom_sensors")

            example.type_of_forming.dam_break.wall_coordinate = req.get("wall_coordinate")

            example.type_of_forming.dam_break.type_of_stratification.lower_layer.density_of_water_g_cm_3_field = req.get("dam_lower_layer_density")
            example.type_of_forming.dam_break.type_of_stratification.lower_layer.name_of_the_dye = req.get("dam_lower_layer_color")
            example.type_of_forming.dam_break.type_of_stratification.lower_layer.layer_height = req.get("dam_lower_layer_height")

            example.type_of_forming.dam_break.type_of_stratification.middle_layer.density_of_water_g_cm_3_field = req.get("dam_middle_layer_density")
            example.type_of_forming.dam_break.type_of_stratification.middle_layer.name_of_the_dye = req.get("dam_middle_layer_color")
            example.type_of_forming.dam_break.type_of_stratification.middle_layer.layer_height = req.get("dam_middle_layer_height")

            example.type_of_forming.dam_break.type_of_stratification.top_layer.density_of_water_g_cm_3_field = req.get("dam_top_layer_density")
            example.type_of_forming.dam_break.type_of_stratification.top_layer.name_of_the_dye = req.get("dam_top_layer_color")
            example.type_of_forming.dam_break.type_of_stratification.top_layer.layer_height = req.get("dam_top_layer_height")

        if (req.get("wave") == "Поверхностная"):
            if req.get("capasitive_sensors"):
                example.result.string_sensors.capasitive_sensors_res = req.get("capasitive_sensors")
            
            if req.get("resistive_sensors"):
                example.result.string_sensors.resistive_sensors_res = req.get("resistive_sensors")

            example.type_of_forming.wave_maker.amplitude = req.get("amplitude")
            example.type_of_forming.wave_maker.quantity_of_waves = req.get("quantity")
            example.type_of_forming.wave_maker.frequency = req.get("frequency")
            # example.type_of_forming.wave_maker.operating_time = 
            example.type_of_forming.wave_maker.water_height = req.get("thickness")

        example.type_of_wave = req.get("wave")
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
    return render(request, "dbapp/index.html", {"database": database})
