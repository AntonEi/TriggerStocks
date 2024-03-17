from django.shortcuts import render, get_object_or_404
from .models import sharetrigger  # Change the import to match the model name

def share_trigger(request):
    """
    Renders the Sharetrigger page
    """
    sharetrigger_instance = sharetrigger.objects.all().order_by('-created_on').first()

    return render(
        request,
        "sharetrigger/sharetrigger.html",
        {"sharetrigger_instance": sharetrigger_instance},  # Update variable name here
    )


from django.shortcuts import render, redirect
from .models import sharetrigger
from .forms import SharetriggerForm

def share_trigger(request):
    """
    Renders the Sharetrigger page
    """
    if request.method == 'POST':
        form = SharetriggerForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or home page
            return redirect('home')  # Replace 'home' with the name of your home page URL
    else:
        form = SharetriggerForm()
    
    return render(
        request,
        "sharetrigger/sharetrigger.html",
        {"form": form},
    )

# Create your views here.
