from django.contrib import admin
from django.urls import path, include
from . import views
from django.views import View
from .views import *
# from Forms.views import advanceSearch

urlpatterns = [
    path('', Home.as_view(), name='Home'),
    path('order_entry_form/', OrderEntry.as_view(), name='OrderEntry'),
    path('cost_info_form/', CostInfo.as_view(), name='Costinfo'),
    path('main_fabric/', MainFabric.as_view(), name='Main_fabric'),
    path('knitt_dying/', KnittDying.as_view(), name='KnittDying'),
    path('sample_info/', SampleInfo.as_view(), name='SampleInfo'),
    path('order_update/', OrderUpdate.as_view(), name='Order_update'),
    path('lapdip_info/', LapdipInfo.as_view(), name='LapdipInfo'),
    path('quote_enquiry/', QuotationEnquiry.as_view(), name='Quote_enquiry'),
    path('access_info/', AccessoriesInfo.as_view(), name='AccessoriesInfo'),
    
    path('list_view/', ListView.as_view(), name='List_view'),
    path('country_view/<int:id>/', CountryView.as_view(), name='Country_view'),
    path('lib_buyer/', RelatedLibBuyer.as_view(), name='RelatedLibBuyer'),
    path('lib_style/', RelatedLibStyle.as_view(), name='RelatedLibStyle'),
    path('lib_company/', LibCompany.as_view(), name='LibCompany'),
    path('lib_department/', LibDepartment.as_view(), name='LibDepartment'),
    path('lib_division/', LibDivision.as_view(), name='LibDivision'),
    
    path('lib_sub_dept/', LibSubDept.as_view(), name='LibSubDept'),
    path('lib_prod_cat/', LibProdCat.as_view(), name='LibProdCat'),
    path('libseason/', LibSeason.as_view(), name='LibSeason'),
    
    path('lib_agent/', LibAgent.as_view(), name='LibAgent'),
    path('lib_client/', LibClient.as_view(), name='LibClient'),
    path('lib_unit/', LibUnit.as_view(), name='LibUnit'),
    path('hr_employee/', HrEmployeeForm.as_view(), name='HrEmployeeForm'),
    path('lib_currency/', LibCurrency.as_view(), name='LibCurrency'),
    path('inv_prod_info/', INV.as_view(), name='INV'),
    path('lib_color/', LibColor.as_view(), name='LibColor'),
    path('lib_size/', LibSize.as_view(), name='LibSize'),
    path('lib_country/', LibCountry.as_view(), name='LibCountry'),
    

]
