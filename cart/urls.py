from django.conf.urls import include, url
from . import views

urlpatterns = [

	url(r'^add/(?P<pk>\d+)/$', views.add_item, name='add_item'),
	url(r'^remove/(?P<pk>\d+)/$', views.remove_item, name='remove_item'),
	url(r'^$', views.show_cart, name='show_cart'),
	
]