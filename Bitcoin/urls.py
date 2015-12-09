from django.conf.urls import include, url
from django.contrib import admin
from Bitcoin import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home),
    url(r'^get_balance$', views.get_balance),
    url(r'^login$', views.login),
    url(r'^signin$', views.signin),
]
