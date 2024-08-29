from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from tdmdocs.models import (PartNumber,TestResulstAchieve)
from tdmdocs.serializers import (PartNumberSerializer, TestResulstAchieveSerializer)
                             

# Create your views here.

"""
CRUD List Template Operation with Django Rest Framework 
"""
class TlistCRUD(APIView):
    def __init__(self, model_table:object, serializer_obj:object, order_by):
        self.model_table = model_table
        self.serializer_obj = serializer_obj
        self.order_by = order_by

    """
    GET   (QUERY All records)
        Ex. All items: http://127.0.0.1:8000/api/part-numbers/
    """
    def get(self, request, format=None): 
        try:
            # checking for the parameters from the URL
            items= self.model_table.objects.all().order_by(self.order_by)
            # if there is something in items else raise error
            if items:
                    serializers =  self.serializer_obj(items, many=True)
                    return Response({'Status': 'Success', self.model_table._meta.object_name: serializers.data}, 
                            status=status.HTTP_200_OK )  
            else:  
                return Response({"Status": "error", "data": items}, status= status.HTTP_204_NO_CONTENT)
                # return Response({"Status": "error", "data": items}, status= status.HTTP_400_BAD_REQUEST)
        except self.model_table.DoesNotExist:
            raise Http404

    """
    POST   (CREATE new record(s))
        Ex. New Item  : http://127.0.0.1:8000/api/part-numbers/
        POST:          
        [ {
            "partnumber": "halcon-006",
            "description": "description halcon-006"
          },
          {
            "partnumber": "halcon-007",
            "description": "description halcon-007"
        } ]
        fields id, and date_created auto-created
    """
    def post(self, request, format=None):
        item = self.serializer_obj(data=request.data, many=True)  #input
        # if valid update changes
        if item.is_valid():
            item.save()
            return Response({"Status": "sucess", "data": item.data }, status= status.HTTP_200_OK )
        else:
            return Response({"Status": "error", "data": item.errors}, status= status.HTTP_400_BAD_REQUEST)



"""
CRUD details Template Operation with Django Rest Framework 
"""
class TdetailsCRUD(APIView):
    def __init__(self, model_obj:object, serializer_obj:object):
        self.model_obj = model_obj
        self.model_table = model_obj._meta.object_name
        self.serializer_obj = serializer_obj

    """
    function to be override by child
    """
    def get_object(self, item):
        pass

    """
    GET   (QUERY Individual records)
    Ex. Item 2   : http://127.0.0.1:8000/api/part-numbers/partnumber=halcon-002
    """
    def get(self, request, item, format=None): 
        item = self.get_object(item)
        # if there is something in items else raise error
        if item:
            serializers =  self.serializer_obj(item)
            return Response({'Status': 'Success', self.model_table: serializers.data}, 
                        status=status.HTTP_200_OK)
        else:    
            # return Response({'Status': 'error', self.model_table: serializers.data}, status=status.HTTP_400_BAD_REQUEST )
            return Response({"Status": "error", "data": item}, status= status.HTTP_204_NO_CONTENT)
            # return Response({"Status": "error", "data": items}, status= status.HTTP_400_BAD_REQUEST)
            
    """
    PUT   (Modify a record, only if exist)
    Ex. Item 2   : http://127.0.0.1:8000/api/part_numbers/partnumber=halcon-002    
    """
    def put(self, request, item, format= None):
        item = self.get_object(item)
        serializer = self.serializer_obj(instance=item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Status": "sucess", "data": serializer.data }, 
                            status= status.HTTP_200_OK )
        else:
            return Response({"Status": "error", "data": serializer.data },
                             status=status.HTTP_400_BAD_REQUEST )

    """
    POST    (CREATE one new record)
    Ex.  http://127.0.0.1:8000/api/part_numbers/partnumber    
    POST   (CREATE new record(s))
        Ex. New Item  : http://127.0.0.1:8000/api/part-numbers/
        POST:          
        {
            "partnumber": "halcon-006",
            "description": "description halcon-006"
        }
        other fields are auto-created
    """
    def post(self, request, item, format=None):
        item = self.serializer_obj(data=request.data) 
        # if valid update changes
        if item.is_valid():
            item.save()
            # item.create()
            return Response({"Status": "sucess", "data": item.data }, status= status.HTTP_200_OK )
        else:
            return Response({"Status": "error", "data": item.errors}, status= status.HTTP_400_BAD_REQUEST)

    """
    DELETE   (Remove a record, if not exist cerate  a new one)
    Ex Item 2   : http://127.0.0.1:8000/api/part_numbers/partnumber=halcon-002  
    """
    def delete(self, request, item, format= None):
        item = self.get_object(item)
        item.delete()
        return Response({"Status": "sucess"}, 
                        status= status.HTTP_204_NO_CONTENT )


"""
CRUD List/Details PartNumbers Operation with Django Rest Framework 
"""
class PartNumberListCRUD(TlistCRUD):
    def __init__(self):
            super().__init__(
            model_table=PartNumber,
            serializer_obj=PartNumberSerializer,
            order_by='partnumber'
        )

class PartNumberDetailsCRUD(TdetailsCRUD):
    def __init__(self):
        super().__init__(
            model_obj=PartNumber,
            serializer_obj=PartNumberSerializer,
        )
    def get_object(self, item):
        try:
            return PartNumber.objects.get(partnumber=item)
        except self.model_obj.DoesNotExist:
            raise Http404


"""
CRUD List/Details TestResulstAchieve Operation with Django Rest Framework 
"""
class TestResulstAchieveListCRUD(TlistCRUD):
    def __init__(self):
            super().__init__(
            model_table=TestResulstAchieve,
            serializer_obj=TestResulstAchieveSerializer,
            order_by='serialnumber'
        )
            
class TTestResulstAchieveDetailsCRUD(TdetailsCRUD):
    def __init__(self):
        super().__init__(
            model_obj=TestResulstAchieve,
            serializer_obj=TestResulstAchieveSerializer,
        )
    def get_object(self, item):
        try:
            return TestResulstAchieve.objects.get(serialnumber=item)
        except self.model_obj.DoesNotExist:
            raise Http404