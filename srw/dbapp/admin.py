from django.contrib import admin
from django.utils.html import format_html
from django.db.models import Q
from itertools import chain
# from django_reverse_admin import ReverseModelAdmin
from .models import Experiment, Results, Bottomsensorsresults, \
    Stringsensorsresults, Forming, Wavemaker, Dambreak, \
    Typeofstratification, Compositionofwaterlayer, \
    Typesofexperiment, Particlesonthesurface, \
    Spreadoveranobstacle, Laser


def layer_html_compilation(layer, level):
    if not (layer.density_of_water_g_cm_3_field):
        density = '-'
    else:
        density = layer.density_of_water_g_cm_3_field

    if not (layer.name_of_the_dye):
        dye = '-'
    else:
        dye = layer.name_of_the_dye

    if not (layer.layer_height):
        height = '-'
    else:
        height = layer.layer_height

    html_filed = format_html(
            '<b>{0} layer</b> <hr><p>Density of water (g/cm^3): <b>{1}</b> <br> Name of the dye: <b>{2}</b> <br> Water heght: <b>{3}</b></p><hr>',
            level,
            density,
            dye,
            height
        )
    return html_filed

def wave_maker_sett_html_comp(wave_maker):
    if not (wave_maker.amplitude):
        amplitude = '-'
    else:
        amplitude = str(wave_maker.amplitude)

    if not (wave_maker.quantity_of_waves):
        quantity_of_waves = '-'
    else:
        quantity_of_waves = str(wave_maker.quantity_of_waves)

    if not (wave_maker.frequency):
        frequency = '-'
    else:
        frequency = str(wave_maker.frequency)

    if not (wave_maker.operating_time):
        operating_time = '-'
    else:
        operating_time = str(wave_maker.operating_time)

    if not (wave_maker.water_height):
        water_height = '-'
    else:
        water_height = str(wave_maker.water_height)

    html_filed = format_html(
            '<p> Wave apmplitude: <b>{0}</b> <br> Quantity of waves: <b>{1}</b> <br> Frequency: <b>{2}</b> <br> Operating time: <b>{3}</b> <br> Water height: <b>{4}</b> </p>',
            amplitude,
            quantity_of_waves,
            frequency,
            operating_time,
            water_height
        ) 
    return html_filed

def video_ref_html_comp(obj):
    if not (obj.video_reference):
        return "-"
    else:
        return format_html('<a href="{0}">YouTube</a>', obj.video_reference)

def spread_over_an_obstacle_html_comp(obj):
    if not (obj.obstacle_coordinate):
        coordinate = "-"
    else:
        coordinate = obj.obstacle_coordinate

    if not (obj.obstacle_height):
        height = "-"
    else:
        height = obj.obstacle_height

    res = format_html('<p>Obstacle coordinate: {0}</p><p>Obstacle height: {1}</p>',
        str(coordinate), str(height))
        
    return res

def particles_on_the_surface_html_comp(obj):
    if not (obj.type_of_particles):
        particles = "-"
    else:
        particles = obj.type_of_particles
        
    res = format_html('Type of particles: {0}', str(particles))

    return res

def float_params_filter(data_list, search_term_as_float):

    queryset1 = data_list.filter(
        Q(type_of_forming__wave_maker__amplitude__range=(search_term_as_float-0.001,search_term_as_float+0.001)) |
        Q(type_of_forming__wave_maker__quantity_of_waves__range=(search_term_as_float-0.001,search_term_as_float+0.001)) |
        Q(type_of_forming__wave_maker__frequency__range=(search_term_as_float-0.001,search_term_as_float+0.001)) |
        Q(type_of_forming__wave_maker__water_height__range=(search_term_as_float-0.001,search_term_as_float+0.001)) |
        Q(type_of_stratification__top_layer__density_of_water_g_cm_3_field__range=(search_term_as_float-0.001,search_term_as_float+0.001)) |
        Q(type_of_stratification__top_layer__layer_height__range=(search_term_as_float-0.001,search_term_as_float+0.001))
    )

    print(data_list)

    # buffer = data_list.type_of_forming.dam_break.type_of_stratification.top_layer.filter(layer_height__range=(search_term_as_float-0.001,search_term_as_float+0.001)).all()
    # print(buffer)

    queryset2 = data_list.filter(
        Q(type_of_forming__dam_break__wall_coordinate__range=(search_term_as_float-0.001,search_term_as_float+0.001))
        # Q(type_of_forming__dam_break__type_of_stratification__middle_layer__density_of_water_g_cm_3_field__range=(search_term_as_float-0.001,search_term_as_float+0.001)) |
        # Q(type_of_forming__dam_break__type_of_stratification__middle_layer__layer_height__range=(search_term_as_float-0.001,search_term_as_float+0.001)) |
        # Q(type_of_forming__dam_break__type_of_stratification__lower_layer__density_of_water_g_cm_3_field__range=(search_term_as_float-0.001,search_term_as_float+0.001)) |
        # Q(type_of_forming__dam_break__type_of_stratification__lower_layer__layer_height__range=(search_term_as_float-0.001,search_term_as_float+0.001))
    )

    queryset3 = data_list.filter(
        Q(type_of_stratification__top_layer__density_of_water_g_cm_3_field__range=(search_term_as_float-0.001,search_term_as_float+0.001)) |
        Q(type_of_stratification__top_layer__layer_height__range=(search_term_as_float-0.001,search_term_as_float+0.001))
    )

    queryset4 = data_list.filter(
        Q(type_of_stratification__middle_layer__density_of_water_g_cm_3_field__range=(search_term_as_float-0.001,search_term_as_float+0.001)) |
        Q(type_of_stratification__middle_layer__layer_height__range=(search_term_as_float-0.001,search_term_as_float+0.001))
    )

    queryset5 = data_list.filter(
        Q(type_of_stratification__lower_layer__density_of_water_g_cm_3_field__range=(search_term_as_float-0.001,search_term_as_float+0.001)) |
        Q(type_of_stratification__lower_layer__layer_height__range=(search_term_as_float-0.001,search_term_as_float+0.001))
    )

    queryset6 = data_list.filter(
        Q(types_of_experiment__spread_over_an_obstacle__obstacle_coordinate__range=(search_term_as_float-0.001,search_term_as_float+0.001)) |
        Q(types_of_experiment__spread_over_an_obstacle__obstacle_height__range=(search_term_as_float-0.001,search_term_as_float+0.001))
    )

    queryset7 = data_list.filter(
        Q(laser__laser_coordinate__range=(search_term_as_float-0.001,search_term_as_float+0.001)) |
        Q(laser__viewing_angle__range=(search_term_as_float-0.001,search_term_as_float+0.001))
    )

    queryset = data_list.none()

    if queryset1:
        queryset1 = queryset1.order_by('id')
        queryset |= queryset1

    if queryset2:
        queryset2 = queryset2.order_by('id')
        queryset |= queryset2

    if queryset3:
        queryset3 = queryset3.order_by('id')
        queryset |= queryset3

    if queryset4:
        queryset4 = queryset4.order_by('id')
        queryset |= queryset4
    
    if queryset5:
        queryset5 = queryset5.order_by('id')
        queryset |= queryset5
    
    if queryset6:
        queryset6 = queryset6.order_by('id')
        queryset |= queryset6

    if queryset7:
        queryset7 = queryset7.order_by('id')
        queryset |= queryset7

    # queryset = queryset1 | queryset3
    print(queryset)
    print(queryset1)
    print(queryset2)
    print(queryset3)
    print(queryset4)
    print(queryset5)
    print(queryset6)
    print(queryset7)

    return queryset


# Register your models here.

class DamBreakAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'wall_coordinate',
        'top_layer_sett', 
        'middle_layer_sett', 
        'lower_layer_sett', 
        'all_layers_sett'
    )

    ordering = ['id']

    def all_layers_sett(self, obj):
        all_ls = '__Top layer__\n' + \
                'Density of water (g/cm^3): ' + str(obj.type_of_stratification.top_layer.density_of_water_g_cm_3_field) + '\n' + \
                'Name of the dye: ' + obj.type_of_stratification.top_layer.name_of_the_dye + '\n' + \
                'Water heght: ' + str(obj.type_of_stratification.top_layer.layer_height) + '\n' + \
                '__Middle layer__\n' + \
                'Density of water (g/cm^3): ' + str(obj.type_of_stratification.middle_layer.density_of_water_g_cm_3_field) + '\n' + \
                'Name of the dye: ' + obj.type_of_stratification.middle_layer.name_of_the_dye + '\n' + \
                'Water heght: ' + str(obj.type_of_stratification.middle_layer.layer_height) + '\n' + \
                '__Lower layer__\n' + \
                'Density of water (g/cm^3): ' + str(obj.type_of_stratification.lower_layer.density_of_water_g_cm_3_field) + '\n' + \
                'Name of the dye: ' + obj.type_of_stratification.lower_layer.name_of_the_dye + '\n' + \
                'Water heght: ' + str(obj.type_of_stratification.lower_layer.layer_height)
        return all_ls
    all_layers_sett.short_description = 'All laeyrs'

    def top_layer_sett(self, obj):
        top_layer = obj.type_of_stratification.top_layer
        field = layer_html_compilation(top_layer, 'Top')
        return field
    top_layer_sett.short_description = 'Top layer'

    def middle_layer_sett(self, obj):
        middle_layer = obj.type_of_stratification.middle_layer
        field = layer_html_compilation(middle_layer, 'Middle')
        return field
    middle_layer_sett.short_description = 'Middle Layer'

    def lower_layer_sett(self, obj):
        lower_layer = obj.type_of_stratification.lower_layer
        field = layer_html_compilation(lower_layer, 'Lower')
        return field
    lower_layer_sett.short_description = 'Lower layer'

class WavemakerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'amplitude',
        'quantity_of_waves',
        'frequency',
        'operating_time_f',
        'water_height'
    )

    ordering = ['id']

    def operating_time_f(self, obj):
        if not (obj.operating_time):
            return '-'
        else:
            return str(obj.operating_time)
    operating_time_f.short_description = 'OPERATING TIME'

    # pass

class FormingAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'wave_maker_f', 
        'dam_wall_coordinate', 
        'dam_top_layer_settings',
        'dam_middle_layer_settings',
        'dam_lower_layer_settings')

    ordering = ['id']

    def wave_maker_f(self, obj):
        wave_maker = obj.wave_maker
        html_data = wave_maker_sett_html_comp(wave_maker)

        return html_data
    wave_maker_f.short_description = 'Wavemaker'

    def dam_wall_coordinate(self, obj):
        dwc = 'Wall coordinate: ' + str(obj.dam_break.wall_coordinate)
        return dwc
    dam_wall_coordinate.short_description = 'Dam wall coordinate'

    def dam_top_layer_settings(self, obj):
        top_layer = obj.dam_break.type_of_stratification.top_layer
        field = layer_html_compilation(top_layer, 'Top')
        return field
    dam_top_layer_settings.short_description = 'Dam break top layer'

    def dam_middle_layer_settings(self, obj):
        middle_layer = obj.dam_break.type_of_stratification.middle_layer
        field = layer_html_compilation(middle_layer, 'Middle')
        return field
    dam_middle_layer_settings.short_description = 'Dam break middle layer'

    def dam_lower_layer_settings(self, obj):
        lower_layer = obj.dam_break.type_of_stratification.lower_layer
        field = layer_html_compilation(lower_layer, 'Lower')
        return field
    dam_lower_layer_settings.short_description = 'Dam break lower layer'

class LaserAdmin(admin.ModelAdmin):
    list_display = ('id', 'video_ref', 'laser_coordinate', 'viewing_angle')

    orering = ['id']

    def video_ref(self, obj):
        # if not (obj.video_reference):
        #     return "-"
        # else:
        #     return format_html('<a href="{0}">YouTube</a>', obj.video_reference)
        res = video_ref_html_comp(obj)
        return res

    video_ref.short_description = 'Video reference'

class ParticlesonthesurfaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_of_particles')
    
    ordering = ['id']

class SpreadoveranobstacleAdmin(admin.ModelAdmin):
    list_display = ('id', 'obstacle_coordinate', 'obstacle_height')

    ordering = ['id']

class TypesofexperimentAdmin(admin.ModelAdmin):
    list_display = ('id', 'spread_over_an_obstacle_f', 'particles_on_the_surface_f')

    ordering = ['id']

    def spread_over_an_obstacle_f(self, obj):
        res = spread_over_an_obstacle_html_comp(obj.spread_over_an_obstacle)

        return res
    spread_over_an_obstacle_f.short_description = 'spread over an obstacle'

    def particles_on_the_surface_f(self, obj):
        res = particles_on_the_surface_html_comp(obj.particles_on_the_surface)

        return res
    particles_on_the_surface_f.short_description = 'particles on the surface'

class ExperimentAdmin(admin.ModelAdmin):


    list_display = ('id', 'date_and_time', 'duration_of_exp', 'title_of_exp', 'type_of_bottom', 'video_ref', \
        'string_sensors_results', 'bottom_sensors_results', 'schema_of_exp', \
        'wavemaker_settings', \
        'dam_wall_coordinate', 'dam_top_layer_settings', 'dam_middle_layer_settings', 'dam_lower_layer_settings', \
        'stratification_top_layer_sett', 'stratification_middle_layer_sett', 'stratification_lower_layer_sett', \
        'type_of_wave', \
        'polarity', 'laser_settings', 'spread_over_an_obstacle', 'particles' \
    )

    list_filter = (
        'title_of_exp', 
        'type_of_bottom', 
        'type_of_wave', 'polarity',
        'type_of_forming__wave_maker__amplitude', 
        'type_of_forming__wave_maker__quantity_of_waves',
        'type_of_forming__wave_maker__frequency',
        'type_of_forming__wave_maker__water_height',
        'type_of_forming__dam_break__wall_coordinate'
        )
    
    date_hierarchy = 'date_and_time'

    ordering = ['id']

    search_fields = ['id']

    def get_search_results(self, request, queryset, search_term):
        
        try:
            search_term_as_float = float(search_term)
        except ValueError:
            pass
        else:
            data_list = self.model.objects
            queryset = float_params_filter(data_list, search_term_as_float)

        return super().get_search_results(request, queryset, '')

    fieldsets = (
        (None,{
            'fields': (
                'date_and_time', 
                'title_of_exp', 
                'type_of_bottom', 
                'video_reference',
                'result',
                'schema_of_exp_reference',
                'type_of_forming',
                'type_of_wave', 
                'duration_of_the_exp',
                'type_of_stratification',
                'polarity',
                'laser',
                'types_of_experiment'
            )
        }),
        # ('Results',{
        #     'fields': (
        #         'result__bottom_sensors__results',
        #         'result__string_sensors__results'
        #     )
        # })
        # ('Laser',{
        #     # 'fields': (
        #     #     'laser__video_reference',
        #     #     'laser__laser_coordinate',
        #     #     'laser__viewing_angle'
        #     # )
        # })
    )

    def duration_of_exp(self, obj):
        return str(obj.duration_of_the_exp)
    duration_of_exp.short_description = 'Duration of exp.'

    def video_ref(self, obj):
        res = video_ref_html_comp(obj)
        return res
    video_ref.short_description = 'Video reference'

    def schema_of_exp(self, obj):
        if not (obj.schema_of_exp_reference):
            return "No data"
        else:
            return format_html('<a href="{0}">Shema</a>', obj.schema_of_exp_reference)
    schema_of_exp.short_description = 'Shema of the experiment'

    def string_sensors_results(self, obj):
        if not (obj.result.string_sensors.resistive_sensors_res):
            return format_html('<a href="{0}">Capasitive sensors results</a>', obj.result.string_sensors.capasitive_sensors_res)
        elif not (obj.result.string_sensors.capasitive_sensors_res):
            return format_html('<a href="{0}">Resistive sensors results</a>', obj.result.string_sensors.resistive_sensors_res)
        elif not (obj.result.string_sensors.capasitive_sensors_res and obj.result.string_sensors.resistive_sensors_res):
            return 'No data'
        elif (obj.result.string_sensors.capasitive_sensors_res and obj.result.string_sensors.resistive_sensors_res):
            return format_html('<a href="{0}">Resistive sensors results</a><hr><a href="{1}">Capasitive sensors results</a>', obj.result.string_sensors.resistive_sensors_res, obj.result.string_sensors.capasitive_sensors_res)
    string_sensors_results.short_description = 'String sensors results'

    def bottom_sensors_results(self, obj):
        return format_html('<a href="{0}">Bottom sensors</a>', obj.result.bottom_sensors.results)
    bottom_sensors_results.short_description = 'Bottom sensors results'

    def wavemaker_settings(self, obj):
        wave_maker = obj.type_of_forming.wave_maker
        html_data = wave_maker_sett_html_comp(wave_maker)

        return html_data
    wavemaker_settings.short_description = 'Wavemaker'

    def dam_break_experiment_settings(self, obj):
        dam_break = obj.type_of_forming.dam_break
        if (dam_break):
            type_of_stratification = dam_break.type_of_stratification
            if (dam_break.wall_coordinate):
                fields = format_html('<p>Wall coordinate: "{0}"</p>', obj.type_of_forming.dam_break.wall_coordinate)
            if (type_of_stratification):
                top_layer = type_of_stratification.top_layer
                # middle_layer = type_of_stratification.middle_layer
                # lower_layer = type_of_stratification.lower_layer
                if (top_layer):
                    fields += layer_html_compilation(top_layer, "Top")
                    # if (lower_layer):
                    fields += format_html('<p>proverka svyazi</p>')         
        return fields
    dam_break_experiment_settings.shortdescription = 'Dam break settings'

    def dam_wall_coordinate(self, obj):
        dwc = 'Wall coordinate: ' + str(obj.type_of_forming.dam_break.wall_coordinate)
        return dwc
    dam_wall_coordinate.short_description = 'Dam wall coordinate'

    def dam_top_layer_settings(self, obj):
        top_layer = obj.type_of_forming.dam_break.type_of_stratification.top_layer
        field = layer_html_compilation(top_layer, 'Top')
        return field
    dam_top_layer_settings.short_description = 'Dam break top layer'

    def dam_middle_layer_settings(self, obj):
        middle_layer = obj.type_of_forming.dam_break.type_of_stratification.middle_layer
        field = layer_html_compilation(middle_layer, 'Middle')
        return field
    dam_middle_layer_settings.short_description = 'Dam break middle layer'

    def dam_lower_layer_settings(self, obj):
        lower_layer = obj.type_of_forming.dam_break.type_of_stratification.lower_layer
        field = layer_html_compilation(lower_layer, 'Lower')
        return field
    dam_lower_layer_settings.short_description = 'Dam break lower layer'

    def stratification_top_layer_sett(self, obj):
        top_layer = obj.type_of_stratification.top_layer
        field = layer_html_compilation(top_layer, 'Top')
        return field
    stratification_top_layer_sett.short_description = 'Stratification top layer'

    def stratification_middle_layer_sett(self, obj):
        middle_layer = obj.type_of_stratification.middle_layer
        field = layer_html_compilation(middle_layer, 'Middle')
        return field
    stratification_middle_layer_sett.short_description = 'Stratification middle layer'

    def stratification_lower_layer_sett(self, obj):
        lower_layer = obj.type_of_stratification.lower_layer
        field = layer_html_compilation(lower_layer, 'Lower')
        return field
    stratification_lower_layer_sett.short_description = 'Stratification lower layer'

    def laser_settings(self, obj):
        if not (obj.laser.laser_coordinate):
            coordinate = "-"
        else:
            coordinate = obj.laser.laser_coordinate

        if not (obj.laser.viewing_angle):
            angle = "-"
        else:
            angle = obj.laser.viewing_angle

        video = video_ref_html_comp(obj.laser)

        res = format_html(
            '<p>Laser coord.: {0}</p><p>Viewing angle: {1}</p><p>Video ref: {2}',
            str(coordinate),
            str(angle),
            video
        )

        return res 
    laser_settings.short_description = 'Laser'

    def spread_over_an_obstacle(self, obj):
        res = spread_over_an_obstacle_html_comp(obj.types_of_experiment.spread_over_an_obstacle)

        return res
    spread_over_an_obstacle.short_description = 'Spread over an obstacle'

    def particles(self, obj):
        res = particles_on_the_surface_html_comp(obj.types_of_experiment.particles_on_the_surface)
        return res
    particles.short_description = 'Particles on the surface'

class BottomsensorsresultsAdmin(admin.ModelAdmin):
    list_display = ('id', 'results_f')

    ordering = ['id']

    def results_f(self, obj):
        if not (obj.results):
            return 'No data'
        else:
            return format_html('<a href="{0}">Bottom sensors</a>', obj.results)
    results_f.short_description = 'Bottom sens. res.'        

class StringSensorsResultsAdmin(admin.ModelAdmin):
    # fields = (
    #     'capasitive_sensors_res',
    #     'resistive_sensors_res'
    # )

    list_display = ('id', 'capasitive_sensors_res_f', 'resistive_sensors_res_f')

    ordering = ['id']

    def capasitive_sensors_res_f(self, obj):
        if not (obj.capasitive_sensors_res):
            return 'No data'
        else:
            return format_html('<a href="{0}">Capasitive sensors results</a>', obj.capasitive_sensors_res)
    capasitive_sensors_res_f.short_description = 'Capacitive sens. res.'

    def resistive_sensors_res_f(self, obj):
        if not (obj.resistive_sensors_res):
            return 'No data'
        else:
            return format_html('<a href="{0}">Resistive sensors results</a>', obj.resistive_sensors_res)

class ResultsAdmin(admin.ModelAdmin):
    list_display = ('id', 'bottom_sensors_res', 'string_sensors_res')

    ordering = ['id']

    fields = (
        'bottom_sensors',
        'string_sensors'
    )

    def bottom_sensors_res(self, obj):
        if not (obj.bottom_sensors.results):
            return 'No data'
        else:
            return format_html('<a href="{0}">Bottom sensors</a>', obj.bottom_sensors.results)
    bottom_sensors_res.short_description = 'Bottom sens. res.'

    def string_sensors_res(self, obj):
        if not (obj.string_sensors.resistive_sensors_res):
            return format_html('<a href="{0}">Capasitive sensors results</a>', obj.string_sensors.capasitive_sensors_res)
        elif not (obj.string_sensors.capasitive_sensors_res):
            return format_html('<a href="{0}">Resistive sensors results</a>', obj.string_sensors.resistive_sensors_res)
        elif not (obj.string_sensors.capasitive_sensors_res and obj.string_sensors.resistive_sensors_res):
            return 'No data'
        elif (obj.string_sensors.capasitive_sensors_res and obj.string_sensors.resistive_sensors_res):
            return format_html('<a href="{0}">Resistive sensors results</a><hr><a href="{1}">Capasitive sensors results</a>', obj.string_sensors.resistive_sensors_res, obj.string_sensors.capasitive_sensors_res)
    string_sensors_res.short_description = 'String sens. res.'

    # pass

class CompositionofwaterlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'density_of_water', 'name_of_the_dye_f', 'layer_height_f')

    ordering = ['id']

    fields = (
        'density_of_water_g_cm_3_field',
        'name_of_the_dye',
        'layer_height'
    )

    def density_of_water(self, obj):
        if not (obj.density_of_water_g_cm_3_field):
            return 'No data'
        else:
            return obj.density_of_water_g_cm_3_field
    density_of_water.short_description = 'Density of water layer (g/cm^3)'

    def name_of_the_dye_f(self, obj):
        if not (obj.name_of_the_dye):
            return 'No data'
        else:
            return obj.name_of_the_dye
    name_of_the_dye_f.short_description = 'Name of the dye'

    def layer_height_f(self, obj):
        if not (obj.layer_height):
            return 'No data'
        else:
            return obj.layer_height
    layer_height_f.short_description = 'Layer height'

class TypeofstratificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'top_layer_sett', 'middle_layer_sett', 'lower_layer_sett')

    ordering = ['id']

    fields = (
        'top_layer',
        'middle_layer',
        'lower_layer'
    )

    def top_layer_sett(self, obj):
        top_layer = obj.top_layer
        field = layer_html_compilation(top_layer, 'Top')
        return field
    top_layer_sett.short_description = 'Stratification top layer'

    def middle_layer_sett(self, obj):
        middle_layer = obj.middle_layer
        field = layer_html_compilation(middle_layer, 'Middle')
        return field
    middle_layer_sett.short_description = 'Stratification middle layer'

    def lower_layer_sett(self, obj):
        lower_layer = obj.lower_layer
        field = layer_html_compilation(lower_layer, 'Lower')
        return field
    lower_layer_sett.short_description = 'Stratification lower layer'

# Register the admin class with the associated model

admin.site.register(Dambreak, DamBreakAdmin)
admin.site.register(Wavemaker, WavemakerAdmin)
admin.site.register(Forming, FormingAdmin)
admin.site.register(Laser, LaserAdmin)
admin.site.register(Particlesonthesurface, ParticlesonthesurfaceAdmin)
admin.site.register(Spreadoveranobstacle, SpreadoveranobstacleAdmin)
admin.site.register(Typesofexperiment, TypesofexperimentAdmin)
admin.site.register(Experiment, ExperimentAdmin)
admin.site.register(Bottomsensorsresults, BottomsensorsresultsAdmin)
admin.site.register(Stringsensorsresults, StringSensorsResultsAdmin)
admin.site.register(Results, ResultsAdmin)
admin.site.register(Compositionofwaterlayer, CompositionofwaterlayerAdmin)
admin.site.register(Typeofstratification, TypeofstratificationAdmin)

# admin.site.register(Bottomsensorsresults)
# # admin.site.register(Stringsensorsresults)
# admin.site.register(Forming)
# admin.site.register(Wavemaker)
# admin.site.register(Dambreak)