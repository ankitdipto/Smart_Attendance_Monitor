from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import students,teachers
# Create your views here.

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        group=request.post['group']
        if(group == 'teacher'):
            obj=teachers.get.objects(name=username)
        else:  obj=students.get.objects(name=username)
        user=auth.authenticate(username=username,password=password)

        if user is not None and obj is not None:
            
            auth.login(request,user)
            if group == "teacher":
                return redirect("teacher_control",username)
            else :return redirect("student_control",username)
        else:
            messages.info(request,'User Does Not Exist')
            return redirect('login')
    else:
        return render(request,'login.html')   

def register(request):

    if request.method == 'POST':
        
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already present')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email)
                user.save()
                return redirect('login')
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
