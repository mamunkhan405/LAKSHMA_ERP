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
        return render(request, 'Home/home.html')
    
class EmployeeInfo(View):
    def get(self, request):
        # Employee_information = Employee_Info.objects.all()
        # context = {'Employee_information':Employee_information}
        return render(request, 'Order_Entry/order_entry.html')

    # def post(self, request):
    #     emp_Image = request.FILES['emp_Image']

    #     emp_first_Name = request.POST['emp_first_Name']
    #     emp_middle_Name = request.POST['emp_middle_Name']
    #     emp_last_Name = request.POST['emp_last_Name']

    #     emp_join_Date = request.POST['emp_join_Date']
    #     emp_confirm_Date = request.POST['emp_confirm_Date']
    #     emp_birth_Date = request.POST['emp_birth_Date']

    #     emp_father_Name = request.POST['emp_father_Name']
    #     emp_mother_Name = request.POST['emp_mother_Name']

    #     emp_category = request.POST['emp_category']
    #     emp_blood_group = request.POST['emp_blood_group']
    #     emp_marital_status = request.POST['emp_marital_status']
    #     emp_spouse_Name = request.POST['emp_spouse_Name']
    #     emp_present_number = request.POST['emp_present_Number']
    #     emp_national_id_no = request.POST['emp_national_No']
    #     emp_designation = request.POST['emp_designation']
    #     emp_company = request.POST['emp_company']

    #     emp_bank_name = request.POST['emp_bank_name']
    #     emp_bankaccount_number = request.POST['emp_bankaccount_number']
    #     emp_mobilebanking_Name = request.POST['emp_mobilebanking_Name']
    #     emp_mobileaccount_number = request.POST['emp_mobileaccount_number']

    #     emp_status = request.POST['emp_status']
    #     emp_group = request.POST['emp_group']
    #     emp_reporting_manager = request.POST['emp_reporting_Manager']
    #     emp_gender = request.POST['emp_gender']
    #     emp_official_email = request.POST['emp_official_email']
    #     emp_personal_email = request.POST['emp_personal_email']

    #     emp_present_address = request.POST['emp_present_Address']
    #     emp_permanent_address = request.POST['emp_permanent_Address']
    #     emp_division = request.POST['emp_division']
    #     emp_department = request.POST['emp_department']
    #     emp_sub_department = request.POST['emp_sub_department']
    #     emp_section = request.POST['emp_section']
    #     emp_sub_section = request.POST['emp_sub_section']
    #     emp_location = request.POST['emp_location']

    #     Employee_information = Employee_Info(
    #         emp_Image =emp_Image,

    #         emp_first_Name=emp_first_Name,
    #         emp_middle_Name=emp_middle_Name,
    #         emp_last_Name=emp_last_Name,

    #         emp_join_Date=emp_join_Date,
    #         emp_confirm_Date=emp_confirm_Date,
    #         emp_birth_Date=emp_birth_Date,

    #         emp_father_Name=emp_father_Name,
    #         emp_mother_Name=emp_mother_Name,

    #         emp_category=emp_category,
    #         emp_blood_group=emp_blood_group,
    #         emp_marital_status=emp_marital_status,
    #         emp_spouse_Name=emp_spouse_Name,
    #         emp_present_number=emp_present_number,
    #         emp_national_id_no=emp_national_id_no,
    #         emp_designation=emp_designation,
    #         emp_company=emp_company,

    #         emp_bank_name=emp_bank_name,
    #         emp_bankaccount_number=emp_bankaccount_number,
    #         emp_mobilebanking_Name=emp_mobilebanking_Name,
    #         emp_mobileaccount_number=emp_mobileaccount_number,

    #         emp_status=emp_status,
    #         emp_group=emp_group,
    #         emp_reporting_manager=emp_reporting_manager,
    #         emp_gender=emp_gender,
    #         emp_official_email=emp_official_email,
    #         emp_personal_email=emp_personal_email,

    #         emp_present_address=emp_present_address,
    #         emp_permanent_address=emp_permanent_address,
    #         emp_division=emp_division,
    #         emp_department=emp_department,
    #         emp_sub_department=emp_sub_department,
    #         emp_section=emp_section,
    #         emp_sub_section=emp_sub_section,
    #         emp_location=emp_location,
    #      )
    #     Employee_information.save()
    #     messages.success(
    #         request, 'Congratulations! Employee information has been Added Successfully...')
    #     Employee_information = Employee_Info.objects.all()
    #     params = {'Employee_information':Employee_information}
    #     return render(request, 'Forms/Add_Employee/employeeInfo.html', params)

class MainFabric(View):
    def get(self, request):
        return render(request, 'Order_Entry/main_fabric.html')

class SampleRequisition(View):
    def get(self, request):
        return render(request, 'Order_Entry/sample_req.html')
    
class OrderUpdate(View):
    def get(self, request):
        return render(request, 'Order_Entry/order_update.html')
    
class BuyerQuotation(View):
    def get(self, request):
        return render(request, 'Order_Entry/buyer_quote.html')
    
class QuotationEnquiry(View):
    def get(self, request):
        return render(request, 'Order_Entry/quote_enquiry.html')
    
class ColorSizeBreakdown(View):
    def get(self, request):
        return render(request, 'Order_Entry/color_size.html')
    
    
    
    

