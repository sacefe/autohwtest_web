from rest_framework import serializers
from tdmdocs.models import (PartNumber, TestResulstAchieve)


"""
Partnumber serializer
"""
class PartNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartNumber
        # fields = ('__all__')  
        fields = (#'id',
                  'partnumber',
                  #'description',
                  #'date_created'
                  ) 
        
"""
TestResulstAchieve serializer
"""
class TestResulstAchieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestResulstAchieve
        fields = ('id',
                  'serialnumber',
                  'partnumber',
                  'fprocess_step',
                  'station_name',
                  'username',
                  'evidence_link',
                  'test_id',
                  'test_name',
                  'spec_type',
                  'max_value',
                  'min_value',
                  'expected_value',
                  'result',
                  'test_time',
                  'tc_outcome',
                  'date_created'  )