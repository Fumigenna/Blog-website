from django.conf.urls import url
from . import views

urlpatterns = [

   url(r'^$', views.index_blog, name='index'),
   url(r'^blog', views.index_blog, name='index')
]