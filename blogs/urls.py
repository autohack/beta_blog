from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new_blog/', views.add_blog, name='add_blog'),
    url(r'^(?P<blog_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^profile/',views.profile,name='profile'),
    url(r'^(?P<blog_id>[0-9]+)/edit/$', views.edit, name='edit'),

]