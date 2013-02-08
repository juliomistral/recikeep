from django.shortcuts import render
from django.contrib.auth import authenticate, login

from .forms import UserCreationForm


def handle_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=user.username, password=form.password1)
            login(request, user)
            return render(request,'success.html', { "user" :  user})
    else:
        form = UserCreationForm()

    context = { 'form' : form }
    return render(request,'signup.html', context)