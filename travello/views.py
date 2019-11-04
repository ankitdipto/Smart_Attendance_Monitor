from django.shortcuts import render

from django.shortcuts import render
#from projects.models import project
import socket
import geoip2.database
# Create your views here.

def visitor_ip_address(request):
    x_forwarded_for=request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip=x_forwarded_for.split(',')[0]
        print("for",x_forwarded_for)
    else:
        ip=request.META.get('REMOTE_ADDR')
        print("remote",ip)
    return ip


def locate(request):
    
    ip=visitor_ip_address(request)
    print(ip)
    latitude=0
    longitude=0
    try:
        socket.inet_aton(ip)
        ip_valid=True
    except socket.error:
        ip_valid=False

    if ip_valid:
        reader=geoip2.database.Reader('travello/GeoLite2-City_20191029/GeoLite2-City.mmdb')
        print(ip)
        try:
            response=reader.city(ip)
            latitude=float(response.location.latitude)
            longitude=float(response.location.longitude)

        except :
            print("error occured")
            

    return {'latitude':latitude,'longitude':longitude}
# Create your views here.
def index(request):
    
     #ob=locate(request)
     #dest1=Destination()
     #dest1.name='Mumbai'
     #dest1.desc='The city that never sleep'
     #dest1.price=700
     return render(request,"project_index.html", {})

