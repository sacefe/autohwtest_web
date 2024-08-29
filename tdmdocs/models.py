from django.db import models
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
    date_created = models.DateTimeField() #blank=True)
    def __str__(self):
        partnumbres = [
             self.id,
        #     #self.uuid,
             self.partnumber,
             self.description,
             self.date_created,          
        ]
        return partnumbres
    
    
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
    test_time = models.TimeField() #blank=True) 
    tc_outcome = models.BooleanField()
    date_created = models.DateTimeField() #(blank=True)
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
       