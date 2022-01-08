from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,DeleteView,ListView,DetailView
from .models import course

# Create your views here.
class NewCourseView(CreateView):
    model = course
    fields = '__all__'

# model_form.html     course_form.html

class ListCourseView(ListView):
    model = course
    context_object_name = 'courselist'

#model_list.html  course_list.html
#courses=course.objects.all()

class UpdateCourseView(UpdateView):
    model = course
    fields = '__all__'

#course_form.html
class DetailCourseView(DetailView):
    model = course

#course_detail.html
class DeleteCourseView(DeleteView):
    model = course
    template_name = "courses/course_delete_confirm.html"
    success_url = '/course/view'

#course_delete_confirm.html