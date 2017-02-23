from django.conf.urls import url

from . import views

app_name = 'posts'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<submitted_text>)/$', views.add_item, name='add_item'),
    url(r'^/(?P<post_id>[0-9]+)/remove$', views.remove_item, name='remove_item'),
]