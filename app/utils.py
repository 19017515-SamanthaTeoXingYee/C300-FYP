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

def currentdate():
    currentdate = str(datetime.now().year) + '-' + str(datetime.now().month) + '-' + str(datetime.now().day)
    return currentdate

def currenttime():
    currenttime = str(datetime.now().hour) + '.' + str(datetime.now().minute)
    return currenttime

def currentyear():
    return str(datetime.now().year)

def filename():
    filename = 'ldmreport' + currentdate() + '-' + currenttime()
    return filename

def generatepdf():    
    config = pdfkit.configuration(wkhtmltopdf='app\\utils\\wkhtmltopdf.exe')
    html = f"""
        <!DOCTYPE html>
    <html>
    <head>
    <meta charset = "utf-8">
    <title>Let's! Datacentre Monitoring</title>
    </head>
    <body>
    <h1>Let's! Datacentre Monitoring</h1>
    <p>This is the report for your datacentre. This information is accurate as at """ + currentdate() + """ at """ + currenttime() + """.</p>

    <img src="deeznuts.png" alt="Fipy 1 temperature" width="320" height="240">
    <p>The temperature reported for Fipy 1 is """ + get_ypointpeak() + """. (Above is where the graph would go)</p>
    <p>The humidity for Fipy 1 is <bold> ( humidity ) </bold>.
    
    <p> (So basically there is supposed to be a for-loop for what is happening above.) </p>
    
    <footer>
    <p>(C) """ + currentyear() + """- Let's! Datacentre Monitoring</p>
    </footer>
    
    </body>
    </html> 
    """
    pdf = pdfkit.from_string(html, False, configuration=config)
    return pdf

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
    graph = plt.savefig('deeznuts.png')
    return graph

def get_slaabove():
    slaint1 = 20
    slaabove = np.array([slaint1,slaint1,slaint1,slaint1,slaint1])
    return slaabove

def get_slabelow():
    slaint2 = 24
    slabelow = np.array([slaint2,slaint2,slaint2,slaint2,slaint2])
    return slabelow

def get_xpoints():
    xpoints = np.array([20.0, 15.0, 10.0, 5.0, 0.0])
    return xpoints

def get_ypoints():
    ypoint1 = round(random.uniform(20.1, 23.9), 1)
    ypoint2 = round(random.uniform(20.1, 23.9), 1)
    ypoint3 = round(random.uniform(20.1, 23.9), 1)
    ypoint4 = round(random.uniform(20.1, 23.9), 1)
    ypoint5 = round(random.uniform(20.1, 23.9), 1)
    ypointarray = np.array([ypoint1, ypoint2, ypoint3, ypoint4, ypoint5])
    return ypointarray

def get_ypointpeak():
    ypointarray = get_ypoints()
    controlvar = 0
    ypointpeak = 0
    for i in ypointarray:
        if ypointpeak <= ypointarray[controlvar]:
            ypointpeak = ypointarray[controlvar]
        controlvar = controlvar + 1
    return str(ypointpeak)


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
    plt.ylim(18, 26);

    graph = get_graphwithbase64()
    return graph

def kininarimasu():
    playsound("app\sound\curious.wav")
