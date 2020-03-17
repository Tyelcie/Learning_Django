# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators import csrf
from cc.models import inbound

def search_post(request):
    ctx = {}
    if request.POST:
        test1 = inbound(general_source = request.POST['general_source'],
                        general_innum = request.POST['general_innum'])
        test1.save()
        ctx['msg'] = '提交成功！'
    return render(request, 'post.html', ctx)