from django.db import models
from django.contrib.postgres.functions import RandomUUID
from django.core.validators import RegexValidator

# Create your models here.

"""
Part numbers using surrogate primary key PK integer
GUID (UUID)  not required since PNs amount is small 
   (uuid will cerate query delays and extra memory usage 128bits)
but partnumber must be unirque and database idnex 
"""
class PartNumber(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, help_text="ID for part numer")
    #uuid= models.UUIDField(default=RandomUUID, auto_created=True, help_text="UUID for part numder")
    partnumber = models.CharField(max_length=20, db_index=True, unique=True, blank=False)
    description = models.CharField(max_length=100)
    date_created = models.DateTimeField(blank=True)
    def __str__(self):
        partnumbres = [
             self.id,
        #     #self.uuid,
             self.partnumber,
             self.description,
             self.date_created,          
        ]
        return partnumbres
    

class Stations(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, help_text="ID for stations")
    station_name = models.CharField(unique=True, db_index=True, max_length=20, blank=False)
    sibling_lname_fk = models.ForeignKey("StationSiblings", on_delete= models.DO_NOTHING)
    description = models.CharField(max_length=100)
    date_created = models.DateTimeField(blank=True)
    date_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        stations = [
            self.id,
            self.station_name,
            self.sibling_lname_fk,
            self.description,
            self.date_created,
            self.date_updated,          
        ]     
        return stations
    

class StationSiblings(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, help_text="ID for stations")
    sibling_lname = models.CharField(unique=True, db_index=True, max_length=20, blank=False)
    fprocess_step_fk = models.ForeignKey("FlowProcessStep", on_delete= models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True)
    date_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        station_siblings = [
            self.id,
            self.sibling_lname,
            self.fprocess_step_fk,
            self.date_created,
            self.date_updated,          
        ]     
        return station_siblings
    

class TestMatrix(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, help_text="ID for test matrix")
    partnumber_fk = models.ForeignKey("PartNumber", on_delete= models.CASCADE)
    sibling_lname_fk = models.ForeignKey("StationSiblings", on_delete= models.DO_NOTHING)
    testplan_name = models.CharField(max_length=20, blank=False)
    employee_id = models.IntegerField(blank=False)
    date_created = models.DateTimeField(blank=True)
    date_updated = models.DateTimeField(auto_now=True)
    class Meta:  
            # unique_together are [ 'partnumber_id' and [unique_togheter('sibling_lname' 'fprocess_step_fk')] ]
           unique_together = ('partnumber_fk', 'sibling_lname_fk')
    def __str__(self):
        testmatrix = [
            self.id,
            self.partnumber_fk,
            self.sibling_lname_fk,
            self.testplan_name,
            self.employee_id,
            self.date_created,
            self.date_updated      
        ]     
        return testmatrix
    

class TestPlan(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, help_text="ID for test matrix")
    testplan_name = models.CharField(db_index=True, max_length=20, blank=False)
    group_id =  models.IntegerField()  # blank deaulft is False
    test_id = models.IntegerField()
    test_name  = models.CharField(max_length=100)
    spec_type_fk =  models.ForeignKey("SpecType", on_delete= models.DO_NOTHING)
    max_value = models.CharField(max_length=20, blank=True)
    min_value = models.CharField(max_length=20, blank=True)
    expected_value = models.CharField(max_length=20)
    date_created = models.DateTimeField(blank=True)
    date_updated = models.DateTimeField(auto_now=True)   
    class Meta:
        unique_together = ('testplan_name', 'test_id')
    def __str__(self):
        testplan = [
            self.id,
            self.testplan_name,
            self.group_id,
            self.test_id,
            self.test_name,
            self.spec_type_fk,
            self.max_value,
            self.min_value,
            self.expected_value,
            self.date_created,
            self.date_updated      
        ]     
        return testplan


class SpecType(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, help_text="ID for test matrix")
    type = models.CharField(db_index=True, max_length=20, blank=False,
                            validators=[RegexValidator('^[A-Z_]*$',
                            'Only uppercase letters and underscores allowed.')])
    date_created = models.DateTimeField(blank=True)
    date_updated = models.DateTimeField(auto_now=True)   
    def __str__(self):
        spectype = [
            self.id,
            self.type,
            self.date_created,
            self.date_updated      
        ]     
        return spectype


class TestResultsOverAll(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, help_text="ID for test matrix")
    serialnumber = models.CharField(unique=True, db_index=True, max_length=20, blank=False)
    partnumber_fk = models.ForeignKey("PartNumber", on_delete= models.CASCADE)
    overall_outcome  = models.BooleanField() 
    date_created = models.DateTimeField(blank=True)
    def __str__(self):
        test_results_overall = [
            self.id,
            self.serialnumber,
            self.partnumber_fk,
            self.overall_outcome,
            self.date_created,      
        ]     
        return test_results_overall


class TestResultsProcess(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, help_text="ID for test matrix")
    overall_TR_fk = models.ForeignKey("TestResultsOverAll", on_delete= models.CASCADE)
    fprocess_step_fk = models.ForeignKey("FlowProcessStep", on_delete= models.DO_NOTHING)
    station_id = models.IntegerField(blank=False)
    process_outcome  = models.BooleanField()
    employee_id = models.IntegerField(blank=False)
    test_time = models.TimeField(blank=True)  
    evidence_link = models.CharField(max_length=100, blank=False)
    date_created = models.DateTimeField(blank=True)
    def __str__(self):
        test_results_process = [
            self.id,
            self.overall_TR_fk,
            self.fprocess_step_fk,
            self.station_id,
            self.process_outcome,
            self.employee_id,
            self.test_time,
            self.evidence_link,
            self.date_created,      
        ]     
        return test_results_process     


class TestCaseResults(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, help_text="ID for test matrix")
    process_TR_fk = models.ForeignKey("TestResultsProcess", on_delete= models.CASCADE)
    test_id = models.IntegerField(blank=False)
    test_name  = models.CharField(max_length=100, blank=False)
    spec_type_fk =  models.ForeignKey("SpecType", on_delete= models.DO_NOTHING)
    max_value = models.CharField(max_length=20, blank=True)
    min_value = models.CharField(max_length=20, blank=True)
    expected_value = models.CharField(max_length=20)
    result = models.CharField(max_length=20)
    tc_outcome = models.BooleanField()
    date_created = models.DateTimeField(blank=True)
    class Meta:
        unique_together = ('test_id', 'test_name')
    def __str__(self):
        test_case_results = [
            self.id,
            self.process_TR_fk,
            self.test_id,
            self.test_name,
            self.spec_type_fk,
            self.max_value,
            self.min_value,
            self.expected_value,
            self.result,
            self.tc_outcome,
            self.date_created,      
        ]     
        return test_case_results   


class TestResulstAchieve(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, help_text="ID for test matrix")
    serialnumber = models.CharField(db_index=True, max_length=20, blank=False)
    partnumber = models.CharField(max_length=20, db_index=True, blank=False)
    fprocess_step =models.CharField(db_index=True, max_length=20)
    station_name = models.CharField(max_length=20, blank=False)
    username = models.CharField(max_length=150, blank=False)
    evidence_link = models.CharField(max_length=100, blank=False)
    test_id = models.IntegerField(blank=False)
    test_name  = models.CharField(db_index=True, max_length=100, blank=False)
    spec_type =  models.CharField(max_length=20, blank=False)
    max_value = models.CharField(max_length=20)
    min_value = models.CharField(max_length=20)
    expected_value = models.CharField(max_length=20)
    result = models.CharField(max_length=20)
    test_time = models.TimeField(blank=True) 
    tc_outcome = models.BooleanField()
    date_created = models.DateTimeField(blank=True)
    def __str__(self):
        test_results_achieve = [
            self.id,
            self.serialnumber,
            self.partnumber,
            self.fprocess_step,
            self.station_name,
            self.username,
            self.evidence_link,
            self.test_id,
            self.test_name,
            self.spec_type,
            self.max_value,
            self.min_value,
            self.expected_value,
            self.result,
            self.test_time,
            self.tc_outcome,
            self.date_created,      
        ]     
        return test_results_achieve
       

class FlowProcessStep(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, help_text="ID for test matrix")
    fprocess_step =models.CharField(db_index=True, max_length=20, unique=True, 
                                    validators=[RegexValidator('^[A-Z_0-9]*$',
                                    'Only uppercase letters, numbers, and underscores allowed.')])
    date_created = models.DateTimeField(blank=True)
    date_updated = models.DateTimeField(auto_now=True)   
    def __str__(self):
        flow_process_step = [
            self.id,
            self.fprocess_step,
            self.date_created,
            self.date_updated,     
        ]      
        return flow_process_step

class FlowTable(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, help_text="ID for test matrix")
    flow_name =  models.CharField(db_index=True, max_length=20, blank=False)
    fprocess_priority = models.IntegerField(blank=False)
    fprocess_step_fk = models.ForeignKey("FlowProcessStep", on_delete= models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True)
    date_updated = models.DateTimeField(auto_now=True)   
    class Meta:
        unique_together = ('flow_name', 'fprocess_priority')
    def __str__(self):
        flow_table = [
            self.id,
            self.flow_name,
            self.fprocess_priority,
            self.fprocess_step_fk,
            self.date_created,
            self.date_updated,     
        ]      
        return flow_table

class FlowMatrix(models.Model):
    partnumber_id = models.OneToOneField(PartNumber, on_delete= models.CASCADE, primary_key=True,)
    flow_name =  models.CharField(db_index=True, max_length=20, blank=False)
    employee_id = models.IntegerField(blank=False)
    date_created = models.DateTimeField(blank=True)
    date_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        flow_matrix = [
            self.partnumber_id,
            self.flow_name,
            self.employee_id,
            self.date_created,
            self.date_updated,     
        ]     
        return flow_matrix

class FlowStatus(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, help_text="ID for test matrix")
    serialnumber = models.CharField(db_index=True, unique=True, max_length=20, blank=False)
    partnumber_fk = models.ForeignKey("PartNumber", on_delete= models.CASCADE, db_index=True)
    flow_name =  models.CharField(max_length=20, blank=False)
    fprocess_priority = models.IntegerField(blank=False)
    curr_fprocess_step_fk = models.ForeignKey("FlowProcessStep", on_delete= models.DO_NOTHING)
    flow_status = models.BooleanField()
    employee_id = models.IntegerField()
    date_arrival = models.DateTimeField(auto_now=True)
    date_departure = models.DateTimeField(blank=True)
    class Meta:
        unique_together = ('flow_name', 'fprocess_priority')
    def __str__(self):
        flow_status = [
            self.id,
            self.serialnumber,
            self.partnumber_fk,
            self.flow_name,
            self.fprocess_priority,
            self.curr_fprocess_step_fk,
            self.flow_status,
            self.employee_id,
            self.date_arrival,
            self.date_departure,     
        ]      
        return flow_status  


class FlowHistory(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, help_text="ID for test matrix")
    serialnumber = models.CharField(db_index=True, max_length=20, blank=False)
    partnumber = models.CharField(max_length=20, db_index=True, blank=False)
    flow_name =  models.CharField(max_length=20, blank=False)
    fprocess_priority = models.IntegerField(blank=False)
    fprocess_step =models.CharField(db_index=True, max_length=20)
    flow_status = models.BooleanField()
    employee_id = models.IntegerField(blank=False)
    date_arrival = models.DateTimeField(auto_now=True)
    date_departure = models.DateTimeField(blank=True) 
    def __str__(self):
        flow_status = [
            self.id,
            self.serialnumber,
            self.partnumber,
            self.flow_name,
            self.fprocess_priority,
            self.fprocess_step,
            self.flow_status,
            self.employee_id,
            self.date_arrival,
            self.date_departure,     
        ]      
        return flow_status  
