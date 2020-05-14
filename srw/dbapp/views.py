from django.shortcuts import render
from django.http import HttpResponseRedirect
from dbapp.models import Experiment
import datetime

def home(request):
    return render(request, "dbapp/home.html")
    # return HttpResponse("Hello World!")

def test(request):
    return render(request, "test.html")

def test_search(request):
    req = request.POST
    print('test complited')
    print(req.get("id"))
    return render(request, "test.html")
    
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

        year = int(req.get("year"))
        month = int(req.get("month"))
        day = int(req.get("day"))
        hour = int(req.get("hour"))
        minute = int(req.get("min"))
        seconds = int(req.get("sec"))

        date_time = datetime.datetime(year, month, day, hour, minute, seconds)
        example.date_and_time = date_time
        example.title_of_exp = req.get("title")
        example.type_of_bottom = req.get("bottom")
        example.type_of_wave = req.get("wave")
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

            hour = int(req.get("wavemaker_dur_hour"))
            minute = int(req.get("wavemaker_dur_min"))
            seconds = int(req.get("wavemaker_dur_sec"))
            wavemaker_dur_time = datetime.time(hour, minute, seconds)

            example.type_of_forming.wave_maker.operating_time = wavemaker_dur_time
            example.type_of_forming.wave_maker.water_height = req.get("thickness")

        example.schema_of_exp_reference = req.get("schema")

        hour = int(req.get("dur_hour"))
        minute = int(req.get("dur_min"))
        seconds = int(req.get("dur_sec"))
        exp_dur_time = datetime.time(hour, minute, seconds)

        example.duration_of_the_exp = exp_dur_time

        example.type_of_stratification.lower_layer.density_of_water_g_cm_3_field = req.get("lower_layer_density")
        example.type_of_stratification.lower_layer.name_of_the_dye = req.get("lower_layer_color")
        example.type_of_stratification.lower_layer.layer_height = req.get("lower_layer_height")

        example.type_of_stratification.middle_layer.density_of_water_g_cm_3_field = req.get("middle_layer_density")
        example.type_of_stratification.middle_layer.name_of_the_dye = req.get("middle_layer_color")
        example.type_of_stratification.middle_layer.layer_height = req.get("middle_layer_height")

        example.type_of_stratification.top_layer.density_of_water_g_cm_3_field = req.get("top_layer_density")
        example.type_of_stratification.top_layer.name_of_the_dye = req.get("top_layer_color")
        example.type_of_stratification.top_layer.layer_height = req.get("top_layer_height")

        example.polarity = req.get("polarity")

        if(req.get("used") == "Не использовался"):
            example.laser.used = req.get("used")

        if(req.get("used") == "Использовался"):
            example.laser.used = req.get("used")
            example.laser.video_reference = req.get("laser_video")
            example.laser.laser_coordinate = req.get("laser_coordinate")
            example.laser.viewing_angle = req.get("laser_angle")

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
