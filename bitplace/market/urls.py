from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^callback', 'market.views.callback', name='callback'),
)
