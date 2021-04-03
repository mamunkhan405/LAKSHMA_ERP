from django.contrib import admin
from django.urls import path, include
from . import views
from django.views import View
from .views import *
# from Forms.views import advanceSearch

urlpatterns = [
    path('', Home.as_view(), name='Home'),

]
