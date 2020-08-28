from django.db import models
from django.db.models import Count
from time import strftime


class Party(models.Model):
    max_registrations = models.IntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    day = models.CharField(max_length=15)


class YearOfBirth(models.Model):
    year = models.IntegerField()

    def __str__(self):
        return str(self.year)


class Registration(models.Model):
    year_of_birth = models.ForeignKey(YearOfBirth, on_delete=models.CASCADE)
    email = models.CharField(max_length=200)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
