from django.shortcuts import render

# Create your views here.
from app.models import User


def quanxian(request):
    #查找小陈，小杨用户的权限
    if request.method == 'GET':
        user = User.objects.filter(username='小陈').first()
        print(user.username)
        print(user.id)
        print(user.role.r_name)
        print(user.role.id)
        print(user.role.r_p)
        print(user.role.r_p.first().p_name)
        print(user.role.r_p.last().p_name)

