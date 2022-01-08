from django.urls import  path
from .views import NewCourseView,ListCourseView,UpdateCourseView,DetailCourseView,DeleteCourseView
urlpatterns=[
     path("new/",NewCourseView.as_view(),name="new-course"),
     path("view/",ListCourseView.as_view(),name="list-course"),
     path("update/<int:pk>",UpdateCourseView.as_view(),name="update-course"),
     path("detail/<int:pk>",DetailCourseView.as_view(),name="detail-course"),
     path("delete/<int:pk>",DeleteCourseView.as_view(),name="delete-course")
]