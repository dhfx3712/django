from django.shortcuts import render

# Create your views here.
from web import models
def student_list(request):
    student_queryset = models.Student.objects.all()
    print (student_queryset.values())
    return render(request,"student.html",{"student_queryset":student_queryset})