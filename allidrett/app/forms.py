from django import forms
from django.core.exceptions import ValidationError
from django.db.models import Count
from . import models


class BirthYearSelect(forms.Select):
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex, attrs)
        if value:
            option['attrs']['birthyear'] = value.instance.year
        return option


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = models.Registration
        fields = ['year_of_birth', 'email', 'party', 'name']
        widgets = {'year_of_birth': BirthYearSelect, }

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['party'].label_from_instance = lambda party: '%s-%s (%s ledige plasser)' % \
            (party.start_time.strftime("%H:%M")
            ,party.end_time.strftime("%H:%M")
            ,party.max_registrations - models.Registration.objects.filter(party=party).count())

    def save(self, commit=True):
        m = super(RegistrationForm, self).save(commit=False)
        
        party = models.Party.objects.get(id=m.party.id)
        registered_count = models.Registration.objects.filter(party=m.party).count()
        
        if(party.max_registrations <= registered_count):
            raise ValidationError

        if commit:
            m.save()

        return m
