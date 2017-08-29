from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.cart),
    url(r'^add$', views.add),
    url(r'^cart_num$', views.cart_num),
    url(r'^cart_del$', views.cart_del),
    url(r'^edit$', views.edit),
]
