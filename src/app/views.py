import os
import sys

from django.shortcuts import render

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from Experiment import experiment


def home(request):
    return render(request, "home.html")


def thanks(request):
    global experiment
    experiment.save(request.session)
    experiment.reset()
    return render(request, "thanks.html")
