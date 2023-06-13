from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User
from .forms import UserForm
from django import forms

@login_required
def edit_profile(request):
    if request.method == "POST":
        form = UserForm(data=request.POST , instance=request.user)
        if form.is_valid():
            user = form.save(request.user)
            user.save()
            return redirect('profile')
    else:
        form = UserForm(instance=request.user)
        return render(request, 'edit_profile.html' , {'form' : form})
    return render(request, 'edit_profile.html')

# @login_required(login_url="/accounts/login")
def register(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        mob_no = request.POST.get('mob_no')
        username = mob_no
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request,'Email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username ,first_name=first_name, password=password1, email=email, last_name=last_name , mob_no=mob_no )
                user.save()
                return redirect('login')
        else:
            messages.error(request,'Password not matching')
            return redirect('register')
    else:
        return render(request, 'register.html')
    

def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request,'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


@login_required(login_url="/accounts/login")
def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required(login_url="/accounts/login")
def profile(request):
    user =  request.user
    if user.is_authenticated:
        # data = UserProfile.objects.get(user)
        # print(user)
        data = User.objects.get(id = user.id)
        # print(data.first_name)
        return render(request, 'profile_info.html',{'data' :data})    
    else:
        return redirect('/')



@login_required(login_url="/accounts/login")
def change_password(request):
    user = request.user
    # if user.is_authenticated:
    if 1:
        if request.method =='POST':
        # if 1:
            oldpass = request.POST.get('oldpass')
            # pass2 = request.POST.get('pass2')
            newpass1 = request.POST.get('newpass1')        
            newpass2 = request.POST.get('newpass2')        

            if newpass1 == newpass2 :
                usr = User.objects.get(id = user.id)
                if usr.check_password(oldpass):
                    usr.set_password(newpass1)
                    usr.save()
                    messages.error(request,'Sucess')
                    return render(request, 'login.html')
                else:
                    messages.error(request,'Old password is Wrong')
                    return render(request, 'change_pass.html')

            else:
                messages.error(request,'New passwords are not matching')
                return render(request, 'change_pass.html')
        else:
            return render(request, 'change_pass.html')
        
        return render(request, 'change_pass.html')

    # else:
        # return redirect('/')




