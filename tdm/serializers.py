from rest_framework import serializers
from tdm.models import (PartNumber, Stations,
                        TestMatrix, TestPlan)


class PartNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartNumber
        # fields = ('__all__')  
        fields = ('id',
                  'partnumber',
                  'description',
                  'date_created') 

class StationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stations
        fields = ('id',
                  'station_name',
                  'station_family',
                  'description',
                  'date_created')
        
class TestMatrixSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestMatrix
        fields = ('id',
                  'partnumber_id',
                  'station_family',
                  'fprocess_step',
                  'testplan_name',
                  'date_created',
                  'date_updated')
        
class TestPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestPlan
        fields = ('id',
                  'testplan_name',
                  'test_id',
                  'test_name',
                  'spec_type',
                  'max_value',
                  'min_value',
                  'expected_value',
                  'date_created',
                  'date_updated')
        
