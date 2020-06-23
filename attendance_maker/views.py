from django.shortcuts import render,redirect
from .models import CLASS_CODE,Students_Record,Teachers_Record,Subject_Information
from anand.settings import MEDIA_ROOT
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
import socket
import geoip2.database
from accounts.models import teachers
from accounts.models import students
#import face_recognition as fr
#import cv2
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

def isPresentInClass(student,prof):
    print(student.latitude,student.longitude)
    if abs(student.latitude-prof.latitude) <= 0.1 and abs(student.longitude-prof.longitude) <= 0.1 :
        return True
    else :
        return False

def verify_TeacherToSubject(ClassCode,TeacherName,SubjectName):
    print("in verify teacher to subject")
    objCode=CLASS_CODE.objects.get(Code=ClassCode)
    teacher=Teachers_Record.objects.get(Code=objCode)
    subinfo=Subject_Information.objects.get(Code=objCode)
    result=False
    print(teacher.A,subinfo.A)
    if(teacher.A==TeacherName and subinfo.A==SubjectName):
        result=True
    if(teacher.B==TeacherName and subinfo.B==SubjectName):
        result=True
    if(teacher.C==TeacherName and subinfo.C==SubjectName):
        result=True
    if(teacher.D==TeacherName and subinfo.D==SubjectName):
        result=True
    if(teacher.E==TeacherName and subinfo.E==SubjectName):
        result=True
    if(teacher.F==TeacherName and subinfo.F==SubjectName):
        result=True
    return result

def IdentifyFace(pathToPicture):
    """
    imgComp=fr.load_image_file(MEDIA_ROOT+'/'+pathToPicture)
    faceDetect=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    cam=cv2.VideoCapture(0)
    #sample_num=0
    image=None
    print('Trying to identify the student')
    while(True):
        ret,image=cam.read()
        #time.sleep(3)
        gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        faces=faceDetect.detectMultiScale(gray,1.3,5)
        flag=False
        for (x,y,w,h) in faces:
            #sample_num=sample_num+1
            #cv2.imwrite('/home/ankit/Pictures/Webcam/face'+str(sample_num)+'.jpg',gray[y:y+h,x:x+w])
            cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.waitKey(250)
            imageEnc=fr.face_encodings(image)
            #print(imageEnc)
            if len(imageEnc)>0:
                print("length of imageEnc",len(imageEnc))
                flag=True
        

        cv2.imshow("Face",image)
        cv2.waitKey(1)
        if flag==True:
            break

    #print(imgComp)
    if image is not None:
        imgCompEnc=fr.face_encodings(imgComp)
        #imageEnc=fr.face_encodings(image)[0]
        #print(imgCompEnc)
        result=fr.compare_faces(imgCompEnc,imageEnc[0])
        print(result)
    cam.release()
    cv2.destroyAllWindows()
    """
    result=True
    return result

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
#and IP.objects.get(address=ip).exist()
#location[0]==stud_location[0] and location[1]==stud_location[1] and
def for_students(request):
    username=""
    subject=""
    print("in for_students")
    if request.user.is_authenticated:
        username = request.user.username
    flag=0   
    """
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
    """
    
    student=Students_Record.objects.get(Student_Name=username)
    
    if student.status==False:
        flag=1
    
    if flag:
        if request.method == 'POST':
            
            #stud_location=locate(request)
            
            #student=record.objects.get(name=username)
            #student2=students.objects.get(name=username)
            ip=visitor_ip_address(request)
            try:
                socket.inet_aton(ip)
                ip_valid=True
            except socket.error:
                ip_valid=False


            #if ip_valid :
                #try:
                    #obj=Students_Record.objects.filter(Code=student.Code,IP=ip)
                    #messages.info(request,"A response has been already recorded from this ip address in this class!")
                    #return redirect('project_index')
                #except Students_Record.DoesNotExist :
                    #pass
               
           
            subject=student.SubjectName
            subInfo=Subject_Information.objects.get(Code=student.Code)

            faceRecognised=IdentifyFace(str(student.Image))
            if faceRecognised == False :
                messages.info('Sorry ,your face did not to match.In case of error try again!')
                return redirect('project_index')
                #student[sub[teacher]]=student[subteacher]]+1
               #for field in student._meta.fields:
                #   if field.name == sub[teacher]:
                #       student.field.name+=1

            present=False
            if subject == subInfo.A:
                prof=teachers.objects.get(name=Teachers_Record.objects.get(Code=student.Code).A)
                if isPresentInClass(student,prof):
                    student.A=student.A+1
                    present=True

            if subject == subInfo.B:
                prof=teachers.objects.get(name=Teachers_Record.objects.get(Code=student.Code).B)
                if isPresentInClass(student,prof):
                    student.B=student.B+1
                    present=True

            if subject == subInfo.C:
                prof=teachers.objects.get(name=Teachers_Record.objects.get(Code=student.Code).C)
                if isPresentInClass(student,prof):
                    student.C=student.C+1
                    present=True

            if subject == subInfo.D:
                prof=teachers.objects.get(name=Teachers_Record.objects.get(Code=student.Code).D)
                if isPresentInClass(student,prof):
                    student.D=student.D+1
                    present=True

            if subject == subInfo.E:
                prof=teachers.objects.get(name=Teachers_Record.objects.get(Code=student.Code).E)
                if isPresentInClass(student,prof):
                    student.E=student.E+1
                    present=True

            if subject == subInfo.F:
                prof=teachers.objects.get(name=Teachers_Record.objects.get(Code=student.Code).F)
                if isPresentInClass(student,prof):
                    student.F=student.F+1
                    present=True

            if present:
                student.status=True
                student.IP=ip
                student.save()
                #addr=IP(address=ip)
                #addr.save()
                messages.info(request,"Your Attendance has been marked.")
                return redirect('project_index')
            else: 
                 messages.info(request,'You are not allowed to mark your Attendance.')
                 return redirect('project_index')
        else:
            return render(request,'students_desk.html',{})
    
    else: 
          return redirect("/")  



def for_teachers(request):
    
    if request.user.is_authenticated:
        username = request.user.username               
        try:
            prof=teachers.objects.get(name=username) 
        except teachers.DoesNotExist :
            messages.info(request,'You are not a teacher according to the database')
            return redirect('project_index')
        
    if request.method == 'POST':
        
        inp=request.POST['control']
        ClassCode=request.POST['Class Code']
        SubjectName=request.POST['Subject Name']
        objCode=CLASS_CODE.objects.get(Code=ClassCode)
        if verify_TeacherToSubject(ClassCode,username,SubjectName)==False:
            #messages.info('You do not teach this subject!')
            print('You do not teach this subject')
            return redirect('teachers_desk')

        if inp.lower() == 'start' :
            #record.objects.all().update(status=False)
            Students_Record.objects.filter(Code=objCode).update(SubjectName=SubjectName,status=False)   
            #location=locate(request)
            """location[0]=
            location[1]=0"""
            #prof=teachers.objects.get(name=username) 
            #prof.latitude=prof_lat
            #prof.longitude=prof_lon
            #prof.save()
            print(prof.latitude,prof.longitude)
            return redirect('teachers_desk')
        elif inp.lower() == 'stop' :
            prof.latitude=-1
            prof.longitude=-1
            prof.save()
            #IP.objects.all().delete()
            Students_Record.objects.filter(Code=objCode).update(SubjectName='#',latitude=-1,longitude=-1,IP='#')
            return redirect('/')
    else:
        
        return render(request,"teachers_desk.html",{}) 

@csrf_exempt   
def send_response(request):
    if request.method=='POST':
        print("in response")
        get_value=dict(request.POST)
        lat=float(get_value['lat'][0])
        lon=float(get_value['lon'][0])
        print(lat,lon)

        #la1=lat
        #lon1=lon
        if request.user.is_authenticated:
            username = request.user.username
            try:
                prof=teachers.objects.get(name=username) 
                prof.latitude=lat
                prof.longitude=lon
                prof.save()

            except teachers.DoesNotExist :
                messages.info(request,'You are not a teacher according to the database')
                auth.logout()
                return redirect('login.html')
        
        
        return redirect("teachers_desk")
    else:
        return render(request,"location.html", {})

@csrf_exempt   
def send_response2(request):
    if request.method=='POST':
        print("in response")
        get_value=dict(request.POST)
        lat=float(get_value['lat'][0])
        lon=float(get_value['lon'][0])
        print(lat,lon)
        if request.user.is_authenticated:
            username=request.user.username
        try:
            student=Students_Record.objects.get(Student_Name=username)
            student.latitude=lat
            student.longitude=lon
            student.save()
        except:
            pass
        return redirect("students_desk")
    else:
        return render(request,"location_stud.html",{})
