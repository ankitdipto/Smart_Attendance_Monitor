from django.shortcuts import render
from django.contrib.auth.models import auth,User
from django.shortcuts import render
#from attendance_maker.models import record
from accounts.models import teachers,students
from attendance_maker.models import CLASS_CODE,Students_Record,Subject_Information
#from projects.models import project
import socket
import geoip2.database
from django.views.decorators.csrf import csrf_exempt
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
     #queryset=record.objects.all()
     
    """
     if request.user.is_authenticated:
        username = request.user.username
        try:
            obj=students.objects.get(name=username)
            val='s'
        except students.DoesNotExist: 
            pass

        try:
            obj=teachers.objects.get(name=username)
            val='t'
        except teachers.DoesNotExist:    
            pass
    """

    group=None
    if request.user.is_authenticated:
        name=request.user.username
        try:
            obj=teachers.objects.get(name=name)
            group='Teacher'
        except:
            pass

        try:
            obj=students.objects.get(name=name)
            group='Student'
        except:
            pass
    print('group is',group)
    return render(request,"project_index.html", {'group':group})
    


def contact(request):
     return render(request,"contact.html",{})

def aboutus(request):
    return render(request,"aboutus.html",{})
def record(request):
    
    if request.method == 'POST' :
        code=request.POST['Class Code']
        #objCode=CLASS_CODE.objects.get(Code=code)
        #student=Students_Record.objects.get(Student_Name=name)
        objCode=code
        StudentsRecord=Students_Record.objects.filter(Code=objCode)
        SubjectInformation=Subject_Information.objects.filter(Code=objCode)
        return render(request,"record.html", {'StudentsRecord': StudentsRecord,'SubjectInformation':SubjectInformation})
    else :
        return render(request,"ViewClassRecord.html",{})