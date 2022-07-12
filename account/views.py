
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from . import tasks
from account.forms import RegistrationForm



def register_view(request):#, *args, **kwargs):
    # user = request.user
    # if user.is_authenticated: 
    #     return HttpResponse("You are already authenticated as " + str(user.email))
    # else:
    #     pass
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        # print(form)
        print(form.errors)
        if form.is_valid():
            form.save()
            HASH = form.generate_password()
            print(HASH)
            # SEND MAIL
            tasks.emails(form.cleaned_data['email'],'welcome_mail')


            # if destination:
            return redirect('account:register')
            # return redirect('home')
        else:
            print(50)
            return HttpResponse(form.errors.items())
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'register.html', context)