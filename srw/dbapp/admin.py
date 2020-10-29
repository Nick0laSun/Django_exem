from django.contrib import admin
from django.utils.html import format_html
# from django_reverse_admin import ReverseModelAdmin
from .models import Experiment, Results, Bottomsensorsresults, \
    Stringsensorsresults, Forming, Wavemaker, Dambreak, \
    Typeofstratification, Compositionofwaterlayer, \
    Typesofexperiment, Particlesonthesurface, \
    Spreadoveranobstacle, Laser

# Register your models here.

class StringSensorsResultsAdmin(admin.ModelAdmin):
    # fields = (
    #     'capasitive_sensors_res',
    #     'resistive_sensors_res'
    # )

    list_display = ('id', 'capasitive_sensors_res', 'resistive_sensors_res')

class DamBreakAdmin(admin.ModelAdmin):
    list_display = (
        'wall_coordinate', 'top_layer_sett', 'middle_layer_sett', 'lower_layer_sett', 'all_layers_sett'
    )

    def top_layer_sett(self, obj):
        tls = 'Density of water (g/cm^3): ' + str(obj.type_of_stratification.top_layer.density_of_water_g_cm_3_field) + ' \n' + \
                'Name of the dye: ' + obj.type_of_stratification.top_layer.name_of_the_dye + ' \n' + \
                'Water heght: ' + str(obj.type_of_stratification.top_layer.layer_height)
        
        return tls
    top_layer_sett.short_description = 'Top layer'

    def middle_layer_sett(self, obj):
        if obj.type_of_stratification.middle_layer:
            mls = 'Density of water (g/cm^3): ' + str(obj.type_of_stratification.middle_layer.density_of_water_g_cm_3_field) + ' \n' + \
                'Name of the dye: ' + obj.type_of_stratification.middle_layer.name_of_the_dye + ' \n' + \
                'Water heght: ' + str(obj.type_of_stratification.middle_layer.layer_height)
        else: 
            mls = obj.type_of_stratification.top_layer
        return mls
    middle_layer_sett.short_description = 'Middle Layer'

    def lower_layer_sett(self, obj):
        lls = 'Density of water (g/cm^3): ' + str(obj.type_of_stratification.lower_layer.density_of_water_g_cm_3_field) + ' \n' + \
                'Name of the dye: ' + obj.type_of_stratification.lower_layer.name_of_the_dye + ' \n' + \
                'Water heght: ' + str(obj.type_of_stratification.lower_layer.layer_height)
        return lls
    lower_layer_sett.short_description = 'Lower layer'

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


def layer_html_compilation(layer, level):
    html_filed = format_html(
            '<b>{0} layer</b> <hr><p>Density of water (g/cm^3): <b>{1}</b> <br> Name of the dye: <b>{2}</b> <br> Water heght: <b>{3}</b></p><hr>',
            level,
            layer.density_of_water_g_cm_3_field,
            layer.name_of_the_dye,
            layer.layer_height
        )
    return html_filed

# admin.site.register(Experiment)
# Define the admin class
class ExperimentAdmin(admin.ModelAdmin):
# class ExperimentAdmin(ReverseModelAdmin):
    # list_display = ('date_and_time', 'title_of_exp', 'type_of_bottom', 'video_reference', \
    #     'result', 'schema_of_exp_reference', 'type_of_forming', 'type_of_wave', \
    #     'duration_of_the_exp', 'type_of_stratification', 'polarity', \
    #     'laser', 'types_of_experiment')

    # pass

    list_display = ('id', 'date_and_time', 'title_of_exp', 'type_of_bottom', 'video_ref', \
        'string_sensors_results', 'bottom_sensors_results', 'schema_of_exp', \
        'wavemaker_settings', 'dam_break_experiment_settings', \
        'dam_wall_coordinate', 'dam_top_layer_settings', 'dam_middle_layer_settings', 'dam_lower_layer_settings', \
        'stratification_top_layer_sett', 'stratification_middle_layer_sett', 'stratification_lower_layer_sett', \
        'type_of_wave', 'duration_of_exp', \
        'polarity', 'laser_settings', 'spread_over_an_obstacle', 'particles' \
    )

    list_filter = (
        'title_of_exp', 
        'type_of_bottom', 
        'type_of_wave', 'polarity',
        'type_of_forming__wave_maker__amplitude', 
        'type_of_forming__wave_maker__quantity_of_waves',
        'type_of_forming__wave_maker__frequency',
        # 'type_of_forming__wave_maker__operating_time',
        'type_of_forming__wave_maker__water_height',
        'type_of_forming__dam_break__wall_coordinate',
        # 'type_of_forming__dam_break__type_of_stratification__top_layer__density_of_water_g_cm_3_field',
        # 'type_of_forming__dam_break__type_of_stratification__top_layer__name_of_the_dye',
        # 'type_of_forming__dam_break__type_of_stratification__top_layer__layer_height',
        # 'type_of_forming__dam_break__type_of_stratification__middle_layer__density_of_water_g_cm_3_field',
        # 'type_of_forming__dam_break__type_of_stratification__middle_layer__name_of_the_dye',
        # 'type_of_forming__dam_break__type_of_stratification__middle_layer__layer_height',
        # 'type_of_forming__dam_break__type_of_stratification__lower_layer__density_of_water_g_cm_3_field',
        # 'type_of_forming__dam_break__type_of_stratification__lower_layer__name_of_the_dye',
        # 'type_of_forming__dam_break__type_of_stratification__lower_layer__layer_height'
        )
    
    date_hierarchy = 'date_and_time'

    ordering = ['id']

    search_fields = [
        'type_of_forming__wave_maker__amplitude', 
        'type_of_forming__wave_maker__quantity_of_waves',
        'type_of_forming__wave_maker__frequency',
        'type_of_forming__wave_maker__operating_time',
        'type_of_forming__wave_maker__water_height'
    ]

    # inline_reverse = ['laser']

    fieldsets = (
        (None,{
            'fields': (
                'date_and_time', 
                'title_of_exp', 
                'type_of_bottom', 
                'video_reference',
                'schema_of_exp_reference',
                'type_of_wave', 
                'duration_of_the_exp',
                'polarity',
                'result',
                'laser'
            )
        }),
        # ('Laser',{
        #     # 'fields': (
        #     #     'laser__video_reference',
        #     #     'laser__laser_coordinate',
        #     #     'laser__viewing_angle'
        #     # )
        # })
    )

    # search_fields = [
    #     'type_of_forming__dam_break__wall_coordinate',
    #     'type_of_forming__dam_break__type_of_stratification__top_layer__density_of_water_g_cm_3_field',
    #     'type_of_forming__dam_break__type_of_stratification__top_layer__name_of_the_dye',
    #     'type_of_forming__dam_break__type_of_stratification__top_layer__layer_height',
    #     'type_of_forming__dam_break__type_of_stratification__middle_layer__density_of_water_g_cm_3_field',
    #     'type_of_forming__dam_break__type_of_stratification__middle_layer__name_of_the_dye',
    #     'type_of_forming__dam_break__type_of_stratification__middle_layer__layer_height',
    #     'type_of_forming__dam_break__type_of_stratification__lower_layer__density_of_water_g_cm_3_field',
    #     'type_of_forming__dam_break__type_of_stratification__lower_layer__name_of_the_dye',
    #     'type_of_forming__dam_break__type_of_stratification__lower_layer__layer_height'
    # ]

    def duration_of_exp(self, obj):
        return str(obj.duration_of_the_exp)
    duration_of_exp.short_description = 'Duration of exp.'

    def video_ref(self, obj):
        if not (obj.video_reference):
            return "No data"
        else:
            return format_html('<a href="{0}">YouTube</a>', obj.video_reference)
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
        fields = format_html(
            '<p> Wave apmplitude: <b>{0}</b> <br> Quantity of waves: <b>{1}</b> <br> Frequency: <b>{2}</b> <br> Operating time: <b>{3}</b> <br> Water height: <b>{4}</b> </p>',
            str(obj.type_of_forming.wave_maker.amplitude),
            str(obj.type_of_forming.wave_maker.quantity_of_waves),
            str(obj.type_of_forming.wave_maker.frequency),
            str(obj.type_of_forming.wave_maker.operating_time),
            str(obj.type_of_forming.wave_maker.water_height)
        )
        return fields
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
        sett = '<a href=' + str(obj.laser.video_reference) + '>Video</a><br>' + \
            'Laser coordinate: ' + str(obj.laser.laser_coordinate) + \
            'Viewing angle: ' + str(obj.laser.viewing_angle)
        return sett
    laser_settings.short_description = 'Laser'

    def spread_over_an_obstacle(self, obj):
        soo = 'Wall coordinate: ' + str(obj.types_of_experiment.spread_over_an_obstacle.obstacle_coordinate) + '\n' +\
            'Wall heght: ' + str(obj.types_of_experiment.spread_over_an_obstacle.obstacle_height)
        return soo
    spread_over_an_obstacle.short_description = 'Spread over an obstacle'

    def particles(self, obj):
        part = obj.types_of_experiment.particles_on_the_surface.type_of_particles
        return part
    particles.short_description = 'Particles on the surface'

# class ExperimentInline(admin.StackedInline):
#     model = Experiment

# class LaserAdmin(admin.ModelAdmin):
#     inlines = [ ExperimentInline ]

# admin.site.register(Results)
class ResultsAdmin(admin.ModelAdmin):
    # list_display = ('id', 'bottom_sensors', 'string_sensors')
    pass

# Register the admin class with the associated model

# admin.site.register(Stringsensorsresults, StringSensorsResultsAdmin)
admin.site.register(Dambreak, DamBreakAdmin)
admin.site.register(Experiment, ExperimentAdmin)
admin.site.register(Results, ResultsAdmin)

# admin.site.register(Bottomsensorsresults)
# # admin.site.register(Stringsensorsresults)
# admin.site.register(Forming)
# admin.site.register(Wavemaker)
# admin.site.register(Dambreak)
admin.site.register(Typeofstratification)
# admin.site.register(Compositionofwaterlayer)
# admin.site.register(Typesofexperiment)
# admin.site.register(Particlesonthesurface)
# admin.site.register(Spreadoveranobstacle)
# admin.site.register(Laser, LaserAdmin)