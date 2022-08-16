from django.contrib import admin

# Register your models here.

from .models import *

class LectureAdmin(admin.StackedInline):
    model = Lecture
    extra = 0

class QuizAdmin(admin.StackedInline):
    model = Quiz
    extra = 0

class CourseAdmin(admin.ModelAdmin):
    inlines = [LectureAdmin, QuizAdmin]


admin.site.register(Course, CourseAdmin)
