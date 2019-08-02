import os
import sys

from django.shortcuts import render

# Prevent error for relative import
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
# This should be included: from Experiment import experiment
from Experiment import experiment


# Render home page
def home(request):
    return render(request, "home.html")

# Render thank you page
def thanks(request):
    # experiment variable is globally defined in the Experiments.py class.
    global experiment
    # When the thank you page is loaded, the experiment is saved and reset for a next session.
    experiment.save(request.session)
    experiment.reset()
    return render(request, "thanks.html")
