from django.shortcuts import render
from .models import Creator
# Create your views here.

def index(request):
    return render(request,'mytfg/templates/index.html')