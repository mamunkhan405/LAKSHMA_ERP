from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register((
    LibBuyer,
    LibStyle,
    LibCompany,
    LibDepartment,
    LibDivision,
    LibSubDepartment,
    LibProductCate,
    LibSeason,
    LibRegion,
    LibAgent,
    LibClient,
    LibUnit,
    HRmEmployee,
    LibCurrency,   
    InvProductInfo,  
    LibColor,   
    LibSize,  
    LibCountry, 
    OrderEntryInfo,
    OmPoCostDetail,
    OmPoBreakDown,
    OmPoDetailsMaster,  
    WoPOCountryDetails, 
    OmPoColorSizeBreakDown,
    OmPoColorInfo,
    OmPoSampleInfo,
    OmPoLabdipInfo,
    OmPoAccesoriesInfo,)
)

