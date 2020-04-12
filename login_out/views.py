from django.shortcuts import render
from login_out.forms import User_Form , User_Profile_Form , login_form

#LOGIN AND LOGOUT
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request , 'login_out/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = User_Form(request.POST)
        profile_form = User_Profile_Form(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit = False)
            profile.user = user

            profile.save()

            registered = True
            print("REGISTRATION SUCCESSFULL!!")
            print("USERNAME : " + user.username)
            print('PASSWORD(HASHED) : ' + user.password)
            print('NAME : ' + profile.name)
        else:
            print("FORM INVALID")
            print(user_form.errors , profile_form.errors)

        username = user_form.cleaned_data['username']
        password = user_form.cleaned_data['password']

        user1 = authenticate(username=username , password=password)

        login(request , user)
        return HttpResponseRedirect(reverse('index'))


    else:
        user_form = User_Form()
        profile_form = User_Profile_Form()

    return render(request , 'login_out/register.html' , {'user_form' : user_form,
                                                        'profile_form' : profile_form,
                                                        'registered' : registered})

def user_login(request):
    form = login_form()

    if request.method == 'POST':
        form = login_form(request.POST)

        if form.is_valid():
            username = form.cleaned_data['USERNAME']
            password = form.cleaned_data['PASSWORD']

            user = authenticate(username=username , password=password)

            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse('USER IS INACTIVE')

        else:
            print('SOMEONE TREID TO LOGIN : ')
            print('USERNAME : {}       PASSWORD : {}'.format(username,password))
            return HttpResponse('INVALID LOGIN CREDENTIALS!!')

    else:
        return render(request , 'login_out/login.html' , {'form' : form})
