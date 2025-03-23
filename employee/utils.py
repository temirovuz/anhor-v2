from django.db.models import Sum
from django.apps import apps


def get_models(model_name):
    return apps.get_model('employee', model_name)


def get_employees_by_date_range(start_date, end_date):
    Employee = get_models('Employee')
    return Employee.objects.filter(
        attendances__check_in__date__gte=start_date,
        attendances__check_in__date__lte=end_date
    ).distinct()


def calculate_salary_bulk(employees, start_date, end_date):
    Attendance = get_models('Attendance')
    attendance_data = Attendance.objects.filter(
        employee__in=employees,
        check_in__date__gte=start_date,
        check_in__date__lte=end_date
    ).values('employee').annotate(total_hours=Sum('worked_hours'))

    total_hours_dict = {entry['employee']: entry['total_hours'] or 0 for entry in attendance_data}

    DailyProduct = get_models('DailyProduct')
    produced_products = DailyProduct.objects.filter(
        date__gte=start_date,
        date__lte=end_date
    ).aggregate(total_income=Sum('total_amount'))['total_income'] or 0
    SalaryRecord = get_models('SalaryRecord')
    SalaryRecord.objects.filter(
        employee__in=employees,
        start_date__lt=start_date,
        end_date__gte=start_date
    ).delete()

    salary_records = []
    for employee in employees:
        total_hours = total_hours_dict.get(employee.id, 0)
        total_amount = (produced_products / total_hours) * total_hours if total_hours else 0
        salary_records.append(
            SalaryRecord(employee=employee, start_date=start_date, end_date=end_date, total_amount=total_amount))

    return salary_records
