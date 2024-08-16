from django.urls import path
from tdm import views

urlpatterns = [
    # path('run_create_partnumbers/', views.run_create_partnumbers , name= 'run_create_partnumbers'),
    # path('view_part_numbers_all/', views.PartNumberViewAll.as_view(), name='view_part_numbers_all' ),
    # API's  class-based
 #   path('user/', views.UserDetailsREAD.as_view()),
    path('partnumbers/', views.PartNumberListCRUD.as_view()),
    path('partnumbers/<str:item>/', views.PartNumberDetailsCRUD.as_view()),
    path('stationsiblings/', views.StationSiblingsListCRUD.as_view()),
    path('stationsiblings/<str:item>/', views.StationSiblingsDetailsCRUD.as_view()),
    path('stations/', views.StationsListCRUD.as_view()),
    path('stations/<str:item>/', views.StationsDetailsCRUD.as_view()),
    path('testmatrix/', views.TestMatrixListCRUD.as_view()),
    path('testmatrix/<str:item>', views.TestMatrixDetailsCRUD.as_view()),
    path('testplans/', views.TestPlanListCRUD.as_view()),
    path('testplans/<str:item>/', views.TestPlanDetailsCRUD.as_view()),
    path('spectype/', views.SpecTypeListCRUD.as_view()),
    path('spectype/<str:item>/', views.SpecTypeDetailsCRUD.as_view()),
    path('flowprocess-steps/', views.FlowProcessStepListCRUD.as_view()),
    path('flowprocess-steps/<str:item>/', views.FlowProcessStepDetailsCRUD.as_view()), 
    path('flowtable/', views.FlowTableListCRUD.as_view()),
    path('flowtable/<str:item>/', views.FlowTableDetailsCRUD.as_view()),    
    path('flowmatrix/', views.FlowMatrixListCRUD.as_view()),
    path('flowmatrix/<str:item>/', views.FlowMatrixDetailsCRUD.as_view()),
    #Not Testtes
    path('testresults_overall/', views.TestResultsOverAllListCRUD.as_view()),
    path('testresults_overall/<str:item>/', views.TestResultsOverAllDetailsCRUD.as_view()),

    path('testresults_process/', views.TestResultsProcessListCRUD.as_view()),
    path('testresults_process/<str:item>/', views.TestResultsProcessDetailsCRUD.as_view()),

    path('testcaseresults/', views.TestCaseResultsListCRUD.as_view()),
    path('testcaseresults/<str:item>/', views.TestCaseResultsDetailsCRUD.as_view()),

    path('testresults_achieve/', views.TestResulstAchieveListCRUD.as_view()),
    path('testresults_achieve/<str:item>/', views.TTestResulstAchieveDetailsCRUD.as_view()),

    path('flowstatus/', views.FlowStatusListCRUD.as_view()),
    path('flowstatus/<str:item>/', views.FlowStatusDetailsCRUD.as_view()),

    path('flowhistory/', views.FlowHistoryListCRUD.as_view()),
    path('flowhistory/<str:item>/', views.FlowHistoryDetailsCRUD.as_view()),
]


