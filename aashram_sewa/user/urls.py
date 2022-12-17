from django.urls import path
from . import views

urlpatterns = [
    path('', views.seva_form, name='seva_form'),
]