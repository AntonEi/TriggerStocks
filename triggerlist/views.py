from django.shortcuts import render
from django.views import generic
from .models import Trigger

# Create your views here.

class TriggerList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "trigger_list.html"