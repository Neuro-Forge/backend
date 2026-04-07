from django.shortcuts import render
import random
from .models import Quote
# Create your views here.

def home(request):
    if request.method == 'POST':
        submitted_text = request.POST.get('qoute')
        if submitted_text:
            Quote.objects.create(quote=submitted_text)

    quote_list = Quote.objects.all()
    selected_quote = random.choice(quote_list) if quote_list else None
    selected_quote_text = selected_quote.quote if selected_quote else None

    request.session['quote'] = selected_quote_text
    
    
    defult_quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Success is not the key to happiness. Happiness is the key to success. - Albert Schweitzer",
        "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "Believe you can and you're halfway there. - Theodore Roosevelt",  
        "The only way to do great work is to love what you do. - Steve Jobs",
        "do not let the fear of losing be greater than the excitement of winning. - Robert Kiyosaki",
    ]
    
    random_quote = random.choice(defult_quotes)
    data ={
        "random_quote": random_quote,
    }
    
    return render(request, 'home.html', data)

def qoutes(request):
    pass
