from django.shortcuts import render
from django.utils import timezone 
from django.views.generic import ListView
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status, serializers
from rest_framework.response import Response
from tdm.models import PartNumber
from tdm.serializers import PatrNumberSerializer


# Create your views here.

# Example: Dummy part numer for demonstration TODO Delete 
pn = 'halcon-00'
qty = 3
def run_create_partnumbers(request):
    # Save part number to database
    for i in range(qty):
        partnumbers = PartNumber(partnumber=pn+str(i), 
                                 product_description="description " + pn + str(i), 
                                 date_created=timezone.now() )
        partnumbers.save()
    return render(request, 'create_part_numbers.html', {'partnumbers': partnumbers})

# Get DB part numbers for - TODO moved to dashboard
class PartNumberViewAll(ListView): # APIView):
    model  = PartNumber #.objects.all()
    template_name= 'view_part_number_all.html'
    context_object_name = 'partnumbers'


"""
CRUD List Part Number Operation with Django Rest Framework 
"""
class PartNumberListCRUD(APIView):
    """
    GET   (QUERY All records)
        All items: http://127.0.0.1:8000/api/part-numbers/
    """
    def get(self, request, format=None): 
        # checking for the parameters from the URL
        items= PartNumber.objects.all()
         # if there is something in items else raise error
        if items:
            serializers =  PatrNumberSerializer(items, many=True)
            return Response({'Status': 'Success', "partnumbers": serializers.data}, 
                        status=status.HTTP_200_OK )
        else:    
            return Response({'Status': 'error', "partnumbers": serializers.data}, 
                        status=status.HTTP_400_BAD_REQUEST )

    """
    POST   (CREATE new record(s))
        New Item  : http://127.0.0.1:8000/api/part-numbers/
        POST:          
        [ {
            "partnumber": "halcon-006",
            "product_description": "description halcon-006"
          },
          {
            "partnumber": "halcon-007",
            "product_description": "description halcon-007"
        } ]
        fields id, uui and date_created auto-created
    """
    def post(self, request, format=None):
        item = PatrNumberSerializer(data=request.data, many=True)  #input
        # if valid update changes
        if item.is_valid():
            item.save()
            return Response({"Status": "sucess", "data": item.data }, status= status.HTTP_200_OK )
        else:
            return Response({"Status": "error", "data": item.errors}, status= status.HTTP_400_BAD_REQUEST)



"""
CRUD details Part Number Operation with Django Rest Framework 
"""
class PartNumberDetailsCRUD(APIView):
    def get_object(self, partnumber):
        try:
            return PartNumber.objects.get(partnumber=partnumber)
        except PartNumber.DoesNotExist:
            raise Http404

    """
    GET   (QUERY Individual records)
    Item 2   : http://127.0.0.1:8000/api/part-numbers/partnumber=halcon-002
    """
    def get(self, request, partnumber, format=None): 
        # item= PartNumber.objects.get(partnumber= partnumber) 
        item = self.get_object(partnumber)   
        # if there is something in items else raise error
        if item:
            serializers =  PatrNumberSerializer(item)
            return Response({'Status': 'Success', "partnumber": serializers.data}, 
                        status=status.HTTP_200_OK )
        else:    
            return Response({'Status': 'error', "partnumber": serializers.data}, 
                        status=status.HTTP_400_BAD_REQUEST )

    """
    PUT   (Modify a record, only if exist)
        Item 2   : http://127.0.0.1:8000/api/part_numbers/partnumber=halcon-002
        
    """
    def put(self, request, partnumber, format= None):
        item = self.get_object(partnumber)
        serializer = PatrNumberSerializer(instance=item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Status": "sucess", "data": serializer.data }, 
                            status= status.HTTP_200_OK )
        else:
            return Response({"Status": "error", "data": serializer.data },
                             status=status.HTTP_400_BAD_REQUEST )
                             


    """
    DELETE   (Remove a record, if not exist cerate  a new one)
        Item 2   : http://127.0.0.1:8000/api/part_numbers/partnumber=halcon-002
        
    """
    def delete(self, request, partnumber, format= None):
        item = self.get_object(partnumber)
        item.delete()
        return Response({"Status": "sucess"}, 
                        status= status.HTTP_204_NO_CONTENT )
                             