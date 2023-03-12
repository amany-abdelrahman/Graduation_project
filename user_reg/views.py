from django.shortcuts import render,redirect,HttpResponse
# from .forms import UserForm
from .models import User
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
# from django.utils.datastructures import MultiValueDict

# Create your views here.

@login_required(login_url='login')
def HomePage(request):
    return render(request,'home.html')


def SignupPage(request):
    if request.method=='POST':
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')


        if password!=re_password:
            return HttpResponse("Your Password and conform password are not same")
        else:
            my_user = User.objects.create_user(username, email, password)
            #my_user= User.objects.create_user(username,email,password)
            my_user.first_name = fname
            my_user.last_name = lname    
        my_user.save()
        return redirect ('login')
    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('your_pass')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('Username or password is incorrect')
    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')



from .api import registeration
from rest_framework.views import APIView
from .models import User
from rest_framework.response import Response

class register(APIView):
    def get(self,request):
        r1=User.objects.all()
        r2=registeration(r1,many=True)
        return Response(r2.data)