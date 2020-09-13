from django.contrib import admin
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

    
# admin.site.register(Experiment)
# Define the admin class
class ExperimentAdmin(admin.ModelAdmin):
# class ExperimentAdmin(ReverseModelAdmin):
    # list_display = ('date_and_time', 'title_of_exp', 'type_of_bottom', 'video_reference', \
    #     'result', 'schema_of_exp_reference', 'type_of_forming', 'type_of_wave', \
    #     'duration_of_the_exp', 'type_of_stratification', 'polarity', \
    #     'laser', 'types_of_experiment')

    # pass

    list_display = ('id', 'date_and_time', 'title_of_exp', 'type_of_bottom', 'video_reference', \
        'string_sensors_results', 'bottom_sensors_results', 'schema_of_exp_reference', \
        'wavemaker_settings', \
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
        'type_of_forming__wave_maker__operating_time',
        'type_of_forming__wave_maker__water_height',
        'type_of_forming__dam_break__wall_coordinate',
        'type_of_forming__dam_break__type_of_stratification__top_layer__density_of_water_g_cm_3_field',
        'type_of_forming__dam_break__type_of_stratification__top_layer__name_of_the_dye',
        'type_of_forming__dam_break__type_of_stratification__top_layer__layer_height',
        'type_of_forming__dam_break__type_of_stratification__middle_layer__density_of_water_g_cm_3_field',
        'type_of_forming__dam_break__type_of_stratification__middle_layer__name_of_the_dye',
        'type_of_forming__dam_break__type_of_stratification__middle_layer__layer_height',
        'type_of_forming__dam_break__type_of_stratification__lower_layer__density_of_water_g_cm_3_field',
        'type_of_forming__dam_break__type_of_stratification__lower_layer__name_of_the_dye',
        'type_of_forming__dam_break__type_of_stratification__lower_layer__layer_height'
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

    def string_sensors_results(self, obj):
        # if obj.result.string_sensors.capasitive_sensors_res and obj.result.string_sensors.resistive_sensors_res:
        #     return u'<a href="{0}">{1}</a><br><a href="{2}">{3}</a>' \
        #         .format(obj.result.string_sensors.capasitive_sensors_res, 'Capasitive sensors', \
        #         obj.result.string_sensors.resistive_sensors_res, 'Resistive sensors')
        return [ obj.result.string_sensors.capasitive_sensors_res, obj.result.string_sensors.resistive_sensors_res]
    string_sensors_results.short_description = 'String sensors results'

    def bottom_sensors_results(self, obj):
        bsr = '<a href=' + obj.result.bottom_sensors.results + '>Bottom sensors<\a>'
        return obj.result.bottom_sensors.results
        # return bsr
    bottom_sensors_results.short_description = 'Bottom sensors results'
    # bottom_sensors_results.allow_tags = True

    def wavemaker_settings(self, obj):
        fields = 'Wave apmplitude: ' + str(obj.type_of_forming.wave_maker.amplitude) + '\n' +\
            'Quantity of waves:' +  str(obj.type_of_forming.wave_maker.quantity_of_waves) + '\n' +\
            'Frequency: ' + str(obj.type_of_forming.wave_maker.frequency) + '\n' +\
            'Operating time: ' + str(obj.type_of_forming.wave_maker.operating_time) + '\n' +\
            'Water height: ' + str(obj.type_of_forming.wave_maker.water_height)
        return fields
    wavemaker_settings.short_description = 'Wavemaker'

    def dam_wall_coordinate(self, obj):
        dwc = 'Wall coordinate: ' + str(obj.type_of_forming.dam_break.wall_coordinate)
        return dwc
    dam_wall_coordinate.short_description = 'Dam wall coordinate'

    def dam_top_layer_settings(self, obj):
        top_layer = 'Density of water (g/cm^3): ' + str(obj.type_of_forming.dam_break.type_of_stratification.top_layer.density_of_water_g_cm_3_field) + '\n' + \
            'Name of the dye: ' + obj.type_of_forming.dam_break.type_of_stratification.top_layer.name_of_the_dye + '\n' + \
            'Water heght: ' + str(obj.type_of_forming.dam_break.type_of_stratification.top_layer.layer_height)
        return top_layer
    dam_top_layer_settings.short_description = 'Dam break top layer'

    def dam_middle_layer_settings(self, obj):
        middle_layer = 'Density of water (g/cm^3): ' + str(obj.type_of_forming.dam_break.type_of_stratification.middle_layer.density_of_water_g_cm_3_field) + '\n' + \
            'Name of the dye: ' + obj.type_of_forming.dam_break.type_of_stratification.middle_layer.name_of_the_dye + '\n' + \
            'Water heght: ' + str(obj.type_of_forming.dam_break.type_of_stratification.middle_layer.layer_height)
        return middle_layer
    dam_middle_layer_settings.short_description = 'Dam break middle layer'

    def dam_lower_layer_settings(self, obj):
        lower_layer = 'Density of water (g/cm^3): ' + str(obj.type_of_forming.dam_break.type_of_stratification.lower_layer.density_of_water_g_cm_3_field) + '\n' + \
            'Name of the dye: ' + obj.type_of_forming.dam_break.type_of_stratification.lower_layer.name_of_the_dye + '\n' + \
            'Water heght: ' + str(obj.type_of_forming.dam_break.type_of_stratification.lower_layer.layer_height)
        return lower_layer
    dam_lower_layer_settings.short_description = 'Dam break middle layer'

    def stratification_top_layer_sett(self, obj):
        stls = 'Density of water (g/cm^3): ' + str(obj.type_of_stratification.top_layer.density_of_water_g_cm_3_field) + '\n' + \
            'Name of the dye: ' + obj.type_of_stratification.top_layer.name_of_the_dye + '\n' + \
            'Water heght: ' + str(obj.type_of_stratification.top_layer.layer_height)
        return stls
    stratification_top_layer_sett.short_description = 'Stratification top layer'

    def stratification_middle_layer_sett(self, obj):
        smls = 'Density of water (g/cm^3): ' + str(obj.type_of_stratification.middle_layer.density_of_water_g_cm_3_field) + '\n' + \
            'Name of the dye: ' + obj.type_of_stratification.middle_layer.name_of_the_dye + '\n' + \
            'Water heght: ' + str(obj.type_of_stratification.middle_layer.layer_height)
        return smls
    stratification_middle_layer_sett.short_description = 'Stratification middle layer'

    def stratification_lower_layer_sett(self, obj):
        slls = 'Density of water (g/cm^3): ' + str(obj.type_of_stratification.lower_layer.density_of_water_g_cm_3_field) + '\n' + \
            'Name of the dye: ' + obj.type_of_stratification.lower_layer.name_of_the_dye + '\n' + \
            'Water heght: ' + str(obj.type_of_stratification.lower_layer.layer_height)
        return slls
    stratification_lower_layer_sett.short_description = 'Stratification lower layer'

    def laser_settings(self, obj):
        sett = '<a href=' + obj.laser.video_reference + '>Video</a><br>' + \
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
# admin.site.register(Results, ResultsAdmin)

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