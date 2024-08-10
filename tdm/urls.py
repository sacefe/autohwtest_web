from django.urls import path
from tdm import views

urlpatterns = [
    path('run_create_partnumbers/', views.run_create_partnumbers , name= 'run_create_partnumbers'),
    path('view_part_numbers_all/', views.PartNumberViewAll.as_view(), name='view_part_numbers_all' ),
    # API's  class-based
   path('part-numbers/', views.PartNumberListCRUD.as_view()),
   path('part-numbers/partnumber=<str:partnumber>/', views.PartNumberDetailsCRUD.as_view())
]

