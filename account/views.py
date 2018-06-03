from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from account.forms import LoginForm


# Create your views here.
def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])

            if user:
                login(request, user)
                return HttpResponse("Wellcome You. You have been authenticated successfully")
            else:
                return HttpResponse("Sorry, Your name or password is not right.")
        else:
            return HttpResponse("Invalid login")

    if request.method == 'GET':
        login_form = LoginForm()
        return render(request, "account/login.html", {'form': login_form})
