from django.contrib import admin
from .models import *
# Register your models here.
from .views import JobAppAdmin

admin.site.register(JobApplication)
admin.site.register(Person)
admin.site.register(CloseContact)
admin.site.register(JobDetails)
admin.site.register(Qualification)
admin.site.register(Lang)
admin.site.register(LangExam)
admin.site.register(ComputerKnowledge)
admin.site.register(Courses)
admin.site.register(DrivingLicense)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Position)
admin.site.register(Acchievemnts)
admin.site.register(Inqueries)

#admin.site.register(JobApp)
admin.site.register(JobApp, JobAppAdmin)


admin.site.site_header="Job Apply"
admin.AdminSite.index_template='admin/index.html'