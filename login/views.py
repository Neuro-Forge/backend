from django.shortcuts import render
from register.models import register
import home
from django.contrib.auth.models import User, auth

# Create your views here.
def login(request):
    if request.method == 'POST':
    
        username = request.POST.get('username')
        password = request.POST.get('password')
        if register.objects.filter(username = username, password = password):
            print("login successful")
            return render(request, home.templates + 'home.html')
        
    return render(request, 'login/login.html')