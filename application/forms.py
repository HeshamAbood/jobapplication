from django import forms
from django.forms import ModelForm, DateField

from application.models import *


class JobAppAdminForm(ModelForm):
    class Meta:
        model = JobApp
        fields='__all__'
        widgets = {
            'ID_issue_date': forms.DateInput(format=('%d-%m-%Y'),
                                             attrs={'type': 'date',
                                                    'placeholder': 'Select a date'}),
            'birth_date': forms.DateInput(format=('%d-%m-%Y'),
                                             attrs={'type': 'date',
                                                    'placeholder': 'Select a date'}),
            'residence_place': forms.HiddenInput(attrs={'type':'text',
                                                        'pleaceholder':'resident place'}),
        }

class QualificationForm(ModelForm):
    class Meta:
        model = Qualification
        fields='__all__'
        widgets = {
            'clfy_from_date': forms.DateInput(format=('%d-%m-%Y'),
                                             attrs={'type': 'date',
                                                    'placeholder': 'Select a date'}),
            'clfy_to_date': forms.DateInput(format=('%d-%m-%Y'),
                                             attrs={'type': 'date',
                                                    'placeholder': 'Select a date'}),
        }

class QualificationForm(ModelForm):
    class Meta:
        model = Qualification
        fields='__all__'
        widgets = {
            'clfy_from_date': forms.DateInput(format=('%d-%m-%Y'),
                                             attrs={'type': 'date',
                                                    'placeholder': 'Select a date'}),
            'clfy_to_date': forms.DateInput(format=('%d-%m-%Y'),
                                             attrs={'type': 'date',
                                                    'placeholder': 'Select a date'}),
            'clfy_graduate_date': forms.DateInput(format=('%d-%m-%Y'),
                                             attrs={'type': 'date',
                                                    'placeholder': 'Select a date'}),
        }

class CoursesForm(ModelForm):
    class Meta:
        model = Courses
        fields='__all__'
        widgets = {
            'start_date': forms.DateInput(format=('%d-%m-%Y'),
                                             attrs={'type': 'date',
                                                    'placeholder': 'Select a date'}),
            'end_date': forms.DateInput(format=('%d-%m-%Y'),
                                             attrs={'type': 'date',
                                                    'placeholder': 'Select a date'}),

        }

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = '__all__'
        widgets = {
            'position1_from_date': forms.DateInput(format=('%d-%m-%Y'),
                                          attrs={'type': 'date',
                                                 'placeholder': 'Select a date'}),
            'position1_to_date': forms.DateInput(format=('%d-%m-%Y'),
                                        attrs={'type': 'date',
                                               'placeholder': 'Select a date'}),
            'position2_from_date': forms.DateInput(format=('%d-%m-%Y'),
                                          attrs={'type': 'date',
                                                 'placeholder': 'Select a date'}),
            'position2_to_date': forms.DateInput(format=('%d-%m-%Y'),
                                        attrs={'type': 'date',
                                               'placeholder': 'Select a date'}),
            'position3_from_date': forms.DateInput(format=('%d-%m-%Y'),
                                          attrs={'type': 'date',
                                                 'placeholder': 'Select a date'}),
            'position3_to_date': forms.DateInput(format=('%d-%m-%Y'),
                                        attrs={'type': 'date',
                                               'placeholder': 'Select a date'}),
            'join_date': forms.DateInput(format=('%d-%m-%Y'),
                                                    attrs={'type': 'date',
                                                           'placeholder': 'Select a date'}),
            'end_date': forms.DateInput(format=('%d-%m-%Y'),
                                                    attrs={'type': 'date',
                                                           'placeholder': 'Select a date'}),

        }