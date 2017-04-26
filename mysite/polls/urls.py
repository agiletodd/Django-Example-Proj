from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', login_required(views.IndexView.as_view()), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', login_required(views.DetailView.as_view()), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', login_required(views.ResultsView.as_view()), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', login_required(views.vote), name='vote'),
]