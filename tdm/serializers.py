from rest_framework import serializers
from tdm.models import (PartNumber, Stations,
                        TestMatrix, TestPlan,
                        StationSiblings, FlowProcessStep,
                        SpecType, FlowTable,
                        FlowMatrix,TestResultsOverAll,
                        TestResultsProcess, TestCaseResults,
                        TestResulstAchieve, FlowStatus,
                        FlowHistory
                        )

"""
Partnumber/Stations serializer
"""
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
                  'sibling_lname_fk',
                  'description',
                  'date_created',
                  'date_updated')  


class StationSiblingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StationSiblings
        fields =('id',
                 'sibling_lname',
                 'fprocess_step_fk',
                 'date_created',
                 'date_updated')  

"""
Test serializer
"""
class TestMatrixSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestMatrix
        fields = ('id',
                  'partnumber_fk',
                  'sibling_lname_fk',
                  'testplan_name',
                  'employee_id',
                  'date_created',
                  'date_updated')

 
class TestPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestPlan
        fields = ('id',
                  'testplan_name',
                  'group_id',
                  'test_id',
                  'test_name',
                  'spec_type_fk',
                  'max_value',
                  'min_value',
                  'expected_value',
                  'date_created',
                  'date_updated')


class SpecTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecType
        fields = ('id',
                  'type',
                  'date_created',
                  'date_updated')

        
"""
Flow serializer
"""
class FlowProcessStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlowProcessStep
        fields =('id',
                 'fprocess_step',
                 'date_created',
                 'date_updated')  
        

class FlowTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlowTable
        fields = ('id',
                  'flow_name',
                  'fprocess_priority',
                  'fprocess_step_fk',
                  'date_created',
                  'date_updated')


class FlowMatrixSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlowMatrix
        fields = ('partnumber_id',
                  'flow_name',
                  'employee_id',
                  'date_created',
                  'date_updated')

        
class TestResultsOverAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestResultsOverAll
        fields = ('id',
                  'serialnumber',
                  'partnumber_fk',
                  'overall_outcome',
                  'date_created')
                  
class  TestResultsProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestResultsProcess
        fields =  ('id',
                   'overall_TR_fk',
                   'fprocess_step_fk',
                   'station_id',
                   'process_outcome',
                   'employee_id',
                   'test_time',
                   'evidence_link',
                   'date_created')
        
class  TestCaseResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCaseResults
        fields = ('id',
                  'process_TR_fk',
                  'test_id',
                  'test_name',
                  'spec_type_fk',
                  'max_value',
                  'min_value',
                  'expected_value',
                  'result',
                  'tc_outcome',
                  'date_created')

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

class FlowStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlowStatus
        fields = ('id',
                  'serialnumber',
                  'partnumber_fk',
                  'flow_name',
                  'fprocess_priority',
                  'curr_fprocess_step_fk',
                  'flow_status',
                  'employee_id',
                  'date_arrival',
                  'date_departure')

class FlowHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FlowHistory
        fields = ('id',
                  'serialnumber',
                  'partnumber',
                  'flow_name',
                  'fprocess_priority',
                  'fprocess_step',
                  'flow_status',
                  'employee_id',
                  'date_arrival',
                  'date_departure')
  

                                                