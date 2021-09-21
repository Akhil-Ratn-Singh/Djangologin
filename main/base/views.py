from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from .models import User

# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("userdetail/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('/')

    else:
        return render(request,'login.html')    

def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        address = request.POST['address']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('/')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('/')
            else:   
                user = User.objects.create_user(username=username, password=password1, email=email, address=address)
                user.save()
                messages.info(request,'User Created')
                return redirect('/')

        else:
            messages.info(request,'password not matching..')    
            return redirect('/')
        return redirect('/')
        
    else:
        return render(request,'register.html')

@login_required
def userdetail(request):
    return render(request, 'userdetail.html')

def logout(request):
    auth.logout(request)
    return redirect('/')



         
