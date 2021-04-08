from __future__ import absolute_import, unicode_literals

from celery import shared_task


@shared_task(name='new_task')
def new_task(x, y):
    res = {
        'x': x,
        'y': y,
        'result': x * y
    }
    return res
