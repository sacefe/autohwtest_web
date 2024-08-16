from typing import Any
from django.shortcuts import render
from django.utils import timezone 
from django.views.generic import ListView
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status, serializers
from rest_framework.response import Response
from tdm.models import (PartNumber, Stations, 
                        TestMatrix, TestPlan,
                        StationSiblings, FlowProcessStep,
                        SpecType, FlowTable,
                        FlowMatrix, TestResultsOverAll,
                        TestResultsProcess, TestCaseResults,
                        TestResulstAchieve, FlowStatus,
                        FlowHistory)
from tdm.serializers import (PartNumberSerializer, StationsSerializer, 
                             TestMatrixSerializer, TestPlanSerializer,
                             StationSiblingsSerializer, FlowProcessStepSerializer,
                             SpecTypeSerializer, FlowTableSerializer,
                             FlowMatrixSerializer, TestResultsOverAllSerializer,
                             TestResultsProcessSerializer, TestCaseResultsSerializer,
                             TestResulstAchieveSerializer, FlowStatusSerializer,
                             FlowHistorySerializer )


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
CRUD List/Details Station Operation with Django Rest Framework 
"""
class StationsListCRUD(TlistCRUD):
    def __init__(self):
            super().__init__(
            model_table=Stations,
            serializer_obj=StationsSerializer,
            order_by='station_name'
        )   

class StationsDetailsCRUD(TdetailsCRUD):
    def __init__(self):
        super().__init__(
            model_obj=Stations,
            serializer_obj=StationsSerializer,
        )
    def get_object(self, item):
        try:
            return Stations.objects.get(station_name=item)
        except self.model_obj.DoesNotExist:
            raise Http404


"""
CRUD List/Details Station Operation with Django Rest Framework 
"""
class StationSiblingsListCRUD(TlistCRUD):
    def __init__(self):
            super().__init__(
            model_table=StationSiblings,
            serializer_obj=StationSiblingsSerializer,
            order_by='id'            
        )   

class StationSiblingsDetailsCRUD(TdetailsCRUD):
    def __init__(self):
        super().__init__(
            model_obj=StationSiblings,
            serializer_obj=StationSiblingsSerializer,
            order_by='id'
        )
    def get_object(self, item):
        try:
            return StationSiblings.objects.get(id=item)
        except self.model_obj.DoesNotExist:
            raise Http404


"""
CRUD List/Details TestMatrix Operation with Django Rest Framework 
"""
class TestMatrixListCRUD(TlistCRUD):
    def __init__(self):
            super().__init__(
            model_table=TestMatrix,
            serializer_obj=TestMatrixSerializer,
            order_by='partnumber_fk'
        )          

class TestMatrixDetailsCRUD(TdetailsCRUD):
    def __init__(self):
        super().__init__(
            model_obj=TestMatrix,
            serializer_obj=TestMatrixSerializer
        )
    def get_object(self, item):
        try:
            item_arr = item.split(",")
            return TestMatrix.objects.get(partnumber_fk=item_arr[0],
                                          sibling_lname_fk=item_arr[1])
        except self.model_obj.DoesNotExist:
            raise Http404


"""
CRUD List/Details TestPlan Operation with Django Rest Framework 
"""
class TestPlanListCRUD(TlistCRUD):
    def __init__(self):
            super().__init__(
            model_table=TestPlan,
            serializer_obj=TestPlanSerializer,
            order_by='testplan_name'
        )

class TestPlanDetailsCRUD(TdetailsCRUD):
    def __init__(self):
        super().__init__(
            model_obj=TestPlan,
            serializer_obj=TestPlanSerializer,
        )
    def get_object(self, item):
        try:
            return TestPlan.objects.get(testplan_name=item)
        except self.model_obj.DoesNotExist:
            raise Http404


"""
CRUD List/Details TestPlan Operation with Django Rest Framework 
"""
class SpecTypeListCRUD(TlistCRUD):
    def __init__(self):
            super().__init__(
            model_table=SpecType,
            serializer_obj=SpecTypeSerializer,
            order_by='id'
        )

class SpecTypeDetailsCRUD(TdetailsCRUD):
    def __init__(self):
        super().__init__(
            model_obj=SpecType,
            serializer_obj=SpecTypeSerializer,
        )
    def get_object(self, item):
        try:
            return SpecType.objects.get(id=item)
        except self.model_obj.DoesNotExist:
            raise Http404


"""
CRUD List/Details FlowProcessStep Operation with Django Rest Framework 
"""
class FlowProcessStepListCRUD(TlistCRUD):
    def __init__(self):
            super().__init__(
            model_table=FlowProcessStep,
            serializer_obj=FlowProcessStepSerializer,
            order_by='id'
        )

class FlowProcessStepDetailsCRUD(TdetailsCRUD):
    def __init__(self):
        super().__init__(
            model_obj=FlowProcessStep,
            serializer_obj=FlowProcessStepSerializer,
        )
    def get_object(self, item):
        try:
            return FlowProcessStep.objects.get(id=item)
        except self.model_obj.DoesNotExist:
            raise Http404



"""
CRUD List/Details FlowTable Operation with Django Rest Framework 
"""
class FlowTableListCRUD(TlistCRUD):
    def __init__(self):
            super().__init__(
            model_table=FlowTable,
            serializer_obj=FlowTableSerializer,
            order_by='flow_name'
        )

class FlowTableDetailsCRUD(TdetailsCRUD):
    def __init__(self):
        super().__init__(
            model_obj=FlowTable,
            serializer_obj=FlowTableSerializer,
        )
    def get_object(self, item):
        try:
            return FlowTable.objects.get(flow_name=item)
        except self.model_obj.DoesNotExist:
            raise Http404


"""
CRUD List/Details FlowMatrix Operation with Django Rest Framework 
"""
class FlowMatrixListCRUD(TlistCRUD):
    def __init__(self):
            super().__init__(
            model_table=FlowMatrix,
            serializer_obj=FlowMatrixSerializer,
            order_by='partnumber_id'
        )
                        
class FlowMatrixDetailsCRUD(TdetailsCRUD):
    def __init__(self):
        super().__init__(
            model_obj=FlowMatrix,
            serializer_obj=FlowMatrixSerializer,
        )
    def get_object(self, item):
        try:
            return FlowMatrix.objects.get(partnumber_id=item)
        except self.model_obj.DoesNotExist:
            raise Http404


# NOT TESTED ====>
"""
CRUD List/Details TestResultsOverAll Operation with Django Rest Framework 
"""
class TestResultsOverAllListCRUD(TlistCRUD):
    def __init__(self):
            super().__init__(
            model_table=TestResultsOverAll,
            serializer_obj=TestResultsOverAllSerializer,
            order_by='serialnumber'
        )
            
class TestResultsOverAllDetailsCRUD(TdetailsCRUD):
    def __init__(self):
        super().__init__(
            model_obj=TestResultsOverAll,
            serializer_obj=TestResultsOverAllSerializer,
        )
    def get_object(self, item):
        try:
            return TestResultsOverAll.objects.get(serialnumber=item)
        except self.model_obj.DoesNotExist:
            raise Http404




"""
CRUD List/Details TestResultsProcess Operation with Django Rest Framework 
"""
class TestResultsProcessListCRUD(TlistCRUD):
    def __init__(self):
            super().__init__(
            model_table=TestResultsProcess,
            serializer_obj=TestResultsProcessSerializer,
            order_by='overall_TR_fk'
        )
            
class TestResultsProcessDetailsCRUD(TdetailsCRUD):
    def __init__(self):
        super().__init__(
            model_obj=TestResultsProcess,
            serializer_obj=TestResultsProcessSerializer,
        )
    def get_object(self, item):
        try:
            return TestResultsProcess.objects.get(overall_TR_fk=item)
        except self.model_obj.DoesNotExist:
            raise Http404


"""
CRUD List/Details TestCaseResults Operation with Django Rest Framework 
"""
class TestCaseResultsListCRUD(TlistCRUD):
    def __init__(self):
            super().__init__(
            model_table=TestCaseResults,
            serializer_obj=TestCaseResultsSerializer,
            order_by='process_TR_fk'
        )
            
class TestCaseResultsDetailsCRUD(TdetailsCRUD):
    def __init__(self):
        super().__init__(
            model_obj=TestCaseResults,
            serializer_obj=TestCaseResultsSerializer,
        )
    def get_object(self, item):
        try:
            return TestCaseResults.objects.get(process_TR_fk=item)
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
                

"""
CRUD List/Details FlowStatus Operation with Django Rest Framework 
"""
class FlowStatusListCRUD(TlistCRUD):
    def __init__(self):
            super().__init__(
            model_table=FlowStatus,
            serializer_obj=FlowStatusSerializer,
            order_by='serialnumber'
        )
            
class FlowStatusDetailsCRUD(TdetailsCRUD):
    def __init__(self):
        super().__init__(
            model_obj=FlowStatus,
            serializer_obj=FlowStatusSerializer,
        )
    def get_object(self, item):
        try:
            return FlowStatus.objects.get(serialnumber=item)
        except self.model_obj.DoesNotExist:
            raise Http404


"""
CRUD List/Details FlowHistory Operation with Django Rest Framework 
"""
class FlowHistoryListCRUD(TlistCRUD):
    def __init__(self):
            super().__init__(
            model_table=FlowHistory,
            serializer_obj=FlowHistorySerializer,
            order_by='serialnumber'
        )
            
class FlowHistoryDetailsCRUD(TdetailsCRUD):
    def __init__(self):
        super().__init__(
            model_obj=FlowHistory,
            serializer_obj=FlowHistorySerializer,
        )
    def get_object(self, item):
        try:
            return FlowHistory.objects.get(serialnumber=item)
        except self.model_obj.DoesNotExist:
            raise Http404
                                   


################# ORIGINAL ##########################
# """
# CRUD List PartNumbers Operation with Django Rest Framework 
# """
# class PartNumberListCRUD(APIView):
#     """
#     GET   (QUERY All records)
#         All items: http://127.0.0.1:8000/api/part-numbers/
#     """
#     def get(self, request, format=None): 
#         # checking for the parameters from the URL
#         items= PartNumber.objects.all()
#          # if there is something in items else raise error
#         if items:
#             serializers =  PartNumberSerializer(items, many=True)
#             return Response({'Status': 'Success', "partnumbers": serializers.data}, 
#                         status=status.HTTP_200_OK )
#         else:    
#             return Response({'Status': 'error', "partnumbers": serializers.data}, 
#                         status=status.HTTP_400_BAD_REQUEST )

#     """
#     POST   (CREATE new record(s))
#         New Item  : http://127.0.0.1:8000/api/part-numbers/
#         POST:          
#         [ {
#             "partnumber": "halcon-006",
#             "description": "description halcon-006"
#           },
#           {
#             "partnumber": "halcon-007",
#             "description": "description halcon-007"
#         } ]
#         fields id, uui and date_created auto-created
#     """
#     def post(self, request, format=None):
#         item = PartNumberSerializer(data=request.data, many=True)  #input
#         # if valid update changes
#         if item.is_valid():
#             item.save()
#             return Response({"Status": "sucess", "data": item.data }, status= status.HTTP_200_OK )
#         else:
#             return Response({"Status": "error", "data": item.errors}, status= status.HTTP_400_BAD_REQUEST)


# """
# CRUD details PartNumber Operation with Django Rest Framework 
# """
# class PartNumberDetailsCRUD(APIView):
#     def get_object(self, partnumber):
#         try:
#             return PartNumber.objects.get(partnumber=partnumber)
#         except PartNumber.DoesNotExist:
#             raise Http404

#     """
#     GET   (QUERY Individual records)
#     Item 2   : http://127.0.0.1:8000/api/part-numbers/partnumber=halcon-002
#     """
#     def get(self, request, partnumber, format=None): 
#         # item= PartNumber.objects.get(partnumber= partnumber) 
#         item = self.get_object(partnumber)   
#         # if there is something in items else raise error
#         if item:
#             serializers =  PartNumberSerializer(item)
#             return Response({'Status': 'Success', "partnumber": serializers.data}, 
#                         status=status.HTTP_200_OK )
#         else:    
#             return Response({'Status': 'error', "partnumber": serializers.data}, 
#                         status=status.HTTP_400_BAD_REQUEST )

#     """
#     PUT   (Modify a record, only if exist)
#         Item 2   : http://127.0.0.1:8000/api/part_numbers/partnumber=halcon-002
        
#     """
#     def put(self, request, partnumber, format= None):
#         item = self.get_object(partnumber)
#         serializer = PartNumberSerializer(instance=item, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"Status": "sucess", "data": serializer.data }, 
#                             status= status.HTTP_200_OK )
#         else:
#             return Response({"Status": "error", "data": serializer.data },
#                              status=status.HTTP_400_BAD_REQUEST )
                             

#     """
#     DELETE   (Remove a record, if not exist cerate  a new one)
#         Item 2   : http://127.0.0.1:8000/api/part_numbers/partnumber=halcon-002
        
#     """
#     def delete(self, request, partnumber, format= None):
#         item = self.get_object(partnumber)
#         item.delete()
#         return Response({"Status": "sucess"}, 
#                         status= status.HTTP_204_NO_CONTENT )

#################################################################
#     CREATE data in DB  directhly
# Create your views here.

# # Example: Dummy part numer for demonstration TODO Delete 
# pn = 'halcon-00'
# qty = 3
# def run_create_partnumbers(request):
#     # Save part number to database
#     for i in range(qty):
#         partnumbers = PartNumber(partnumber=pn+str(i), 
#                                  description="description " + pn + str(i), 
#                                  date_created=timezone.now() )
#         partnumbers.save()
#     return render(request, 'create_part_numbers.html', {'partnumbers': partnumbers})

# # Get DB part numbers for - TODO moved to dashboard
# class PartNumberViewAll(ListView): # APIView):
#     model  = PartNumber #.objects.all()
#     template_name= 'view_part_number_all.html'
#     context_object_name = 'partnumbers'
