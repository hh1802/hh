import os
import io
import sys
# from StringIO import StringIO
from datetime import datetime, timedelta
# import StringIO


from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
# from django.utils.six import StringIO

from user.models import Usermodel, UserTicketModel
# Create your views here.
from utils.funtions import get_ticket


def register(request):
    """
    :param request: 注册
    :return:
    """
    if request.method == 'GET':
        return render(request,'user/user_register.html')
    if request.method =='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        icon = request.FILES.get('icon')
        #验证参数都不能为空
        if not all([username,email,password,icon]):
            #验证不通过，提示参数不能为空，返回页面错误提示
            msg = '参数不能为空'
            return render(request, 'user/user_register.html',{'msg':msg})
        password = make_password(password)#加密
        #创建
        Usermodel.objects.create(username=username,
                                 password=password,
                                 email=email,
                                 icon=icon)

        return HttpResponseRedirect(reverse('user:login'))


from django.http import HttpResponse
from xlwt import *
# from io import StringIO
def excel_export(request):
    """
    导出excel表格
    """
    list_obj = Usermodel.objects.all().order_by("-id")
    if list_obj:
        # 创建工作薄
        ws = Workbook(encoding='utf-8')
        w = ws.add_sheet(u"数据报表第一页")
        w.write(0, 0, "id")
        w.write(0, 1, u"用户名")
        w.write(0, 2, u"发布时间")
        # w.write(0, 3, u"内容")
        # w.write(0, 4, u"来源")
        # # 写入数据
        excel_row = 1
        for obj in list_obj:
            data_id = obj.id
            data_user = obj.username
            data_email = obj.email
            # data_time = obj.time.strftime("%Y-%m-%d")[:10]
            # data_content = obj.content
            # dada_source = obj.source
            w.write(excel_row, 0, data_id)
            w.write(excel_row, 1, data_user)
            w.write(excel_row, 2, data_email)
            # w.write(excel_row, 3, data_content)
            # w.write(excel_row, 4, dada_source)
            excel_row += 1
        # 检测文件是够存在
        # 方框中代码是保存本地文件使用，如不需要请删除该代码
        ###########################
        exist_file = os.path.exists("test.xls")
        if exist_file:
            os.remove(r"test.xls")
        ws.save("test.xls")
        ############################
        sio = io.StringIO()
        ws.save(sio)
        sio.seek(0)
        response = HttpResponse(sio.getvalue(), content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=test.xls'
        response.write(sio.getvalue())
        return response

def login(request):
    """登录"""
    if request.method =='GET':
        return render(request,'user/user_login.html')

    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        #验证用户
        user = Usermodel.objects.filter(username=username).first()
        if user:
            #验证密码是否正确
            if check_password(password,user.password):
                #保存ticket在客户端
                ticket = get_ticket()
                response = HttpResponseRedirect(reverse('axf:home'))
                out_time=datetime.now() + timedelta(days=1)
                response.set_cookie('ticket',ticket,expires=out_time)
                #2.保存ticket到服务端的user_ticket表中
                UserTicketModel.objects.create(user=user,
                                              out_time=out_time,
                                              ticket=ticket)
                return response
            else:
                msg='密码错误'
                return render(request,'user/user_login.html',{'msg':msg})
