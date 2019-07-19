from django.shortcuts import render
from django.http import JsonResponse

from .TrainingSession import *

training_ses = TrainingSession("test")
training_ses.load_cases()


# Create your views here.
def training(request):
    return render(request, 'training.html')


def get_case(request, index=0):
    cur_case = training_ses.cases[index]
    cur_case.load_case()
    path = cur_case.path
    return JsonResponse(path, safe=False)
