#!/usr/bin/env python
# -*- coding: utf8 -*-

# from django.http import HttpResponse
from django.http import JsonResponse


def api(request):
    a = request.POST.get('foo')
    b = request.POST.get('bar')
    result = {'msg': '{} {}'.format(a, b)}
    return JsonResponse(result)
