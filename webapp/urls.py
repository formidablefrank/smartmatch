from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    #url(r'^view/(?P<book_id>[0-9]+)$', views.view, name='view')
]
