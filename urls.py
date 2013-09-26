# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('apps.intellectmoney.views',
    url(r'^result/$',  'receive_result', name='intellectmoney-result'),
    url(r'^success/$',  'success', name='intellectmoney-success'),
    url(r'^fail/$',  'fail', name='intellectmoney-fail'),

)
