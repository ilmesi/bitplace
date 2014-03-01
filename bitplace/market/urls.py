from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^product/(?P<id>\d)/$', 'market.views.product', name='product'),
    url(r'^callback', 'market.views.callback', name='callback'),
    url(r'^pay', 'market.views.pay', name='pay'),
)
