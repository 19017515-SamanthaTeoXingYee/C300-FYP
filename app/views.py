"""
Definition of views.
"""
import os
import pdfkit

from django.core.exceptions import PermissionDenied
from django.db import connection
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from django.template.loader import render_to_string
from django.template import Context

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from .forms import SLAManagementForm
from .models import App
from .utils import get_plot
from .utils import generatepdf
from .utils import currentdate
from .utils import currenttime
from .utils import get_humidity
from .utils import get_latestypoint
from .utils import get_ypointpeak
from .utils import get_ypointspike
from .utils import get_slaabovesingle
from .utils import get_slabelowsingle
from .utils import send_email
from .forms import SLAManagementForm
from django.contrib.auth.decorators import login_required



def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    ypointpeak = get_ypointpeak()
    ypointspike = get_ypointspike()
    slaabovesingle = get_slaabovesingle()
    slabelowsingle = get_slabelowsingle()

    if ypointpeak > slaabovesingle or ypointspike < slabelowsingle:
        send_email()
    return render(
        request,
        'app/index.html',
        {
            'title':'Welcome',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Credits',
            'message':'Learn about members!',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Learn about the project!',
            'year':datetime.now().year,
        }
    )

@login_required(login_url='/login/')
def statisticsobservation(request):
    """Renders the statistics observation page."""
    assert isinstance(request, HttpRequest)
    x = 5
    y = 5
    latesttemperaturelevel = get_latestypoint()
    latesthumiditylevel = get_humidity()
    chart = get_plot(x,y)
    return render(
        request,
        'app/statisticsobservation.html',
        {
            'title':'Statistics Observation',
            'message':'Observe our datacentre\'s temperature!', 
            'chart': chart,
            'latesttemperaturelevel':latesttemperaturelevel,
            'latesthumiditylevel':latesthumiditylevel,
            'year':datetime.now().year,
        }
    )

@login_required(login_url='/login/')
def slamanagement(request):
    form = SLAManagementForm()
    if request.method == 'POST':
        form = SLAManagementForm(request.POST)
    context = {'form':form}
    return render(request, 'app/slamanagement.html', context)

@login_required(login_url='/login/')
def slaoperation(request):
    """Renders the SLA Operation page."""
    if request.method == 'POST':
        form = SLAManagementForm(request.POST)
    if form.is_valid():
        minimumSLA = form.cleaned_data.get('minimumSLA')
        maximumSLA = form.cleaned_data.get('maximumSLA')
        with connection.cursor() as cursor:
            cursor.execute("UPDATE DataCentre SET min_temperature = " + str(minimumSLA) + "WHERE DataCentre_id = 4")
            cursor.execute("UPDATE DataCentre SET max_temperature = " + str(maximumSLA) + "WHERE DataCentre_id = 4")
        context = {'form':form}
    return render(
        request,
        'app/slaoperation.html',
        {
            'title':'SLA Operation',
            'message':'Successful SLA Operation!',
            'year':datetime.now().year,
        }
    )

#@login_required(login_url='/login/')
#def fipyaddition(request):
#    form = FipyAdditionForm()
#    if request.method == 'POST':
#        form = FipyAdditionForm(request.POST)
#    context = {'form':form}
#    return render(request, 'app/fipyaddoperation.html', context)
#
#@login_required(login_url='/login/')
#def fipyaddoperation(request):
#    """Renders the SLA Operation page."""
#    if request.method == 'POST':
#        form = SLAManagementForm(request.POST)
#    if form.is_valid():
#        minimumSLA = form.cleaned_data.get('minimumSLA')
#        maximumSLA = form.cleaned_data.get('maximumSLA')
#        with connection.cursor() as cursor:
#            cursor.execute("UPDATE DataCentre SET min_temperature = " + str(minimumSLA) + "WHERE DataCentre_id = 4")
#            cursor.execute("UPDATE DataCentre SET max_temperature = " + str(maximumSLA) + "WHERE DataCentre_id = 4")
#        context = {'form':form}
#    return render(
#        request,
#        'app/fipyaddoperation.html',
#        {
#            'title':'Fipy Operation',
#            'message':'Successful Fipy Operation!',
#            'year':datetime.now().year,
#        }
#    )

def reportprinting():
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/fipyslaoperation.html',
        {
            'title':'Fipy or SLA Operation',
            'message':'Successful Fipy or SLA Operation!',
            'year':datetime.now().year,
        }
    )

@login_required(login_url='/login/')
def reportprint(request):
    filename = 'ldmreport' + currentdate() + '-' + currenttime()
    response = generatepdf()
    return response