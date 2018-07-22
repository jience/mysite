from django.views.generic import TemplateView, ListView
from django.contrib.auth.models import User
from .models import Course


class CourseListView(ListView):
    model = Course
    context_object_name = "course"
    template_name = 'course/course_list.html'

    def get_queryset(self):
        qs = super(CourseListView, self).get_queryset()
        return qs.filter(user=User.objects.filter(username='alex'))


class UserMixin:
    def get_queryset(self):
        qs = super(UserMixin, self).get_queryset()
        return qs.filter(user=self.request.user)


class UserCourseMixin(UserMixin):
    model = Course


class ManageCourseListView(UserCourseMixin, ListView):
    context_object_name = "courses"
    template_name = 'course/manage/manage_course_list.html'
