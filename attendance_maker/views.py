from django.shortcuts import render,redirect
from .models import record

from django.contrib import messages
# Create your views here.
import socket
import geoip2.database
from accounts.models import teachers
# Create your views here.

#sub={'SKS':'subject1','AC':'subject2','PC':'subject3','RS Verma':'subject4'}
#loc={'SKS':[-1,-1],'AC':[-1,-1],'PC':[-1,-1],'RS Verma':[-1,-1]}

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


def for_students(request):
    username=""
    sub=""
    print("in for_students")
    if request.user.is_authenticated:
        username = request.user.username
    flag=0   
    teacher=""
    location=[-1,-1] 
    profs=teachers.objects.all()
    for prof in profs:
        if prof.latitude != -1 and prof.longitude != -1 :
            location=[prof.latitude,prof.longitude]
            teacher=prof.name
            sub=prof.subject
            flag=1
            break

    
    
    if flag:
        if request.method == 'POST':
            stud_location=locate(request)
            if(location[0]==stud_location[0] and location[1]==stud_location[1]):
                student=record.objects.get(name=username)
                #student[sub[teacher]]=student[sub[teacher]]+1
                #for field in student._meta.fields:
                #   if field.name == sub[teacher]:
                #       student.field.name+=1
                if sub == 'subject1':
                    student.subject1=student.subject1+1
                elif sub == 'subject2':
                    student.subject2=student.subject2+1
                elif sub == 'subject3':
                    student.subject3=student.subject3+1
                elif sub == 'subject4':
                    student.subject4=student.subject4+1
                elif sub == 'subject5':
                    student.subject5=student.subject5+1
                elif sub == 'subject6':
                    student.subject6=student.subject6+1
                elif sub == 'subject7':
                    student.subject7=student.subject7+1
                elif sub == 'subject8':
                    student.subject8=student.subject8+1
                elif sub == 'subject9':
                    student.subject9=student.subject9+1
                elif sub == 'subject10':
                    student.subject10=student.subject10+1
                elif sub == 'subject11':
                    student.subject11=student.subject11+1
                elif sub == 'subject12':
                    student.subject12=student.subject12+1

                student.status=True
                student.save()
                
                return redirect('/')
            else: 
                 messages.info(request,'User Does Not Exist')
                 return redirect('students_desk')
        else:
            return render(request,'students_desk.html',{})
    
    else: 
          return redirect("/")  



def for_teachers(request):
    username=""
    if request.user.is_authenticated:
        username = request.user.username
        prof=teachers.objects.get(name=username) 
    if request.method == 'POST':
        inp=request.POST['control']
        if inp == 'start' or inp=='Start':
            record.objects.all().update(status=False)
            location=locate(request)
            #prof=teachers.objects.get(name=username) 
            prof.latitude=location[0]
            prof.longitude=location[1]
            prof.save()
            print(prof.latitude,prof.longitude)
            return redirect('/')
        elif inp == 'stop' or inp=='Stop':
            prof.latitude=-1
            prof.longitude=-1
            prof.save()
            return redirect('/')
    else:
        return render(request,"teachers_desk.html",{})   
