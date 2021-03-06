from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
   	url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
   	url(r'^search/$', TemplateView.as_view(template_name='search.html'), name='search'),
    url(r'^register/$', TemplateView.as_view(template_name='register.html'), name='register'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^recipients/$', views.rec, name='rec'),
    url(r'^recipients/add$', views.addrec, name='addrec'),
    url(r'^person/(?P<person_id>[0-9]+)$', views.person, name='person'),
    url(r'^organs/$', views.org, name='org'),
    url(r'^organs/add$', views.addorg, name='addorg'),
    url(r'^matches/$', views.matches, name='matches'),
    url(r'^notify/(?P<person_id>[0-9]+)$', views.notify, name='notify')
]
