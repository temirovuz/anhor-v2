from django.db import models
from django.db.models import UniqueConstraint

from employee.utils import get_employees_by_date_range, calculate_salary_bulk


class Product(models.Model):
    name = models.CharField(max_length=255)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['id']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name


class DailyProduct(models.Model):
    date = models.DateField()
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=False)
    quantity = models.IntegerField(null=False, blank=False)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Daily Product'
        verbose_name_plural = 'Daily Products'

    def save(self, *args, **kwargs):
        if self.product:
            product = Product.objects.filter(id=self.product.id).first()
            if product:
                self.total_amount = self.quantity * product.price_per_unit
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.date} - {self.product.name} - {self.quantity} - {self.total_amount}"


class Employee(models.Model):
    STATUS_CHOICES = [
        ('yangi', 'Yangi'),
        ('doimiy', 'Doimiy'),
        ('bola', 'Bola'),
    ]
    status = models.CharField(max_length=155, choices=STATUS_CHOICES, default='yangi')
    full_name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        return self.full_name + ' ' + self.status


class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="attendances")  # Ishchi kim
    check_in = models.DateTimeField(db_index=True)
    check_out = models.DateTimeField(db_index=True, null=True, blank=True)
    worked_hours = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Ishlagan soati

    def save(self, *args, **kwargs):
        if self.check_out:
            duration = (self.check_out - self.check_in).total_seconds() / 3600
            self.worked_hours = round(duration, 2)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-check_in']
        verbose_name = "Attendance"
        verbose_name_plural = "Attendances"
        indexes = [
            models.Index(fields=["check_in"]),
            models.Index(fields=["check_out"]),
        ]

    def __str__(self):
        return f"{self.employee} - {self.check_in.strftime('%Y-%m-%d %H:%M')}"


class SalaryRecord(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['employee', 'start_date', 'end_date'], name='unique_salary_record')
        ]
        ordering = ['-start_date']

    @classmethod
    def bulk_create_salaries(cls, start_date, end_date):
        employees = get_employees_by_date_range(start_date, end_date)
        if not employees.exists():
            return

        salary_records = calculate_salary_bulk(employees, start_date, end_date)

        cls.objects.filter(
            employee__in=employees,
            start_date__lt=start_date,
            end_date__gte=start_date
        ).delete()


        cls.objects.bulk_create(salary_records)