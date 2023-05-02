from django.shortcuts import render, reverse, redirect, get_object_or_404
from .models import Advert

# from .forms import ContactForm
# from videos.models import Video
# from news.models import News
# from pictures.models import Picture
# from django.core.mail import send_mail
#from django.template.loader import render_to_string

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.db.models import Count
from taggit.models import Tag

from datetime import datetime
from django.contrib import messages

def showAbout(request):
    return render(request, 'home/about.html')
def post_list(request, tag_slug=None):

    object_list = Advert.objects.filter(status="Approved")
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    paginator = Paginator(object_list, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, 'home/home.html', {'page': page,
                                                   'posts': posts,
                                                   'tag': tag})

class PostListView(ListView):
    queryset = Advert.objects.filter(status="Approved")
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'home/home.html'

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Advert, slug=post,
                                   status='Approved',

                                   created__year=year,
                                   created__month=month,
                                   created__day=day)

    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Advert.objects.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags',
                                                                             '-created')[:4]
    return render(request, 'home/detail.html', {'post': post,
                                                     # 'comments': comments,
                                                     # 'comment_form': comment_form,
                                                     'similar_posts': similar_posts})
