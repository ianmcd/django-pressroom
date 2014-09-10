from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse
from django.template import RequestContext, loader
from itertools import chain
from operator import attrgetter

from pressapp.models import InTheNews, PressRelease

def index(request):
  news_list = InTheNews.objects.order_by('published_date')
  release_list = PressRelease.objects.order_by('published_date')

  result_list = sorted(chain(news_list, release_list), key=attrgetter('published_date'), reverse=True)

  context = {'press_list': result_list}
  return render(request, 'pressapp/index.html', context)


def detail(request, slug):
  post = get_object_or_404(PressRelease, slug=slug)
  return render(request, 'pressapp/detail.html', {'post': post})
