from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import CourseListView, CourseDetailView, LessonDetailView, course_list_form,  CourseDetailFormView

urlpatterns = [
    path('course_list/', CourseListView.as_view(), name='courses_list'),
    path('course_detail/<int:pk>/', CourseDetailView.as_view(), name="course_detail"),
    path('course_detail_with_form/<int:pk>/', CourseDetailFormView.as_view(), name='course_detail_with_form'),
    path('lesson/<int:pk>/', LessonDetailView.as_view(), name='lesson_detail'),
    path('course_list_form/', course_list_form, name="course_list_form"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
