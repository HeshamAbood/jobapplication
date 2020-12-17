from django import forms
from django.forms import ModelForm

from application.models import JobApplication
from django.forms.models import inlineformset_factory
from application.models import *

class JobApplicationForm(ModelForm):
    class Meta:
        fields = "__all__"
        model = JobApplication
