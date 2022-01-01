from django.urls import  path
from .views import NewCourseView
urlpatterns=[
     path("new/",NewCourseView.as_view(),name="new-course")
]