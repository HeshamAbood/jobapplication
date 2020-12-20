from django.contrib import admin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from .forms import *
# Create your views here.
from django.views import generic
from .models import JobApplication
from django.views.generic.edit import CreateView, BaseFormView

class ApplicationView(CreateView):
    template_name = "application/jobapplication_form.html"
    model = JobApplication
    form_class = JobApplicationForm
    success_url = '/application/'

class ApplicationCreateView(CreateView):
    template_name = "application/job_application.html"
    model = JobApplication
    form_class = JobApplicationForm

class AppCreateView(CreateView):
    model = JobApplication
    fields = ['first_name','father_name', 'grandfather_name', 'surname', 'birth_date', 'nationality', 'blood_type', 'father_birth_place', 'ID_type', 'ID_issued_from', 'ID_number', 'ID_issue_date', 'marital_status']
#    form_class = ModelForm
    success_url = '/createapp/'


class ApplicationCView(CreateView):
    template_name = "application/register.html"
    model = JobApplication
    form_class = JobApplicationForm


class ApplySuccessView(TemplateView):
    template_name = "application/success.html"




class ApplyCreateView(CreateView):
#    template_name = "application/person.html"
    model = JobApp
    success_url = '/apply/success/'
    template_name = "/admin/change_list.html"


class CloseContactInline(admin.StackedInline):
    model = CloseContact
    extra = 1
    fields = ('close_contacts_Name',
              ('close_contacts_residence_place', 'close_contacts_relation'),
              ('close_contacts_phone', 'close_contacts_other_phone'),
              ('close_contacts_job', 'close_contacts_work_address'),)

class JobDetailsInline(admin.StackedInline):
    model = JobDetails
    fields = (('job_fit_name', 'job_know_channel'),
              ('job_salary_exp', 'job_favorite_hours'),
              ('job_non_announcement', 'job_least_income'),
              ('job_in_bank_relat', 'job_out_bank_relat'),)
    extra = 1
    max_num = 1
class QualificationInline(admin.TabularInline):
    model = Qualification
    fields = ('clfy_name', 'clfy_from_date', 'clfy_to_date', 'clfy_place', 'clfy_country',
              'clfy_type', 'clfy_graduate_date','clfy_ranking',)
    extra = 1

class LangInline(admin.TabularInline):
    model = Lang
    fields = ('lang_type','conv_level','writing_level','reading_level',)
    extra = 2
class LangExamInline(admin.TabularInline):
    model = LangExam
    fields = ('lang_ex_type','lang_score',)

class ComputerKnowledgeInline(admin.StackedInline):
    model = ComputerKnowledge
    extra = 1
    max_num = 1
class CoursesInline(admin.TabularInline):
    model = Courses
    fields = ('courses_Name', 'start_date', 'end_date', 'palce', 'country', 'cert_type', 'interval', 'score', 'specialization', )

class DrivingLicenseInline(admin.TabularInline):
    model = DrivingLicense
    extra = 1
    max_num = 1

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1
    max_num = 1
class ExperienceInline(admin.StackedInline):
    model = Experience
    fields = ('place',
                 ('position1_name', 'position1_from_date', 'position1_to_date'),
                 ('position2_name', 'position2_from_date', 'position2_to_date'),
                 ('position3_name', 'position3_from_date', 'position3_to_date'),
                 ('resp_desc','join_date', 'end_date'),
                 ('salary_begin', 'salary_end', 'allowance'),
                 ('last_supervison', 'last_supervison_phone'),
                 'end_service_reason')
    extra = 1
class AcchievemntsInline(admin.TabularInline):
    model = Acchievemnts
    extra = 1
    max_num = 1
class InqueriesInline(admin.StackedInline):
    model = Inqueries
    extra = 1
    max_num = 1

class JobAppAdmin(admin.ModelAdmin):
    model=JobApp
    fields = (('first_name', 'father_name'),
              ('grandfather_name', 'surname'),
              ('birth_date', 'nationality'),
              ('blood_type', 'father_birth_place'),
              ('ID_type', 'ID_number',
              'ID_issued_from', 'ID_issue_date'),
              ('mobile', 'mobile_other'),
              ('email', 'email_other'),
              'Hobbies',
              ('residence_place', 'residence_city'),
              ('residence_district', 'residence_street'),
              ('home_phone', 'whatsapp', 'telegram'), )



    inlines = [
        CloseContactInline,JobDetailsInline,QualificationInline,LangInline,LangExamInline,ComputerKnowledgeInline,CoursesInline,DrivingLicenseInline,SkillInline,ExperienceInline, AcchievemntsInline, InqueriesInline
    ]