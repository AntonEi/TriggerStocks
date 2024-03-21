from django.shortcuts import render, redirect
from .models import sharetrigger
from .forms import SharetriggerForm


def share_trigger(request):
    if request.method == 'POST':
        form = SharetriggerForm(request.POST)
        if form.is_valid():
            sharetrigger_instance = form.save(commit=False)
            sharetrigger_instance.author = request.user
            sharetrigger_instance.save()

            return redirect('home')
        else:
            print('form invalid')
    else:
        form = SharetriggerForm()

    return render(
        request,
        "sharetrigger/sharetrigger.html",
        {"form": form},
    )
