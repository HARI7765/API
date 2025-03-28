from rest_framework import serializers
from .models import *


class sample(serializers.Serializer):
    roll = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()

class model_serializer(serializers.ModelSerializer):
    class Meta:
        model =students
        fields = '__all__'