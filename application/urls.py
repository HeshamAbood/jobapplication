from django.conf.urls import url
from django.views.generic import TemplateView

from . import views
from .views import ApplySuccessView

urlpatterns = [
    url(r'^$', views.ApplicationView.as_view(), name='index'),
    url(r'^create/', views.ApplicationCreateView.as_view(), name='create'),
    url(r'^createap/', views.ApplicationCView.as_view(), name='create'),
    url(r'^createapp/', views.AppCreateView.as_view(), name='createApp'),
    url(r'^apply/', views.ApplyCreateView.as_view(), name='apply'),
    url(r'^apply/success', ApplySuccessView.as_view(), name='success'),

]
