from django.shortcuts import render
from django.views import generic
from .models import Trigger

# Create your views here.

class TriggerList(generic.ListView):
    queryset = Trigger.objects.all()
    template_name = "triggerlist/index.html"