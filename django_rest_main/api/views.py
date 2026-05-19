from django.shortcuts import render, get_object_or_404
from api.serializers import StudentSerializer, EmployeeSerializer
from api.models import Student
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

# Create your views here.


@api_view(['GET', 'POST'])
def student(request):
    if request.method == 'GET':
        students = Student.objects.all()
        print(students)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT', 'DELETE'])
def singleStudentViewDetails(request,pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

from employees.models import Employees
from rest_framework.views import APIView
# class based view
# class Employees(APIView):
#     def get(self, request):
#         employee = Employees.objects.all()
#         serializer = EmployeeSerializer(employee, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request):
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# from django.http import Http404
# class SingleEmployee(APIView):
#     def get_object(self,pk):
#         try:
#             employee = Employees.objects.get(pk=pk)
#             return employee
#         except Employees.DoesNotExist:
#             raise Http404
    
#     def get(self, request, pk):
#         employee = self.get_object(pk)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def put(self, request, pk):
#             employee = self.get_object(pk)
#             serializer = EmployeeSerializer(employee, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_200_OK)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         employee = self.get_object(pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


from employees.models import Employees

'''
# mixins
from rest_framework import mixins, generics
class EmployeesList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
# to perform primary key type operations we use
class SingleEmployee(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,  generics.GenericAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)

'''

'''
# generic
from rest_framework import generics
# class EmployeesList(generics.ListAPIView, generics.CreateAPIView):
class EmployeesList(generics.ListCreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer

# class SingleEmployee(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
class SingleEmployee(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'

'''

from rest_framework import viewsets
# class EmployeesViewset(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Employees.objects.all()
#         serializer = EmployeeSerializer(queryset, many=True)
#         return Response(serializer.data)
    
#     def create(self, request):
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors)
    
#     def retrieve(self, request, pk=None):
#         employee = get_object_or_404(Employees, pk=pk)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def update(self, request, pk=None):
#         employee = get_object_or_404(Employees, pk=pk)
#         serializer = EmployeeSerializer(employee)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors)

#     def delete(self, request, pk=None):
#         employee = get_object_or_404(Employees, pk=pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class EmployeesViewset(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer