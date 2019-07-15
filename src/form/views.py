from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import RegistrationForm
import time

def form(request):
    # Get data out form when POST method is used
    if request.method == 'POST':
        # Get the form from the POST request
        form = RegistrationForm(request.POST)
        # If the from is valid, extract the data from the form into a Session
        if form.is_valid():
            # Add user details to the current session
            request.session['first_name'] = form.cleaned_data.get('first_name')
            request.session['last_name'] = form.cleaned_data.get('last_name')
            request.session['age'] = form.cleaned_data.get('age')
            request.session['email'] = form.cleaned_data.get('email')
            request.session['timestamp'] = time.time()

            # Redirect to the next page after registration
            return HttpResponseRedirect('/training')
    else:
        # Return empty form for a not POST request
        form = RegistrationForm()

    # Render the registration form from template
    return render(request, 'registration_form.html', {'form': form})
