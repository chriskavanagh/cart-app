from django.conf.urls import include, url
from . import views

urlpatterns = [

	url(r'^$', views.product_list, name='product_list'),

	url(r'^like_product/$', views.like_product, name='like_product'),

	
	url(r'^(?P<slug>[-\w]+)/user-like-product/$', views.user_likes, name='user_likes'),

	url(r'^(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
	
]