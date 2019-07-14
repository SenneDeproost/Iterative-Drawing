from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
import os
cwd = os.getcwd()


def index(request):
    return render(request, "registration_form.html")