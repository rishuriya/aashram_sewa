from django.shortcuts import render
from .forms import UserForm
# Create your views here.
def seva_form(request):
    context ={}
    context['form']= UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
    return render(request, 'user/form.html', context)