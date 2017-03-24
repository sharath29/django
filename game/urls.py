from django.conf.urls import url
from . import views

app_name = 'game'
urlpatterns = [
    url(r'^$', views.AboutView.as_view(), name='index'),
    url(r'^check/$', views.index, name='check'),
]