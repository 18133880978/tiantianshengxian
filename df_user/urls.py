from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register$', views.register),
    url(r'^register_handle$', views.register_handle),
    url(r'^login$', views.login),
    url(r'^register_exist', views.register_exist),
    url(r'^login_handle$', views.login_handle),
    url(r'^logout$', views.logout),
    url(r'^info$', views.user_info),
    url(r'^order$', views.user_order),
    url(r'^site$', views.user_site),
    url(r'^areas', views.areas),
]