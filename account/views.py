from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from .forms import LoginForm,UserRegistrationForm,UserEditForm, ProfileEditForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Profile
from django.contrib import messages


from django.contrib.auth.decorators import login_required
@login_required
def dashboard(request):
    messages.error(request, messages.INFO,'Something went wrong')
    return render(request,'dashboard.html',{'section': 'dashboard'})

import time
# Create your views here.
def user_login(request):
    return HttpResponse("home")
    if request.method=='POST':
        form = LoginForm(request.POST)


        if form.is_valid():
            cd =form.cleaned_data
            user=authenticate(request,username=cd['username'],password=cd['password'])
            print("bhuban")
            if user is not None: 
                print("bhuban1")               
                if user.is_active:
                    print("bhuban2")
                    
                    print("Printed immediately.")
                    time.sleep(2.4)
                    print("Printed after 2.4 seconds.")
                    login(request, user)
                    
                    return HttpResponse('Authenticated ''successfully')
                else:
                    return HttpResponse("user desabled")
            else:
                return HttpResponse("invalid id password")
    else:
        form=LoginForm()

    return render(request,'account/login.html',{'form':form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileEditForm(request.POST,request.FILES)
        print(profile_form)
        if (user_form.is_valid() and profile_form.is_valid()):
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            Profile.objects.create(user=new_user,date_of_birth=profile_form.cleaned_data['date_of_birth'],photos=profile_form.cleaned_data['photos'])
            return render(request,'account/register_done.html',{'new_user': new_user})
    
    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileEditForm()
    return render(request,'account/register.html',{'user_form': user_form,'profile_form': profile_form})



@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,data=request.POST,files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect("dashboard")
        else:
            messages.error(request, 'Error updating your profile')

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,'account/edit.html',{'user_form': user_form,'profile_form': profile_form})