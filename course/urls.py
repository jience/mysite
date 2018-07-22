from django.conf.urls import url
from django.views.generic import TemplateView
from .views import CourseListView


urlpatterns = [
    url(r'^about/$', TemplateView.as_view(template_name="course/about.html"), name="about"),
    url(r'^course-list/$', CourseListView.as_view(), name="course_list"),
]