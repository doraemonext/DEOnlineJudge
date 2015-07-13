# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from DEOnlineJudge.celery import app


@app.task(bind=True)
def execute_program(self, record_id):
    print 'aaabbb'
    pass
