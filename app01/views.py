import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app01.models import Student, Grade


def hello(request):
    return render(request, 'app01/index.html')


def show_grade(request):
    student = Student.objects.get(pk=2)
    grade = student.u_grade
    return HttpResponse("Grade {}".format(grade.g_name))


def show_students(request):
    grades = Grade.objects.get(pk=2)
    stu = grades.student_set.all()
    return render(request, 'app01/student.html',{'stus': stu})