from django.shortcuts import render, redirect
from django.shortcuts import HttpResponseRedirect
from .forms import RegistrationForm
from .models import Registration


def index(request):
    return render(request, 'registration.html')


def get_registration_form(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_registration = form.save()
            # TODO: handle raised errors on save, see forms.py
            return redirect('registrationreceipt', registration_id=new_registration.id)

    else:
        form = RegistrationForm()

    return render(request, 'registration.html', {'form': form})


def on_success(request, registration_id):
    registration = Registration.objects.get(id=registration_id)
    return render(request, 'registration_receipt.html', {'registration': registration})
