from django.urls import path

from employee.api.views import (EmployeeListCreateAPIView, ProductListCreateAPIView, DailyProductListCreateAPIView,
                                CheckInView, CheckOutView)

urlpatterns = [
    path('employee/', EmployeeListCreateAPIView.as_view(), name='employee-list-create'),
    path('product/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('daily-product/', DailyProductListCreateAPIView.as_view(), name='daily-product-list-create'),
    path('check-in/', CheckInView.as_view(), name='check-in'),
    path('check-out/', CheckOutView.as_view(), name='check-out'),
]
