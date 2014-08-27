from django.conf.urls import patterns, url
from  news import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index' )
    #/news/5/
    #url(r'^(?P<news_story_id>)\d+)/$', views.detail, name='detail'),
 )
