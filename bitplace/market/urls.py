from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^product/$', 'market.views.product', name='product'),
    url(r'^callback', 'market.views.callback', name='callback'),
)
