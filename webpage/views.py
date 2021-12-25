from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request,'webpage/index.html')


def account(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'The Email ALready Exists')
                return redirect('account')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Exist')
                return redirect('account')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('index')
        else:
            messages.info(request, 'password not the same')
            return redirect('account')

    return render(request,'webpage/account.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request,'incorrect username or password')
            return redirect('login')
    return render(request,'webpage/login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')



