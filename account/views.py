from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from .forms import LoginForm
from django.contrib.auth.models import User
from django.http import HttpResponse


from django.contrib.auth.decorators import login_required
@login_required
def dashboard(request):
    return render(request,'dashboard.html',{'section': 'dashboard'})


# Create your views here.
def user_login(request):
    return HttpResponse("home")
    if request.method=='POST':
        form = LoginForm(request.POST)


        if form.is_valid():
            cd =form.cleaned_data
            user=authenticate(request,username=cd['username'],password=cd['password'])

            if user is not None:
                # user= User.objects.get(username=cd['username'],password=cd['password'])
                
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated ''successfully')
                else:
                    return HttpResponse("user desabled")
            else:
                return HttpResponse("invalid id password")
    else:
        form=LoginForm()

    return render(request,'account/login.html',{'form':form})


