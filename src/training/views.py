from django.shortcuts import render
from django.http import JsonResponse

from .TrainingSession import *

import time

# Global variable for the TrainingSession object.
training_ses = None


# When training is loaded, create a new TrainingSession.
def training(request):
    global training_ses
    training_ses = TrainingSession(str(time.time()))
    # Load all training cases into the TrainingSession class
    training_ses.load_cases()
    # Render the page
    return render(request, 'training.html')


# Call for training case path in JSON format.
def get_case(request, index=0):
    cur_case = training_ses.cases[index]
    path = cur_case.path
    return JsonResponse(path, safe=False)


# To do when the user submits input: extract, verify and judge the data.
def post_case(request):
    if request.method == 'POST':
        print("Ontvangen die handel!")
