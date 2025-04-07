from django.shortcuts import render
def index(request):
    return render(request, 'main/index.html')
def pendulum(request):
    return render(request, 'main/about.html')
def pespring(request):
    return render(request, 'main/pespring.html')
def trenie(request):
    return render(request, 'main/Trenie.html')
def brosok(request):
    return render(request, 'main/Brosok.html')
def kolibel(request):
    return render(request, 'main/kolibel.html')
def error(request):
    return render(request, 'main/error.html')
