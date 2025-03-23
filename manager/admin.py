from django.contrib import admin
from django.contrib.admin import ModelAdmin

from employee.models import Employee, Attendance, Product, DailyProduct, SalaryRecord


# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(ModelAdmin):
    fields = ['status', 'full_name']
    list_display = ['id', 'status', 'full_name']
    search_fields = ['full_name', 'status']
    search_help_text = "ID bo'yicha qidirish"


@admin.register(Attendance)
class AttendanceAdmin(ModelAdmin):
    fields = ['employee', 'check_in', 'check_out']
    list_display = ['id', 'employee', 'check_in', 'check_out', 'worked_hours']


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    fields = ['name', 'price_per_unit']
    list_display = ['id', 'name', 'price_per_unit']


@admin.register(DailyProduct)
class DailyProductionAdmin(ModelAdmin):
    fields = ['date', 'product', 'quantity']
    list_display = ['id', 'date', 'product', 'quantity', 'total_amount']

@admin.register(SalaryRecord)
class SalaryRecordAdmin(ModelAdmin):
    fields = ['employee', 'start_date', 'end_date', 'total_amount']
    list_display = ['id', 'employee', 'start_date', 'end_date', 'total_amount']
