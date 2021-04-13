from django.db import models
import datetime
from django.utils.timezone import now

# Create your models here.
#########################################################
############### Related Table Start #####################
##########################################################
class LibBuyer(models.Model):
    BUYER_SUB_TYPE = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    buyer_name = models.CharField(max_length=200, null=True)
    contact_person = models.CharField(max_length=200, null=True)
    buyer_email = models.CharField(max_length=200, null=True)
    contact_no = models.CharField(max_length=20, null=True)
    website = models.CharField(max_length=200, null=True)
    address = models.TextField(null=True)
    subcontract_party = models.CharField(max_length=200, choices=BUYER_SUB_TYPE, default=0, null=True)
    remark = models.TextField(null=True)
    inserted_by = models.CharField(max_length=120, null=True)
    insert_date = models.DateTimeField(default=now)
    updated_by = models.CharField(max_length=120, null=True)
    update_date = models.DateTimeField(default=now)
    status_active = models.CharField(max_length=20, choices=STATUS, null=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.buyer_name

class LibStyle(models.Model):
    STATUS = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    style_name = models.CharField(max_length=200, null=True)
    inserted_by = models.CharField(max_length=120, null=True)
    insert_date = models.DateTimeField(default=now)
    updated_by = models.CharField(max_length=120, null=True)
    update_date = models.DateTimeField(default=now)
    status_active = models.CharField(max_length=20, choices=STATUS, default=0, null=True)
    is_deleted = models.CharField(max_length=20, choices=STATUS, default=0, null=True)

    def __str__(self):
        return self.style_name


class LibCompany(models.Model):
    STATUS = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    group_id = models.CharField(max_length=15, default=0, null=True)
    company_name = models.CharField(max_length=200, null=True)
    company_short_name = models.CharField(max_length=200, null=True)
    service_cost_allocation = models.CharField(max_length=200, null=True)
    posting_pre_year = models.CharField(max_length=15, default=0, null=True)
    statutory_account = models.CharField(max_length=200, null=True)
    contact_person = models.CharField(max_length=200, null=True)
    cfo = models.CharField(max_length=200, null=True)
    company_nature = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=200, null=True)
    core_business = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    website = models.CharField(max_length=200, null=True)
    ac_code_length = models.IntegerField( default=0)
    profit_center_affected = models.CharField(max_length=10, choices=STATUS, default=0)
    plot_no = models.CharField(max_length=20, null=True)
    level_no = models.CharField(max_length=20, null=True)
    road_no = models.CharField(max_length=20, null=True)
    block_no = models.CharField(max_length=20, null=True)
    country_id = models.CharField(max_length=20, null=True)
    province = models.CharField(max_length=120, null=True)
    city = models.CharField(max_length=120, null=True)
    zip_code = models.CharField(max_length=120, null=True)
    trade_license_no = models.CharField(max_length=20, null=True)
    incorporation_no = models.CharField(max_length=20, null=True)
    erc_no = models.CharField(max_length=20, null=True)
    irc_no = models.CharField(max_length=20, null=True)
    tin_number = models.CharField(max_length=20, null=True)
    vat_number = models.CharField(max_length=20, null=True)
    epb_reg_no = models.CharField(max_length=20, null=True)
    trade_license_renewal = models.CharField(max_length=20, null=True)
    erc_expiry_date = models.CharField(max_length=50, null=True)
    irc_expiry_date = models.CharField(max_length=50, null=True)
    bangladesh_bank_reg_no = models.CharField(max_length=200, null=False)
    graph_color = models.CharField(max_length=20, null=False)
    logo_location = models.CharField(max_length=20, null=False)
    inserted_by = models.CharField(max_length=120, null=True)
    insert_date = models.DateTimeField(default=now)
    updated_by = models.CharField(max_length=120, null=True)
    update_date = models.DateTimeField(default=now)
    status_active = models.CharField(max_length=20, choices=STATUS, default=0, null=True)
    is_deleted = models.CharField(max_length=20, choices=STATUS, default=1, null=True)
    is_locked = models.CharField(max_length=20, choices=STATUS, default=1, null=True)

    def __str__(self):
        return self.company_name

class LibDepartment(models.Model):
    STATUS = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    department_name = models.CharField(max_length=200, null=True)
    department_id = models.CharField(max_length=20, default=0)
    remark = models.TextField(null=True)
    inserted_by = models.CharField(max_length=120, null=True)
    insert_date = models.DateTimeField(default=now)
    updated_by = models.CharField(max_length=120, null=True)
    update_date = models.DateTimeField(default=now)
    status_active = models.CharField(max_length=20, choices=STATUS, default=0, null=True)
    is_deleted = models.CharField(max_length=20, choices=STATUS, default=1, null=True)
    is_locked = models.CharField(max_length=20, choices=STATUS, default=1, null=True)

    def __str__(self):
        return self.department_name

class LibDivision(models.Model):
    STATUS = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    division_name = models.CharField(max_length=200, null=True)
    location_id = models.CharField(max_length=20, default=0)
    remark = models.TextField(null=True)
    inserted_by = models.CharField(max_length=120, null=True)
    insert_date = models.DateTimeField(default=now)
    updated_by = models.CharField(max_length=120, null=True)
    update_date = models.DateTimeField(default=now)
    status_active = models.CharField(max_length=20, choices=STATUS, default=0, null=True)
    is_deleted = models.CharField(max_length=20, choices=STATUS, default=0, null=True)
    is_locked = models.CharField(max_length=20, choices=STATUS, default=0, null=True)

    def __str__(self):
        return self.division_name

class LibSubDepartment(models.Model):
    STATUS = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    sub_department_name = models.CharField(max_length=200, null=True)
    department_id = models.CharField(max_length=20, default=0)
    remark = models.TextField(null=True)
    inserted_by = models.CharField(max_length=120, null=True)
    insert_date = models.DateTimeField(default=now)
    updated_by = models.CharField(max_length=120, null=True)
    update_date = models.DateTimeField(default=now)
    status_active = models.CharField(max_length=20, choices=STATUS, default=0, null=True)
    is_deleted = models.CharField(max_length=20, choices=STATUS, default=1, null=True)
    is_locked = models.CharField(max_length=20, choices=STATUS, default=1, null=True)

    def __str__(self):
        return self.sub_department_name

class LibProductCate(models.Model):
    STATUS = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    product_cate = models.CharField(max_length=200, null=True)
    inserted_by = models.CharField(max_length=120, null=True)
    insert_date = models.DateTimeField(default=now)
    updated_by = models.CharField(max_length=120, null=True)
    update_date = models.DateTimeField(default=now)
    status_active = models.CharField(max_length=20, choices=STATUS, default=0, null=True)
    is_deleted = models.CharField(max_length=20, choices=STATUS, default=1, null=True)

    def __str__(self):
        return self.product_cate

class LibSeason(models.Model):
    STATUS = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    season_name = models.CharField(max_length=200, null=True)
    inserted_by = models.CharField(max_length=120, null=True)
    insert_date = models.DateTimeField(default=now)
    updated_by = models.CharField(max_length=120, null=True)
    update_date = models.DateTimeField(default=now)
    status_active = models.CharField(max_length=20, choices=STATUS, default=0, null=True)
    is_deleted = models.CharField(max_length=20, choices=STATUS, default=1, null=True)

    def __str__(self):
        return self.season_name

class LibRegion(models.Model):
    STATUS = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    region_name = models.CharField(max_length=200, null=True)
    inserted_by = models.CharField(max_length=120, null=True)
    insert_date = models.DateTimeField(default=now)
    updated_by = models.CharField(max_length=120, null=True)
    update_date = models.DateTimeField(default=now)
    status_active = models.CharField(max_length=20, choices=STATUS, default=0, null=True)
    is_deleted = models.CharField(max_length=20, choices=STATUS, default=1, null=True)

    def __str__(self):
        return self.region_name

class LibAgent(models.Model):
    STATUS = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    agent_name = models.CharField(max_length=200, null=True)
    inserted_by = models.CharField(max_length=120, null=True)
    insert_date = models.DateTimeField(default=now)
    updated_by = models.CharField(max_length=120, null=True)
    update_date = models.DateTimeField(default=now)
    status_active = models.CharField(max_length=20, choices=STATUS, default=0, null=True)
    is_deleted = models.CharField(max_length=20, choices=STATUS, default=1, null=True)

    def __str__(self):
        return self.agent_name

class LibClient(models.Model):
    STATUS = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    client_name = models.CharField(max_length=200, null=True)
    inserted_by = models.CharField(max_length=120, null=True)
    insert_date = models.DateTimeField(default=now)
    updated_by = models.CharField(max_length=120, null=True)
    update_date = models.DateTimeField(default=now)
    status_active = models.CharField(max_length=20, choices=STATUS, default=0, null=True)
    is_deleted = models.CharField(max_length=20, choices=STATUS, default=1, null=True)

    def __str__(self):
        return self.client_name

class LibUnit(models.Model):
    STATUS = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    unit_name = models.CharField(max_length=200, null=True)
    description = models.TextField(blank=True)
    inserted_by = models.CharField(max_length=120, null=True)
    insert_date = models.DateTimeField(default=now)
    updated_by = models.CharField(max_length=120, null=True)
    update_date = models.DateTimeField(default=now)
    status_active = models.CharField(max_length=20, choices=STATUS, default=0, null=True)
    is_deleted = models.CharField(max_length=20, choices=STATUS, default=1, null=True)

    def __str__(self):
        return self.unit_name

class HRmEmployee(models.Model):
    STATUS = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    MARITAL_STATUS = (
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Separated', 'Separated'),
        ('Widow', 'Widow'),
    )

    SEX_TYPE = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    COMMENT = (
        ('Original doj', 'Original doj'),
        ('After rejoin date', 'After rejoin date'),
    )

    CATEGORY = (
        ('Top', 'Top'),
        ('Mid', 'Mid'),
        ('Non', 'Non')
    )
    emp_code = models.CharField(max_length=20, null=False)
    first_name = models.CharField(max_length=120, null=False)
    middle_name = models.CharField(max_length=120, null=True)
    last_name = models.CharField(max_length=120, null= False)
    full_name_bangla = models.CharField(max_length=120, null=False)
    id_card_no = models.CharField(max_length=120, null=True)
    punch_card_no = models.CharField(max_length=120, null=True)
    date_of_birth = models.DateTimeField(auto_now_add=True, null=True)
    father_name = models.CharField(max_length=120, null=True)
    father_name_bangla = models.CharField(max_length=120, null= False)
    mother_name =  models.CharField(max_length=180, null=True)
    mother_name_bangla =  models.CharField(max_length=180, null=False)
    birth_place =  models.CharField(max_length=180, null=True)
    religion =  models.CharField(max_length=180, null=True)
    blood_group =  models.CharField(max_length=10, null=True)
    marital_status =  models.CharField(max_length=10, choices=MARITAL_STATUS, default=0, null=True)
    sex =  models.CharField(max_length=10, choices=SEX_TYPE, default=0, null=True)
    nationality = models.CharField(max_length=120, null=True)
    national_id = models.CharField(max_length=120, null=True)
    passport_no = models.CharField(max_length=120, null=True)
    designation_id = models.CharField(max_length=80, null=True)
    designation_level = models.CharField(max_length=80, null=True)
    joining_date = models.DateTimeField(auto_now_add=True, null=True)
    confirmation_date = models.DateTimeField(auto_now_add=True, null=True )
    service_benifit_from = models.CharField(max_length=50, choices=COMMENT, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY, default=2, null=True)
    functional_superior = models.CharField(max_length=50, null=True)
    admin_superior = models.CharField(max_length=40, null=True)
    salary_grade = models.CharField(max_length=40, null=True)
    salary_rule = models.CharField(max_length=40, null=True)
    gross_salary = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    bank_gross = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    remark = models.TextField(null=True)
    status_active = models.CharField(max_length=10, choices=STATUS, default=0)
    status_suspension = models.CharField(max_length=10, choices=STATUS, default=1)
    status_attendance = models.CharField(max_length=10, choices=STATUS, default=0)
    status_salary = models.CharField(max_length=10, choices=STATUS, default=0)
    ot_entitled = models.CharField(max_length=30, null=True)
    holiday_allowance_entitled = models.CharField(max_length=80, null=True)
    pf_entitled = models.CharField(max_length=80, null=True)
    gi_entitled = models.CharField(max_length=80, null=True)
    overtime_policy = models.CharField(max_length=80, null=True)
    holiday_incentive_policy = models.CharField(max_length=80, null=True)
    duty_roster_policy = models.CharField(max_length=80, null=True)
    leave_policy = models.CharField(max_length=80, null=True)
    maternity_leave_policy = models.CharField(max_length=80, null=True)
    attendance_bonus_policy = models.CharField(max_length=80, null=True)
    absent_deduction_policy = models.CharField(max_length=80, null=True)
    late_deduction_policy = models.CharField(max_length=80, null=True)
    bonus_policy = models.CharField(max_length=80, null=True)
    tax_policy = models.CharField(max_length=80, null=True)
    shift_policy = models.CharField(max_length=80, null=True)
    company_id = models.CharField(max_length=80, null=True)
    location_id = models.CharField(max_length=80, null=True)
    division_id = models.CharField(max_length=80, null=True)
    department_id = models.CharField(max_length=80, null=True)
    section_id = models.CharField(max_length=80, null=True)
    inserted_by = models.DateTimeField(default=now)
    insert_date = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=120, null=True)
    update_date = models.DateTimeField(default=now)
    is_deleted = models.CharField(max_length=20, choices=STATUS, default=1, null=True)
    is_locked = models.CharField(max_length=20, choices=STATUS, default=1, null=True)

    def __str__(self):
        return self.first_name

class LibCurrency(models.Model):
    STATUS = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    currency_code = models.CharField(max_length=200, null=True)
    description = models.TextField(blank=True)
    inserted_by = models.CharField(max_length=120, null=True)
    insert_date = models.DateTimeField(default=now)
    updated_by = models.CharField(max_length=120, null=True)
    update_date = models.DateTimeField(default=now)
    status_active = models.CharField(max_length=20, choices=STATUS, default=0, null=True)
    is_deleted = models.CharField(max_length=20, choices=STATUS, default=1, null=True)

    def __str__(self):
        return self.currency_code

class InvProductInfo(models.Model):
    DELETED = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    STATUS = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )

    product_code = models.CharField(max_length=20, null=False)
    product_name_details = models.CharField(max_length=200, null=False)
    item_group = models.CharField(max_length=80, null=True)
    product_name_short = models.CharField(max_length=180, null=True)
    unit_of_measure = models.CharField(max_length=80, null=True)
    item_category = models.CharField(max_length=80, null=True)
    vat_per_unit = models.CharField(max_length=80, null=True)
    rate_per_unit = models.CharField(max_length=80, null=True)
    current_stock = models.CharField(max_length=80, null=False)
    inserted_by = models.CharField(max_length=120, null=True)
    insert_date = models.DateTimeField(default=now)
    updated_by = models.CharField(max_length=120, null=True)
    update_date = models.DateTimeField(default=now)
    status_active = models.CharField(max_length=20, choices=STATUS, default=0, null=True)
    is_deleted = models.CharField(max_length=20, choices=DELETED, default=1, null=True)

    def __str__(self):
        return self.product_code

class LibColor(models.Model):
    DELETED = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    STATUS = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )

    color_name = models.CharField(max_length=200, null=True)
    inserted_by = models.CharField(max_length=120, null=True)
    insert_date = models.DateTimeField(default=now)
    updated_by = models.CharField(max_length=120, null=True)
    update_date = models.DateTimeField(default=now)
    status_active = models.CharField(max_length=20, choices=STATUS, default=0, null=True)
    is_deleted = models.CharField(max_length=20, choices=DELETED, default=1, null=True)

    def __str__(self):
        return self.color_name

class LibSize(models.Model):
    DELETED = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    STATUS = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )

    size_name = models.CharField(max_length=200, null=True)
    inserted_by = models.CharField(max_length=120, null=True)
    insert_date = models.DateTimeField(default=now)
    updated_by = models.CharField(max_length=120, null=True)
    update_date = models.DateTimeField(default=now)
    status_active = models.CharField(max_length=20, choices=STATUS, default=0, null=True)
    is_deleted = models.CharField(max_length=20, choices=DELETED, default=1, null=True)

    def __str__(self):
        return self.size_name

class LibCountry(models.Model):
    DELETED = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    STATUS = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    country_code = models.CharField(max_length=20, null=True)
    country_name = models.CharField(max_length=200, null=True)
    inserted_by = models.CharField(max_length=120, null=True)
    insert_date = models.DateTimeField(default=now)
    updated_by = models.CharField(max_length=120, null=True)
    update_date = models.DateTimeField(default=now)
    status_active = models.CharField(max_length=20, choices=STATUS, default=0, null=True)
    is_deleted = models.CharField(max_length=20, choices=DELETED, default=1, null=True)

    def __str__(self):
        return self.country_name
#########################################################
############### Related Table End #####################
##########################################################



#########################################################
############### Main Table Start ########################
##########################################################

class OrderEntryInfo(models.Model):
    STATUS = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    SHIP_MODE = (
        ('Sea', 'Sea'),
        ('Air', 'Air'),
        ('Road', 'Road'),
    )

    ORDER_TYPE = (
        ('Knit', 'Knit'),
        ('Oven', 'Oven'),
        ('Sweater', 'Sweater'),
    )
    job_no = models.CharField(max_length=120, null=True)
    buyer_id = models.ForeignKey(LibBuyer, related_name='buyer_id', on_delete=models.CASCADE)
    style_ref_no = models.ForeignKey(LibStyle, related_name='style_ref_no', on_delete=models.CASCADE)
    order_repeat_no = models.CharField(max_length=50, choices=STATUS, default=0)
    working_company = models.ForeignKey(LibCompany, related_name='working_company', on_delete=models.CASCADE, null=False)
    working_company_location = models.CharField(max_length=40, null=False)
    lc_company = models.ForeignKey(LibCompany, related_name='lc_company', on_delete=models.CASCADE, null=False)
    lc_company_location = models.CharField(max_length=120, null=False)
    file_no = models.CharField(max_length=50, null=True)
    projected_job_no = models.CharField(max_length=50, null=False)
    department_id = models.ForeignKey(LibDepartment, related_name='main_department_id', on_delete=models.CASCADE)
    sub_department_id = models.ForeignKey(LibSubDepartment, related_name='sub_department_id', on_delete=models.CASCADE)
    product_cat_id = models.ForeignKey(LibProductCate, related_name='working_company', on_delete=models.CASCADE)
    season_id = models.ForeignKey(LibSeason, related_name='season_id', on_delete=models.CASCADE)
    region_id = models.ForeignKey(LibRegion, related_name='region_id', on_delete=models.CASCADE)
    agent_id = models.ForeignKey(LibAgent, related_name='agent_id', on_delete=models.CASCADE)
    client_id = models.ForeignKey(LibClient, related_name='client_id', on_delete=models.CASCADE)
    quality_label = models.CharField(max_length=30, choices=STATUS, default=1)
    unit_id = models.ForeignKey(LibUnit, related_name='unit_id', on_delete=models.CASCADE)
    smv = models.CharField(max_length=30, null=True)
    buying_house_merchandiser = models.CharField(max_length=200, null=True)
    ship_mode = models.CharField(max_length=30, choices=SHIP_MODE, null=True)
    team_lead_emp_id = models.ForeignKey(HRmEmployee, on_delete=models.CASCADE)
    dealing_merchandiser_emp_id = models.ForeignKey(HRmEmployee, related_name='dealing_merchandiser_emp_id', on_delete=models.CASCADE)
    factory_merchandiser_emp_id = models.ForeignKey(HRmEmployee, related_name='factory_merchandiser_emp_id', on_delete=models.CASCADE)
    ready_for_bom = models.CharField(max_length=20, choices=STATUS, default=0)
    copy_from_job_no = models.CharField(max_length=80, null=True)
    file_name_link = models.CharField(max_length=80, null=True)
    internal_ref_no = models.CharField(max_length=80, null=False)
    currency_id = models.ForeignKey(LibCurrency, related_name='currency_id', on_delete=models.CASCADE)
    order_type = models.CharField(max_length=30, default=0, choices=ORDER_TYPE, null=True)
    remarks = models.TextField(null=True)
    inserted_by = models.CharField(max_length=120, null=True)
    insert_date = models.DateTimeField(default=now)
    updated_by = models.CharField(max_length=120, null=True)
    update_date = models.DateTimeField(default=now)
    status_active = models.CharField(max_length=20, choices=STATUS, default=0, null=True)
    is_deleted = models.CharField(max_length=20, choices=STATUS, default=1, null=True)


class OmPoCostDetail(models.Model):
    STATUS = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    job_no_cost_mst = models.CharField(max_length=30, null=False)
    product_id = models.ForeignKey(InvProductInfo, related_name='product_id', on_delete=models.CASCADE)
    unit_price =  models.DecimalField(max_digits=12, decimal_places=2, default=0, null=True)
    set_pc_rate =  models.DecimalField(max_digits=12, decimal_places=2, default=0, null=True)
    set_quantity = models.CharField(max_length=30, null=False)
    set_total_quantity = models.CharField(max_length=30, null=False)
    sewing_smv =  models.DecimalField(max_digits=12, decimal_places=2, default=0, null=False)
    cutting_smv =  models.DecimalField(max_digits=12, decimal_places=2, default=0, null=False)
    finishing_smv =  models.DecimalField(max_digits=12, decimal_places=2, default=0, null=False)
    fabric_cost_total =  models.DecimalField(max_digits=12, decimal_places=2, default=0, null=False)
    fabric_cost_percent =  models.DecimalField(max_digits=12, decimal_places=2, default=0, null=False)
    trims_cost_total =  models.DecimalField(max_digits=12, decimal_places=2, default=0, null=False)
    trims_cost_percent =  models.DecimalField(max_digits=12, decimal_places=2, default=0, null=False)
    embellish_cost_total =  models.DecimalField(max_digits=12, decimal_places=2, default=0, null=False)
    embellish_cost_percent =  models.DecimalField(max_digits=12, decimal_places=2, default=0, null=False)
    commercial_cost_total =  models.DecimalField(max_digits=12, decimal_places=2, default=0, null=False)
    commercial_cost_percent =  models.DecimalField(max_digits=12, decimal_places=2, default=0, null=False)
    commision_cost_total =  models.DecimalField(max_digits=12, decimal_places=2, default=0, null=False)
    commission_cost_percent =  models.DecimalField(max_digits=12, decimal_places=2, default=0, null=False)
    testing_cost_total =  models.DecimalField(max_digits=12, decimal_places=2, default=0, null=False)
    testing_cost_percent =  models.DecimalField(max_digits=12, decimal_places=2, default=0, null=False)
    freight_cost_total =  models.DecimalField(max_digits=12, decimal_places=2, default=0, null=False)
    freight_cost_percent =  models.DecimalField(max_digits=12, decimal_places=2, default=0, null=False)
    inspection_cost =  models.DecimalField(max_digits=12, decimal_places=2, default=0, null=False)
    inspection_cost_per =  models.DecimalField(max_digits=12, decimal_places=2, default=0, null=False)
    courier_cost =  models.DecimalField(max_digits=12, decimal_places=2, default=0, null=False)
    courier_cost_per =  models.DecimalField(max_digits=12, decimal_places=2, default=0, null=False)
    total_cost =  models.DecimalField(max_digits=12, decimal_places=2, default=0, null=False)
    total_cost_per =  models.DecimalField(max_digits=12, decimal_places=2, default=0, null=False)
    cm_per_unit =  models.DecimalField(max_digits=12, decimal_places=2, default=0, null=False)
    cm_per_unit_per =  models.DecimalField(max_digits=12, decimal_places=2, default=0, null=False)
    price_per_unit =  models.DecimalField(max_digits=12, decimal_places=2, default=0, null=False)
    price_per_unit_per =  models.DecimalField(max_digits=12, decimal_places=2, default=0, null=False)
    price_per_pc =  models.DecimalField(max_digits=12, decimal_places=2, default=0, null=False)
    bep_cm_per =  models.DecimalField(max_digits=12, decimal_places=2, default=0, null=False)
    asking_cm_per =  models.DecimalField(max_digits=12, decimal_places=2, default=0, null=False)
    cm_from_ie =  models.DecimalField(max_digits=12, decimal_places=2, default=0, null=False)
    profit_loss =  models.DecimalField(max_digits=12, decimal_places=2, default=0, null=False)
    inserted_by = models.CharField(max_length=120, null=True)
    insert_date = models.DateTimeField(default=now)
    updated_by = models.CharField(max_length=120, null=True)
    update_date = models.DateTimeField(default=now)
    status_active = models.CharField(max_length=20, choices=STATUS, default=0, null=True)
    is_deleted = models.CharField(max_length=20, choices=STATUS, default=1, null=True)
    



class OmPoBreakDown(models.Model):
    STATUS = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    job_no_mst = models.CharField(max_length=50, null=False)
    po_number = models.CharField(max_length=50, null=False)
    po_quantity = models.CharField(max_length=50, null=False)
    plan_quantity = models.CharField(max_length=50, null=False)
    shipped_date = models.DateTimeField(auto_now_add=True, null=False)
    is_deleted = models.CharField(max_length=50, null=False)
    is_countable = models.CharField(max_length=50, null=False)
    is_projected = models.CharField(max_length=50, null=False)
    remarks = models.TextField(null=True)
    inserted_by = models.CharField(max_length=120, null=True)
    insert_date = models.DateTimeField(default=now)
    updated_by = models.CharField(max_length=120, null=True)
    update_date = models.DateTimeField(default=now)
    status_active = models.CharField(max_length=20, choices=STATUS, default=0, null=True)
    is_locked = models.CharField(max_length=20, choices=STATUS, default=1, null=True)
    po_status =  models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.po_number

class WoPOCountryDetails(models.Model):
    STATUS = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    job_no = models.CharField(max_length=50, null=False)
    po_number = models.ForeignKey(OmPoBreakDown, related_name='om_po_number', on_delete=models.CASCADE)
    country_id = models.ForeignKey(LibCountry, related_name='lib_country_id', on_delete=models.CASCADE)
    code = models.CharField(max_length=50, null=False)
    product_id = models.ForeignKey(InvProductInfo, related_name='inv_product_id', on_delete=models.CASCADE)
    cut_off = models.CharField(max_length=50, null=False)
    po_quantity = models.CharField(max_length=50, null=False)
    plan_quantity = models.CharField(max_length=50, null=False)
    shipped_date = models.DateTimeField(auto_now_add=True, null=False)
    is_projected = models.CharField(max_length=50, null=False)
    projected_id = models.CharField(max_length=50, null=False)
    agent_name = models.CharField(max_length=100, null=False)
    exporting_item_catg = models.CharField(max_length=100, null=False)
    is_deleted = models.CharField(max_length=50, null=False)
    status_active = models.CharField(max_length=20, choices=STATUS, default=0, null=True)
    inserted_by = models.CharField(max_length=120, null=True)
    insert_date = models.DateTimeField(default=now)
    updated_by = models.CharField(max_length=120, null=True)
    update_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.job_no

class OmPoDetailsMaster(models.Model):
    STATUS = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    job_no_mst = models.CharField(max_length=50, null=False)
    breakdown_type = models.CharField(max_length=50, null=False)
    round_type = models.CharField(max_length=50, null=False)
    copy_from =  models.CharField(max_length=20, choices=STATUS, default=0, null=True)
    cpy_po_number = models.ForeignKey(OmPoBreakDown, on_delete=models.CASCADE, related_name='copy_po_number')
    po_detail = models.ForeignKey(WoPOCountryDetails, on_delete=models.CASCADE, related_name='po_detail', blank=True, null=True)
    po_number = models.CharField(max_length=50, null=False)
    po_received_date = models.DateTimeField(auto_now_add=True, null=False)
    po_quantity =  models.DecimalField(max_digits=12, decimal_places=2, default=0, null=False)
    unit_price =  models.DecimalField(max_digits=12, decimal_places=2, default=0, null=False)
    set_pc_rate =  models.DecimalField(max_digits=12, decimal_places=2, default=0, null=False)
    set_quantity = models.CharField(max_length=50, null=False)
    set_total_quantity = models.CharField(max_length=50, null=False)
    po_total_price =  models.DecimalField(max_digits=12, decimal_places=2, default=0, null=False)
    shipment_date = models.DateTimeField(auto_now_add=True, null=False)
    original_shipment_date = models.DateTimeField(auto_now_add=True, null=False)
    avg_fob =  models.DecimalField(max_digits=12, decimal_places=2, default=0, null=False)
    up_charge =  models.DecimalField(max_digits=12, decimal_places=2, default=0, null=False)
    ctn =  models.CharField(max_length=50, null=False)
    projected_po_number =  models.CharField(max_length=50, null=True)
    actual_po_number =  models.CharField(max_length=50, null=True)
    t_year =  models.CharField(max_length=50, null=True)
    t_month =  models.CharField(max_length=50, null=True)
    is_deleted =  models.CharField(max_length=50, null=True)
    is_countable =  models.CharField(max_length=50, null=True)
    is_projected =  models.CharField(max_length=50, null=True)
    remarks = models.TextField(null=True)
    inserted_by = models.CharField(max_length=120, null=True)
    insert_date = models.DateTimeField(default=now)
    updated_by = models.CharField(max_length=120, null=True)
    update_date = models.DateTimeField(default=now)
    status_active = models.CharField(max_length=20, choices=STATUS, default=0, null=True)
    is_locked = models.CharField(max_length=20, choices=STATUS, default=1, null=True)
    po_status =  models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.job_no_mst


class OmPoColorSizeBreakDown(models.Model):
    STATUS = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    po_break_down_id = models.CharField(max_length=30, null=False)
    job_no_mst = models.CharField(max_length=50, null=False)
    po_no_mst = models.CharField(max_length=50, null=False)
    size_number_id = models.ForeignKey(LibSize, related_name='lib_size_number_id', on_delete=models.CASCADE)
    color_number_id = models.ForeignKey(LibColor, related_name='lib_color_number_id', on_delete=models.CASCADE)
    prod_quantity = models.IntegerField(default= 0, null = True, blank = True)
    po_total =  models.DecimalField(max_digits=12, decimal_places=2, default=0, null=False)
    is_deleted = models.CharField(max_length=50, null=False)
    is_used = models.CharField(max_length=50, null=False)
    status_active = models.CharField(max_length=20, choices=STATUS, default=0, null=True)
    inserted_by = models.CharField(max_length=120, null=True)
    insert_date = models.DateTimeField(default=now)
    updated_by = models.CharField(max_length=120, null=True)
    update_date = models.DateTimeField(default=now)
    is_locked = models.CharField(max_length=20, choices=STATUS, default=1, null=True)

    def __str__(self):
        return self.po_break_down_id

class OmPoColorInfo(models.Model):
    STATUS = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    
    job_no_mst = models.CharField(max_length=50, null=False)
    po_no_mst_id = models.CharField(max_length=50, null=False)
    po_number_mst = models.CharField(max_length=50, null=False)
    color_name = models.CharField(max_length=50, null=False)
    is_deleted = models.CharField(max_length=50, null=False)
    is_master_color = models.CharField(max_length=30, choices=STATUS, null=False)
    inserted_by = models.CharField(max_length=120, null=True)
    insert_date = models.DateTimeField(default=now)
    updated_by = models.CharField(max_length=120, null=True)
    update_date = models.DateTimeField(default=now)
    status_active = models.CharField(max_length=20, choices=STATUS, default=0, null=True)
    is_locked = models.CharField(max_length=20, choices=STATUS, default=1, null=True)

    def __str__(self):
        return self.color_name

class OmPoSampleInfo(models.Model):
    STATUS = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    
    job_no_mst = models.CharField(max_length=50, null=False)
    po_no_mst_id = models.CharField(max_length=50, null=False)
    po_number_mst = models.CharField(max_length=50, null=False)
    sample_type = models.CharField(max_length=50, null=False)
    is_deleted = models.CharField(max_length=50, null=False)
    inserted_by = models.CharField(max_length=120, null=True)
    insert_date = models.DateTimeField(default=now)
    updated_by = models.CharField(max_length=120, null=True)
    update_date = models.DateTimeField(default=now)
    status_active = models.CharField(max_length=20, choices=STATUS, default=0, null=True)
    is_locked = models.CharField(max_length=20, choices=STATUS, default=1, null=True)

    def __str__(self):
        return self.sample_type

class OmPoAccesoriesInfo(models.Model):
    STATUS = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    
    job_no_mst = models.CharField(max_length=50, null=False)
    po_no_mst_id = models.CharField(max_length=50, null=False)
    po_number_mst = models.CharField(max_length=50, null=False)
    accesories_name = models.CharField(max_length=50, null=False)
    is_deleted = models.CharField(max_length=50, null=False)
    inserted_by = models.CharField(max_length=120, null=True)
    insert_date = models.DateTimeField(default=now)
    updated_by = models.CharField(max_length=120, null=True)
    update_date = models.DateTimeField(default=now)
    status_active = models.CharField(max_length=20, choices=STATUS, default=0, null=True)
    is_locked = models.CharField(max_length=20, choices=STATUS, default=1, null=True)

    def __str__(self):
        return self.job_no_mst
    
























    

