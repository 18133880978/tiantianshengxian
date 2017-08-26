from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^detail$',views.detail),
    url(r'^goods_num$', views.goods_num),
]