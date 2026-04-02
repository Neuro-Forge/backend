from django.shortcuts import render
import random
from .models import Quote
# Create your views here.

def home(request):
    return render(request, 'home.html')

def qoutes(request):
    
    quote_options = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful. - Albert Schweitzer",
        "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
        "The best way to predict the future is to create it. - Peter Drucker",
    ]
    selected_quote = random.choice(quote_options)
    submitted_qoute = None
    if request.method == 'POST':
        submitted_qoute = request.POST.get('qoute')
        if submitted_qoute:
            quote_options.append(submitted_qoute)
            Quote.objects.create(quote=submitted_qoute)
    
    qoutes_list = Quote.objects.all()
    data = {
        'qoute': selected_quote,
        'all_qoutes': quote_options,
        'submitted_qoute': submitted_qoute,
        'qoutes_list': qoutes_list,
    }
    
    return render(request, 'qoutes.html',data)