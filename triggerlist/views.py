from django.shortcuts import render
from django.views import generic, View
from .models import Trigger
from .forms import CommentForm
from django.contrib import messages

# Create your views here.



def CommentList(request, trigger_id):
    queryset = Trigger.objects.get_all()
    trigger = get_object_or_404(queryset,)  # Change pk=1 to the appropriate condition
    comments = trigger.comments.all().order_by("-created_on")
    comment_count = trigger.comments.count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.trigger = trigger
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()

    return render(
        request,
        "triggerlist/index.html",
        {
            "trigger": trigger,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )

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