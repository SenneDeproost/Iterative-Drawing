import time

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import sys
import os
import json

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from Experiment import experiment

# Global variable for the TrainingSession object.
training_ses = experiment.training


# When training is loaded, create a new TrainingSession.
def training(request):
    global training_ses
   # training_ses = TrainingSession(str(time.time()))
    # Load all training cases into the TrainingSession class
    training_ses.load_cases()
    # Render the page
    return render(request, 'training.html')


# Call for training case path in JSON format.
def get_case(request):
    case = training_ses.get_case()
    return JsonResponse(case, safe=False)


@csrf_exempt
# To do when the user submits input: extract, verify and judge the data.
def post_case(request):
    if request.method == 'POST':
        user_input = json.loads(request.body)
        case = training_ses.current_case()
        res = case.try_trial(user_input)
        return HttpResponse(res, content_type="text/plain")
