from rest_framework import serializers
from .models import Prediction
import datetime

"""class DayOfWeekField(serializers.ReadOnlyField):
  def to_representation(self, value):
   
    day_of_week = value.weekday()
    day_map = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }
    return day_map[day_of_week]"""


class PredictionSerializer(serializers.ModelSerializer):
    #day_of_week = serializers.SerializerMethodField()
    class Meta:
        model = Prediction
        fields = [
            "date",
            "text",
            "prediction",
            #"day_of_week",
            "id"
        ]
    
    """def get_day_of_week(self, obj):
        day_of_week = obj.date.weekday()
        day_map = {
            0: "Monday",
            1: "Tuesday",
            2: "Wednesday",
            3: "Thursday",
            4: "Friday",
            5: "Saturday",
            6: "Sunday"
        }
        return day_map[day_of_week]"""
