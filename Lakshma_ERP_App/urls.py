from django.contrib import admin
from django.urls import path, include
from . import views
from django.views import View
from .views import *
# from Forms.views import advanceSearch

urlpatterns = [
    path('', Home.as_view(), name='Home'),
    path('employeeInfo/', EmployeeInfo.as_view(), name='EmployeeInfo'),
    path('main_fabric/', MainFabric.as_view(), name='Main_fabric'),
    path('sample_req/', SampleRequisition.as_view(), name='Sample_req'),
    path('order_update/', OrderUpdate.as_view(), name='Order_update'),
    path('buyer_quote/', BuyerQuotation.as_view(), name='Buyer_quote'),
    path('quote_enquiry/', QuotationEnquiry.as_view(), name='Quote_enquiry'),
    path('color_size/', ColorSizeBreakdown.as_view(), name='Color_size'),
    

]
