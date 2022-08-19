# from django.shortcuts import render, redirect


# def login(request):
#     return render(request, 'login.html')

# def signup(request):
#     return render(request, 'signup.html')


from types import MethodType
from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
# from accounts.forms import UserForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method =='POST':
        userid=request.POST['username']
        pwd=request.POST['password']
        user=auth.authenticate(request,username=userid,password=pwd)
        if user is not None:
            auth.login(request,user)
            return redirect('login')
        else:
            return render(request,'home')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

# def signup(request):
#     if request.method == "POST":
#       form = UserForm(request.POST)
#       if form.is_valid():
#           form.save()
#           username = form.cleaned_data.get('username')
#           raw_password = form.cleaned_data.get('password1')
#           user = auth.authenticate(username=username, password=raw_password)  # 사용자 인증
#           login(request, user)  # 로그인
#           return redirect('index.html')
#     else:
#         form = UserForm()
#     return render(request, 'common/signup.html', {'form': form})