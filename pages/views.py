from django.shortcuts import render

def home(request):
    return render(request, 'pages/index.html', {'title': 'Главная'})

def about(request):
    return render(request, 'pages/about.html', {'title': 'О проекте'})

def map(request):
    return render(request, 'pages/map.html', {'title': 'Карта боксов'})

def view(request):
    return render(request, 'pages/view.html', {'title': 'Камеры'})

def card(request):
    return render(request, 'pages/card.html', {'title': 'Питомцы'})

def pay(request):
    return render(request, 'pages/pay.html', {'title': 'Поддержать'})

def profile(request):
    return render(request, 'pages/profile.html', {'title': 'Кабинет'})

def registration(request):
    return render(request, 'pages/registration.html', {'title': 'Вход'})