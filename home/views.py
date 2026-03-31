from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'home.html')

def qoutes(request):
    
    qoutes = [
        
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful. - Albert Schweitzer",
        "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
        "The best way to predict the future is to create it. - Peter Drucker",
        
    ]
    qoute = random.choice(qoutes)
    
    data ={}
    data['qoute'] = qoute
    
    return render(request, 'qoutes.html',data)