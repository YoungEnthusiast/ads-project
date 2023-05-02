from django.shortcuts import render, reverse, redirect
from .models import Advert
# from .forms import ContactForm
# from videos.models import Video
# from news.models import News
# from pictures.models import Picture
# from django.core.mail import send_mail
#from django.template.loader import render_to_string

from datetime import datetime
from django.contrib import messages

def showHome(request):
    adverts = Advert.objects.all()

    context = {'adverts': adverts}

    return render(request, 'home/home.html', context)

def showAbout(request):
    return render(request, 'home/about.html')
