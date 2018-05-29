#!/usr/bin/env python
# coding=utf-8
"""

__created__ = '4/22/18'
__author__ = 'deling.ma'
"""
import multiprocessing

bind = '0.0.0.0:3333'
max_requests = 10000
keepalive = 5

proc_name = 'pypy_website'

workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'gevent'

loglevel = 'info'
errorlog = '-'

x_forwarded_for_header = 'X-FORWARDED-FOR'
