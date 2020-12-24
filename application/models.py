import os
from datetime import date

from django import forms
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, FileExtensionValidator
from django.db import models
from django.forms import DateInput

from .validators import validate_file_extension
from jobsApp import settings
from django.contrib.auth import get_user_model

class JobApp(models.Model):
    nationalities = (('Y', 'يمني'), ('O', 'أخرى'))
    blood_groups = (('A1', 'A+'),('A2', 'A-'), ('B1', 'B+'), ('B2', 'B-'), ('AB1', 'AB+'), ('AB2', 'AB-'), ('O1', 'O+'),('O2', 'O-'),)
    id_types = (('ID', 'بطاقة شخصية'), ('PS', 'جوازسفر'), ('O', 'أخرى'))
    marital_options = (('S', 'عازب'), ('M', 'متزوج'), ('O', 'أخرى'))
    city_options = ((23,'الأمانة'),
    (1, 'عمران'), (2, 'محافظة صنعاء'), (3, 'الحديدة'), (4, 'الجوف'), (5, 'المحويت'), (6, 'أمانة'), (7, 'ذمار'), (8, 'حجة'),
    (9, 'إب'), (10, 'مأرب'), (11, 'محافظة'), (12, 'صعدة'),
    (13, 'صنعاء'), (14, 'تعز'), (15, 'عدن'), (16, 'أبين'), (17, 'محافظة'), (18, 'المهرة'), (19, 'حضرموت'),
    (20, 'أرخبيل'), (21, 'لحج'), (22, 'شبوة'))
    yn_choices = (('Y', 'نعم'), ('N', 'لا'))
    YEAR_CHOICES = tuple([(str(x),str(x)) for x in range(1950,2020)])

    def user_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return 'user_{0}\photo\{1}'.format(instance.ID_number, filename)

    first_name = models.CharField(max_length=200, verbose_name=u"الاسم الأول")
    father_name = models.CharField(max_length=200, verbose_name=u"اسم الأب")
    grandfather_name = models.CharField(max_length=200, verbose_name=u"اسم الجد")
    surname = models.CharField(max_length=200, verbose_name=u"اللقب:")
    birth_date = models.DateField(default=date.today, verbose_name=u"تاريخ الميلاد ", )
    birth_place=models.CharField(max_length=200, verbose_name=u"مكان الميلاد")

    nationality = models.CharField(max_length=200, choices=nationalities, verbose_name=u"الجنسية")
    blood_type = models.CharField(max_length=200, choices=blood_groups, verbose_name=u"فصيلة الدم", null=True, blank=True, )
    father_birth_place = models.CharField(max_length=200, verbose_name=u"مكان ميلاد الأب")
    ID_type = models.CharField(max_length=200, choices=id_types, verbose_name=u"نوع الهوية", )
    ID_issued_from = models.CharField(max_length=200, verbose_name=u"صادرة من" )
    ID_number = models.CharField(max_length=200, verbose_name=u"برقم" )
    ID_issue_date = models.DateField(default=date.today, verbose_name=u"وبتاريخ" ,)
#    ID_photo = models.ImageField(upload_to=user_directory_path,validators=[validate_file_extension], default="", verbose_name=u"صورة شخصية" )
    marital_status=models.CharField(max_length=200, verbose_name=u"الحالة الإجتماعية" ,choices=marital_options)
    childs_number=models.CharField(max_length=200, verbose_name=u"عدد الأولاد",default="", null=True, blank=True,  )

    mobile = models.CharField(max_length=200, verbose_name=u"رقم هاتفك المحمول" )
    mobile_other = models.CharField(max_length=200, verbose_name=u"رقم أخر", default="", null=True, blank=True, )

    email = models.EmailField(max_length=100, default="", verbose_name=u"البريد الإلكتروني")
    email_other = models.EmailField(max_length=100, default="", verbose_name=u"أخر",  null=True, blank=True,)

    Hobbies = models.TextField(max_length=2000, default="", verbose_name=u"الهوايات", null=True, blank=True, )

    residence_place = models.CharField(max_length=100, verbose_name=u"عنوان السكن الدائم",blank=True,null=True, db_column=False)
    residence_city = models.IntegerField( choices=city_options, verbose_name=u"المحافظة",  )
    residence_district = models.CharField(max_length=200, default="", verbose_name=u"بجوار أو بالقرب ", )
    residence_street = models.CharField(max_length=200, default="", verbose_name=u"الحي أو الشارع", )

    home_phone = models.CharField(max_length=200, default="", verbose_name=u"رقم هاتف المنزل", null=True, blank=True, )
    whatsapp = models.CharField(max_length=200, default="", verbose_name=u"حساب واتساب", null=True, blank=True, )
    telegram = models.CharField(max_length=200, default="", verbose_name=u"حساب التليجرام", null=True, blank=True, )
#    photo = models.ImageField(upload_to=user_directory_path,validators=[validate_file_extension],verbose_name=u"صورة شخصية" ,default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,)

    def __str__(self):
        return str(self.user)+" "+str(self.first_name)+" "+str(self.father_name)+" "+str(self.surname)+" "+str(self.ID_number)

    class Meta:
        verbose_name ="استمارة طلب توظيف"


class CloseContact(models.Model):
    close_contacts_Name = models.CharField(max_length=200,verbose_name=u"الاسم" , default="", )
    close_contacts_residence_place = models.CharField(max_length=200,verbose_name=u"عنوان السكن", default="",)
    close_contacts_relation = models.CharField(max_length=200,verbose_name=u"نوع القرابة" ,default="", )
    close_contacts_phone = models.CharField(max_length=200,verbose_name=u"رقم الهاتف" ,default="", )
    close_contacts_other_phone = models.CharField(max_length=200,verbose_name=u"رقم أخر" ,default="", null=True, blank=True, )
    close_contacts_job = models.CharField(max_length=200,verbose_name=u"العمل" ,default="", )
    close_contacts_work_address = models.CharField(max_length=200,verbose_name=u"عنوان العمل" ,default="", )
    job = models.ForeignKey(JobApp, on_delete=models.CASCADE,verbose_name=u" ", default="" )

class JobDetails(models.Model):
    yn_choices = (('Y', 'نعم'), ('N', 'لا'))
    rel_choices=(('B','بنوك'),('EX','شركات ومنشآت صرافة'),('O','أخرى'))
    job_fit_name = models.CharField(max_length=200,verbose_name=u"الوظيفة التي تقدمت لشغلها و التي تتناسب مع مؤهلك" ,default="", )
    job_know_channel = models.CharField(max_length=200,verbose_name=u"كيف علمت بهذه الوظيفة" ,default="", )
    job_salary_exp = models.CharField(max_length=100,verbose_name=u"الراتب والمزايا المتوقعة" ,default="", )
    job_favorite_hours = models.CharField(max_length=200,verbose_name=u"ساعات العمل التي تفضلها" ,default="", )
    job_non_announcement = models.CharField(max_length=200,verbose_name=u"حدد وضيفة أخرى معلن عنها وترغب بالتقدم لها وتعتقد أنك مؤهل لها عدا الوظيفة المتقدم لها" ,default="", null=True, blank=True, )
    job_least_income = models.CharField(max_length=200,verbose_name=u"ما هو أقل دخل شهري يمكنك العمل به شاملاً جميع البدلات" ,default="", )
    job_in_bank_relat = models.CharField(max_length=200,verbose_name=u"هل لديك أقارب في البنك المركزي اليمني" ,choices=yn_choices,default="", null=True, blank=True, )
    job_in_bank_relat_desc = models.CharField(max_length=200,verbose_name=u"في حالة الإجابة بنعم – نرجو تحديد اسم وصلة الشخص" ,default="", null=True, blank=True, )
    job_out_bank_relat = models.CharField(max_length=200,verbose_name=u"هل لديك أقارب في الجهات ذات الصلة بالبنك", choices=yn_choices,default="", null=True, blank=True, )
    job_out_bank_relat_desc = models.CharField(max_length=200,verbose_name=u"في حالة الإجابة بنعم – نرجو تحديد اسم الجهة واسم وصلة الشخص", default="", null=True, blank=True, )
    job = models.ForeignKey(JobApp, on_delete=models.CASCADE,default="" )

class Qualification(models.Model):
    types=(('s','الثانوية'),('id', 'دبلوم متوسط'),
            ('b','بكالوريوس'),('hd','دبلوم عالي'),('m','ماجيستير'),
            ('phd','دكتوراه'),('o','اخرى'))

    def user_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return 'user_{0}\docs\{1}'.format(instance.job.ID_number, filename)

    clfy_name = models.CharField(max_length=100, default="",verbose_name=u"المؤهل الدراسي", null=True, blank=True, choices=types, )
    clfy_from_date =  models.DateField(default=date.today,verbose_name=u"من",)
    clfy_to_date =  models.DateField(default=date.today,verbose_name=u"إلى",)
    clfy_place = models.CharField(max_length=80, default="",verbose_name=u"اسم المدرسة/الجامعة", null=True, blank=True,)
    clfy_country = models.CharField(max_length=80, default="",verbose_name=u"الدولة", null=True, blank=True, )
    clfy_type = models.CharField(max_length=80, default="",verbose_name=u"التخصص", null=True, blank=True,)
    clfy_graduate_date = models.DateField(default=date.today,verbose_name=u"سنة التخرج",)
    clfy_ranking = models.CharField(max_length=80, default="", verbose_name=u"التقدير العام", null=True, blank=True, )
#    clfy_photo = models.FileField(upload_to=user_directory_path,validators=[validate_file_extension] , verbose_name=u"وثيقة المؤهل",default="")
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
    job = models.ForeignKey(JobApp, on_delete=models.CASCADE,null=True, blank=True)


    class Meta:
        def __format__(self):
            setattr(width='15em')


class Lang(models.Model):
    type_options=(('en','الإنجليزية'),('ar','العربية'),('o','اخرى'))
    target_level=(('e','ممتاز'),('vg','جيد جد ا'),('g','جيد'),('ac','متوسط'),(('w','ضعيف')))
    lang_type = models.CharField(max_length=200, default="",verbose_name=u"اللغة", choices=type_options, )
    conv_level=models.CharField(max_length=200, null=True, blank=True, default="",verbose_name=u"محادثة", choices=target_level, )
    writing_level=models.CharField(max_length=200, null=True, blank=True, default="",verbose_name=u"كتابة", choices=target_level, )
    reading_level=models.CharField(max_length=200, null=True, blank=True, default="",verbose_name=u"قراءة", choices=target_level, )

    job = models.ForeignKey(JobApp, on_delete=models.CASCADE,default="" )

class RelatedLang(models.Model):
    x= models.CharField(max_length=100, default="",verbose_name=u"نوع الإختبار",  null=True, blank=True)
    y = models.CharField(max_length=100, default="",verbose_name=u"التقدير العام", null=True, blank=True, )

    job = models.ForeignKey(JobApp, on_delete=models.CASCADE,default="" )

class Exam(models.Model):
    yn_choices = (('Y', 'نعم'), ('N', 'لا'))

    type_options = (('T', 'Toefel'), ('en', 'امتحان أخر باللغة الانجليزية'), ('o', 'امتحان أخر بلغة أخرى'))
    ex_type= models.CharField(max_length=100, default="",verbose_name=u"نوع الإختبار",  null=True, choices=type_options, )
    ex_score = models.CharField(max_length=100, default="",verbose_name=u"التقدير العام", null=True, blank=True, )

    job = models.ForeignKey(JobApp, on_delete=models.CASCADE,default="" )

class ComputerKnowledge(models.Model):
    yn_choices = (('Y', 'نعم'), ('N', 'لا'))
    computer_knowledge = models.CharField(max_length=200,verbose_name=u"هل تستطيع استخدام الحاسب الآلي", default="", null=True, blank=True, choices=yn_choices , )
    computer_knowledge_details=models.CharField(max_length=200, default="",verbose_name=u"عند الإجابة بنعم نرجو تحديد أسماء البرامج", null=True, blank=True, )
    internet_knowledge = models.CharField(max_length=200,verbose_name=u"هل تستطيع استخدام البريد الإلكتروني", default="", null=True, blank=True, choices=yn_choices  )
    internet_knowledge_details=models.CharField(max_length=200, default="",verbose_name=u"عند الإجابة بنعم نرجو تحديد أسماء البريد", null=True, blank=True, )

    job = models.ForeignKey(JobApp, on_delete=models.CASCADE,default="" )

class Courses(models.Model):
    courses_Name = models.CharField(max_length=200,verbose_name=u"اسم الدورة", default="", null=True, blank=True, )
    start_date = models.DateField(default=date.today,verbose_name=u"الفترة من", null=True, blank=True, )
    end_date = models.DateField(default=date.today,verbose_name=u"الفترة إلى", null=True, blank=True, )
    palce = models.CharField(max_length=200, default="",verbose_name=u"الجهة المنفذة للدورة", null=True, blank=True, )
    country = models.CharField(max_length=200, default="",verbose_name=u"الدولة", null=True, blank=True, )
    cert_type = models.CharField(max_length=200, default="",verbose_name=u"التخصص", null=True, blank=True, )
    interval = models.CharField(max_length=200, default="",verbose_name=u"عدد الساعات", null=True, blank=True, )
    score = models.CharField(max_length=200, default="",verbose_name=u"التقدير العام", null=True, blank=True, )

    job = models.ForeignKey(JobApp, on_delete=models.CASCADE,default="" )

class DrivingLicense(models.Model):
    yn_choices = (('Y', 'نعم'), ('N', 'لا'))
    driving_license = models.CharField(max_length=200,verbose_name=u"هل تستطيع قيادة السيارات وسائل النقل",blank=True, default="", null=True, choices=yn_choices, )
    driving_license_active = models.CharField(max_length=20,verbose_name=u"هل لديك رخصة قيادة سارية المفعول",blank=True, default="",null=True, choices=yn_choices)
    job = models.ForeignKey(JobApp, on_delete=models.CASCADE,default="" )

class Skill(models.Model):
    skill = models.TextField(max_length=500, default="",verbose_name=u"الرجاء تحديد أي مهارات/قدرات خاصة بك", null=True, blank=True, )
    job = models.ForeignKey(JobApp, on_delete=models.CASCADE,default="" )

class Experience(models.Model):
    place = models.CharField(max_length=200, default="",verbose_name=u"أسم المنشأة وعنوانها", null=True, blank=True, )
    position1_name=models.CharField(max_length=200, default="",verbose_name=u"مسميات الوظائف التي شغلتها 1", null=True, blank=True, )
    position1_from_date=models.DateField(default=date.today,verbose_name=u"من تاريخ", null=True, blank=True, )
    position1_to_date=models.DateField(default=date.today,verbose_name=u"الى تاريخ", null=True, blank=True, )
    position2_name=models.CharField(max_length=200, default="",verbose_name=u"مسميات الوظائف التي شغلتها 2", null=True, blank=True, )
    position2_from_date=models.DateField(default=date.today,verbose_name=u"من تاريخ", null=True, blank=True, )
    position2_to_date=models.DateField( default=date.today,verbose_name=u"الى تاريخ", null=True, blank=True, )
    position3_name=models.CharField(max_length=200, default="",verbose_name=u"مسميات الوظائف التي شغلتها 3", null=True, blank=True, )
    position3_from_date=models.DateField(default=date.today,verbose_name=u"من تاريخ", null=True, blank=True, )
    position3_to_date=models.DateField(default=date.today,verbose_name=u"الى تاريخ", null=True, blank=True, )
    resp_desc=models.CharField(max_length=200, default="",verbose_name=u"وصف مختصر للمهام والواجبات والمسؤوليات لأخر وظيفة", null=True, blank=True, )
    join_date=models.DateField(default=date.today, verbose_name=u"تاريخ الالتحاق بالعمل",null=True, blank=True, )
    end_date=models.DateField(default=date.today, verbose_name=u"تاريخ انتهاء الخدمة",null=True, blank=True, )
    salary_begin=models.CharField(max_length=200,verbose_name=u"الراتب الشهري عند التوظيف", default="", null=True, blank=True, )
    salary_end = models.CharField(max_length=200,verbose_name=u"الراتب الشهري عند انتهاء الخدمة", default="", null=True, blank=True, )
    allowance = models.CharField(max_length=200, verbose_name=u"العلاوات الأخرى بالتفصيل",default="", null=True, blank=True, )
    last_supervison=models.CharField(max_length=200, verbose_name=u"اسم أخر رئيس مباشر عليك",default="", null=True, blank=True, )
    last_supervison_phone = models.CharField(max_length=200,verbose_name=u"رقم هاتفه", default="", null=True, blank=True, )
    end_service_reason= models.CharField(max_length=200, verbose_name=u"أسباب انتهاء الخدمة",default="", null=True, blank=True, )
    job = models.ForeignKey(JobApp, on_delete=models.CASCADE,default="" )

class Position(models.Model):
    verbose_name_plural = "الوظائف"
    name=models.CharField(max_length=200,verbose_name=u" ",default="", null=True, blank=True, )
    from_date=models.DateField(default=date.today,verbose_name=u" ",)
    to_date=models.DateField(default=date.today, verbose_name=u" ",)
    experience=models.ForeignKey(Experience, on_delete=models.CASCADE,default="" )

class Acchievemnts(models.Model):
    details=models.TextField(max_length=500, default="",verbose_name=u"اذكر باختصار أهم انجازاتك المهنية", null=True, blank=True, )
    job = models.ForeignKey(JobApp, on_delete=models.CASCADE,verbose_name=u" ",default="" )

class Inqueries(models.Model):
    city_options = ((23,'الأمانة'),
    (1, 'عمران'), (2, 'محافظة صنعاء'), (3, 'الحديدة'), (4, 'الجوف'), (5, 'المحويت'), (6, 'أمانة'), (7, 'ذمار'), (8, 'حجة'),
    (9, 'إب'), (10, 'مأرب'), (11, 'محافظة'), (12, 'صعدة'),
    (13, 'صنعاء'), (14, 'تعز'), (15, 'عدن'), (16, 'أبين'), (17, 'محافظة'), (18, 'المهرة'), (19, 'حضرموت'),
    (20, 'أرخبيل'), (21, 'لحج'), (22, 'شبوة'))
    yn_choices = (('Y', 'نعم'), ('N', 'لا'))
    yn_choices_2 = (('Y', 'نعم'), ('N', 'لا'),('NN','ليس الان'))

    inq_loan=models.CharField(max_length=20,blank=True, default="",verbose_name=u"هل عليك قروض أو ديون أو مشاكل مادية", choices=yn_choices)
    inq_training=models.CharField(max_length=20,blank=True, default="",verbose_name=u"هل ترغب في الحصول على دورات تدريبية في مجال عملك", choices=yn_choices_2)
    inq_training_detail=models.CharField(max_length=200,default="",verbose_name=u"عند الإجابة بنعم - نرجو تحديدها",null=True, blank=True, )
    inq_long_term_disease=models.CharField(max_length=200,default="",verbose_name=u"هل تعاني من أي مشاكل صحية أو نفسية أو أمراض مزمنة",null=True, blank=True ,choices=yn_choices )
    inq_long_term_disease_detail=models.CharField(max_length=200,default="",verbose_name=u"في حالة الإجابة ب )نعم( نرجو ذكرها",null=True, blank=True, )
    inq_surgery=models.CharField(max_length=200,default="",null=True,verbose_name=u"هل سبق ان أجريت لك أي عملية جراحية", blank=True,choices=yn_choices  )
    inq_surgery_detail=models.CharField(max_length=200,default="",verbose_name=u"عند الإجابة بنعم - نرجو تحديدها",null=True, blank=True ,)
    inq_cust_contact=models.CharField(max_length=20,blank=True,default="",verbose_name=u"هل سبق وكانت طبيعة عملك تتطلب التعامل مع العملاء؟",choices=yn_choices )
    inq_favor_w_place=models.IntegerField(default="0",blank=True,verbose_name=u"ماهي المحافظة التي تفضل العمل فيها، بحكم تواجد السكن الأصلي لك؟" , choices=city_options )
    inq_accept_w_place=models.CharField(max_length=200,blank=True,default="",verbose_name=u"وهل تقبل العمل في محافظة إذا طلب منك ذلك", choices=yn_choices )
    inq_explain=models.TextField(max_length=200,default="",verbose_name=u"لماذا ترغب في العمل لدى البنك المركزي اليمني؟")
    job = models.ForeignKey(JobApp, on_delete=models.CASCADE,default="" )

