from django.urls import path
from tdmdocs import views

urlpatterns = [
    path('partnumbers/', views.PartNumberListCRUD.as_view()),
    path('partnumbers/<str:item>/', views.PartNumberDetailsCRUD.as_view()),

    path('testresults_achieve/', views.TestResulstAchieveListCRUD.as_view()),
    path('testresults_achieve/<str:item>/', views.TTestResulstAchieveDetailsCRUD.as_view()),
]
