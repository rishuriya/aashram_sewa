from django.shortcuts import render
from .forms import UserForm
# Create your views here.
def seva_form(request):
    context ={}
    context['form']= UserForm()
    return render(request, 'user/form.html', context)