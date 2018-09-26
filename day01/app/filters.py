import django_filters

from rest_framework import filters

from app.models import Student


class StudentFilter(filters.FilterSet):
    s_name = django_filters.CharFilter('s_name',lookup_expr='contains')
    ss = django_filters.NumberFilter('ss',lookup_expr='gte')
    sy = django_filters.NumberFilter('sy',lookup_expr='lte')


    class Meta:
        model = Student
        fields = ['s_name',]
