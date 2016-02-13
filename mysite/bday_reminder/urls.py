from django.conf.urls import url
from . import views

app_name = 'bday_reminder'
urlpatterns = [
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^send/$', views.send, name='send'),
]