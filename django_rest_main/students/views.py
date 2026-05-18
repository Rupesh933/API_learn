from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.


def student(request):
    students = {
        'id' : 10,
        'name' : 'Rupesh',
        'age' : 22,
        'location' : 'Noida',
    }
    return JsonResponse(students)