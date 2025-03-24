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
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(),  write_only=True)
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = DailyProduct
        fields = ['id', 'date', 'product', 'product_name', 'quantity', 'total_amount']
        extra_kwargs = {
            'id': {'read_only': True},
            'total_amount': {'read_only': True}
        }


class AttendanceSerializer(serializers.ModelSerializer):
    employee_name = serializers.ReadOnlyField(source='employee.full_name')

    class Meta:
        model = Attendance
        fields = ['id', 'employee', 'employee_name', 'check_in', 'check_out', 'worked_hours']
        read_only_fields = ['worked_hours']


class CheckInRequestSerializer(serializers.Serializer):
    employee_ids = serializers.ListField(
        child=serializers.IntegerField(),
        required=True,
        help_text="List of employee IDs to check in"
    )
    check_in_time = serializers.DateTimeField(
        required=True,
        help_text="Custom check-in time (defaults to current time if not provided)"
    )


class CheckOutRequestSerializer(serializers.Serializer):
    employee_ids = serializers.ListField(
        child=serializers.IntegerField(),
        required=True,
        help_text="List of employee IDs to check out"
    )
    check_out_time = serializers.DateTimeField(
        required=True,
        help_text="Custom check-out time (defaults to current time if not provided)"
    )
