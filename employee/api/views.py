from rest_framework import generics
from rest_framework import views

from employee.api.serializers import EmployeeSerializer, ProductSerializer, DailyProductSerializer
from employee.models import Employee, Product, DailyProduct, Attendance, SalaryRecord



class EmployeeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class DailyProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = DailyProduct.objects.all()
    serializer_class = DailyProductSerializer