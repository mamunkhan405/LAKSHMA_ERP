from django.contrib import admin
from django.urls import path, include
from . import views
from django.views import View
from .views import *
# from Forms.views import advanceSearch

urlpatterns = [
    path('', Home.as_view(), name='Home'),
    path('order_entry_form/', OrderEntry.as_view(), name='OrderEntry'),
    path('knitt_dying/', KnittDying.as_view(), name='KnittDying'),
    path('sample_info/', SampleInfo.as_view(), name='SampleInfo'),
    path('order_update/', OrderUpdate.as_view(), name='Order_update'),
    path('lapdip_info/', LapdipInfo.as_view(), name='LapdipInfo'),
    path('quote_enquiry/', QuotationEnquiry.as_view(), name='Quote_enquiry'),
    path('access_info/', AccessoriesInfo.as_view(), name='AccessoriesInfo'),
    

]
