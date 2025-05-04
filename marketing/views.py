from django.shortcuts import render
from .forms import WaitlistSignupForm

def index(request):
    submitted = False
    if request.method == 'POST':
        form = WaitlistSignupForm(request.POST)
        if form.is_valid():
            form.save()
            submitted = True
    else:
        form = WaitlistSignupForm()
    return render(request, 'marketing/index.html', {'form': form, 'submitted': submitted})