from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework import routers
#router=routers.DefaultRouter()
#router.register(r'user/',views.SampleViewSet)
urlpatterns = [
    path('home',views.home),
    path('student_form/',views.student_form,name='student_form'),
    path('students_marks/',views.students_marks,name='students_marks'),
    path('api/',views.StudentDataAPIView.as_view()),
    path('pageredirect/',views.PageRedirect),
]