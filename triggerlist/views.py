from django.shortcuts import render, get_object_or_404, reverse, redirect, HttpResponseRedirect
from django.views import generic, View
from .models import Trigger, Comment
from .forms import CommentForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def favourite_list(request):
    new = Trigger.objects.filter(favourites=request.user)
    return render(
        request,
        "triggerlist/favourites.html",
        {"new": new},
    )


@login_required 
def favourite_add(request, trigger_id):
    trigger = get_object_or_404(Trigger, pk=trigger_id)
    if trigger.favourites.filter(id=request.user.pk).exists():
        trigger.favourites.remove(request.user)
        messages.add_message(request, messages.SUCCESS, 'Favourite removed!')
    else:
        trigger.favourites.add(request.user)
        messages.add_message(request, messages.SUCCESS, 'Favourite Added!')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


class TriggerList(generic.ListView):
    queryset = Trigger.objects.all()
    template_name = "triggerlist/index.html"



def trigger_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """
    queryset = Trigger.objects.all()
    trigger = get_object_or_404(queryset, slug=slug)
    comments = trigger.comments.all().order_by("-created_on")
    comment_count = trigger.comments.count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.trigger = trigger
            comment.save()

    comment_form = CommentForm()

    return render(
        request,
        "triggerlist/trigger_detail.html",
        {
            "trigger": trigger,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )

    return render(
        request,
        "triggerlist/trigger_detail.html",
        {"trigger": trigger},
    )


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Trigger.objects.all()
        trigger = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.trigger = trigger
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('trigger_detail', args=[slug]))

def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Trigger.objects.all()
    trigger = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return redirect ('trigger_detail', slug=trigger.slug)




    
# class TriggerSearch(View):
#    def post(self, request):
#        """
#        This method is called when a POST request is made to the view
#        via the comment form or the meal plan form.
#        """
#        print(f"Search {request.POST['search']}")
#        found_triggers = Trigger.objects.filter(Q(stock_name__istartswith=request.POST['search'])
#                                                 | Q(summary__icontains=request.POST['search'])
#                                                 | Q(trigger_headline__istartswith=request.POST['search'])
#                                                )
#        
#
#       return render(
#            request,
#           "triggerlist/index.html",
#            {
#                "trigger_list": found_triggers,
#            },
#        )
#
#    def get(self, request):
#        """
#        Filters the MealPlanItems table by user and creates a dictionary with
#        day and meal plan item as a key, value pair.
#        """
#        return render(
#            request,
#            "triggerlist/index.html",
#            {
#                "trigger_list": Trigger.objects.all(),
#            },
#        )