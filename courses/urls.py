from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import CourseListView, CourseDetailView, LessonDetailView

urlpatterns = [
    path('course_list/', CourseListView.as_view(), name='courses_list'),
    path('course_detail/<int:pk>/', CourseDetailView.as_view(), name="course_detail"),
    path('lesson/<int:pk>/', LessonDetailView.as_view(), name='lesson_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
