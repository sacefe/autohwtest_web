from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from authentication.forms import LoginForm
from django.contrib.auth import logout

# Create your views here.

def logout_view(request):
  logout(request)
  return redirect('/accounts/login/')

# Authentication
class UserLoginView(LoginView):
  template_name = 'accounts/login.html'
  form_class = LoginForm