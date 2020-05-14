# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bottomsensorsresults(models.Model):
    results = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bottomsensorsresults'


class Stringsensorsresults(models.Model):
    capasitive_sensors_res = models.CharField(max_length=45, blank=True, null=True)
    resistive_sensors_res = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stringsensorsresults'


class Compositionofwaterlayer(models.Model):
    density_of_water_g_cm_3_field = models.FloatField(db_column='density_of_water(g/cm^3)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    name_of_the_dye = models.CharField(max_length=45, blank=True, null=True)
    layer_height = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compositionofwaterlayer'


class Typeofstratification(models.Model):
    lower_layer = models.ForeignKey(Compositionofwaterlayer, models.CASCADE, related_name='lower_layer', db_column='lower_layer')
    middle_layer = models.ForeignKey(Compositionofwaterlayer, models.CASCADE, related_name='middle_layer', db_column='middle_layer')
    top_layer = models.ForeignKey(Compositionofwaterlayer, models.CASCADE, related_name='top_layer', db_column='top_layer')

    class Meta:
        managed = False
        db_table = 'typeofstratification'


class Dambreak(models.Model):
    wall_coordinate = models.FloatField(blank=True, null=True)
    type_of_stratification = models.ForeignKey(Typeofstratification, models.CASCADE, related_name='type_of_stratification', db_column='type_of_stratification', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dambreak'


class Wavemaker(models.Model):
    amplitude = models.FloatField(blank=True, null=True)
    quantity_of_waves = models.FloatField(blank=True, null=True)
    frequency = models.FloatField(blank=True, null=True)
    operating_time = models.TimeField(blank=True, null=True)
    water_height = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wavemaker'


class Forming(models.Model):
    wave_maker = models.ForeignKey(Wavemaker, models.CASCADE, related_name='wave_maker', db_column='wave_maker')
    dam_break = models.ForeignKey(Dambreak, models.CASCADE, related_name='dam_break', db_column='dam_break')

    class Meta:
        managed = False
        db_table = 'forming'


class Laser(models.Model):
    used = models.IntegerField(blank=True, null=True)
    video_reference = models.CharField(max_length=256, blank=True, null=True)
    laser_coordinate = models.FloatField(blank=True, null=True)
    viewing_angle = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'laser'


class Particlesonthesurface(models.Model):
    type_of_particles = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'particlesonthesurface'


class Results(models.Model):
    bottom_sensors = models.ForeignKey(Bottomsensorsresults, models.CASCADE, related_name='bottom_sens', db_column='bottom_sensors')
    string_sensors = models.ForeignKey(Stringsensorsresults, models.CASCADE, related_name='string_sens', db_column='string_sensors')

    class Meta:
        managed = False
        db_table = 'results'


class Spreadoveranobstacle(models.Model):
    obstacle_coordinate = models.FloatField(blank=True, null=True)
    obstacle_height = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spreadoveranobstacle'


class Typesofexperiment(models.Model):
    spread_over_an_obstacle = models.ForeignKey(Spreadoveranobstacle, models.CASCADE, related_name='spread_over_an_obstacle', db_column='spread_over_an_obstacle')
    particles_on_the_surface = models.ForeignKey(Particlesonthesurface, models.CASCADE, related_name='particles_on_the_surface', db_column='particles_on_the_surface')

    class Meta:
        managed = False
        db_table = 'typesofexperiment'


class Experiment(models.Model):
    date_and_time = models.DateTimeField(blank=True, null=True)
    title_of_exp = models.CharField(max_length=100, blank=True, null=True)
    type_of_bottom = models.CharField(max_length=100, blank=True, null=True)
    video_reference = models.CharField(max_length=256, blank=True, null=True)
    result = models.ForeignKey(Results, models.CASCADE, related_name='result', db_column='result')
    schema_of_exp_reference = models.CharField(max_length=256, blank=True, null=True)
    type_of_forming = models.ForeignKey(Forming, models.CASCADE, related_name='forming', db_column='type_of_forming')
    type_of_wave = models.CharField(max_length=45, blank=True, null=True)
    duration_of_the_exp = models.TimeField(blank=True, null=True)
    type_of_stratification = models.ForeignKey(Typeofstratification, models.CASCADE, related_name='stratification', db_column='type_of_stratification')
    polarity = models.CharField(max_length=45, blank=True, null=True)
    laser = models.ForeignKey(Laser, models.CASCADE, related_name='laser', db_column='laser')
    types_of_experiment = models.ForeignKey(Typesofexperiment, models.CASCADE, related_name='types_of_experiment', db_column='types_of_experiment')

    class Meta:
        managed = False
        db_table = 'experiment'