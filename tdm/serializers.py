from rest_framework import serializers
from tdm.models import PartNumber


class PatrNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartNumber
        # fields = ('__all__')  
        fields = ('partnumber',
                  'product_description',
                  'date_created') 
