from rest_framework import serializers

from employee.models import Employee, Attendance, Product, DailyProduct, SalaryRecord


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'status', 'full_name']
        extra_kwargs = {'id': {'read_only': True}}


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price_per_unit']
        extra_kwargs = {'id': {'read_only': True}}


class DailyProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyProduct
        fields = ['id', 'date', 'product', 'quantity', 'total_amount']
        extra_kwargs = {'id': {'read_only': True}, 'total_amount': {'read_only': True}}


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['id', 'employee', 'check_in', 'check_out', 'worked_hours']
        extra_kwargs = {'id': {'read_only': True}}


# class EmployeeCameSerializer(serializers.ModelSerializer):
#     class Meta:
#         model =
#         fields = ['id', 'employee', 'check_in']
#         extra_kwargs = {'id': {'read_only': True}}
