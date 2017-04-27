from django.conf.urls import url
from . import views

urlpatterns = [

   url(r'^$', views.index_contact, name='index'),
   url(r'^contact', views.index_contact, name='index')

]