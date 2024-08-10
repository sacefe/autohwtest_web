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
    id= models.AutoField(auto_created=True, primary_key=True, help_text="ID for specific test result")
    #uuid= models.UUIDField(default=RandomUUID, auto_created=True, help_text="UUID for part numder")
    partnumber= models.CharField(max_length=15, unique=True, blank=False, db_index=True)
    product_description= models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now=True)
    def __str__(self):
        partnumbres = [
            self.id,
            #self.uuid,
            self.partnumber,
            self.product_description,
            self.date_created,          
        ]     
        return partnumbres
    
    
#  TODO  First Create class diagram 
# """
# Part numbers using surrogate primary key PK integer
# GUID (UUID)  not required since PNs amount is small 
#    (uuid will cerate query delays and extra memory usage 128bits)
# but testplan must be unirque and database idnex 
# """
# class TestPlan(models.Model):
#     id= models.AutoField(auto_created=True, primary_key=True, help_text="ID for specific test result")
#     testplan= models.CharField(max_length=20)
#     test_name= models.CharField(max_length=20)
#     script= models.CharField(max_length=50)
#     dateCreated = models.DateTimeField(auto_now=True)
#     def __str__(self):
#         tesplans = [
#             self.id,
#             self.testplan,
#             self.group
#             selg.gid

#             self.test_name,
#             self.script,
#             self.dateCreated,          
#         ]     
#         return tesplans

# class PN_TP(models.Model):
#     id= models.AutoField(auto_created=True, primary_key=True, help_text="ID for specific test result")
#     PNkey = models.ForeignKey("PartNumber", on_delete= models.DO_NOTHING)
#     TPuuid= models.UUIDField(help_text="UUID for test Plan")
#     dateCreated = models.DateTimeField(auto_now=True)
#     def __str__(self):
#         tesplans = [
#             self.id,
#             self.PNkey,
#             self.TPuuid,
#             self.dateCreated,          
#         ]     
#         return tesplans