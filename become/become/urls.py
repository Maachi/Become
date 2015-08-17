"""become URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'organizations.views.index'),
    url(r'^login/$', 'organizations.views.login_page'),
    url(r'^dashboard/$', 'organizations.views.dashboard'),
    url(r'^clients/create/$', 'clients.views.create_client'),
    url(r'^logout/$', 'organizations.views.logout_request'),
    url(r'^clients/(?P<client_name>.*)/(?P<client_id>\d+)/$', 'clients.views.client_detail'),
    url(r'^clients/(?P<client_name>.*)/(?P<client_id>\d+)/invoice/create/$', 'invoices.views.create_invoice'),
    url(r'^clients/(?P<client_name>.*)/(?P<client_id>\d+)/contract/create/$', 'contracts.views.create_contract'),
]
