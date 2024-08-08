from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pages/index.html', { 'segment':'index' })

def tables(request):
    return render(request, 'pages/tables.html', { 'segment': 'index' })