from django.conf.urls import url
from django.contrib.auth import admin
from django.contrib.auth.views import logout
from django.views.generic import TemplateView

from . import views
from .views import ApplySuccessView

urlpatterns = [
#    url(r'^$', logout, {'template_name': 'logged_out.html'}, name='final'),
#    url(r'^apply/success', ApplySuccessView.as_view(), name='success'),

]
