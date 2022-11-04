from rest_framework import serializers
from .models import student

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = student
        fields = '__all__'