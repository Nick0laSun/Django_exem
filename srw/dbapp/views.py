from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db.models import Q
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import Serializer
from dbapp.models import Experiment
import datetime
import time
from datetime import timedelta

# from rest_framework import generics
from .models import Experiment, Wavemaker
from .forms import BottomForm, DateAndTimeForm, IdForm, LayerForm, PolarityForm, TimeForm, TitleForm, WaveTypeForm, WavemakerForm
from dbapp import serializers

# class ExperimentBrowsableAPIRenderer(BrowsableAPIRenderer):
#     def experiment_list(request, fromat=None):

#         queryset = Experiment.objects.all()  
#         serializer = ExperimentSerializer(queryset, many=True)
#         return Response(serializer.data)

       
def time_to_str(queryset):
    for point in queryset:
        point.duration_of_the_exp = str(point.duration_of_the_exp)
        try:
            point.type_of_forming.wave_maker.operating_time = str(point.type_of_forming.wave_maker.operating_time)
        except:
            continue
    return queryset

def home(request):
    return render(request, "dbapp/home.html")
    # return HttpResponse("Hello World!")

def test(request):
    return render(request, "test.html")

def search_form(request):
    req = request.POST

    database = Experiment.objects.all()
    choice = req.get("select_data_field")
    if choice == "id":
        form = IdForm()
    elif choice == "title":
        form = TitleForm()
    elif choice == "date_time":
        form = DateAndTimeForm()
    elif choice == "time":
        form = TimeForm()
    elif choice == "bottom":
        form = BottomForm()
    elif choice == "polarity":
        form = PolarityForm()
    elif choice == "wave_type":
        form = WaveTypeForm()
    elif choice == "stratif3":
        form = {
            "mod": 'strat',
            "top_layer": LayerForm(),
            "middle_layer": LayerForm(),
            "lower_layer": LayerForm(),
        }
    elif choice == "stratif2":
        form = {
            "mod": 'strat',
            "top_layer": LayerForm(),
            "lower_layer": LayerForm(),
        }
    elif choice == "stratif1":
        form = {
            "mod": 'strat',
            "top_layer": LayerForm(),
        }
    elif choice == "wave_maker":
        form = {
            "mod": 'wm',
            "wavemaker": WavemakerForm(),
        }

    database = time_to_str(database)
    # print(form)
    return render(request, "dbapp/index.html", {"database": database, "form": form})
    
def search(request):
    req = request.POST

    if req.get('id'):
        if req.get('id') == 0:
            database = Experiment.objects.all()
        else:
            database = Experiment.objects.filter(id=req.get('id'))
    elif req.get('title'):
        database = Experiment.objects.filter(title_of_exp=req.get('title'))
    elif req.get('date_time'):
        try:
            value = time.strptime(req.get('date_time')+':00', "%Y-%m-%d %H:%M:%S")
        except:
            database = Experiment.objects.all()
            database = time_to_str(database)
            return render(request, "dbapp/index.html", {"database": database})
    
        database = Experiment.objects.filter(date_and_time__range=(req.get('date_time')+':00', req.get('date_time')+':59'))
    elif req.get('time'):
        try:
            value = time.strptime(req.get('time'), '%H:%M:%S')
        except:
            database = Experiment.objects.all()
            database = time_to_str(database)
            return render(request, "dbapp/index.html", {"database": database})
    
        database = Experiment.objects.filter(duration_of_the_exp__range=(req.get('time')+'.000', req.get('time')+'.001'))
    elif req.get('bottom'):

        if req.get('bottom') == '0':
            select = 'Нет'
        elif req.get('bottom') == '1':
            select = 'Подводный уступ'
        elif req.get('bottom') == '2':
            select = 'Параболическое дно'

        database = Experiment.objects.filter(type_of_bottom=select)
    elif req.get('polarity'):

        if req.get('polarity') == '+':
            select = 'Положительная'
        else:
            select = 'Отрицательная'

        database = Experiment.objects.filter(polarity=select)
    elif req.get('wave_type'):

        if req.get('wave_type') == '0':
            select = 'Поверхностная'
        else:
            select = 'Внутренняя'

        database = Experiment.objects.filter(type_of_wave=select)
    elif (req.get('amplitude') and req.get('quantity_of_waves') and req.get('frequency') and req.get('water_height')):
        amplitude = float(req.get('amplitude'))
        quantity_of_waves = float(req.get('quantity_of_waves'))
        frequency = float(req.get('frequency'))
        water_height = float(req.get('water_height'))

        database = Experiment.objects.filter(
            Q(type_of_forming__wave_maker__amplitude__range=(amplitude-0.001,amplitude+0.001)) |
            Q(type_of_forming__wave_maker__quantity_of_waves__range=(quantity_of_waves-0.001,quantity_of_waves+0.001)) |
            Q(type_of_forming__wave_maker__frequency__range=(frequency-0.001,frequency+0.001)) |
            Q(type_of_forming__wave_maker__water_height__range=(water_height-0.001,water_height+0.001))
        )
    elif (req.getlist('density')[0] and req.getlist('height')[0]):
        if (len(req.getlist('density')) == 1 or len(req.getlist('height')) == 1):
            density = float(req.getlist('density')[0])
            height = float(req.getlist('height')[0])
            database = Experiment.objects.filter(
                Q(type_of_stratification__top_layer__density_of_water_g_cm_3_field__range=(density-0.001,density+0.001)) |
                Q(type_of_stratification__top_layer__layer_height__range=(height-0.001,height+0.001))
            )
        elif (len(req.getlist('density')) == 2 or len(req.getlist('height')) == 2):
            density_0 = float(req.getlist('density')[0])
            height_0 = float(req.getlist('height')[0])
            density_1 = float(req.getlist('density')[1])
            height_1 = float(req.getlist('height')[1])
            database = Experiment.objects.filter(
                Q(type_of_stratification__top_layer__density_of_water_g_cm_3_field__range=(density_0-0.001,density_0+0.001)) |
                Q(type_of_stratification__top_layer__layer_height__range=(height_0-0.001,height_0+0.001))
            ).filter(
                Q(type_of_stratification__lower_layer__density_of_water_g_cm_3_field__range=(density_1-0.001,density_1+0.001)) |
                Q(type_of_stratification__lower_layer__layer_height__range=(height_1-0.001,height_1+0.001))
            )
        elif (len(req.getlist('density')) == 3 or len(req.getlist('height')) == 3):
            density_0 = float(req.getlist('density')[0])
            height_0 = float(req.getlist('height')[0])
            density_1 = float(req.getlist('density')[1])
            height_1 = float(req.getlist('height')[1])
            density_2 = float(req.getlist('density')[2])
            height_2 = float(req.getlist('height')[2])
            database = Experiment.objects.filter(
                Q(type_of_stratification__top_layer__density_of_water_g_cm_3_field__range=(density_0-0.001,density_0+0.001)) |
                Q(type_of_stratification__top_layer__layer_height__range=(height_0-0.001,height_0+0.001))
            ).filter(
                Q(type_of_stratification__middle_layer__density_of_water_g_cm_3_field__range=(density_1-0.001,density_1+0.001)) |
                Q(type_of_stratification__middle_layer__layer_height__range=(height_1-0.001,height_1+0.001))
            ).filter(
                Q(type_of_stratification__lower_layer__density_of_water_g_cm_3_field__range=(density_2-0.001,density_2+0.001)) |
                Q(type_of_stratification__lower_layer__layer_height__range=(height_2-0.001,height_2+0.001))
            )
    else:
        database = Experiment.objects.all()

    database = time_to_str(database)
    return render(request, "dbapp/index.html", {"database": database})

def detailed_view(request, id):
    database = Experiment.objects.filter(id=id)
    database = time_to_str(database)
    experiment = database[0]

    return render(request, "dbapp/view.html", {"Experiment": experiment})

def index(request):
    database = Experiment.objects.all()
    # print(database[1].duration_of_the_exp)
    database = time_to_str(database)
    return render(request, "dbapp/index.html", {"database": database})
    # header = "Personal Data"
    # langs = ["English", "German", "Spanish"]
    # user = {"name": "Tom", "age": 23}
    # addr = ("Абрикосовая", 23, 45)

    # data = { "header": header, "langs": langs, "user": user, "address": addr }
    # return render(request, "index.html", context=data)
    # # return render(request, "index.html")