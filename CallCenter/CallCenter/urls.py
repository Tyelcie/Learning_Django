# -*- coding: utf-8 -*-


from django.conf.urls import *
from . import view, db, post

urlpatterns = [
    url(r'^index$', view.hello),
    url(r'^db$', db.opdb),
    url(r'^search-post$', post.search_post),
]
