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

# Global variable fot the TestingSession object.
testing_ses = experiment.testing


# When testing is loaded, create a new TestingSession.
def testing(request):
    global testing_ses
   # testing_ses = TestingSession(str(time.time()))
    # Load all testing cases into the TestingSession class
    # testing_ses.load_cases()
    # Render the page
    return render(request, 'testing.html')


# Call for testing case path in JSON format.
def get_case(request):
    case = testing_ses.get_case()
    return JsonResponse(case, safe=False)


@csrf_exempt
# To do when the user submits input: extract, verify and judge the data.
def post_case(request):
    if request.method == 'POST':
        user_input = json.loads(request.body)
        case = testing_ses.current_case()
        res = case.try_trial(user_input)
        return HttpResponse(res, content_type="text/plain")
