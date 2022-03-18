
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login,logout
from django.core.paginator import Paginator

from imagesharing import settings
from .models import Image

# Create your views here.
    
def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        if username.isalpha() == False:
            messages.error(request, "Enter only alphabets and numbers")
            return render(request, 'signup.html')
        else:
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            email = request.POST.get('email')
            pass1 = request.POST.get('pass1')
            pass2 = request.POST.get('pass2')
            if ((pass1 == pass2) and (' ' in pass1 == False)):
                myuser = User.objects.create_user(username=username,first_name=fname,last_name=lname,email=email,password=pass1)
                myuser.save()
                messages.success(request,"Your account has been successfully created")
                return redirect('signin')
            else:
                messages.error(request, "change password and no space allowed")
                return render(request, 'signup.html')

    return render(request, 'signup.html')


def signin(request):
    print("In signin method")
    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')

        user = authenticate(username= username,password=pass1)
        if user is not None:
            login(request,user)
            fname = user.first_name
            print("After authentication success")
            return redirect('home')
            

        else:
            messages.error(request, "bad credentials")
            return redirect('home')

    return render(request,'signin.html')

def signout(request):
    logout(request)
    messages.success(request,"logged out successfully")
    return redirect('home')

def home(request):
    if request.method == "POST":
        new_image = Image()
        new_image.file = request.FILES.get('img')
        new_image.description=request.POST['caption']
        if not new_image.description:
            new_image.description = ''
        new_image.user=request.user
        new_image.save()
        return redirect('home')
   
    else:
        web_post = Image.objects.all()
        for posts in web_post:
            org_file= posts.file
            posts.file= "../media/"+str(org_file)
        return render(request,'home.html',{'web_post':web_post})

def addfile(request):
    if request.method == "POST":
        new_image = Image()
        new_image.file = request.FILES.get('img')
        new_image.description=request.get['caption']
        new_image.user=request.user
        new_image.save()
        return render(request,'home.html',{'new_image':new_image})
        

        


        
        

    



    

    