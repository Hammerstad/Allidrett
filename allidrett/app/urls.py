from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_registration_form, name='registrationform'),
]
