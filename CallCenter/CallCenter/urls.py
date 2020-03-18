# -*- coding: utf-8 -*-


from django.conf.urls import url
from django.contrib import admin
from . import view, db, post

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index$', view.hello),
    url(r'^db$', db.opdb),
    url(r'^search-post$', post.search_post),
]
