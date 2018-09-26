
from django.conf.urls import url

from user import views
urlpatterns =[
    #登录
    url(r'^register/',views.register, name='register'),
    url(r'^login/',views.login, name='login'),
    url(r'^excel_export/',views.excel_export, name='login'),

]