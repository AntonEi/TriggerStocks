from django.shortcuts import render
from django.views import generic, View
from .models import Trigger
from django.db.models import Q

# Create your views here.

class TriggerList(generic.ListView):
    queryset = Trigger.objects.all()
    template_name = "triggerlist/index.html"


class TriggerSearch(View):
    def post(self, request):
        """
        This method is called when a POST request is made to the view
        via the comment form or the meal plan form.
        """
        print(f"Search {request.POST['search']}")
        found_triggers = Trigger.objects.filter(Q(stock_name__istartswith=request.POST['search'])
                                                 | Q(summary__icontains=request.POST['search'])
                                                 | Q(trigger_headline__istartswith=request.POST['search'])
                                                )
        

        return render(
            request,
            "triggerlist/index.html",
            {
                "trigger_list": found_triggers,
            },
        )

    def get(self, request):
        """
        Filters the MealPlanItems table by user and creates a dictionary with
        day and meal plan item as a key, value pair.
        """
        return render(
            request,
            "triggerlist/index.html",
            {
                "trigger_list": Trigger.objects.all(),
            },
        )