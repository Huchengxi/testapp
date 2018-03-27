# -*- coding: utf-8 -*-

from common.mymako import render_mako_context, render_json
from .models import MultRecord
from django.views.decorators.csrf import csrf_exempt


def home(request):
    """
    首页
    """
    all_record = MultRecord.objects.all()[:5]
    ctx = {
        'all_record': all_record
    }
    return render_mako_context(request, '/home_application/home.html', ctx)


def multiplication_computer(request):
    multiplier = int(request.POST.get('multiplier', ''))
    multiplicand = int(request.POST.get('multiplicand', ''))
    mult_result = multiplier * multiplicand
    MultRecord.objects.create(
        multiplier=multiplier,
        multiplicand=multiplicand,
        mult_result=mult_result,
    )
    return render_json({'result': True, 'mult_result': mult_result})


def dev_guide(request):
    """
    开发指引
    """
    return render_mako_context(request, '/home_application/dev_guide.html')


def contactus(request):
    """
    联系我们
    """
    return render_mako_context(request, '/home_application/contact.html')
