from django.template.defaulttags import url
from django.urls import path


from ..home.views import home

urlpatterns = [
    url(r'^$', home),
    path('form', views.reg_form)
]
