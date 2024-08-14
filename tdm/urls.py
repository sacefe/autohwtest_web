from django.urls import path
from tdm import views

urlpatterns = [
    path('run_create_partnumbers/', views.run_create_partnumbers , name= 'run_create_partnumbers'),
    path('view_part_numbers_all/', views.PartNumberViewAll.as_view(), name='view_part_numbers_all' ),
    # API's  class-based
    path('partnumbers/', views.PartNumberListCRUD.as_view()),
    path('partnumbers/item=<str:item>/', views.PartNumberDetailsCRUD.as_view()),
    path('stations/', views.StationsListCRUD.as_view()),
    path('stations/item=<str:item>/', views.StationsDetailsCRUD.as_view()),
    path('testmatrix/', views.TestMatrixListCRUD.as_view()),
    path('testmatrix/item=<str:item>/', views.TestMatrixDetailsCRUD.as_view()),
    path('testplans/', views.TestPlanListCRUD.as_view()),
    path('testplans/item=<str:item>/', views.TestPlanDetailsCRUD.as_view()),    
]

