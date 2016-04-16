from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^recipients/$', views.rec, name='rec'),
    url(r'^recipients/add$', views.addrec, name='addrec'),
    url(r'^recipients/(?P<rec_id>[0-9]+)$', views.recipient, name='rec'),
    url(r'^organs/$', views.org, name='org'),
    url(r'^organs/add$', views.addorg, name='addorg'),
    url(r'^organs/(?P<org_id>[0-9]+)$', views.organ, name='organ'),
    url(r'^matches/$', views.matches, name='matches'),
]
