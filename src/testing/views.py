import time

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .TestingSession import *

# Global variable fot the TestingSession object.
testing_ses = None


# When testing is loaded, create a new TestingSession.
def testing(request):
    global testing_ses
    testing_ses = TestingSession(str(time.time()))
    # Load all testing cases into the TestingSession class
    testing_ses.load_cases()
    print("-TESTING--------------------------------------------")
    print(testing_ses.cases)
    print("----------------------------------------------------")
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
