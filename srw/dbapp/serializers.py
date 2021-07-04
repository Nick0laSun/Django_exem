from rest_framework import serializers
from .models import Experiment

# class ExperimentSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Experiment
#         fields = (
#             'id',
#             'date_and_time',
#             'title_of_exp',
#             'type_of_bottom',
#             'video_reference',
#             'result',
#             'schema_of_exp_reference',
#             'type_of_wave',
#             'duration_of_the_exp',
#             'type_of_stratification',
#             'polarity',
#             'laser',
#             'types_of_experiment'
#         )