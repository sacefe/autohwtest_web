from django.urls import path
from authentication import views

urlpatterns = [
    path('accounts/login/', views.UserLoginView.as_view(), name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
]
