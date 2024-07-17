from django.shortcuts import render
from django.http import HttpResponse

from .models import *

from .forms import MessageForm


def index(request):
    
    return HttpResponse("Reached here!")




