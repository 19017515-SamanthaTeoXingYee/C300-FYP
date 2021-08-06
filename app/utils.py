import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
import base64
import os
import pdfkit
import random
from app import views
from datetime import datetime
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import get_template
from io import BytesIO
from xhtml2pdf import pisa
from app import models 
from .models import DataCentre
from .models import Customer
from .models import IOT_devices
from .models import StoreData
from .models import Test3

def currentdate():
    currentdate = str(datetime.now().year) + '-' + str(datetime.now().month) + '-' + str(datetime.now().day)
    return currentdate

def currenttime():
    currenttime = str(datetime.now().hour) + '.' + str(datetime.now().minute)
    return currenttime

def currentyear():
    currentyear = str(datetime.now().year)
    return currentyear

def filename():
    filename = 'ldmreport' + currentdate() + '-' + currenttime()
    return filename

def generatepdf():
    pisa.showLogging()
    source_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset = "utf-8">
    <title>Let's! Datacentre Monitoring</title>
    </head>
    <body>
    <h1>Let's! Datacentre Monitoring</h1>
    <p>This is the report for your datacentre. This information is accurate as at """ + currentdate() + """ at """ + currenttime() + """.</p>
    <br>
    <p>The temperature reported for Fipy 1 is """ + get_latestypoint() + """.</p>
    <p>The humidity for Fipy 1 is <bold> """ + get_humidity() + """ </bold>.
    <br>
    <p>The current minimum temperature, as per the SLA, is """ + str(get_slabelowsingle()) + """.</p>
    <p>The current maximum temperature, as per the SLA, is """ + str(get_slaabovesingle()) + """ </p>
    <br>
    <footer>
    <p>&copy; """ + currentyear() + """ - Let's! Datacentre Monitoring</p>
    </footer>
    <br>
    </body>
    </html> 
    """
    filename = 'ldmreport' + currentdate() + '-' + currenttime()
    output_filename = "test.pdf"
    response = HttpResponse(content_type='application/pdf')
    pisa_status = pisa.CreatePDF(source_html,dest=response)
    response['Content-Disposition'] = 'attachment; filename="' + filename + '.pdf"'
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def get_graphwithbase64():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_graph():
    buffer = BytesIO()
    graph = plt.savefig('fipygraph.png')
    return graph

def get_slaabovesingle():
    slaabovesingle = (DataCentre.objects.raw('SELECT max_temperature, DataCentre_id FROM DataCentre')[0]).max_temperature
    return slaabovesingle

def get_slaabove():
    slaint1 = get_slaabovesingle()
    slaabove = np.array([slaint1,slaint1,slaint1,slaint1,slaint1])
    return slaabove

def get_slabelowsingle():
    slabelowsingle = (DataCentre.objects.raw('SELECT min_temperature, DataCentre_id FROM DataCentre')[0]).min_temperature
    return slabelowsingle

def get_slabelow():
    slaint2 = get_slabelowsingle()
    slabelow = np.array([slaint2,slaint2,slaint2,slaint2,slaint2])
    return slabelow

def get_xpoints():
    xpoint1 = 40
    xpoint2 = 30
    xpoint3 = 20
    xpoint4 = 10
    xpoint5 = 0
    xpointarray = np.array([xpoint1, xpoint2, xpoint3, xpoint4, xpoint5])
    return xpointarray

def get_humidity():
    humidity = StoreData.objects.raw('SELECT humidity FROM app_StoreData')
    return humidity

def get_ypoints():
    ypoint1 = Test3.objects.raw('SELECT payload, EventProcessedUtcTime FROM Test3')[4]
    ypoint2 = Test3.objects.raw('SELECT payload, EventProcessedUtcTime FROM Test3')[3]
    ypoint3 = Test3.objects.raw('SELECT payload, EventProcessedUtcTime FROM Test3')[2]
    ypoint4 = Test3.objects.raw('SELECT payload, EventProcessedUtcTime FROM Test3')[1]
    ypoint5 = Test3.objects.raw('SELECT payload, EventProcessedUtcTime FROM Test3')[0]
    ypointarray = np.array([ypoint1.payload, ypoint2.payload, ypoint3.payload, ypoint4.payload, ypoint5.payload])
    return ypointarray

def get_ypointpeak():
    ypointarray = get_ypoints()
    controlvar = 0
    ypointpeak = 0
    for i in ypointarray:
        if ypointpeak <= ypointarray[controlvar]:
            ypointpeak = ypointarray[controlvar]
            print('ypointpeak:' + str(ypointpeak))
        controlvar = controlvar + 1
    return ypointpeak

def get_ypointspike():
    ypointarray = get_ypoints()
    controlvar = 0
    ypointspike = 100
    for i in ypointarray:
        if ypointspike >= ypointarray[controlvar]:
            ypointspike = ypointarray[controlvar]
            print('ypointspike:' + str(ypointspike))
        controlvar = controlvar + 1
    return ypointspike

def get_latestypoint():
    ypointarray = get_ypoints()
    latestypoint = ypointarray[4]
    return str(latestypoint)

def get_latestxpoint():
    xpointarray = get_xpoints()
    latestypoint = xpointarray[4]
    return str(latestxpoint)

def get_plot(x,y):
    fig = plt.figure()
    ax = plt.axes()

    x = np.linspace(0, 10, 1000)
    plt.plot(get_xpoints(), get_ypoints(), 'o-b')
    plt.plot(get_xpoints(), get_slabelow(),'o:r')
    plt.plot(get_xpoints(), get_slaabove(),'o:r')

    plt.title('Temperature of Datacentre')
    plt.xlabel('Time')
    plt.ylabel('Temperature')

    plt.xlim(20, 0)
    plt.ylim(10, 31); #change this to the range the user can input

    graph = get_graphwithbase64()
    return graph

def get_emails():
    emails = []
    for p in Customer.objects.raw('SELECT email, customer_id FROM Customer'):
        theEmail = p.email
    emails.append(theEmail)
    return emails

def send_email():
    subject = 'Notice of Temperature Levels SLA Breach'
    message = f'Dear User, based on the specified SLA levels of ' + str(get_slaabovesingle()) + ' and ' + str(get_slabelowsingle()) + ', we would like to inform you of the breach in your temperature levels being ' + get_latestypoint() + '. It is advised that you rectify this as soon as possible.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = get_emails()
    send_mail(subject, message, email_from, recipient_list )