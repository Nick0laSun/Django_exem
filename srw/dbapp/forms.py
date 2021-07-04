from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator


class IdForm(forms.Form):
    id = forms.IntegerField()

class TitleForm(forms.Form):
    title = forms.CharField(max_length=100)

class DateAndTimeForm(forms.Form):
    date_time = forms.DateTimeField(widget=forms.DateTimeInput)

class TimeForm(forms.Form):
    time = forms.TimeField(widget=forms.widgets.TimeInput)

class BottomForm(forms.Form):
    CHOICES = [
        ('0', 'Нет'),
        ('1', 'Подводный уступ'),
        ('2', 'Параболическое дно'),
    ]
    bottom = forms.ChoiceField(widget=forms.Select, choices=CHOICES)

class PolarityForm(forms.Form):
    CHOICES = [
        ('+', 'Положительная'),
        ('-', 'Отрицательная')
    ]
    polarity = forms.ChoiceField(widget=forms.Select, choices=CHOICES)

class WaveTypeForm(forms.Form):
    CHOICES = [
        ('0', 'Поверхностная'),
        ('1', 'Внутренняя')
    ]
    wave_type = forms.ChoiceField(widget=forms.Select, choices=CHOICES)

class WavemakerForm(forms.Form):
    amplitude = forms.FloatField(validators=[MinValueValidator(0.0), ], )
    quantity_of_waves = forms.FloatField(validators=[MinValueValidator(0.0), ], )
    frequency = forms.FloatField(validators=[MinValueValidator(0.0), ], )
    water_height = forms.FloatField(validators=[MinValueValidator(0.0), ], )

class LayerForm(forms.Form):
    density = forms.FloatField(validators=[MinValueValidator(0.0), ], )
    height = forms.FloatField(validators=[MinValueValidator(0.0), ], )