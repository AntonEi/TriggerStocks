from django.shortcuts import render, redirect
from .models import sharetrigger
from .forms import SharetriggerForm

def share_trigger(request):
    if request.method == 'POST':
        form = SharetriggerForm(request.POST)
        if form.is_valid():
            sharetrigger_instance = form.save(commit=False)
            sharetrigger_instance.author = request.user  # Set the author to the current user
            sharetrigger_instance.save()
            # Redirect to a success page or home page
            return redirect('home')  # Replace 'home' with the name of your home page URL
        else:
            print('form invalid')
    else:
        form = SharetriggerForm()
    
    return render(
        request,
        "sharetrigger/sharetrigger.html",
        {"form": form},
    )