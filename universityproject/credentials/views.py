from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")
    return render(request,"new.html")

def register(request):
    if request.method == 'POST':
        username=request.POST['Username']
        password=request.POST['Password']
        password1=request.POST['password1']
        if password1== password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exist")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save();
                return redirect('login')

        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')
    return  render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
def new(request):
    return render(request,"new.html")
def submit(request):
    return render(request,"submit.html")