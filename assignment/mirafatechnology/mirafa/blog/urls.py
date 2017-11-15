from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$', views.user_login),
    url(r'register/$', views.register),
    url(r'^about/$',views.AboutView.as_view()),
]
