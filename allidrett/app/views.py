from django.shortcuts import render, redirect
from django.shortcuts import HttpResponseRedirect
from .forms import RegistrationForm
from .models import Registration
from django.core.mail import send_mail
from django.conf import settings


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
        subject = 'Allidrett Nidelv IL Høst 2020 Registrering'
        message = """
        Takk for at du har meldt barnet ditt %s på allidrett i regi av Nidelv Idrettslag. 
        Dere er påmeldt partiet som går hver %s fra %s til %s. 
         
        Vi gleder oss til å treffe dere.
        """ % (registration.name, registration.party.day, registration.party.start_time, registration.party.end_time)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [registration.email,]
        send_mail( subject, message, email_from, recipient_list )

    return render(request, 'registration_receipt.html', {'registration': registration})
