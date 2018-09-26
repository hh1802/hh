from django.shortcuts import render

from application.models import Emp


def emps(request,no):
    Emp.objects.filter(dept__no=1)
    Emp.objects.filter(dept__no=1).select_related('dept')
