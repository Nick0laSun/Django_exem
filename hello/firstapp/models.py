# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bottomsensorsresults(models.Model):
    id = models.IntegerField(primary_key=True)
    results = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bottomsensorsresults'


class Compositionofwaterlayer(models.Model):
    id = models.IntegerField(primary_key=True)
    density_of_water_g_cm_3_field = models.FloatField(db_column='density_of_water(g/cm^3)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    name_of_the_dye = models.CharField(max_length=45, blank=True, null=True)
    layer_height = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compositionofwaterlayer'


class Dambreak(models.Model):
    id = models.IntegerField(primary_key=True)
    wall_coordinate = models.FloatField(blank=True, null=True)
    type_of_stratification = models.ForeignKey('Typeofstratification', models.DO_NOTHING, db_column='type_of_stratification')

    class Meta:
        managed = False
        db_table = 'dambreak'
        unique_together = (('id', 'type_of_stratification'),)


class Experiment(models.Model):
    id = models.IntegerField(primary_key=True)
    date_and_time = models.DateTimeField(blank=True, null=True)
    title_of_exp = models.CharField(max_length=100, blank=True, null=True)
    type_of_bottom = models.CharField(max_length=100, blank=True, null=True)
    video_reference = models.CharField(max_length=256, blank=True, null=True)
    result = models.ForeignKey('Results', models.DO_NOTHING, db_column='result')
    sheme_of_exp_reference = models.CharField(max_length=256, blank=True, null=True)
    type_of_forming = models.ForeignKey('Forming', models.DO_NOTHING, db_column='type_of_forming')
    type_of_wave = models.CharField(max_length=45, blank=True, null=True)
    duration_of_the_exp = models.TimeField(blank=True, null=True)
    type_of_stratification = models.ForeignKey('Typeofstratification', models.DO_NOTHING, db_column='type_of_stratification')
    polarity = models.CharField(max_length=45, blank=True, null=True)
    laser = models.ForeignKey('Laser', models.DO_NOTHING, db_column='laser')
    types_of_experiment = models.ForeignKey('Typesofexperiment', models.DO_NOTHING, db_column='types_of_experiment')

    class Meta:
        managed = False
        db_table = 'experiment'
        unique_together = (('id', 'type_of_forming', 'result', 'type_of_stratification', 'laser', 'types_of_experiment'),)


class Forming(models.Model):
    id = models.IntegerField(primary_key=True)
    wave_maker = models.ForeignKey('Wavemaker', models.DO_NOTHING, db_column='wave_maker')
    dam_break = models.ForeignKey(Dambreak, models.DO_NOTHING, db_column='dam_break')

    class Meta:
        managed = False
        db_table = 'forming'
        unique_together = (('id', 'dam_break', 'wave_maker'),)


class Laser(models.Model):
    id = models.IntegerField(primary_key=True)
    used = models.IntegerField(blank=True, null=True)
    video_reference = models.CharField(max_length=256, blank=True, null=True)
    laser_coordinate = models.FloatField(blank=True, null=True)
    viewing_angle = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'laser'


class Particlesonthesurface(models.Model):
    id = models.IntegerField(primary_key=True)
    type_of_particles = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'particlesonthesurface'


class Results(models.Model):
    id = models.IntegerField(primary_key=True)
    bottom_sensors = models.ForeignKey(Bottomsensorsresults, models.DO_NOTHING, db_column='bottom_sensors')
    string_sensors = models.ForeignKey('Stringsensorsresults', models.DO_NOTHING, db_column='string_sensors')

    class Meta:
        managed = False
        db_table = 'results'
        unique_together = (('id', 'bottom_sensors', 'string_sensors'),)


class Spreadoveranobstacle(models.Model):
    id = models.IntegerField(primary_key=True)
    obstacle_coordinate = models.FloatField(blank=True, null=True)
    obstacle_height = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spreadoveranobstacle'


class Stringsensorsresults(models.Model):
    id = models.IntegerField(primary_key=True)
    capasitive_sensors_res = models.CharField(max_length=45, blank=True, null=True)
    resistive_sensors_res = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stringsensorsresults'


class Typeofstratification(models.Model):
    id = models.IntegerField(primary_key=True)
    lower_layer = models.ForeignKey(Compositionofwaterlayer, models.DO_NOTHING, db_column='lower_layer')
    middle_layer = models.ForeignKey(Compositionofwaterlayer, models.DO_NOTHING, db_column='middle_layer')
    top_layer = models.ForeignKey(Compositionofwaterlayer, models.DO_NOTHING, db_column='top_layer')

    class Meta:
        managed = False
        db_table = 'typeofstratification'
        unique_together = (('id', 'lower_layer', 'middle_layer', 'top_layer'),)


class Typesofexperiment(models.Model):
    id = models.IntegerField(primary_key=True)
    spread_over_an_obstacle = models.ForeignKey(Spreadoveranobstacle, models.DO_NOTHING, db_column='spread_over_an_obstacle')
    particles_on_the_surface = models.ForeignKey(Particlesonthesurface, models.DO_NOTHING, db_column='particles_on_the_surface')

    class Meta:
        managed = False
        db_table = 'typesofexperiment'
        unique_together = (('id', 'particles_on_the_surface', 'spread_over_an_obstacle'),)


class Wavemaker(models.Model):
    id = models.IntegerField(primary_key=True)
    amplitude = models.FloatField(blank=True, null=True)
    quantity_of_waves = models.FloatField(blank=True, null=True)
    frequency = models.FloatField(blank=True, null=True)
    operating_time = models.TimeField(blank=True, null=True)
    water_height = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wavemaker'
