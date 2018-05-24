from django.shortcuts import render

# Create your views here.

# https://docs.djangoproject.com/en/2.0/intro/tutorial01/
import logging

from django.http import HttpResponse

log = logging.getLogger("debug")


def index(request):
    log.debug(">>>>jump to polls>>>>")
    return HttpResponse("Hello, world. You're at the polls index.")