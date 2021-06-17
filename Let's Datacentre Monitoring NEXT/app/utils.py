import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
import base64
import random
import pdfkit
from django.http import HttpResponse
from playsound import playsound
from io import BytesIO
from datetime import datetime
from app import views

def generatepdf(request):
    filename = 'ldm_report_' + str(datetime.now().year) + '-' + str(datetime.now().month) + '-' + str(datetime.now().day) + '_' + str(datetime.now().hour) + ':' + str(datetime.now().minute)
    config = pdfkit.configuration(wkhtmltopdf='app\\utils\\wkhtmltopdf.exe')
    projectPath = 'app\\templates\\app\\reportprint.html'
    pdf = pdfkit.from_file(projectPath, filename + '.pdf', configuration=config)
    response = HttpResponse(pdf, content_type ='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="test.pdf"'
    
    return response

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(x,y):

    ypoint1 = round(random.uniform(20.1, 23.9), 1)
    ypoint2 = round(random.uniform(20.1, 23.9), 1)
    ypoint3 = round(random.uniform(20.1, 23.9), 1)
    ypoint4 = round(random.uniform(20.1, 23.9), 1)
    ypoint5 = round(random.uniform(20.1, 23.9), 1)
    ypointarray = np.array([ypoint1, ypoint2, ypoint3, ypoint4, ypoint5])

    xpoints = np.array([20.0, 15.0, 10.0, 5.0, 0.0])
    slaint1 = 20
    slaint2 = 24
    slabelow = np.array([slaint1,slaint1,slaint1,slaint1,slaint1])
    slaabove = np.array([slaint2,slaint2,slaint2,slaint2,slaint2])

    fig = plt.figure()
    ax = plt.axes()

    x = np.linspace(0, 10, 1000)
    plt.plot(xpoints, ypointarray, 'o-b')
    plt.plot(xpoints, slabelow,'o:r')
    plt.plot(xpoints, slaabove,'o:r')

    plt.title('Temperature of Datacentre')
    plt.xlabel('Time')
    plt.ylabel('Temperature')

    plt.xlim(20, 0)
    plt.ylim(18, 26);

    graph = get_graph()
    return graph

def kininarimasu():
    playsound("app\sound\curious.wav")
