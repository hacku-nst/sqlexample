# serializers.py
# Convert models to/from JSON

from rest_framework import serializers
from schapp.models import *

class SchoolSerializer(serializers.ModelSerializer):
    # films = serializers.StringRelatedField(many=True, read_only=True)
 
    class Meta:
        model = School
        fields = ('school_id', 'school', 'district_id', 'district')

class SchoolWriteSerializer(serializers.ModelSerializer):
    schools = serializers.PrimaryKeyRelatedField(queryset=School.objects.all(), allow_null=True)
 
    class Meta:
        model = School
        fields = ('school_id', 'school', 'district_id', 'district')


class PerformanceSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Performance
        fields = ('school_id', 'school', 'district_id', 'district')

class PerformanceWriteSerializer(serializers.ModelSerializer):
    performance = serializers.PrimaryKeyRelatedField(queryset=Performance.objects.all(), allow_null=True)
 
    class Meta:
        model = Performance
        fields = ('schoolid', 'school', 'district_id', 'district', 'academic_year', 'subject', 'subgroup', 'grade_level', 'participation_rate_2014_to_2015', 'percentage_meets_or_exceeds_2014_to_2015')


