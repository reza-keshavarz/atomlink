from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.show_all, name='show_all'),
    url(r'^(?P<username>[-\w]+)/$', views.links_by_user, name='links_by_user'),


]
