from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^news/', include('news.urls', namespace = "news")),
    url(r'^admin/', include(admin.site.urls)),
    
    #url(r'^accounts/', include('registration.backends.default.urls')),
)
