from rest_framework import generics, views, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from django.db.models import Q

from employee.api.serializers import EmployeeSerializer, ProductSerializer, DailyProductSerializer, \
    AttendanceSerializer, CheckOutRequestSerializer, CheckInRequestSerializer
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


class CheckInView(views.APIView):

    def get(self, request):
        current_date = timezone.now().date()

        available_employees = Employee.objects.exclude(
            attendances__check_in__date=current_date,
            attendances__check_out__isnull=True
        )

        serializer = EmployeeSerializer(available_employees, many=True)
        return Response({
            'count': len(available_employees),
            'employees': serializer.data
        })

    def post(self, request):
        serializer = CheckInRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        employee_ids = serializer.validated_data['employee_ids']
        check_in_time = serializer.validated_data.get('check_in_time', timezone.now())

        available_employees = Employee.objects.filter(
            id__in=employee_ids
        ).exclude(
            attendances__check_in__date=check_in_time.date(),
            attendances__check_out__isnull=True
        )

        attendances = [
            Attendance(employee=employee, check_in=check_in_time)
            for employee in available_employees
        ]
        Attendance.objects.bulk_create(attendances)
        processed_ids = [employee.id for employee in available_employees]

        invalid_ids = set(employee_ids) - set(Employee.objects.filter(id__in=employee_ids).values_list('id', flat=True))
        if invalid_ids:
            return Response({
                'success': False,
                'message': f'Invalid employee IDs: {invalid_ids}',
            }, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            'success': True,
            'message': f'Successfully checked in {len(attendances)} employees',
            'processed': processed_ids,
            'not_processed': list(invalid_ids),
            'attendances': AttendanceSerializer(attendances, many=True).data
        })


class CheckOutView(views.APIView):

    def get(self, request):
        current_date = timezone.now().date()

        attendances = Attendance.objects.filter(
            check_out__isnull=True
        )

        employees = [attendance.employee for attendance in attendances]
        serializer = EmployeeSerializer(employees, many=True)

        return Response({
            'count': len(employees),
            'employees': serializer.data
        })

    def post(self, request):

        serializer = CheckOutRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        employee_ids = serializer.validated_data['employee_ids']
        check_out_time = serializer.validated_data.get('check_out_time', timezone.now())

        attendances_to_update = Attendance.objects.filter(
            employee_id__in=employee_ids,
            check_out__isnull=True
        ).select_related('employee')

        attendances_to_update = list(attendances_to_update)
        for attendance in attendances_to_update:
            attendance.check_out = check_out_time

        Attendance.objects.bulk_update(attendances_to_update, ['check_out'])

        for attendance in attendances_to_update:
            attendance.save()

        processed_ids = [attendance.employee_id for attendance in attendances_to_update]

        not_processed = set(employee_ids) - set(processed_ids)

        processed_employees = Employee.objects.filter(id__in=processed_ids)
        not_processed_employees = Employee.objects.filter(id__in=not_processed)

        return Response({
            'success': True,
            'message': f'Successfully checked out {len(attendances_to_update)} employees',
            'processed': EmployeeSerializer(processed_employees, many=True).data,
            'not_processed': EmployeeSerializer(not_processed_employees, many=True).data,
            'attendances': AttendanceSerializer(attendances_to_update, many=True).data
        })
