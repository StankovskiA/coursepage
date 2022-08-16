from django.urls import path
from . import views


urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path('courses/', views.courses, name='courses'),
    path('course/<str:pk>/', views.course, name="course"),
    path('course/<str:pk>/lecture/<str:lecture_id>/', views.course_lecture, name="course_lecture"),
    path('course/<str:pk>/quiz/<str:quiz_id>/', views.course_quiz, name="course_quiz"),
    path('course/<str:pk>/practical/', views.practical, name="practical"),

    # path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    # path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    # path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),


]