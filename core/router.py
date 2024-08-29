from django.conf import settings
from local_settings import DATABASE_APPS_MAPPING

# TODO improve
# DATABASE_APPS_MAPPING = {'tdm': 'default',
#                         'tdmdocs':'mongo_db'} 

"""
Database Router for PostgreSQL and MongoDB
"""
class TestRouter:
    default_db = "default"  # defaul DB is tdm
    tdmdocs_db = "mongo_db"

    def db_for_read(self, model, **hints):
        model_name = model._meta.app_label
        if model_name == "tdmdocs":
            return self.tdmdocs_db
        else:
            return self.default_db
    
    def db_for_write(self, model, **hints):
        model_name = model._meta.app_label   #model_name
        if model_name == 'tdmdocs':
            return self.tdmdocs_db
        else:
            return self.default_db

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'tdmdocs':
            return db ==  self.tdmdocs_db 
        else:
            return db == self.default_db

    