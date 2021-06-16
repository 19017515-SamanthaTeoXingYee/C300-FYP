"""
Definition of urls for Let_s_Datacentre_Monitoring_NEXT.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('slamanagement/',views.slamanagement, name='slamanagement'),
    path('fipyaddition/',views.fipyaddition, name='fipyaddition'),
    path('fipydeletion/',views.fipydeletion, name='fipydeletion'),
    path('fipyslaoperation',views.fipyslaoperation, name='fipyslaoperation'),
    path('statisticsobservation/', views.statisticsobservation, name='statisticsobservation'),
    path('reportprint/', views.reportprint, name='reportprint'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'message': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/',
         LogoutView.as_view
        (
            template_name= 'app/loggedoff.html',
            extra_context=
            {
                'title': 'Log Off',
                'message': 'Please use this service again!',
                'year' : datetime.now().year,
            }
            # 'next_page': '/',
        ),
        name='logout'),
    path('admin/', admin.site.urls),
]
