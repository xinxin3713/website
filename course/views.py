# coding=utf-8
from django.shortcuts import render_to_response
from django.views import generic

from course.models import Course, CourseCategory


class IndexView(generic.ListView):
    template_name = 'index.html'

    def get_queryset(self):
        """Return the last five published questions."""
        return Course.objects.order_by("id")[:6]


class CourseView(generic.ListView):
    template_name = 'course.html'

    def get_queryset(self):
        search = self.request.GET.get("search")
        if search:
            return Course.objects.filter(title__icontains=search)
        category_id = self.request.GET.get("category_id")
        if category_id:
            return Course.objects.filter(category_id=category_id)
        return Course.objects.all()

    def get_context_data(self, **kwargs):
        context = super(CourseView, self).get_context_data(**kwargs)
        context['categories'] = CourseCategory.objects.all()
        return context


class CourseDetailView(generic.DetailView):
    model = Course
    template_name = 'course-intro.html'
    
    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['categories'] = CourseCategory.objects.all()
        return context


class ContactView(generic.View):
    def get(self, *args, **kwargs):
        return render_to_response(template_name='contact.html')

