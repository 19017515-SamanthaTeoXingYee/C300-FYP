"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .models import App
from .utils import get_plot

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
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
            'message':'Let\'s learn about the members of this project!',
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
            'message':'Let\'s learn about the project!',
            'year':datetime.now().year,
        }
    )

def statisticsobservation(request):
    """Renders the statistics observation page."""
    assert isinstance(request, HttpRequest)
    x = 5
    y = 6
    chart = get_plot(x,y)
    return render(
        request,
        'app/statisticsobservation.html',
        {
            'title':'Statistics Observation',
            'message':'Let\'s see the statistics!', 
            'chart': chart,
            'year':datetime.now().year,
        }
    )