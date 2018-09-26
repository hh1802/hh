from django.conf.urls import url

from application import views

urlpattren=[
    url(r'^emp/(?P<no>[0-9]+)',views.emps, )
]