from django.shortcuts import render, redirect
from django.shortcuts import HttpResponseRedirect
from .forms import RegistrationForm
from .models import Registration
from django.conf import settings
from django.core.mail import EmailMessage


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

    if settings.DEBUG:
        email = EmailMessage(
            'Allidrett Nidelv IL Høst 2020 Registrering',
            """Takk for at du har meldt barnet ditt %s på allidrett i regi av Nidelv Idrettslag. 
            Dere er påmeldt partiet som går hver %s fra %s til %s. 
            
            Vi gleder oss til å treffe dere.
            """ % (registration.name, registration.party.day, registration.party.start_time, registration.party.end_time),
            settings.EMAIL_HOST_USER,
            [registration.email, ],
            cc=['allidrett@nidelv-il.no', ],
        )
        email.send()

    return render(request, 'registration_receipt.html', {'registration': registration})
