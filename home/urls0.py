from django.urls import path
from . import views

urlpatterns = [
    # path('', views.showHome, name='index'),
    path('about-us', views.showAbout, name='about'),
    # path('academic-programmes', views.showAcademic, name='academic'),
    # path('news-and-events', views.showNews, name='news'),
    # path('contact-us', views.showContact, name='contact'),

    path('', views.post_list, name='index'),
    path('tag/(?P<tag_slug>[-\w]+)/', views.post_list, name='post_list_by_tag'),
    path('(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/',
        views.post_detail,
        name='post_detail'),
    # url(r'^(?P<post_id>\d+)/share/', views.post_share, name='post_share'),
    # url(r'^feed/$', LatestPostsFeed(), name='post_feed'),
    # url(r'^search/$', views.post_search, name='post_search'),
]
