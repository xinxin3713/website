#!/usr/bin/env python
# coding=utf-8
"""

__created__ = '2018/3/31'
__author__ = 'deling.ma'
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('course/', views.CourseView.as_view(), name='course'),
    path('course/<int:pk>/', views.CourseDetailView.as_view(),
         name='course_detail'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]
