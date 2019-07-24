from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def thanks(request):
    return render(request, "thanks.html")
