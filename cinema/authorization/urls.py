from django.template.defaulttags import url
from django.urls import path

from . import views
#from ..home.views import home

urlpatterns = [
    #url(r'^$', home),
    #path('signup/
    path(r'form', views.forms),
]
