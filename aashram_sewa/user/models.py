from django.conf import settings
from django.db import models
from django.utils import timezone
from .dropdown import *


class user_form(models.Model):
    second_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    spritual_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    date_of_arrival = models.CharField(max_length=10,choices=DATE_OF_ARRIVAL_CHOICES,default='23-OCT')
    time_of_help = models.CharField(max_length=10,choices=DATE_OF_HELP_CHOICES,default='00:00')
    duration_of_help = models.CharField(max_length=5,choices=DURATION_OF_HELP_CHOICES,default='DAY:1')
    help_on_departure = models.CharField(max_length=10,choices=DATE_OF_HELP_CHOICES,default='00:00')
    special_skill = models.CharField(max_length=200)
    previous_volunteering_department = models.CharField(max_length=200)
    hour_of_help = models.IntegerField(default=0)
    primary_manager=models.BooleanField(default=False)
    area_of_management = models.CharField(max_length=200,choices=RESPONSIBILITY_CHOICES)
    register_for_seva=models.CharField(max_length=200,choices=REGISTERED_FOR_SEVA_CHOICES)
    type_of_seva = models.CharField(max_length=200)
    seva_preference = models.CharField(max_length=200,choices=SEVA_CHOICES)
    age=models.CharField(default=0, max_length=10)
    sleep_dormitory=models.BooleanField(default=False)
    message = models.TextField()
    privacy_policy = models.BooleanField(default=False)
    suscribe_to_newsletter = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)