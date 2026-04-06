from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import registerFrom 
from .models import register
from django.contrib.auth.models import User, auth
# Create your views here.
def signup(request):
    
    form =registerFrom()
    if request.method == 'POST':
        username = request.POST['username']
        email  =request.POST['email']
        password = request.POST['password']
        
        if User.objects.filter(username=username).exists():
           return HttpResponse('username already exist')
           
        else:
            user = User.objects.create_user(username=username,email=email,password=password)
            user.save()
            return render(request, 'login.html')
          
    
        
        
    else:
        return render(request, 'register/register.html', )
    
    