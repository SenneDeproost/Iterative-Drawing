from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from .models import RegistrationForm
import time

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
#from app.models import Session


def form(request):
    # Get data out form when POST method is used
    if request.method == 'POST':
        # Get the form from the POST request
        form = RegistrationForm(request.POST)
        # If the from is valid, extract the data from the form into a Session
        if form.is_valid():
            # Add user details to the current session
            request.session['first_name'] = form.first_name
            request.session['last_name'] = form.last_name
            request.session['age'] = form.age
            request.session['email'] = form.email
            request.session['timestamp'] = time.time()

            # Redirect to the next page after registration
            return HttpResponseRedirect('/training')
    else:
        form = RegistrationForm()

    return render(request, 'registration_form.html', {'form': form})
