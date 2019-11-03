from django.shortcuts import render,redirect
from .models import record
from django.contrib import messages
# Create your views here.
import socket
import geoip2.database
# Create your views here.

sub={'SKS':'subject1','AC':'subject2','SD':'subject3'}
loc={'SKS':[-1,-1],'AC':[-1,-1],'SD':[-1,-1]}

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
        reader=geoip2.database.Reader('attendance_maker/GeoLite2-City_20191029/GeoLite2-City.mmdb')
        print(ip)
        try:
            response=reader.city(ip)
            latitude=float(response.location.latitude)
            longitude=float(response.location.longitude)
        except :
            print("error occured")
    return [latitude,longitude]


def for_students(request,username):
    flag=0   
    teacher=""
    location=[-1,-1] 
    for key,value in loc.items():
        
        if value[0]!=-1 and value[1]!=-1:
            teacher=key
            location=value
            flag=1
            break
    
    if flag:
        if request.method == 'POST':
            stud_location=locate(request)
            if(location[0]==stud_location[0] and location[1]==stud_location[1]):
                student=record.objects.get(name=username)
                student[sub[teacher]]=student[sub[teacher]]+1
                student.save()
                return redirect('/')
            else: 
                 messages.info(request,'User Does Not Exist')
                 return redirect('students_desk')
        else:
            return render(request,'students_desk',{})
    
    else: 
          return redirect("/")  



def for_teachers(request,username):
    if request.method == 'POST':
        inp=request.POST['control']
        if inp == 'start':
            location=locate(request) 
            loc[username]=location
            return redirect('/')
        elif inp == 'stop':
            loc[username]=[-1,-1]
    else:
        return render(request,"teachers_desk",{})   
