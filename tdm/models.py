from django.db import models
from django.contrib.postgres.functions import RandomUUID

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
    date_created = models.DateTimeField(auto_now=True)
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
    station_family = models.CharField(max_length=20, blank=False)
    description = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now=True)
    def __str__(self):
        stations = [
            self.id,
            self.station_name,
            self.station_family,
            self.description,
            self.date_created,          
        ]     
        return stations

# TODO  is it OK partnumber_id  in database appeared partnumber_id_id
class TestMatrix(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, help_text="ID for test matrix")
    partnumber_id = models.ForeignKey("PartNumber", on_delete= models.CASCADE)
    station_family = models.CharField(max_length=20, blank=False)
    fprocess_step = models.IntegerField(blank=False)
    testplan_name = models.CharField(max_length=20, blank=False)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField()  #TODO (blank=True)
   # class Meta:
    #        unique_together = ('partnumber_id', 'station_family', 'fprocess_step')
    def __str__(self):
        testmatrix = [
            self.id,
            self.partnumber_id,
            self.station_family,
            self.fprocess_step,
            self.testplan_name,
            self.date_created,
            self.date_updated      
        ]     
        return testmatrix
    

class TestPlan(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, help_text="ID for test matrix")
    testplan_name = models.CharField(db_index=True, max_length=20, blank=False)
    test_id = models.IntegerField(blank=False)
    test_name  = models.CharField(max_length=20, blank=False)
    spec_type =  models.CharField(max_length=20, blank=False)
    max_value = models.CharField(max_length=20)
    min_value = models.CharField(max_length=20)
    expected_value = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField()     #TODO (blank=True)
    class Meta:
        unique_together = ('testplan_name', 'test_id')
    def __str__(self):
        testplan = [
            self.id,
            self.testplan_name,
            self.test_id,
            self.test_name,
            self.spec_type,
            self.max_value,
            self.min_value,
            self.expected_value,
            self.date_created,
            self.date_updated      
        ]     
        return testplan


class TestResultsOverAll(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, help_text="ID for test matrix")
    serialnumber = models.CharField(unique=True, db_index=True, max_length=20, blank=False)
    partnumber_id = models.ForeignKey("PartNumber", on_delete= models.CASCADE)
    overall_outcome  = models.BooleanField() 
    date_created = models.DateTimeField(auto_now=True)
    def __str__(self):
        test_results_overall = [
            self.id,
            self.serialnumber,
            self.partnumber_id,
            self.overall_outcome,
            self.date_created,      
        ]     
        return test_results_overall


class TestResultsProcess(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, help_text="ID for test matrix")
    overall_TR_id = models.ForeignKey("TestResultsOverAll", on_delete= models.CASCADE)
    fprocess_step = models.IntegerField(blank=False)
    station_id = models.IntegerField(blank=False)
    process_outcome  = models.BooleanField()
    employee_id = models.IntegerField(blank=False)
    test_time = models.TimeField()  #TODO (blank=True)
    evidence_link = models.CharField(max_length=100, blank=False)
    date_created = models.DateTimeField(auto_now=True)
    def __str__(self):
        test_results_process = [
            self.id,
            self.overall_TR_id,
            self.fprocess_step,
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
    process_TR_id = models.ForeignKey("TestResultsProcess", on_delete= models.CASCADE)
    test_id = models.IntegerField(blank=False)
    test_name  = models.CharField(max_length=20, blank=False)
    spec_type =  models.CharField(max_length=20, blank=False)
    max_value = models.CharField(max_length=20)
    min_value = models.CharField(max_length=20)
    expected_value = models.CharField(max_length=20)
    result = models.CharField(max_length=20)
    tc_outcome = models.BooleanField()
    date_created = models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = ('test_id', 'test_name')
    def __str__(self):
        test_case_results = [
            self.id,
            self.process_TR_id,
            self.test_id,
            self.test_name,
            self.spec_type,
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
    partnumber_id = models.IntegerField(db_index=True, blank=False)
    fprocess_step = models.IntegerField(db_index=True, blank=False)
    station_id = models.IntegerField(blank=False)
    employee_id = models.IntegerField(blank=False)
    evidence_link = models.CharField(max_length=100, blank=False)
    test_id = models.IntegerField(blank=False)
    test_name  = models.CharField(db_index=True, max_length=20, blank=False)
    spec_type =  models.CharField(max_length=20, blank=False)
    max_value = models.CharField(max_length=20)
    min_value = models.CharField(max_length=20)
    expected_value = models.CharField(max_length=20)
    result = models.CharField(max_length=20)
    test_time = models.TimeField()  #TODO (blank=True)
    tc_outcome = models.BooleanField()
    date_created = models.DateTimeField(auto_now=True)
    def __str__(self):
        test_results_achieve = [
            self.id,
            self.serialnumber,
            self.partnumber_id,
            self.fprocess_step,
            self.station_id,
            self.employee_id,
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
       

class FlowMatrix(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, help_text="ID for test matrix")
    flow_name =  models.CharField(db_index=True, max_length=20, blank=False)
    partnumber_id = models.ForeignKey("PartNumber", on_delete= models.CASCADE)
    employee_id = models.IntegerField(blank=False)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField()   #TODO (blank=True)
    def __str__(self):
        flow_matrix = [
            self.id,
            self.flow_name,
            self.partnumber_id,
            self.employee_id,
            self.date_created,
            self.date_updated,     
        ]     
        return flow_matrix

class FlowTable(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, help_text="ID for test matrix")
    flow_name =  models.CharField(db_index=True, max_length=20, blank=False)
    fprcess_Id = models.IntegerField(blank=False)
    fprocess_step = models.IntegerField(blank=False)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField()   #TODO (blank=True)
    class Meta:
        unique_together = ('flow_name', 'fprcess_Id')
    def __str__(self):
        flow_table = [
            self.id,
            self.flow_name,
            self.fprcess_Id,
            self.fprocess_step,
            self.date_created,
            self.date_updated,     
        ]      
        return flow_table


class FlowStatus(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, help_text="ID for test matrix")
    serialnumber = models.CharField(db_index=True, unique=True, max_length=20, blank=False)
    partnumber_id = models.ForeignKey("PartNumber", on_delete= models.CASCADE)
    flow_name =  models.CharField(max_length=20, blank=False)
    fprcess_Id = models.IntegerField(blank=False)
    current_fprocess_step = models.IntegerField(blank=False)
    flow_status = models.BooleanField()
    employee_id = models.IntegerField(blank=False)
    date_arrival = models.DateTimeField(auto_now=True)
    date_departure = models.DateTimeField()  #TODO (blank=True)
    def __str__(self):
        flow_status = [
            self.id,
            self.serialnumber,
            self.partnumber_id,
            self.flow_name,
            self.fprcess_Id,
            self.current_fprocess_step,
            self.flow_status,
            self.employee_id,
            self.date_arrival,
            self.date_departure,     
        ]      
        return flow_status  


class FlowHistory(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, help_text="ID for test matrix")
    serialnumber = models.CharField(db_index=True, max_length=20, blank=False)
    partnumber_id = models.IntegerField(db_index=True, blank=False)
    flow_name =  models.CharField(max_length=20, blank=False)
    fprcess_Id = models.IntegerField(blank=False)
    fprocess_step = models.IntegerField(blank=False)
    flow_status = models.BooleanField()
    employee_id = models.IntegerField(blank=False)
    date_arrival = models.DateTimeField(auto_now=True)
    date_departure = models.DateTimeField()   #TODO (blank=True)
    def __str__(self):
        flow_status = [
            self.id,
            self.serialnumber,
            self.flow_name,
            self.fprcess_Id,
            self.fprocess_step,
            self.flow_status,
            self.employee_id,
            self.date_arrival,
            self.date_departure,     
        ]      
        return flow_status  
