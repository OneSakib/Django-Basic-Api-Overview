from rest_framework import serializers
from .models import Student


class Student_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
