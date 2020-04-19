# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bottomsensorsresults(models.Model):
    idbottomsensorsresults = models.AutoField(db_column='idBottomSensorsResults', primary_key=True)  # Field name made lowercase.
    results = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bottomsensorsresults'


class Compositionofwater(models.Model):
    idcompositionofwater = models.IntegerField(db_column='idCompositionOfWater', primary_key=True)  # Field name made lowercase.
    densityofwater_g_cm_3_field = models.FloatField(db_column='densityOfWater(g/cm^3)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    nameofthedye = models.CharField(db_column='nameOfTheDye', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'compositionofwater'


class Dambreak(models.Model):
    iddambreak = models.IntegerField(db_column='idDamBreak', primary_key=True)  # Field name made lowercase.
    differenceinliquidlevels = models.FloatField(db_column='differenceInLiquidLevels', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dambreak'


class Stringsensorsresults(models.Model):
    idstringsensorsresults = models.IntegerField(db_column='idStringSensorsResults', primary_key=True)  # Field name made lowercase.
    capasitivesensorsres = models.CharField(db_column='capasitiveSensorsRes', max_length=256, blank=True, null=True)  # Field name made lowercase.
    resistivesensorsres = models.CharField(db_column='resistiveSensorsRes', max_length=256, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stringsensorsresults'


class Wavemaker(models.Model):
    idwavemaker = models.IntegerField(db_column='idWaveMaker', primary_key=True)  # Field name made lowercase.
    amplitude = models.FloatField(blank=True, null=True)
    quantityofwaves = models.FloatField(db_column='quantityOfWaves', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(blank=True, null=True)
    operatingtime = models.TimeField(db_column='operatingTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wavemaker'


class Forming(models.Model):
    idforming = models.IntegerField(db_column='idForming', primary_key=True)  # Field name made lowercase.
    wavemaker = models.ForeignKey(Wavemaker, models.DO_NOTHING, related_name='wavemaker', db_column='waveMaker')  # Field name made lowercase.
    dambreak = models.ForeignKey(Dambreak, models.DO_NOTHING, related_name='dam_break', db_column='damBreak')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'forming'
        unique_together = (('idforming', 'wavemaker', 'dambreak'),)


class Results(models.Model):
    idresults = models.IntegerField(db_column='idResults', primary_key=True)  # Field name made lowercase.
    bottomsensors = models.ForeignKey(Bottomsensorsresults, models.DO_NOTHING, related_name='bottom_res', db_column='bottomSensors')  # Field name made lowercase.
    stringsensors = models.ForeignKey(Stringsensorsresults, models.DO_NOTHING, related_name='string_res', db_column='stringSensors')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'results'
        unique_together = (('idresults', 'bottomsensors', 'stringsensors'),)


class Experiment(models.Model):
    idexperiment = models.AutoField(db_column='idExperiment', primary_key=True)  # Field name made lowercase.
    dataandtime = models.DateTimeField(db_column='dataAndTime', blank=True, null=True)  # Field name made lowercase.
    titleofexp = models.CharField(db_column='titleOfExp', max_length=100, blank=True, null=True)  # Field name made lowercase.
    typeofbottom = models.CharField(db_column='typeOfBottom', max_length=100, blank=True, null=True)  # Field name made lowercase.
    videoreference = models.CharField(db_column='videoReference', max_length=256, blank=True, null=True)  # Field name made lowercase.
    result = models.ForeignKey(Results, models.DO_NOTHING, related_name='result', db_column='result')
    shemeofexpreference = models.CharField(db_column='shemeOfExpReference', max_length=256, blank=True, null=True)  # Field name made lowercase.
    typeofforming = models.ForeignKey(Forming, models.DO_NOTHING, related_name='forming', db_column='typeOfForming')  # Field name made lowercase.
    compositionofwater = models.ForeignKey(Compositionofwater, models.DO_NOTHING, related_name='composition_of_water', db_column='compositionOfWater')  # Field name made lowercase.
    typeofwave = models.CharField(db_column='typeOfWave', max_length=45, blank=True, null=True)  # Field name made lowercase.
    durationoftheexp = models.TimeField(db_column='durationOfTheExp', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'experiment'
        unique_together = (('idexperiment', 'result', 'typeofforming', 'compositionofwater'),)