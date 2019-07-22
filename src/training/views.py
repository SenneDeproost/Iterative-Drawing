from django.shortcuts import render
from django.http import JsonResponse

from .TrainingSession import *

# Global variable for the TrainingSession object.
training_ses = None

# When training is loaded, create a new TrainingSession.
def training(request):
    global training_ses
    training_ses = TrainingSession("request.session['timestamp']")
    training_ses.load_cases()
    return render(request, 'training.html')


def get_case(request, index=0):
    cur_case = training_ses.cases[index]
    path = cur_case.path
    return JsonResponse(path, safe=False)
