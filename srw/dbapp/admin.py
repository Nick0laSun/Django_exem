from django.contrib import admin
from .models import Experiment, Results, Bottomsensorsresults, \
    Stringsensorsresults, Forming, Wavemaker, Dambreak, \
    Typeofstratification, Compositionofwaterlayer, \
    Typesofexperiment, Particlesonthesurface, \
    Spreadoveranobstacle, Laser

# Register your models here.

# admin.site.register(Experiment)
# Define the admin class
class ExperimentAdmin(admin.ModelAdmin):
    # list_display = ('date_and_time', 'title_of_exp', 'type_of_bottom', 'video_reference', \
    #     'result', 'schema_of_exp_reference', 'type_of_forming', 'type_of_wave', \
    #     'duration_of_the_exp', 'type_of_stratification', 'polarity', \
    #     'laser', 'types_of_experiment')
    pass

# Register the admin class with the associated model
admin.site.register(Experiment, ExperimentAdmin)

# admin.site.register(Results)
class ResultsAdmin(admin.ModelAdmin):
    # list_display = ('id', 'bottom_sensors', 'string_sensors')
    pass

admin.site.register(Results, ResultsAdmin)

admin.site.register(Bottomsensorsresults)
admin.site.register(Stringsensorsresults)
admin.site.register(Forming)
admin.site.register(Wavemaker)
admin.site.register(Dambreak)
admin.site.register(Typeofstratification)
admin.site.register(Compositionofwaterlayer)
admin.site.register(Typesofexperiment)
admin.site.register(Particlesonthesurface)
admin.site.register(Spreadoveranobstacle)
admin.site.register(Laser)