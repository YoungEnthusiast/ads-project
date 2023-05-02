import json
# import urllib.request
# from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .forms import CustomPasswordChangeForm, CustomRegisterForm, StrangerForm
from .models import Person
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import update_session_auth_hash, login, authenticate
from django.contrib.auth.decorators import login_required, permission_required
# from .filters import InitiatedCollabFilter, BellNotificationFilter, CollabDocFilter, TaskFilter, FolderFilter
from django.core.paginator import Paginator
from django.core.mail import send_mail
# from django.db.models import Q
from django.http import HttpResponseRedirect
from django.views.generic import View
# from django.contrib.auth.models import User
# from django.contrib.sites.shortcuts import get_current_site
# from django.utils.encoding import force_bytes, force_str
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.template.loader import render_to_string
# from datetime import datetime, date
from django.core.mail import send_mass_mail

# from django.contrib.auth import logout
# from dateutil.rrule import rrule, DAILY
# from subscription.models import Subscription


def join(request):
    form = StrangerForm()
    if request.method == 'POST':
        form = StrangerForm(request.POST or None)
        if form.is_valid():
            form.save()
            try:
                send_mail(
                    'Create Account',
                    'Please follow the link https://postsads.com/join/' + str(username) + ' to create an account',
                    'no-reply@postsads.com',
                    [username],
                    fail_silently=False,
                    #html_message = render_to_string('home/home1.html')
                )
                messages.info(request, "Please check your inbox")
            except:
                messages.info(request, "Please enter a valid email address")
    else:
        messages.error(request, 'Please make sure you pass the recaptcha.')

    return redirect('join')
    return render(request, 'account/join.html', {'form': form})

def create(request, username):
    username = username
    if request.method == "POST":
        form = CustomRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False).username = username
            form.save(commit=False).email = username
            try:
                is_exist = Person.objects.get(username=username)
                messages.error(request, "A user with the email already exists")
            except:
                form.save()
                messages.info(request, "Registration was successful!")
                return redirect('poster_board')
        else:
            messages.error(request, "Please review and correct form input fields")
    else:
        form = CustomRegisterForm()
    return render(request, 'account/account.html', {'form': form, 'username':username})

def logoutRequest(request):
    logout(request)
    return redirect('login')

def loginRequest(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # messages.info(request, f"You are now logged in as {username}")
                return redirect('poster_board')
            else:
                messages.info(request, "Either your email address or password is incorrect.")
        else:
            messages.info(request, "Either your email address or password is incorrect.")
    form = AuthenticationForm()
    return render(request = request, template_name = "account/login.html", context={"form":form})








@login_required
def loginTo(request):
    if request.user.type == "Poster":
        return HttpResponseRedirect(reverse('poster_board'))
    # elif request.user.type == "QwikA--":
    #     return HttpResponseRedirect(reverse('qwikadmin_board'))
    # elif request.user.type == "QwikVendor":
    #     return HttpResponseRedirect(reverse('qwikvendor_board'))
    # elif request.user.type == "QwikPartner":
    #     return HttpResponseRedirect(reverse('qwikpartner_board'))
