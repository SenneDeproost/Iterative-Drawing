from django.shortcuts import render

# Create your views here.
def training(request):
    return render(request, 'training.html')