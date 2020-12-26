from django.contrib import admin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from .models import *
from .forms import *
# Create your views here.
from django.views import generic

from django.views.generic.edit import CreateView, BaseFormView



class JobAppCreateView(CreateView):
#    template_name="admin/change_list.html"
    model = JobApp
#    fields = ['first_name','father_name', 'grandfather_name', 'surname', 'birth_date', 'nationality', 'blood_type', 'father_birth_place', 'ID_type', 'ID_issued_from', 'ID_number', 'ID_issue_date', 'marital_status']
#    form_class = ModelForm
    fields = '__all__'
    success_url = '/createapp/'


class ApplySuccessView(TemplateView):
    template_name = "application/success.html"


class ApplyCreateView(CreateView):
#    template_name = "application/person.html"
    model = JobApp
    success_url = '/apply/logout/'
    template_name = "/admin/change_list.html"


class CloseContactInline(admin.StackedInline):
    model = CloseContact
    extra = 1
    fields = ('close_contacts_Name',
              ('close_contacts_residence_place', 'close_contacts_relation'),
              ('close_contacts_phone', 'close_contacts_other_phone'),
              ('close_contacts_job', 'close_contacts_work_address'),)
    verbose_name_plural = "أسماء مقربين للتواصل بهم عند الحاجة يجب ذكر شخصين على الأقل"
    verbose_name = "أسماء مقربين للتواصل بهم عند الحاجة"


class JobDetailsInline(admin.StackedInline):
    model = JobDetails
    fields = (('job_fit_name', 'job_know_channel'),
              ('job_salary_exp', 'job_favorite_hours'),
              ('job_non_announcement', 'job_least_income'),
              ('job_in_bank_relat', 'job_in_bank_relat_desc'),
              ('job_out_bank_relat', 'job_out_bank_relat_desc'),)
    extra = 1
    max_num = 1
    verbose_name_plural = "معلومات الوظيفة التي تم التقدم لها"
    verbose_name = "معلومات الوظيفة التي تم التقدم لها"

class QualificationInline(admin.StackedInline):
    model = Qualification
    form = QualificationForm
    fields = (('clfy_name', 'clfy_from_date', 'clfy_to_date'),
              ( 'clfy_place', 'clfy_country'),
              ('clfy_type', 'clfy_graduate_date','clfy_ranking',))
    extra = 1
    verbose_name_plural = "المعلومات الخاصة بالمؤهلات العلمية"
    verbose_name = "المعلومات الخاصة بالمؤهلات العلمية"


class LangInline(admin.TabularInline):
    model = Lang
    fields = ('lang_type','conv_level','writing_level','reading_level',)
    extra = 2
    verbose_name_plural = "اللغات التي تجيدها"
    verbose_name = "اللغة التي تجيدها"

class ExamInline(admin.TabularInline):
    model = Exam
    fields = ('ex_type','ex_score',)
    verbose_name_plural =  "هل سبق وتقدمت لامتحان اللغة"
    verbose_name = "هل سبق وتقدمت لامتحان اللغة"
    extra = 1

class RelatedLangInline(admin.TabularInline):
    model = RelatedLang
    fields = ('x','y',)
    verbose_name_plural = "إختبار اللغة"
    verbose_name = "إختبار اللغة"
    extra = 2

class ComputerKnowledgeInline(admin.StackedInline):
    model = ComputerKnowledge
    fields = (('computer_knowledge', 'computer_knowledge_details'),
              ('internet_knowledge','internet_knowledge_details'))
    extra = 1
    max_num = 1
    verbose_name_plural = "استخدام الحاسب الآلي والانترنت"
    verbose_name = "استخدام الحاسب الآلي والانترنت"

class CoursesInline(admin.StackedInline):
    model = Courses
    form = CoursesForm
    fields = (('courses_Name'),
               ('start_date', 'end_date'),
              ('palce', 'country'),
                ('cert_type', 'interval', 'score', ))
    verbose_name_plural = "الدورات التدريبة"
    verbose_name = "الدورات التدريبة"
    extra = 1

class DrivingLicenseInline(admin.StackedInline):
    model = DrivingLicense
    extra = 1
    max_num = 1
    fields = (('driving_license'),
              ('driving_license_active'),)
    verbose_name_plural = "معلومات رخصة القيادة"
    verbose_name = "معلومات رخصة القيادة"

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1
    max_num = 1
    verbose_name_plural = "المهارات والقدرات"
    verbose_name = "المهارات والقدرات"

class ExperienceInline(admin.StackedInline):
    model = Experience
    form = ExperienceForm
    fields = ('place',
                 ('position1_name', 'position1_from_date', 'position1_to_date'),
                 ('position2_name', 'position2_from_date', 'position2_to_date'),
                 ('position3_name', 'position3_from_date', 'position3_to_date'),
                 ('resp_desc','join_date', 'end_date'),
                 ('salary_begin', 'salary_end', 'allowance'),
                 ('last_supervison', 'last_supervison_phone'),
                 'end_service_reason')
    extra = 1
    verbose_name_plural = "الخبرات العملية"
    verbose_name = "الخبرات العملية"

class AcchievemntsInline(admin.TabularInline):
    model = Acchievemnts
    extra = 1
    max_num = 1
    verbose_name_plural = "الانجازات"
    verbose_name = "الانجازات"

class InqueriesInline(admin.StackedInline):
    model = Inqueries
    fields = (
        ('inq_loan'),
        ('inq_training','inq_training_detail'),
        ('inq_long_term_disease','inq_long_term_disease_detail'),
        ('inq_surgery','inq_surgery_detail'),
        ('inq_cust_contact'),
        ('inq_favor_w_place', 'inq_accept_w_place'),
        ('inq_explain'),
    )
    extra = 1
    max_num = 1
    verbose_name_plural = "استفسارات عامة"
    verbose_name = "استفسارات عامة"



class JobAppAdmin(admin.ModelAdmin):
    model=JobApp
    form =JobAppAdminForm
    verbose_name_plural = "استمارة طلب توظيف"
    verbose_name ="استمارة طلب توظيف"
    fields = (('first_name', 'father_name'),
              ('grandfather_name', 'surname'),
              ('birth_date','birth_place', 'nationality'),
              ('blood_type', 'father_birth_place'),
              ('ID_type', 'ID_number'),
              ('ID_issued_from', 'ID_issue_date'),
              ('marital_status','childs_number'),
              ('mobile', 'mobile_other'),
              ('email', 'email_other'),
              'Hobbies',
              ('residence_place', ),
              ('residence_city', 'residence_street', 'residence_district'),
              ('home_phone', 'whatsapp', 'telegram'),
              )


    inlines = [
        CloseContactInline,JobDetailsInline,QualificationInline,LangInline,ExamInline,ComputerKnowledgeInline,CoursesInline,DrivingLicenseInline,SkillInline,ExperienceInline, AcchievemntsInline, InqueriesInline
    ]

    def response_add(self, request, obj, post_url_continue=None):
        return redirect('/apply/logout')




    def save_model(self, request, obj, form, change):
        obj.user = request.user
        User = get_user_model()
        tuser = User.objects.get(username=request.user)
#        obj.user.is_staff=False
        tuser.is_staff = False
        print("otype", type(obj.user))
        print("ttype",type(tuser))
        print("o is",obj.user.is_staff)
        print("t is", tuser.is_staff)
        super().save_model(request, obj, form, change)
        tuser.save()
#        obj.user.save()
        print('user group changed')