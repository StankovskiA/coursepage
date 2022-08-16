from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .forms import CreateUserForm
from .models import *


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {
            'form': form
        }
        return render(request, 'accounts/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    courses = Course.objects.all()

    total_courses = courses.count()
    completed = courses.filter(completed=True).count()
    pending = total_courses - completed

    context = {
        'orders': courses,
        'total_courses': total_courses,
        'completed': completed,
        'pending': pending
    }

    return render(request, 'accounts/dashboard.html', context)


@login_required(login_url='login')
def courses(request):
    courses = Course.objects.all()

    return render(request, 'accounts/courses.html', {
        'courses': courses
    })


@login_required(login_url='login')
def course(request, pk):
    course = Course.objects.get(id=pk)

    context = {
        'course': course
    }
    return render(request, 'accounts/course.html', context)

@login_required(login_url='login')
def course_lecture(request, pk, lecture_id):
    course = Course.objects.get(id=pk)
    if int(lecture_id) <= course.lectures:
        lecture = Lecture.objects.get(id=lecture_id)
        course.completed_lectures = lecture_id
        course.save()
        context = {
            'course': course,
            'lecture': lecture
        }
        return render(request, 'accounts/lecture.html', context)

    return render(request, 'accounts/completed_course.html', {'course':course, 'user': request.user.username})

@login_required(login_url='login')
def course_quiz(request, pk, quiz_id):
    course = Course.objects.get(id=pk)
    if int(quiz_id) <= course.lectures:
        quiz = Quiz.objects.get(id=quiz_id)
        course.completed_lectures = quiz_id
        if int(quiz_id) == course.lectures:
            course.completed = True
        course.save()
        answer = request.GET.get('answer', '')
        context = {
            'course': course,
            'quiz': quiz,
            'answer' : answer,
        }
        return render(request, 'accounts/quiz.html', context)
    return render(request, 'accounts/completed_course.html', {'course':course, 'user': request.user.username})

@login_required(login_url='login')
def practical(request, pk):
    course = Course.objects.get(id=pk)
    course.completed = True
    course.save()
    context = {
        'course': course
    }
    return render(request, 'accounts/practical.html', context)
