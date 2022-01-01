from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,DeleteView,ListView
from .models import course

# Create your views here.
class NewCourseView(CreateView):
    model = course
    fields = '__all__'


# model_form.html     course_form.html
