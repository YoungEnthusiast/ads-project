from django.urls import path
from . import views

urlpatterns = [
    path('', views.showHome, name='index'),
    path('about-us', views.showAbout, name='about'),
    # path('academic-programmes', views.showAcademic, name='academic'),
    # path('news-and-events', views.showNews, name='news'),
    # path('contact-us', views.showContact, name='contact'),
]
