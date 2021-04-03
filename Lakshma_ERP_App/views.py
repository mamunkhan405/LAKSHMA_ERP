from django.shortcuts import render,redirect
from django import views
from django.views import View
from django.contrib import messages

# TESTING 
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, 'Forms/home.html')