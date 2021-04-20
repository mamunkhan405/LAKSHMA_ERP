from django.contrib import admin
from django.urls import path, include
from . import views
from django.views import View
from .views import *
# from Forms.views import advanceSearch

urlpatterns = [
    path('', Home.as_view(), name='Home'),
    path('order_entry_form/', OrderEntry.as_view(), name='OrderEntry'),
    path('po_detail/', PoDetails.as_view(), name='PoDetails'),
    path('cost_info_form/', CostInfo.as_view(), name='Costinfo'),
    path('po_breakdown/', POBreakdownInfo.as_view(), name='POBreakdownInfo'),
    path('po_country_detail/', PoCountryInfo.as_view(), name='PoCountryInfo'),
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
    path('lib_company/', LibCompanyInfo.as_view(), name='LibCompany'),
    path('lib_department/', LibDepartmentInfo.as_view(), name='LibDepartmentInfo'),
    path('lib_division/', LibDivisionInfo.as_view(), name='LibDivisionInfo'),
    
    path('lib_sub_dept/', LibSubDept.as_view(), name='LibSubDept'),
    path('lib_prod_cat/', LibProdCat.as_view(), name='LibProdCat'),
    path('libseason/', LibSeasonInfo.as_view(), name='LibSeasonInfo'),
    path('libregion/', LibRegionInfo.as_view(), name='LibRegionInfo'),
    
    path('lib_agent/', LibAgentInfo.as_view(), name='LibAgentInfo'),
    path('lib_client/', LibClientInfo.as_view(), name='LibClientInfo'),
    path('lib_unit/', LibUnitInfo.as_view(), name='LibUnitInfo'),
    path('hr_employee/', HrEmployeeForm.as_view(), name='HrEmployeeForm'),
    path('lib_currency/', LibCurrencyInfo.as_view(), name='LibCurrencyInfo'),
    path('inv_prod_info/', INV.as_view(), name='INV'),
    path('lib_color/', LibColorInfo.as_view(), name='LibColorInfo'),
    path('lib_size/', LibSizeInfo.as_view(), name='LibSizeInfo'),
    path('lib_country/', LibCountryInfo.as_view(), name='LibCountryInfo'),
    

]
