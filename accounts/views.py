from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import students,teachers
from attendance_maker.models import CLASS_CODE,Students_Record,Teachers_Record
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        """
        group=request.POST['group']
        classcode=request.POST['Class Code']
        obj=None
        if(group == 'Teacher'):
            try:
                obj=teachers.objects.get(name=username)
            except:
                pass
                #messages.info(request,'You are not a teacher')
                #return redirect('/')
        else:  
            try:
                obj=students.objects.get(name=username)
                print("student exists")
            except:
                pass
                #messages.info(request,'You are not a student')
                #return redirect('/')
        print("username:",username)
        print("password:",password)
        """
        user=auth.authenticate(username=username,password=password)
        auth.login(request,user)
        print("user is",user)

        """
        if user is not None and obj is not None:
            
            auth.login(request,user)
            if group == "Teacher":
                return redirect("send_response")
            else :
                #r=record.objects.get(name=username)
                objCode=CLASS_CODE.objects.get(Code=classcode)
                SR=Students_Record.objects.get(Code=objCode,Student_Name=username)
                if SR.status == False :
                    return redirect("send_response2")
                else : return redirect("project_index")
               
        else:
            messages.info(request,'User Does Not Exist')
            return redirect('/')
        """
        return redirect('/')
    else:
        return render(request,'login.html')   


def register(request):

    if request.method == 'POST':
        
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        subject=request.POST['subject']
        group=request.POST['group']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already present')
                return redirect('register')
            else:
                if(group == 'Teacher'):
                    teacher=teachers(name=username,subject=subject)
                    #prof=Teachers_Record(code=classcode,A=username)
                    teacher.save()
                else :
                    student=students(name=username)
                    student.save()
                    #r=record(name=username)
                    #r.save()
                
                user=User.objects.create_user(username=username,password=password1,email=email)
                user.save()
                return redirect('project_index')
                #messages.info(request,'user created')
        
        else :
            messages.info(request,'password not matching')
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


# Create your views here.

