from django.conf.urls import url

import blog.views

urlpatterns = [
    url(r'^$', blog.views.home, name = 'home'),
    url(r'^about/$', blog.views.about, name = 'about'),
    url(r'^map/$', blog.views.mymap, name = 'map'),
    url(r'^articles/(?P<article_id>[0-9]+)/$', blog.views.article, name = 'article')

]