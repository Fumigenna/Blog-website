from django.conf.urls import url
from . import views
from Blog import views as views2



urlpatterns = [

   url(r'^$', views.index, name='index'),
   url(r'^blog', views2.index_blog, name='blog_index')
]
