# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import os
import sys
import errno
import shutil
import difflib
from tempfile import mkstemp, mkdtemp

from DEOnlineJudge.celery import app
from app.record.models import Record, RecordDetail


@app.task(bind=True)
def execute_program(self, record_id):
    try:
        record = Record.objects.get(pk=record_id)
    except Record.DoesNotExist:
        return

    record.status = 'RUNNING'
    record.save()

    language = record.language.lower()
    if language == 'c':
        fid, path = mkstemp(suffix='.c')
    elif language == 'c++':
        fid, path = mkstemp(suffix='.cpp')
    elif language == 'pascal':
        fid, path = mkstemp(suffix='.pas')
    else:
        record.status = 'SYSERR'
        record.save()
        return
    source_code = record.source_code
    f = open(path, 'w')
    f.write(source_code.encode('utf8'))
    f.close()

    origin_dir = os.getcwd()
    output_dir = mkdtemp()
    os.chdir(output_dir)
    pid = os.fork()
    if pid == 0:
        try:
            if language == 'c':
                os.execlp('gcc', 'gcc', path, '-Wall', '-o', 'program')
            elif language == 'c++':
                os.execlp('g++', 'g++', path, '-Wall', '-o', 'program')
            elif language == 'pascal':
                os.execlp('fpc', 'fpc', path, '-o' + os.path.join(output_dir, 'program'))
        except Exception as e:
            record.status = 'CE'
            record.message = e
            record.save()
            return
    pid_info = os.waitpid(pid, 0)
    if os.WEXITSTATUS(pid_info[1]) > 0:
        record.status = 'CE'
        record.save()
        return

    os.chdir(os.path.join(origin_dir, 'media/data', str(record.problem.pk)))
    dirlist = os.listdir(os.getcwd())
    file_list = []
    in_ext = record.problem.data_input_extension
    out_ext = record.problem.data_output_extension
    for line in dirlist:
        filepath = os.path.join(os.getcwd(), line)
        if os.path.isfile(filepath) and filepath[-len(in_ext):] == in_ext and os.path.exists(filepath[0:-len(in_ext)]+out_ext):
            file_list.append(filepath)
    total_point = len(file_list)
    record.total_point = total_point
    record.save()
    result_list = []
    os.chdir(output_dir)
    for infile in file_list:
        outfile = infile[0:-len(in_ext)]+out_ext
        shutil.copyfile(infile, os.path.join(output_dir, str(record.problem.pk)+'.in'))
        pid = os.fork()
        if pid == 0:
            os.execl(os.path.join(output_dir, 'program'), os.path.join(output_dir, 'program'))
            return
        pid_info = os.waitpid(pid, 0)
        if os.WEXITSTATUS(pid_info[1]) > 0:
            RecordDetail.objects.create(
                record=record,
                status='CE',
                score=0,
                time_used=0,
                memory_used=0,
                message=os.WEXITSTATUS(pid_info[1]),
            )
            continue

        try:
            str(record.problem.pk)+'.out'
            origin_output = open(outfile, 'r')
            now_output = open(str(record.problem.pk)+'.out', 'r')
        except Exception as exc:
            RecordDetail.objects.create(
                record=record,
                status='RE',
                score=0,
                time_used=0,
                memory_used=0,
                message=exc,
            )
            continue
        diff_origin = origin_output.read()
        diff_now = now_output.read()
        diff_origin_lines = diff_origin.splitlines()
        diff_now_lines = diff_now.splitlines()
        d = difflib.Differ()
        diff = d.compare(diff_origin_lines, diff_now_lines)
        diff_result = '\n'.join(list(diff))
        origin_output.close()
        now_output.close()
        flag = True
        for index, line in enumerate(diff_origin_lines):
            try:
                if diff_origin_lines[index].strip() != diff_now_lines[index].strip():
                    flag = False
                    break
            except Exception as e:
                flag = False
                break
        if flag:
            RecordDetail.objects.create(
                record=record,
                status='AC',
                score=(float(1) / total_point) * 100,
                time_used=0,
                memory_used=0,
                message=''
            )
            result_list.append('AC')
        else:
            RecordDetail.objects.create(
                record=record,
                status='WA',
                score=0,
                time_used=0,
                memory_used=0,
                message=diff_result,
            )
            result_list.append('WA')

    status = {
        'AC': 0,
        'WA': 0,
        'RE': 0,
        'CE': 0,
        'TLE': 0,
    }
    for result in result_list:
        status[result] += 1
    if status['WA'] > 0:
        record.status = 'WA'
    elif status['RE'] > 0:
        record.status = 'RE'
    elif status['CE'] > 0:
        record.status = 'CE'
    elif status['TLE'] > 0:
        record.status = 'TLE'
    else:
        record.status = 'AC'
    record.score = int((float(status['AC']) / total_point) * 100)
    record.save()
    os.chdir(origin_dir)