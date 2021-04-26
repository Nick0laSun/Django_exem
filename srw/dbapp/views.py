from django.shortcuts import render
from django.http import HttpResponseRedirect
from dbapp.models import Experiment
import datetime
import time

def home(request):
    return render(request, "dbapp/home.html")
    # return HttpResponse("Hello World!")

def test(request):
    return render(request, "test.html")

def test_search(request):
    req = request.POST
    print(req)
    print(request)
    database = Experiment.objects.all()
    return render(request, "dbapp/index.html", {"database": database})
    
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

def stratification_search(req):
    layers = int(req.get("layers"))
    if layers == 1:
        condition_1 = req.get("top_layer_height") or req.get("top_layer_density") or req.get("top_layer_color")
        condition_2 = req.get("top_layer_density") or req.get("top_layer_color")
        condition_3 = req.get("top_layer_height") or req.get("top_layer_color")
        condition_4 = req.get("top_layer_height") or req.get("top_layer_density")
        condition_5 = req.get("top_layer_height")
        condition_6 = req.get("top_layer_density")
        condition_7 = req.get("top_layer_color")
        condition_8 = req.get("top_layer_height") and req.get("top_layer_density") and req.get("top_layer_color")

        if not condition_1:
            database = Experiment.objects.all()
        elif not condition_2:
            database = Experiment.objects.filter(type_of_stratification__top_layer__layer_height=req.get("top_layer_height"))
        elif not condition_3:
            database = Experiment.objects.filter(type_of_stratification__top_layer__density_of_water_g_cm_3_field=req.get("top_layer_density"))
        elif not condition_4:
            database = Experiment.objects.filter(type_of_stratification__top_layer__name_of_the_dye__icontains=req.get("top_layer_color"))
        elif not condition_5:
            database = Experiment.objects.filter(type_of_stratification__top_layer__density_of_water_g_cm_3_field=req.get("top_layer_density")) \
            .filter(type_of_stratification__top_layer__name_of_the_dye__icontains=req.get("top_layer_color"))
        elif not condition_6:
            database = Experiment.objects.filter(type_of_stratification__top_layer__layer_height=req.get("top_layer_height")) \
            .filter(type_of_stratification__top_layer__name_of_the_dye__icontains=req.get("top_layer_color"))
        elif not condition_7:
            database = Experiment.objects.filter(type_of_stratification__top_layer__layer_height=req.get("top_layer_height")) \
            .filter(type_of_stratification__top_layer__density_of_water_g_cm_3_field=req.get("top_layer_density"))
        elif condition_8:
            database = Experiment.objects \
            .filter(type_of_stratification__top_layer__layer_height=req.get("top_layer_height")) \
            .filter(type_of_stratification__top_layer__density_of_water_g_cm_3_field=req.get("top_layer_density")) \
            .filter(type_of_stratification__top_layer__name_of_the_dye__icontains=req.get("top_layer_color"))
    elif layers == 2:
        condition_up_1 = req.get("top_layer_height") or req.get("top_layer_density") or req.get("top_layer_color")
        condition_up_2 = req.get("top_layer_density") or req.get("top_layer_color")
        condition_up_3 = req.get("top_layer_height") or req.get("top_layer_color")
        condition_up_4 = req.get("top_layer_height") or req.get("top_layer_density")
        condition_up_5 = req.get("top_layer_height")
        condition_up_6 = req.get("top_layer_density")
        condition_up_7 = req.get("top_layer_color")
        condition_up_8 = req.get("top_layer_height") and req.get("top_layer_density") and req.get("top_layer_color")

        condition_down_1 = req.get("lower_layer_height") or req.get("lower_layer_density") or req.get("lower_layer_color")
        condition_down_2 = req.get("lower_layer_density") or req.get("lower_layer_color")
        condition_down_3 = req.get("lower_layer_height") or req.get("lower_layer_color")
        condition_down_4 = req.get("lower_layer_height") or req.get("lower_layer_density")
        condition_down_5 = req.get("lower_layer_height")
        condition_down_6 = req.get("lower_layer_density")
        condition_down_7 = req.get("lower_layer_color")
        condition_down_8 = req.get("lower_layer_height") and req.get("lower_layer_density") and req.get("lower_layer_color")

        if not (condition_up_1 or condition_down_1):
            database = Experiment.objects.all()
        # Not ended

    return database

def stratification_dam_search(req):
    all_conditions = req.get("wall_coordinate") or req.get("d_layers")

    if all_conditions:
        layers = int(req.get("d_layers"))

        if layers == 1:
            condition_1 = req.get("dam_top_layer_height") or req.get("dam_top_layer_density") or req.get("dam_top_layer_color")
            condition_2 = req.get("dam_top_layer_density") or req.get("dam_top_layer_color")
            condition_3 = req.get("dam_top_layer_height") or req.get("dam_top_layer_color")
            condition_4 = req.get("dam_top_layer_height") or req.get("dam_top_layer_density")
            condition_5 = req.get("dam_top_layer_height")
            condition_6 = req.get("dam_top_layer_density")
            condition_7 = req.get("dam_top_layer_color")
            condition_8 = req.get("dam_top_layer_height") and req.get("dam_top_layer_density") and req.get("dam_top_layer_color")

            if not condition_1:
                database = Experiment.objects.all()
            elif not condition_2:
                database = Experiment.objects.filter(type_of_forming__dam_break__type_of_stratification__top_layer__layer_height=req.get("dam_top_layer_height")) \
                    .filter(type_of_wave__icontains=req.get("wave"))
            elif not condition_3:
                database = Experiment.objects.filter(type_of_forming__dam_break__type_of_stratification__top_layer__density_of_water_g_cm_3_field=req.get("dam_top_layer_density")) \
                    .filter(type_of_wave__icontains=req.get("wave"))
            elif not condition_4:
                database = Experiment.objects.filter(type_of_forming__dam_break__type_of_stratification__top_layer__name_of_the_dye__icontains=req.get("dam_top_layer_color")) \
                    .filter(type_of_wave__icontains=req.get("wave"))
            elif not condition_5:
                database = Experiment.objects.filter(type_of_forming__dam_break__type_of_stratification__top_layer__density_of_water_g_cm_3_field=req.get("dam_top_layer_density")) \
                .filter(type_of_forming__dam_break__type_of_stratification__top_layer__name_of_the_dye__icontains=req.get("dam_top_layer_color")) \
                .filter(type_of_wave__icontains=req.get("wave"))
            elif not condition_6:
                database = Experiment.objects.filter(type_of_forming__dam_break__type_of_stratification__top_layer__layer_height=req.get("dam_top_layer_height")) \
                .filter(type_of_forming__dam_break__type_of_stratification__top_layer__name_of_the_dye__icontains=req.get("dam_top_layer_color")) \
                .filter(type_of_wave__icontains=req.get("wave"))
            elif not condition_7:
                database = Experiment.objects.filter(type_of_forming__dam_break__type_of_stratification__top_layer__layer_height=req.get("dam_top_layer_height")) \
                .filter(type_of_forming__dam_break__type_of_stratification__top_layer__density_of_water_g_cm_3_field=req.get("dam_top_layer_density")) \
                .filter(type_of_wave__icontains=req.get("wave"))
            elif condition_8:
                database = Experiment.objects \
                .filter(type_of_forming__dam_break__type_of_stratification__top_layer__layer_height=req.get("dam_top_layer_height")) \
                .filter(type_of_forming__dam_break__type_of_stratification__top_layer__density_of_water_g_cm_3_field=req.get("dam_top_layer_density")) \
                .filter(type_of_forming__dam_break__type_of_stratification__top_layer__name_of_the_dye__icontains=req.get("dam_top_layer_color")) \
                .filter(type_of_wave__icontains=req.get("wave"))
        elif layers == 2:
            condition_up_1 = req.get("dam_top_layer_height") or req.get("dam_top_layer_density") or req.get("dam_top_layer_color")
            condition_up_2 = req.get("dam_top_layer_density") or req.get("dam_top_layer_color")
            condition_up_3 = req.get("dam_top_layer_height") or req.get("dam_top_layer_color")
            condition_up_4 = req.get("dam_top_layer_height") or req.get("dam_top_layer_density")
            condition_up_5 = req.get("dam_top_layer_height")
            condition_up_6 = req.get("dam_top_layer_density")
            condition_up_7 = req.get("dam_top_layer_color")
            condition_up_8 = req.get("dam_top_layer_height") and req.get("dam_top_layer_density") and req.get("dam_top_layer_color")

            condition_down_1 = req.get("dam_lower_layer_height") or req.get("dam_lower_layer_density") or req.get("dam_lower_layer_color")
            condition_down_2 = req.get("dam_lower_layer_density") or req.get("dam_lower_layer_color")
            condition_down_3 = req.get("dam_lower_layer_height") or req.get("dam_lower_layer_color")
            condition_down_4 = req.get("dam_lower_layer_height") or req.get("dam_lower_layer_density")
            condition_down_5 = req.get("dam_lower_layer_height")
            condition_down_6 = req.get("dam_lower_layer_density")
            condition_down_7 = req.get("dam_lower_layer_color")
            condition_down_8 = req.get("dam_lower_layer_height") and req.get("dam_lower_layer_density") and req.get("dam_lower_layer_color")

            if not (condition_up_1 or condition_down_1):
                database = Experiment.objects.all()
            # Not ended
    else:
        layers = int(req.get("d_layers"))

        if layers == 1:
            condition_1 = req.get("dam_top_layer_height") or req.get("dam_top_layer_density") or req.get("dam_top_layer_color")
            condition_2 = req.get("dam_top_layer_density") or req.get("dam_top_layer_color")
            condition_3 = req.get("dam_top_layer_height") or req.get("dam_top_layer_color")
            condition_4 = req.get("dam_top_layer_height") or req.get("dam_top_layer_density")
            condition_5 = req.get("dam_top_layer_height")
            condition_6 = req.get("dam_top_layer_density")
            condition_7 = req.get("dam_top_layer_color")
            condition_8 = req.get("dam_top_layer_height") and req.get("dam_top_layer_density") and req.get("dam_top_layer_color")

            if not condition_1:
                database = Experiment.objects.all()
            elif not condition_2:
                database = Experiment.objects.filter(type_of_forming__dam_break__type_of_stratification__top_layer__layer_height=req.get("dam_top_layer_height"))
            elif not condition_3:
                database = Experiment.objects.filter(type_of_forming__dam_break__type_of_stratification__top_layer__density_of_water_g_cm_3_field=req.get("dam_top_layer_density"))
            elif not condition_4:
                database = Experiment.objects.filter(type_of_forming__dam_break__type_of_stratification__top_layer__name_of_the_dye__icontains=req.get("dam_top_layer_color"))
            elif not condition_5:
                database = Experiment.objects.filter(type_of_forming__dam_break__type_of_stratification__top_layer__density_of_water_g_cm_3_field=req.get("dam_top_layer_density")) \
                .filter(type_of_forming__dam_break__type_of_stratification__top_layer__name_of_the_dye__icontains=req.get("dam_top_layer_color"))
            elif not condition_6:
                database = Experiment.objects.filter(type_of_forming__dam_break__type_of_stratification__top_layer__layer_height=req.get("dam_top_layer_height")) \
                .filter(type_of_forming__dam_break__type_of_stratification__top_layer__name_of_the_dye__icontains=req.get("dam_top_layer_color"))
            elif not condition_7:
                database = Experiment.objects.filter(type_of_forming__dam_break__type_of_stratification__top_layer__layer_height=req.get("dam_top_layer_height")) \
                .filter(type_of_forming__dam_break__type_of_stratification__top_layer__density_of_water_g_cm_3_field=req.get("dam_top_layer_density"))
            elif condition_8:
                database = Experiment.objects \
                .filter(type_of_forming__dam_break__type_of_stratification__top_layer__layer_height=req.get("dam_top_layer_height")) \
                .filter(type_of_forming__dam_break__type_of_stratification__top_layer__density_of_water_g_cm_3_field=req.get("dam_top_layer_density")) \
                .filter(type_of_forming__dam_break__type_of_stratification__top_layer__name_of_the_dye__icontains=req.get("dam_top_layer_color"))
        elif layers == 2:
            condition_up_1 = req.get("dam_top_layer_height") or req.get("dam_top_layer_density") or req.get("dam_top_layer_color")
            condition_up_2 = req.get("dam_top_layer_density") or req.get("dam_top_layer_color")
            condition_up_3 = req.get("dam_top_layer_height") or req.get("dam_top_layer_color")
            condition_up_4 = req.get("dam_top_layer_height") or req.get("dam_top_layer_density")
            condition_up_5 = req.get("dam_top_layer_height")
            condition_up_6 = req.get("dam_top_layer_density")
            condition_up_7 = req.get("dam_top_layer_color")
            condition_up_8 = req.get("dam_top_layer_height") and req.get("dam_top_layer_density") and req.get("dam_top_layer_color")

            condition_down_1 = req.get("dam_lower_layer_height") or req.get("dam_lower_layer_density") or req.get("dam_lower_layer_color")
            condition_down_2 = req.get("dam_lower_layer_density") or req.get("dam_lower_layer_color")
            condition_down_3 = req.get("dam_lower_layer_height") or req.get("dam_lower_layer_color")
            condition_down_4 = req.get("dam_lower_layer_height") or req.get("dam_lower_layer_density")
            condition_down_5 = req.get("dam_lower_layer_height")
            condition_down_6 = req.get("dam_lower_layer_density")
            condition_down_7 = req.get("dam_lower_layer_color")
            condition_down_8 = req.get("dam_lower_layer_height") and req.get("dam_lower_layer_density") and req.get("dam_lower_layer_color")

            if not (condition_up_1 or condition_down_1):
                database = Experiment.objects.all()
            # Not ended


    return database

def wave_forming_search(req):

    if req.get("wave") == "Поверхностная":
        forming = req.get("surf_form")
        if not forming:
            database = Experiment.objects.filter(type_of_wave__icontains=req.get("wave"))
        elif forming == "Волнопродуктор":
            amplitude = req.get("amplitude")
            quantity = req.get("quantity")
            frequency = req.get("frequency")
            operatingtime = req.get("operatingtime")
            thickness = req.get("thickness")

            all_ = amplitude or quantity or frequency or operatingtime or thickness
            all_except_amplitude = quantity or frequency or operatingtime or thickness
            all_except_quantity = amplitude or frequency or operatingtime or thickness
            all_except_frequency = amplitude or quantity or operatingtime or thickness
            all_except_operatingtime = amplitude or quantity or frequency or thickness
            all_except_thickness = amplitude or quantity or frequency or operatingtime

            all__ = amplitude and quantity and frequency and operatingtime and thickness
            amplitude_quantity = amplitude and quantity
            amplitude_frequency = amplitude and frequency
            amplitude_operatingtime = amplitude and operatingtime
            amplitude_thickness = amplitude and thickness
            quantity_frequency = quantity and frequency
            quantity_operatingtime = quantity and operatingtime
            quantity_thickness = quantity and thickness
            frequency_operatingtime = frequency and operatingtime
            frequency_thickness = frequency and thickness
            operatingtime_thickness = operatingtime and thickness

            amplitude_quantity_frequency = amplitude and quantity and frequency
            amplitude_quantity_operatingtime = amplitude and quantity and operatingtime
            amplitude_quantity_thickness = amplitude and quantity and thickness
            quantity_frequency_operatingtime = quantity and frequency and operatingtime
            quantity_frequency_thickness = quantity and frequency and thickness
            frequency_operatingtime_thickness = frequency and operatingtime and thickness



            if operatingtime:
                operatingtime = "00:" + operatingtime

            if not all_:
                database = Experiment.objects.all()
            elif all__:
                database = Experiment.objects \
                    .filter(type_of_forming__wave_maker__amplitude=amplitude) \
                    .filter(type_of_forming__wave_maker__quantity_of_waves=quantity) \
                    .filter(type_of_forming__wave_maker__frequency=frequency) \
                    .filter(type_of_forming__wave_maker__operating_time=operatingtime) \
                    .filter(type_of_forming__wave_maker__water_height=thickness)
            elif not all_except_amplitude:
                database = Experiment.objects.filter(type_of_forming__wave_maker__amplitude=amplitude)
            elif not all_except_quantity:
                database = Experiment.objects.filter(type_of_forming__wave_maker__quantity_of_waves=quantity)
            elif not all_except_frequency:
                database = Experiment.objects.filter(type_of_forming__wave_maker__frequency=frequency)
            elif not all_except_operatingtime:
                database = Experiment.objects.filter(type_of_forming__wave_maker__operating_time=operatingtime)
            elif not all_except_thickness:
                database = Experiment.objects.filter(type_of_forming__wave_maker__water_height=thickness)
            elif amplitude_quantity_frequency:
                database = Experiment.objects \
                    .filter(type_of_forming__wave_maker__amplitude=amplitude) \
                    .filter(type_of_forming__wave_maker__quantity_of_waves=quantity) \
                    .filter(type_of_forming__wave_maker__frequency=frequency)
            elif amplitude_quantity_operatingtime:
                database = Experiment.objects \
                    .filter(type_of_forming__wave_maker__amplitude=amplitude) \
                    .filter(type_of_forming__wave_maker__quantity_of_waves=quantity) \
                    .filter(type_of_forming__wave_maker__operating_time=operatingtime)
            elif amplitude_quantity_thickness:
                database = Experiment.objects \
                    .filter(type_of_forming__wave_maker__amplitude=amplitude) \
                    .filter(type_of_forming__wave_maker__quantity_of_waves=quantity) \
                    .filter(type_of_forming__wave_maker__water_height=thickness)
            elif quantity_frequency_operatingtime:
                database = Experiment.objects \
                    .filter(type_of_forming__wave_maker__quantity_of_waves=quantity) \
                    .filter(type_of_forming__wave_maker__frequency=frequency) \
                    .filter(type_of_forming__wave_maker__operating_time=operatingtime)
            elif quantity_frequency_thickness:
                database = Experiment.objects \
                    .filter(type_of_forming__wave_maker__quantity_of_waves=quantity) \
                    .filter(type_of_forming__wave_maker__frequency=frequency) \
                    .filter(type_of_forming__wave_maker__water_height=thickness)
            elif frequency_operatingtime_thickness:
                database = Experiment.objects \
                    .filter(type_of_forming__wave_maker__frequency=frequency) \
                    .filter(type_of_forming__wave_maker__operating_time=operatingtime) \
                    .filter(type_of_forming__wave_maker__water_height=thickness)
            elif amplitude_quantity:
                database = Experiment.objects \
                    .filter(type_of_forming__wave_maker__amplitude=amplitude) \
                    .filter(type_of_forming__wave_maker__quantity_of_waves=quantity)
            elif amplitude_frequency:
                database = Experiment.objects \
                    .filter(type_of_forming__wave_maker__amplitude=amplitude) \
                    .filter(type_of_forming__wave_maker__frequency=frequency)
            elif amplitude_operatingtime:
                database = Experiment.objects \
                    .filter(type_of_forming__wave_maker__amplitude=amplitude) \
                    .filter(type_of_forming__wave_maker__operating_time=operatingtime)
            elif amplitude_thickness:
                database = Experiment.objects \
                    .filter(type_of_forming__wave_maker__amplitude=amplitude) \
                    .filter(type_of_forming__wave_maker__water_height=thickness)
            elif quantity_frequency:
                database = Experiment.objects \
                    .filter(type_of_forming__wave_maker__quantity_of_waves=quantity) \
                    .filter(type_of_forming__wave_maker__frequency=frequency)
            elif quantity_operatingtime:
                database = Experiment.objects \
                    .filter(type_of_forming__wave_maker__quantity_of_waves=quantity) \
                    .filter(type_of_forming__wave_maker__operating_time=operatingtime)
            elif quantity_thickness:
                database = Experiment.objects \
                    .filter(type_of_forming__wave_maker__quantity_of_waves=quantity) \
                    .filter(type_of_forming__wave_maker__water_height=thickness)
            elif frequency_operatingtime:
                database = Experiment.objects \
                    .filter(type_of_forming__wave_maker__frequency=frequency) \
                    .filter(type_of_forming__wave_maker__operating_time=operatingtime)
            elif frequency_thickness:
                database = Experiment.objects \
                    .filter(type_of_forming__wave_maker__frequency=frequency) \
                    .filter(type_of_forming__wave_maker__water_height=thickness)
            elif operatingtime_thickness:
                database = Experiment.objects \
                   .filter(type_of_forming__wave_maker__operating_time=operatingtime) \
                    .filter(type_of_forming__wave_maker__water_height=thickness)
            
    elif req.get("wave") == "Внутренняя":
        all_conditions = req.get("wall_coordinate") or req.get("d_layers")
        wall = req.get("wall_coordinate")
        layers = req.get("d_layers")

        if not all_conditions:
            database = Experiment.objects.filter(type_of_wave__icontains=req.get("wave"))
        elif all_conditions:
            database = stratification_dam_search(req)
        elif not layers:
            database = Experiment.objects \
            .filter(type_of_wave__icontains=req.get("wave")) \
            .filter(type_of_forming__dam_break__wall_coordinate=wall)
        elif not wall:
            database = stratification_dam_search(req)

    return database

def laser_search(req):
    all_ =  req.get("laser_coordinate") or req.get("laser_angle")
    all__ = req.get("laser_coordinate") and req.get("laser_angle")

    if not all_:
        database = Experiment.objects.all()
    elif all__:
        database = Experiment.objects \
            .filter(laser__laser_coordinate=req.get("laser_coordinate")) \
            .filter(laser__viewing_angle=req.get("laser_angle"))
    elif req.get("laser_angle"):
        database = Experiment.objects.filter(laser__viewing_angle=req.get("laser_angle"))
    elif req.get("laser_coordinate"):
        database = Experiment.objects.filter(laser__laser_coordinate=req.get("laser_coordinate"))


    return database

def ex_sett_search(req):
    all_ = req.get("obstacle_coordinate") or req.get("obstacle_height") or req.get("type_of_particles")
    all__ = req.get("obstacle_coordinate") and req.get("obstacle_height") and req.get("type_of_particles")
    all_except_coordinate = req.get("obstacle_height") or req.get("type_of_particles")
    all_except_height = req.get("obstacle_coordinate") or req.get("type_of_particles")
    all_except_type = req.get("obstacle_coordinate") or req.get("obstacle_height")
    coordinate_heght = req.get("obstacle_coordinate") and req.get("obstacle_height")
    coordinate_type = req.get("obstacle_coordinate") and req.get("type_of_particles")
    heght_type = req.get("obstacle_height") and req.get("type_of_particles")

    if not all_:
        database = Experiment.objects.all()
    elif all__:
        database = Experiment.objects \
            .filter(types_of_experiment__spread_over_an_obstacle__obstacle_coordinate=req.get("obstacle_coordinate")) \
            .filter(types_of_experiment__spread_over_an_obstacle__obstacle_height=req.get("obstacle_height")) \
            .filter(types_of_experiment__particles_on_the_surface__type_of_particles__icontains=req.get("type_of_particles"))
    elif not all_except_coordinate:
        database = Experiment.objects.filter(types_of_experiment__spread_over_an_obstacle__obstacle_coordinate=req.get("obstacle_coordinate"))
    elif not all_except_height:
        database = Experiment.objects.filter(types_of_experiment__spread_over_an_obstacle__obstacle_height=req.get("obstacle_height"))
    elif not all_except_type:
        database = Experiment.objects.filter(types_of_experiment__particles_on_the_surface__type_of_particles__icontains=req.get("type_of_particles"))
    elif coordinate_heght:
        database = Experiment.objects \
            .filter(types_of_experiment__spread_over_an_obstacle__obstacle_coordinate=req.get("obstacle_coordinate")) \
            .filter(types_of_experiment__spread_over_an_obstacle__obstacle_height=req.get("obstacle_height"))
    elif coordinate_type:
        database = Experiment.objects \
            .filter(types_of_experiment__spread_over_an_obstacle__obstacle_coordinate=req.get("obstacle_coordinate")) \
            .filter(types_of_experiment__particles_on_the_surface__type_of_particles__icontains=req.get("type_of_particles"))
    elif heght_type:
        database = Experiment.objects \
            .filter(types_of_experiment__spread_over_an_obstacle__obstacle_height=req.get("obstacle_height")) \
            .filter(types_of_experiment__particles_on_the_surface__type_of_particles__icontains=req.get("type_of_particles"))

    return database

def search(request):
    req = request.POST
    print(req)
    all_except_id = req.get("datetime_point1") or req.get("datetime_point2") \
        or req.get("duration_of_exp_point1") or req.get("duration_of_exp_point2") \
        or req.get("title") or req.get("bottom") or req.get("polarity") \
        or req.get("layers") or req.get("wave") or req.get("laser") \
        or req.get("ex_sett")

    all_except_datetime = req.get("id") or req.get("duration_of_exp_point1") \
        or req.get("duration_of_exp_point2") or req.get("title") \
        or req.get("bottom") or req.get("polarity") or req.get("layers") \
        or req.get("wave") or req.get("laser") or req.get("ex_sett")

    all_except_duration_of_exp = req.get("id") or req.get("datetime_point1") \
        or req.get("datetime_point2") or req.get("title") or req.get("bottom") \
        or req.get("polarity") or req.get("layers") or req.get("wave") \
        or req.get("laser") or req.get("ex_sett")

    all_except_title = req.get("id") or req.get("datetime_point1") \
        or req.get("datetime_point2") or req.get("duration_of_exp_point1") \
        or req.get("duration_of_exp_point2") or req.get("bottom") \
        or req.get("polarity") or req.get("layers") or req.get("wave") \
        or req.get("laser") or req.get("ex_sett")

    all_except_bottom = req.get("id") or req.get("datetime_point1") \
        or req.get("datetime_point2") or req.get("duration_of_exp_point1") \
        or req.get("duration_of_exp_point2") or req.get("title") or req.get("polarity") \
        or req.get("layers") or req.get("wave") or req.get("laser") or req.get("ex_sett")

    all_except_polarity = req.get("id") or req.get("datetime_point1") or req.get("datetime_point2") \
        or req.get("duration_of_exp_point1") or req.get("duration_of_exp_point2") \
        or req.get("title") or req.get("bottom") or req.get("layers") or req.get("wave") \
        or req.get("laser") or req.get("ex_sett")

    all_except_layers = req.get("id") or req.get("datetime_point1") or req.get("datetime_point2") \
        or req.get("duration_of_exp_point1") or req.get("duration_of_exp_point2") \
        or req.get("title") or req.get("bottom") or req.get("polarity") \
        or req.get("wave") or req.get("laser")  or req.get("ex_sett")

    all_except_wave = req.get("id") or req.get("datetime_point1") or req.get("datetime_point2") \
        or req.get("duration_of_exp_point1") or req.get("duration_of_exp_point2") \
        or req.get("title") or req.get("bottom") or req.get("polarity") or req.get("layers") \
        or req.get("laser") or req.get("ex_sett")

    all_except_laser = req.get("id") or req.get("datetime_point1") or req.get("datetime_point2") \
        or req.get("duration_of_exp_point1") or req.get("duration_of_exp_point2") \
        or req.get("title") or req.get("bottom") or req.get("polarity") or req.get("layers") \
        or req.get("wave") or req.get("ex_sett")

    all_except_ex_sett = req.get("id") or req.get("datetime_point1") or req.get("datetime_point2") \
        or req.get("duration_of_exp_point1") or req.get("duration_of_exp_point2") \
        or req.get("title") or req.get("bottom") or req.get("polarity") or req.get("layers") \
        or req.get("wave") or req.get("laser")

    if (not req.get("id") and not req.get("datetime_point1") and not req.get("datetime_point2") \
        and not req.get("duration_of_exp_point1") and not req.get("duration_of_exp_point2") \
        and not req.get("title") and not req.get("bottom") and not req.get("polarity") \
        and not req.get("layers") and not req.get("wave") and not req.get("laser") \
        and not req.get("ex_sett")) or not req:
        database = Experiment.objects.all()
    else:
        # # database = Experiment.objects.filter(id=id).filter(title_of_exp__icontains=req.get("title"))
        # if not req.get("id") and not req.get("wave"):
        #     database = Experiment.objects.filter(title_of_exp__icontains=req.get("title"))

        # if not req.get("title") and not req.get("wave"):
        #     id = int(req.get("id"))
        #     if (id == 0):
        #         database = Experiment.objects.all()
        #     else:
        #         database = Experiment.objects.filter(id=id)

        # if not req.get("id") and not req.get("title"):
        #     database = Experiment.objects.filter(type_of_wave__icontains=req.get("wave"))

        if not all_except_id:
            id = int(req.get("id"))
            if (id == 0):
                database = Experiment.objects.all()
            else:
                database = Experiment.objects.filter(id=id)
        elif not all_except_datetime:
            database = Experiment.objects.filter(date_and_time__range=[req.get("datetime_point1"),req.get("datetime_point2")])
        elif not all_except_duration_of_exp:
            database = Experiment.objects.filter(duration_of_the_exp__range=[req.get("duration_of_exp_point1"),req.get("duration_of_exp_point2")])
        elif not all_except_title:
            database = Experiment.objects.filter(title_of_exp__icontains=req.get("title"))
        elif not all_except_bottom:
            database = Experiment.objects.filter(type_of_bottom__icontains=req.get("bottom"))
        elif not all_except_polarity:
            database = Experiment.objects.filter(polarity__icontains=req.get("polarity"))
        elif not all_except_layers:
            database = stratification_search(req)
        elif not all_except_wave:
            database = wave_forming_search(req)
        elif not all_except_laser:
            database = laser_search(req)
        elif not all_except_ex_sett:
            database = ex_sett_search(req)




    # if not request.POST.get("id"):
    #     database = Experiment.objects.all()
    # else:
    #     id = int(request.POST.get("id"))
    #     if (id == 0):
    #         database = Experiment.objects.all()
    #     else:
    #         database = Experiment.objects.filter(id=id)
    
    return render(request, "dbapp/index.html", {"database": database})