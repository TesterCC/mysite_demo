# -*- coding:utf-8 -*-

"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view
from rest_framework.schemas import get_schema_view

import drf_yasg

from devtest.views import current_datetime

from django.views.generic import TemplateView

# http://www.django-rest-framework.org/tutorial/7-schemas-and-client-libraries/
schema_view = get_schema_view(title='FSPT Core API')
# terminal test:
# http http://127.0.0.1:8000/schema/ Accept:application/coreapi+json

from quickstart.views import UserViewSet, GroupViewSet
# from snippets.views import *


# http://www.django-rest-framework.org/tutorial/quickstart/
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    # Django rest framework
    url(r'^', include(router.urls)),
    # need namespace, related to settings LOGIN_URL, LOGOUT_URL
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Django 2.0 official
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),

    # FBV
    url(r'^', include('snippets.urls')),    # http://127.0.0.1:8000/snippets/1/

    url(r'^schema/$', schema_view),


]

# API doc config
urlpatterns += [
    # Swagger UI API docs, pip install django-rest-swagger
    # https://marcgibbons.com/django-rest-swagger/
    url(r'^swagger-docs/', get_swagger_view(title="FSPT mysite Swagger API")),
    # DRF Built-in API docs and Generate schema with valid `request` instance, pip install coreapi
    url(r'^drf-docs/', include_docs_urls(title="mysite Built-in DRF API", public=False)),
    # https://drf-yasg.readthedocs.io/en/stable/openapi.html, pip install drf-yasg

]

# little test interface
urlpatterns += [
    # Current Time Test
    # url(r'^current_date/$', TemplateView.as_view(template_name="current_date.html"))
    path('current_date/', current_datetime, name='current_datetime')
]
