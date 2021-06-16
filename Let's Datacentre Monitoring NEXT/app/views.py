"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from .models import App
from .utils import get_plot
from .utils import kininarimasu
from .utils import generatepdf
from django.contrib.auth.decorators import login_required

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
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
    chart = get_plot(x,y)
    return render(
        request,
        'app/statisticsobservation.html',
        {
            'title':'Statistics Observation',
            'message':'Observe our datacentre\'s temperature!', 
            'chart': chart,
            'year':datetime.now().year,
        }
    )

@login_required(login_url='/login/')
def slamanagement(request):
    """Renders the SLA Management page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/slamanagement.html',
        {
            'title':'SLA Management',
            'message':'Set the SLA for the device!',
            'year':datetime.now().year,
        }
    )

@login_required(login_url='/login/')
def fipyaddition(request):
    """Renders the Fipy Addition page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/fipyaddition.html',
        {
            'title':'Fipy Addition',
            'message':'Add Fipy devices!',
            'year':datetime.now().year,
        }
    )

@login_required(login_url='/login/')
def fipydeletion(request):
    """Renders the Fipy Deletion page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/fipydeletion.html',
        {
            'title':'Fipy Deletion',
            'message':'Delete Fipy devices!',
            'year':datetime.now().year,
        }
    )

@login_required(login_url='/login/')
def fipyslaoperation(request):
    """Renders the Fipy/SLA Operation page."""
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
    return HttpResponse(generatepdf())