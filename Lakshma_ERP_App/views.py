from django.shortcuts import render,redirect
from django import views
from django.views import View
from django.contrib import messages

# TESTING 
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import *

# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, 'Home/home.html')
    
class OrderEntry(View):
    def get(self, request):
        # Employee_information = Employee_Info.objects.all()
        # context = {'Employee_information':Employee_information}
        return render(request, 'Order_Entry/order_entry_form.html')

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
class POBreakdownInfo(View):
    def get(self, request):
        return render(request, 'Order_Entry/po_breakdown.html')
    
    def post(self, request):
        job_no_mst = request.POST['job_no_mst']
        po_number = request.POST['po_number']
        po_quantity = request.POST['po_quantity']
        plan_quantity = request.POST['plan_quantity']
        shipped_date = request.POST['shipped_date']
        po_status = request.POST['po_status']
        is_deleted = request.POST['is_deleted']
        is_countable = request.POST['is_countable']
        is_projected = request.POST['is_projected']
        inserted_by = request.POST['inserted_by']
        insert_date = request.POST['insert_date']
        updated_by = request.POST['updated_by']
        update_date = request.POST['update_date']
        status_active = request.POST['status_active']
        is_locked = request.POST['is_locked']
        remarks = request.POST['remarks']

        po_breakdown_info = OmPoBreakDown(
            job_no_mst = job_no_mst,
            po_number = po_number,
            po_quantity = po_quantity,
            plan_quantity = plan_quantity,
            shipped_date = shipped_date,
            po_status = po_status,
            is_deleted = is_deleted,
            is_countable = is_countable,
            is_projected = is_projected,
            inserted_by = inserted_by,
            insert_date = insert_date,
            updated_by = updated_by,
            update_date = update_date,
            status_active = status_active,
            is_locked = is_locked,
            remarks = remarks

        )
        po_breakdown_info.save()
        messages.success(request, 'Congratulations! Po Breakdown information has been Added Successfully...')
        return render(request, 'Order_Entry/po_breakdown.html')

class PoCountryInfo(View):
    def get(self, request):
        po_numbers = OmPoBreakDown.objects.all()
        country_ids = LibCountry.objects.all()
        product_ids = InvProductInfo.objects.all()
        context = {
            'po_numbers': po_numbers,
            'country_ids': country_ids,
            'product_ids': product_ids
        }
        return render(request, 'Order_Entry/po_country_details.html', context)

    def post(self, request):
        job_no = request.POST['job_no']
        po_number = request.POST['po_number']
        country_id = request.POST['country_id']
        code = request.POST['code']
        product_id = request.POST['product_id']
        cut_off = request.POST['cut_off']
        po_quantity = request.POST['po_quantity']
        plan_quantity = request.POST['plan_quantity']
        shipped_date = request.POST['shipped_date']
        is_projected = request.POST['is_projected']
        projected_id = request.POST['projected_id']
        agent_name = request.POST['agent_name']
        exporting_item_catg = request.POST['exporting_item_catg']
        is_deleted = request.POST['is_deleted']
        status_active = request.POST['status_active']
        inserted_by = request.POST['inserted_by']
        insert_date = request.POST['insert_date']
        updated_by = request.POST['updated_by']
        update_date = request.POST['update_date']

        po_country_info = WoPOCountryDetails(
            job_no = job_no,
            po_number = po_number,
            country_id = country_id,
            code = code,
            product_id = product_id,
            cut_off = cut_off,
            po_quantity = po_quantity,
            plan_quantity = plan_quantity,
            shipped_date = shipped_date,
            is_projected = is_projected,
            projected_id = projected_id,
            agent_name = agent_name,
            exporting_item_catg = exporting_item_catg,
            is_deleted = is_deleted,
            status_active = status_active,
            inserted_by = inserted_by,
            insert_date = insert_date,
            updated_by = updated_by,
            update_date = update_date
        )
        po_country_info.save()
        messages.success(request, 'Congratulations! Po country details has been Added Successfully...')
        return render(request, 'Order_Entry/po_country_details.html')

class CostInfo(View):
    def get(self, request):
        
        return render(request, 'Order_Entry/cost_info.html')

class MainFabric(View):
    def get(self, request):
        return render(request, 'Order_Entry/main_fabric.html')

class ListView(View):
    def get(self, request):
        data = OmPoDetailsMaster.objects.all()
        context = {
            'data':data
        }
        return render(request, 'Order_Entry/list_view.html', context)

class CountryView(View):
    def get(self, request, id):
        d = WoPOCountryDetails.objects.get(id=id)
        print(d.id)
        context = {
            'd':d
        }
        return render(request, 'Order_Entry/country_view.html', context)

class KnittDying(View):
    def get(self, request):
        return render(request, 'Order_Entry/knitt_dying.html')

class SampleInfo(View):
    def get(self, request):
        return render(request, 'Order_Entry/sample_info.html')
    
    def post(self, request):
        job_no_mst = request.POST['job_no_mst']
        po_no_mst_id = request.POST['po_no_mst_id']
        po_number_mst = request.POST['po_number_mst']
        sample_type = request.POST['sample_type']
        target_ap_date = request.POST['target_ap_date']
        sent_to_sample = request.POST['sent_to_sample']
        submission_to_buyer = request.POST['submission_to_buyer']
        status_update_date = request.POST['status_update_date']
        approval_reject_date = request.POST['approval_reject_date']
        inserted_by = request.POST['inserted_by']
        insert_date = request.POST['insert_date']
        updated_by = request.POST['updated_by']
        update_date = request.POST['update_date']
        status_active = request.POST['status_active']
        comment = request.POST['comment']

        sample_info = OmPoSampleInfo(
            job_no_mst = job_no_mst,
            po_no_mst_id = po_no_mst_id,
            po_number_mst = po_number_mst,
            sample_type = sample_type,
            target_ap_date = target_ap_date,
            sent_to_sample =sent_to_sample,
            submission_to_buyer = submission_to_buyer,
            status_update_date = status_update_date,
            approval_reject_date = approval_reject_date,
            inserted_by = inserted_by,
            insert_date = insert_date,
            updated_by = updated_by,
            update_date = update_date,
            status_active = status_active,
            comment = comment
        )
        sample_info.save()
        messages.success(request, 'Congratulations! Po sample info has been Added Successfully...')
        return render(request, 'Order_Entry/sample_info.html')
    
class OrderUpdate(View):
    def get(self, request):
        return render(request, 'Order_Entry/order_update.html')
    
class LapdipInfo(View):
    def get(self, request):
        return render(request, 'Order_Entry/lapdip_info.html')
    
class QuotationEnquiry(View):
    def get(self, request):
        return render(request, 'Order_Entry/quote_enquiry.html')
    
class AccessoriesInfo(View):
    def get(self, request):
        return render(request, 'Order_Entry/access_info.html')
    
    def post(self, request):
        job_no_mst = request.POST['job_no_mst']
        po_no_mst_id = request.POST['po_no_mst_id']
        po_number_mst = request.POST['po_number_mst']
        accesories_name = request.POST['accesories_name']
        target_ap_date = request.POST['target_ap_date']
        sent_to_sample = request.POST['sent_to_sample']
        submission_to_buyer = request.POST['submission_to_buyer']
        supplier_name = request.POST['supplier_name']
        status_update_date = request.POST['status_update_date']
        approval_reject_date = request.POST['approval_reject_date']
        inserted_by = request.POST['inserted_by']
        insert_date = request.POST['insert_date']
        updated_by = request.POST['updated_by']
        update_date = request.POST['update_date']
        status_active = request.POST['status_active']
        comment = request.POST['comment']

        accessories_info = OmPoAccesoriesInfo(
            job_no_mst = job_no_mst,
            po_no_mst_id = po_no_mst_id,
            po_number_mst = po_number_mst,
            accesories_name = accesories_name,
            target_ap_date = target_ap_date,
            sent_to_sample =sent_to_sample,
            submission_to_buyer = submission_to_buyer,
            supplier_name = supplier_name,
            status_update_date = status_update_date,
            approval_reject_date = approval_reject_date,
            inserted_by = inserted_by,
            insert_date = insert_date,
            updated_by = updated_by,
            update_date = update_date,
            status_active = status_active,
            comment = comment
        )
        accessories_info.save()
        messages.success(request, 'Congratulations! Po accessories info has been Added Successfully...')
        return render(request, 'Order_Entry/access_info.html')


############ Related Table View ############


class RelatedLibBuyer(View):
    def get(self, request):
        lib_buyer = LibBuyer.objects.all()
        context = {
            'lib_buyer':lib_buyer
        }
        return render(request, 'Order_Entry/lib_buyer.html', context)
    
    def post(self, request):
        buyer_name = request.POST['buyer_name']
        contact_person = request.POST['contact_person']
        buyer_email = request.POST['buyer_email']
        contact_no = request.POST['contact_no']
        website = request.POST['website']
        address = request.POST['address']
        subcontract_party = request.POST['subcontract_party']
        inserted_by = request.POST['inserted_by']
        insert_date = request.POST['insert_date']
        updated_by = request.POST['updated_by']
        update_date = request.POST['update_date']
        status_active = request.POST['status_active']
        is_deleted = request.POST['is_deleted']
        remark = request.POST['remark']

        lib_buyer_info = LibBuyer(
            buyer_name = buyer_name,
            contact_person = contact_person,
            buyer_email = buyer_email,
            contact_no = contact_no,
            website = website,
            address = address,
            subcontract_party = subcontract_party,
            inserted_by = inserted_by,
            insert_date = insert_date,
            updated_by = updated_by,
            update_date = update_date,
            status_active = status_active,
            is_deleted = is_deleted,
            remark = remark
        )

        lib_buyer_info.save()
        messages.success(request, 'Congratulations! Lib buyer information has been Added Successfully...')
        lib_buyer = LibBuyer.objects.all()
        context = {
            'lib_buyer':lib_buyer
        }
        return render(request, 'Order_Entry/lib_buyer.html', context)


class RelatedLibStyle(View):
    def get(self, request):
        style = LibStyle.objects.all()
        context = {
            'style':style
        }
        return render(request, 'Order_Entry/lib_style.html', context)
    
    def post(self, request):
        style_name = request.POST['style_name']
        inserted_by = request.POST['inserted_by']
        insert_date = request.POST['insert_date']
        updated_by = request.POST['updated_by']
        update_date = request.POST['update_date']
        status_active = request.POST['status_active']
        is_deleted = request.POST['is_deleted']
        

        lib_style_info = LibStyle(
            style_name = style_name,
            inserted_by = inserted_by,
            insert_date = insert_date,
            updated_by = updated_by,
            update_date = update_date,
            status_active = status_active,
            is_deleted = is_deleted
            
        )

        lib_style_info.save()
        messages.success(request, 'Congratulations! Lib style information has been Added Successfully...')
        style = LibStyle.objects.all()
        context = {
            'style':style
        }
        return render(request, 'Order_Entry/lib_style.html', context)

class HrEmployeeForm(View):
    def get(self, request):
        return render(request, 'Order_Entry/hrm_employee.html')
    
    def post(self, request):
        emp_code = request.POST['emp_code']
        first_name = request.POST['first_name']
        middle_name = request.POST['middle_name']
        last_name = request.POST['last_name']
        full_name_bangla = request.POST['full_name_bangla']
        id_card_no = request.POST['id_card_no']
        punch_card_no = request.POST['punch_card_no']
        date_of_birth = request.POST['date_of_birth']
        father_name = request.POST['father_name']
        father_name_bangla = request.POST['father_name_bangla']
        mother_name = request.POST['mother_name']
        mother_name_bangla = request.POST['mother_name_bangla']
        birth_place = request.POST['birth_place']
        religion = request.POST['religion']
        blood_group = request.POST['blood_group']
        marital_status = request.POST['marital_status']
        sex = request.POST['sex']
        nationality = request.POST['nationality']
        national_id = request.POST['national_id']
        passport_no = request.POST['passport_no']
        designation_id = request.POST['designation_id']
        designation_level = request.POST['designation_level']
        joining_date = request.POST['joining_date']
        confirmation_date = request.POST['confirmation_date']
        service_benifit_from = request.POST['service_benifit_from']
        category = request.POST['category']
        functional_superior = request.POST['functional_superior']
        admin_superior = request.POST['admin_superior']
        salary_grade = request.POST['salary_grade']
        salary_rule = request.POST['salary_rule']
        gross_salary = request.POST['gross_salary']
        bank_gross = request.POST['bank_gross']
        status_active = request.POST['status_active']
        status_suspension = request.POST['status_suspension']
        status_attendance = request.POST['status_attendance']
        status_salary = request.POST['status_salary']
        ot_entitled = request.POST['ot_entitled']
        holiday_allowance_entitled = request.POST['holiday_allowance_entitled']
        pf_entitled = request.POST['pf_entitled']
        gi_entitled = request.POST['gi_entitled']
        overtime_policy = request.POST['overtime_policy']
        holiday_incentive_policy = request.POST['holiday_incentive_policy']
        duty_roster_policy = request.POST['duty_roster_policy']
        leave_policy = request.POST['leave_policy']
        maternity_leave_policy = request.POST['maternity_leave_policy']
        attendance_bonus_policy = request.POST['attendance_bonus_policy']
        absent_deduction_policy = request.POST['absent_deduction_policy']
        late_deduction_policy = request.POST['late_deduction_policy']
        bonus_policy = request.POST['bonus_policy']
        tax_policy = request.POST['tax_policy']
        shift_policy = request.POST['shift_policy']
        company_id = request.POST['company_id']
        location_id = request.POST['location_id']
        division_id = request.POST['division_id']
        department_id = request.POST['department_id']
        section_id = request.POST['section_id']
        inserted_by = request.POST['inserted_by']
        insert_date = request.POST['insert_date']
        updated_by = request.POST['updated_by']
        update_date = request.POST['update_date']
        is_deleted = request.POST['is_deleted']
        is_locked = request.POST['is_locked']
        remark = request.POST['remark']
        
        hr_employee_info = HRmEmployee(
            emp_code = emp_code,
            first_name = first_name,
            middle_name = middle_name,
            last_name = last_name,
            full_name_bangla = full_name_bangla,
            id_card_no = id_card_no,
            punch_card_no = punch_card_no,
            date_of_birth = date_of_birth,
            father_name = father_name,
            father_name_bangla = father_name_bangla,
            mother_name = mother_name,
            mother_name_bangla = mother_name_bangla,
            birth_place = birth_place,
            religion = religion,
            blood_group = blood_group,
            marital_status = marital_status,
            sex = sex,
            nationality = nationality,
            national_id = national_id,
            passport_no = passport_no,
            designation_id = designation_id,
            designation_level = designation_level,
            joining_date = joining_date,
            confirmation_date = confirmation_date,
            service_benifit_from = service_benifit_from,
            category =category,
            functional_superior = functional_superior,
            admin_superior = admin_superior,
            salary_grade = salary_grade,
            salary_rule = salary_rule,
            gross_salary = gross_salary,
            bank_gross = bank_gross,
            status_active = status_active,
            status_suspension = status_suspension,
            status_attendance = status_attendance,
            status_salary = status_salary,
            ot_entitled = ot_entitled,
            holiday_allowance_entitled = holiday_allowance_entitled,
            pf_entitled = pf_entitled,
            gi_entitled = gi_entitled,
            overtime_policy = overtime_policy,
            holiday_incentive_policy = holiday_incentive_policy,
            duty_roster_policy = duty_roster_policy,
            leave_policy = leave_policy,
            maternity_leave_policy = maternity_leave_policy,
            attendance_bonus_policy = attendance_bonus_policy,
            absent_deduction_policy = absent_deduction_policy,
            late_deduction_policy = late_deduction_policy,
            bonus_policy = bonus_policy,
            tax_policy = tax_policy,
            shift_policy = shift_policy,
            company_id = company_id,
            location_id = location_id,
            division_id = division_id,
            department_id = department_id,
            section_id = section_id,
            inserted_by = inserted_by,
            insert_date = insert_date,
            updated_by = updated_by,
            update_date = update_date,
            is_deleted = is_deleted,
            is_locked = is_locked,
            remark = remark

        )

        hr_employee_info.save()
        messages.success(request, 'Congratulations! Hr Employee information has been Added Successfully...')
        return render(request, 'Order_Entry/hrm_employee.html')
    
    
class LibCompanyInfo(View):
    def get(self, request):
        company = LibCompany.objects.all()
        context = {
            'company':company
        }
        return render(request, 'Order_Entry/lib_company.html', context)

    def post(self, request):
        group_id = request.POST['group_id']
        company_name = request.POST['company_name']
        company_short_name = request.POST['company_short_name']
        service_cost_allocation = request.POST['service_cost_allocation']
        posting_pre_year = request.POST['posting_pre_year']
        statutory_account = request.POST['statutory_account']
        contact_person = request.POST['contact_person']
        cfo = request.POST['cfo']
        company_nature = request.POST['company_nature']
        location = request.POST['location']
        core_business = request.POST['core_business']
        email = request.POST['email']
        website = request.POST['website']
        ac_code_length = request.POST['ac_code_length']
        profit_center_affected = request.POST['profit_center_affected']
        plot_no = request.POST['plot_no']
        level_no = request.POST['level_no']
        road_no = request.POST['road_no']
        block_no = request.POST['block_no']
        country_id = request.POST['country_id']
        province = request.POST['province']
        city = request.POST['city']
        zip_code = request.POST['zip_code']
        trade_license_no = request.POST['trade_license_no']
        incorporation_no = request.POST['incorporation_no']
        erc_no = request.POST['erc_no']
        irc_no = request.POST['irc_no']
        tin_number = request.POST['tin_number']
        vat_number = request.POST['vat_number']
        epb_reg_no = request.POST['epb_reg_no']
        trade_license_renewal = request.POST['trade_license_renewal']
        erc_expiry_date = request.POST['erc_expiry_date']
        irc_expiry_date = request.POST['irc_expiry_date']
        bangladesh_bank_reg_no = request.POST['bangladesh_bank_reg_no']
        graph_color = request.POST['graph_color']
        logo_location = request.POST['logo_location']
        inserted_by = request.POST['inserted_by']
        insert_date = request.POST['insert_date']
        updated_by = request.POST['updated_by']
        update_date = request.POST['update_date']
        status_active = request.POST['status_active']
        is_deleted = request.POST['is_deleted']
        is_locked = request.POST['is_locked']
        
        lib_company_info = LibCompany(
            group_id = group_id,
            company_name = company_name,
            company_short_name = company_short_name,
            service_cost_allocation = service_cost_allocation,
            posting_pre_year = posting_pre_year,
            statutory_account = statutory_account,
            contact_person = contact_person,
            cfo = cfo,
            company_nature = company_nature,
            location = location,
            core_business = core_business,
            email = email,
            website = website,
            ac_code_length = ac_code_length,
            profit_center_affected = profit_center_affected,
            plot_no = plot_no,
            level_no = level_no,
            road_no = road_no,
            block_no = block_no,
            country_id = country_id,
            province = province,
            city = city,
            zip_code = zip_code,
            trade_license_no = trade_license_no,
            incorporation_no = incorporation_no,
            erc_no = erc_no,
            irc_no = irc_no,
            tin_number = tin_number,
            vat_number = vat_number,
            epb_reg_no = epb_reg_no,
            trade_license_renewal = trade_license_renewal,
            erc_expiry_date = erc_expiry_date,
            irc_expiry_date = irc_expiry_date,
            bangladesh_bank_reg_no = bangladesh_bank_reg_no,
            graph_color = graph_color,
            logo_location = logo_location,
            inserted_by = inserted_by,
            insert_date = insert_date,
            updated_by = updated_by,
            update_date = update_date,
            status_active = status_active,
            is_deleted = is_deleted,
            is_locked = is_locked
            
        )

        lib_company_info.save()
        messages.success(request, 'Congratulations! Lib Company information has been Added Successfully...')
        company = LibCompany.objects.all()
        context = {
            'company':company
        }
        return render(request, 'Order_Entry/lib_company.html', context)

    
class LibDepartmentInfo(View):
    def get(self, request):
        department = LibDepartment.objects.all()
        context = {
            'department':department
        }
        return render(request, 'Order_Entry/lib_department.html', context)
    
    def post(self, request):
        department_name = request.POST['department_name']
        department_id = request.POST['department_id']
        inserted_by = request.POST['inserted_by']
        insert_date = request.POST['insert_date']
        updated_by = request.POST['updated_by']
        update_date = request.POST['update_date']
        status_active = request.POST['status_active']
        is_deleted = request.POST['is_deleted']
        is_locked = request.POST['is_locked']
        remark = request.POST['remark']

        lib_department_info = LibDepartment(
            department_name = department_name,
            department_id = department_id,
            inserted_by = inserted_by,
            insert_date = insert_date,
            updated_by = updated_by,
            update_date = update_date,
            status_active = status_active,
            is_deleted = is_deleted,
            is_locked = is_locked,
            remark = remark
        )

        lib_department_info.save()
        messages.success(request, 'Congratulations! Lib Department information has been Added Successfully...')
        department = LibDepartment.objects.all()
        context = {
            'department':department
        }
        return render(request, 'Order_Entry/lib_department.html', context)

    
class LibDivisionInfo(View):
    def get(self, request):
        division = LibDivision.objects.all()
        context = {
            'division': division
        }
        return render(request, 'Order_Entry/lib_division.html', context)
    
    def post(self, request):
        division_name = request.POST['division_name']
        location_id = request.POST['location_id']
        inserted_by = request.POST['inserted_by']
        insert_date = request.POST['insert_date']
        updated_by = request.POST['updated_by']
        update_date = request.POST['update_date']
        status_active = request.POST['status_active']
        is_deleted = request.POST['is_deleted']
        is_locked = request.POST['is_locked']
        remark = request.POST['remark']

        lib_division_info = LibDivision(
            division_name = division_name,
            location_id = location_id,
            inserted_by = inserted_by,
            insert_date = insert_date,
            updated_by = updated_by,
            update_date = update_date,
            status_active = status_active,
            is_deleted = is_deleted,
            is_locked = is_locked,
            remark = remark
        )

        lib_division_info.save()
        messages.success(request, 'Congratulations! Lib sub department information has been Added Successfully...')
        division = LibDivision.objects.all()
        context = {
            'division': division
        }
        return render(request, 'Order_Entry/lib_division.html', context)
    
class LibSubDept(View):
    def get(self, request):
        sub_department = LibSubDepartment.objects.all()
        context = {
            'sub_department':sub_department
        }
        return render(request, 'Order_Entry/lib_sub_dept.html', context)
    
    def post(self, request):
        sub_department_name = request.POST['sub_department_name']
        department_id = request.POST['department_id']
        inserted_by = request.POST['inserted_by']
        insert_date = request.POST['insert_date']
        updated_by = request.POST['updated_by']
        update_date = request.POST['update_date']
        status_active = request.POST['status_active']
        is_deleted = request.POST['is_deleted']
        is_locked = request.POST['is_locked']
        remark = request.POST['remark']

        lib_sub_division_info = LibSubDepartment(
            sub_department_name = sub_department_name,
            department_id = department_id,
            inserted_by = inserted_by,
            insert_date = insert_date,
            updated_by = updated_by,
            update_date = update_date,
            status_active = status_active,
            is_deleted = is_deleted,
            is_locked = is_locked,
            remark = remark
        )

        lib_sub_division_info.save()
        messages.success(request, 'Congratulations! Lib sub department information has been Added Successfully...')
        sub_department = LibSubDepartment.objects.all()
        context = {
            'sub_department':sub_department
        }
        return render(request, 'Order_Entry/lib_sub_dept.html', context)
    
class LibProdCat(View):
    def get(self, request):
        return render(request, 'Order_Entry/lib_prod_cat.html')
    
    def post(self, request):
        product_cate = request.POST['product_cate']
        inserted_by = request.POST['inserted_by']
        insert_date = request.POST['insert_date']
        updated_by = request.POST['updated_by']
        update_date = request.POST['update_date']
        status_active = request.POST['status_active']
        is_deleted = request.POST['is_deleted']

        lib_product_cat_info = LibProductCate(
            product_cate = product_cate,
            inserted_by = inserted_by,
            insert_date = insert_date,
            updated_by = updated_by,
            update_date = update_date,
            status_active = status_active,
            is_deleted = is_deleted,
            
        )

        lib_product_cat_info.save()
        messages.success(request, 'Congratulations! Lib product cate information has been Added Successfully...')
        return render(request, 'Order_Entry/lib_prod_cat.html')
    
class LibSeasonInfo(View):
    def get(self, request):
        return render(request, 'Order_Entry/libseason.html')
     
    def post(self, request):
        season_name = request.POST['season_name']
        inserted_by = request.POST['inserted_by']
        insert_date = request.POST['insert_date']
        updated_by = request.POST['updated_by']
        update_date = request.POST['update_date']
        status_active = request.POST['status_active']
        is_deleted = request.POST['is_deleted']

        lib_season_info = LibSeason(
            season_name = season_name,
            inserted_by = inserted_by,
            insert_date = insert_date,
            updated_by = updated_by,
            update_date = update_date,
            status_active = status_active,
            is_deleted = is_deleted
            
        )

        lib_season_info.save()
        messages.success(request, 'Congratulations! Lib season information has been Added Successfully...')
        return render(request, 'Order_Entry/libseason.html')
    
class LibRegionInfo(View):
    def get(self, request):
        return render(request, 'Order_Entry/lib_region.html')
    
    def post(self, request):
        region_name = request.POST['region_name']
        inserted_by = request.POST['inserted_by']
        insert_date = request.POST['insert_date']
        updated_by = request.POST['updated_by']
        update_date = request.POST['update_date']
        status_active = request.POST['status_active']
        is_deleted = request.POST['is_deleted']

        lib_region_info = LibRegion(
            region_name = region_name,
            inserted_by = inserted_by,
            insert_date = insert_date,
            updated_by = updated_by,
            update_date = update_date,
            status_active = status_active,
            is_deleted = is_deleted
            
        )

        lib_region_info.save()
        messages.success(request, 'Congratulations! Lib region information has been Added Successfully...')
        return render(request, 'Order_Entry/lib_region.html')
    
class LibAgentInfo(View):
    def get(self, request):
        return render(request, 'Order_Entry/lib_agent.html')
    
    def post(self, request):
        agent_name = request.POST['agent_name']
        inserted_by = request.POST['inserted_by']
        insert_date = request.POST['insert_date']
        updated_by = request.POST['updated_by']
        update_date = request.POST['update_date']
        status_active = request.POST['status_active']
        is_deleted = request.POST['is_deleted']

        lib_agent_info = LibAgent(
            agent_name = agent_name,
            inserted_by = inserted_by,
            insert_date = insert_date,
            updated_by = updated_by,
            update_date = update_date,
            status_active = status_active,
            is_deleted = is_deleted
            
        )

        lib_agent_info.save()
        messages.success(request, 'Congratulations! Lib agent information has been Added Successfully...')
        return render(request, 'Order_Entry/lib_agent.html')
    
class LibClientInfo(View):
    def get(self, request):
        return render(request, 'Order_Entry/lib_client.html')
    
    def post(self, request):
        client_name = request.POST['client_name']
        inserted_by = request.POST['inserted_by']
        insert_date = request.POST['insert_date']
        updated_by = request.POST['updated_by']
        update_date = request.POST['update_date']
        status_active = request.POST['status_active']
        is_deleted = request.POST['is_deleted']

        lib_client_info = LibClient(
            client_name = client_name,
            inserted_by = inserted_by,
            insert_date = insert_date,
            updated_by = updated_by,
            update_date = update_date,
            status_active = status_active,
            is_deleted = is_deleted
            
        )

        lib_client_info.save()
        messages.success(request, 'Congratulations! Lib client information has been Added Successfully...')
        return render(request, 'Order_Entry/lib_client.html')
    
class LibUnitInfo(View):
    def get(self, request):
        return render(request, 'Order_Entry/lib_unit.html')
    
    def post(self, request):
        unit_name = request.POST['unit_name']
        description = request.POST['description']
        inserted_by = request.POST['inserted_by']
        insert_date = request.POST['insert_date']
        updated_by = request.POST['updated_by']
        update_date = request.POST['update_date']
        status_active = request.POST['status_active']
        is_deleted = request.POST['is_deleted']

        lib_unit_info = LibUnit(
            unit_name = unit_name,
            description = description,
            inserted_by = inserted_by,
            insert_date = insert_date,
            updated_by = updated_by,
            update_date = update_date,
            status_active = status_active,
            is_deleted = is_deleted
            
        )

        lib_unit_info.save()
        messages.success(request, 'Congratulations! Lib unit information has been Added Successfully...')
        return render(request, 'Order_Entry/lib_unit.html')
    
class LibCurrencyInfo(View):
    def get(self, request):
        return render(request, 'Order_Entry/lib_currency.html')

    def post(self, request):
        currency_code = request.POST['currency_code']
        description = request.POST['description']
        inserted_by = request.POST['inserted_by']
        insert_date = request.POST['insert_date']
        updated_by = request.POST['updated_by']
        update_date = request.POST['update_date']
        status_active = request.POST['status_active']
        is_deleted = request.POST['is_deleted']

        lib_currency_info = LibCurrency(
            currency_code = currency_code,
            description = description,
            inserted_by = inserted_by,
            insert_date = insert_date,
            updated_by = updated_by,
            update_date = update_date,
            status_active = status_active,
            is_deleted = is_deleted
            
        )

        lib_currency_info.save()
        messages.success(request, 'Congratulations! Lib currency information has been Added Successfully...')
        return render(request, 'Order_Entry/lib_currency.html')
    
class INV(View):
    def get(self, request):
        return render(request, 'Order_Entry/inv_prod_info.html')

    def post(self, request):
        product_code = request.POST['product_code']
        product_name_details = request.POST['product_name_details']
        item_group = request.POST['item_group']
        product_name_short = request.POST['product_name_short']
        item_category = request.POST['item_category']
        vat_per_unit = request.POST['vat_per_unit']
        rate_per_unit = request.POST['rate_per_unit']
        current_stock = request.POST['current_stock']
        inserted_by = request.POST['inserted_by']
        insert_date = request.POST['insert_date']
        updated_by = request.POST['updated_by']
        update_date = request.POST['update_date']
        status_active = request.POST['status_active']
        is_deleted = request.POST['is_deleted']

        inv_product_info = InvProductInfo(
            product_code = product_code,
            product_name_details = product_name_details,
            item_group = item_group,
            product_name_short = product_name_short,
            item_category = item_category,
            vat_per_unit = vat_per_unit,
            rate_per_unit = rate_per_unit,
            current_stock = current_stock,
            inserted_by = inserted_by,
            insert_date = insert_date,
            updated_by = updated_by,
            update_date = update_date,
            status_active = status_active,
            is_deleted = is_deleted
            
        )

        inv_product_info.save()
        messages.success(request, 'Congratulations! Inv Product information has been Added Successfully...')
        return render(request, 'Order_Entry/inv_prod_info.html')
    
    
class LibColorInfo(View):
    def get(self, request):
        return render(request, 'Order_Entry/lib_color.html')
    
    def post(self, request):
        color_name = request.POST['color_name']
        inserted_by = request.POST['inserted_by']
        insert_date = request.POST['insert_date']
        updated_by = request.POST['updated_by']
        update_date = request.POST['update_date']
        status_active = request.POST['status_active']
        is_deleted = request.POST['is_deleted']

        lib_color_info = LibColor(
            color_name = color_name,
            inserted_by = inserted_by,
            insert_date = insert_date,
            updated_by = updated_by,
            update_date = update_date,
            status_active = status_active,
            is_deleted = is_deleted
            
        )

        lib_color_info.save()
        messages.success(request, 'Congratulations! Lib color information has been Added Successfully...')
        return render(request, 'Order_Entry/lib_color.html')
    
class LibSizeInfo(View):
    def get(self, request):
        return render(request, 'Order_Entry/lib_size.html')

    def post(self, request):
        size_name = request.POST['size_name']
        inserted_by = request.POST['inserted_by']
        insert_date = request.POST['insert_date']
        updated_by = request.POST['updated_by']
        update_date = request.POST['update_date']
        status_active = request.POST['status_active']
        is_deleted = request.POST['is_deleted']

        lib_size_info = LibSize(
            size_name = size_name,
            inserted_by = inserted_by,
            insert_date = insert_date,
            updated_by = updated_by,
            update_date = update_date,
            status_active = status_active,
            is_deleted = is_deleted
            
        )

        lib_size_info.save()
        messages.success(request, 'Congratulations! Lib size information has been Added Successfully...')
        return render(request, 'Order_Entry/lib_size.html') 
    
class LibCountryInfo(View):
    def get(self, request):
        return render(request, 'Order_Entry/lib_country.html')
    
    def post(self, request):
        country_code = request.POST['country_code']
        country_name = request.POST['country_name']
        inserted_by = request.POST['inserted_by']
        insert_date = request.POST['insert_date']
        updated_by = request.POST['updated_by']
        update_date = request.POST['update_date']
        status_active = request.POST['status_active']
        is_deleted = request.POST['is_deleted']

        lib_country_info = LibCountry(
            country_code = country_code,
            country_name = country_name,
            inserted_by = inserted_by,
            insert_date = insert_date,
            updated_by = updated_by,
            update_date = update_date,
            status_active = status_active,
            is_deleted = is_deleted
            
        )

        lib_country_info.save()
        messages.success(request, 'Congratulations! Lib country information has been Added Successfully...')
        return render(request, 'Order_Entry/lib_country.html')
    
    
    
    

