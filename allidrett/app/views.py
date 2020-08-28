from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from .forms import RegistrationForm


def index(request):
    return render(request, 'registration.html')


def get_registration_form(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Process the form here...
            return HttpResponseRedirect('/registered/')

    else:
        form = RegistrationForm()

    return render(request, 'registration.html', {'form': form})
