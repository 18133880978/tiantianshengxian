from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^place_order$', views.place_order),
    url(r'^order_handle', views.order_handle),
]