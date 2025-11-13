from django.shortcuts import render ,redirect
from django.http import HttpRequest





def home_view(request: HttpRequest):
    return render(request, 'main/index.html')

def state_view(request: HttpRequest):
    return render(request, 'main/state1.html')

def statee_view(request: HttpRequest):
    return render(request, 'main/state2.html')

def unite_view(request: HttpRequest):
    return render(request, 'main/unite.html')

def kings_view(request: HttpRequest):
    return render(request, 'main/kings.html')

def history_view(request: HttpRequest):
    return render(request, 'main/history.html')

def museums_view(request: HttpRequest):
    return render(request, 'main/museums.html')

def education_view(request: HttpRequest):
    return render(request, 'main/education.html')

def book_visit(request):
    return render(request, 'main/book_visit.html')

def login_view(request):
    return render(request, "main/login.html")

def toggle_theme(request: HttpRequest):
    current_theme = request.COOKIES.get('theme', 'light')
    new_theme = 'dark' if current_theme == 'light' else 'light'

    response = redirect(request.META.get('HTTP_REFERER', '/'))
    response.set_cookie('theme', new_theme, max_age=60*60*24*365)
    return response





