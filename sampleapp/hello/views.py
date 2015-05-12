from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.template import RequestContext, loader

from .models import Request


def index(request):
    r = Request(timestamp=timezone.now())
    r.save()

    last_ten = Request.objects.order_by('-timestamp')[:10]
    template = loader.get_template('hello/index.html')
    context = RequestContext(request, {'requests': last_ten})
    return HttpResponse(template.render(context))

