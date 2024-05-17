from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView

from .forms import LessonForm, CourseForm
from .models import Course, Lesson


# Create your views here.

class CourseListView(ListView):
    model = Course
    template_name = 'courses/course_list.html'
    context_object_name = 'courses'


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lessons'] = Lesson.objects.filter(course=self.object)
        return context


class LessonDetailView(DetailView):
    model = Lesson
    template_name = 'courses/lesson_detail.html'
    context_object_name = 'lesson'


class CourseDetailFormView(DetailView):
    model = Course
    template_name = 'courses/course_detail_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lesson_form'] = LessonForm()  # Corrected: Use CourseForm here
        return context

    def post(self, request, *args, **kwargs):
        course = self.get_object()
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.course = course
            lesson.save()
            return redirect('course_detail', pk=course.pk)
        else:
            return render(request, self.template_name, {'lesson_form': form})

def course_list_form(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses_list')
    else:
        form = CourseForm()
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses, 'form': form})