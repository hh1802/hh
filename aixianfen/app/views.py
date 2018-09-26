# import StringIO
import os
# from cStringIO import StringIO

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
# Create your views here.
from app.models import Mainwheel, MainNav, MainMustBuy, MainShop, MainShow, FoodType, Goods

# def mine(request):
#     """个人中心"""
#     if request.method =='GET':
#         user = request.user
#         orders = OrderModel.objects.filter(user=user)
#         payed, wait_pay=0,0
#         for order in orders:
#             if order.o_status ==0:
#                 wait_pay += 1
#             if order.o_status ==1:
#                 payed += 1
#         data = {
#             'wait_pay':wait_pay,
#             'payed':payed
#         }
#         return render(request,'mine/mine.html',data)
from user.models import UserTicketModel, Usermodel



def home(request):
    if request.method == 'GET':
        mainwheel = Mainwheel.objects.all()
        mainnavs = MainNav.objects.all()
        mainbuys=MainMustBuy.objects.all()
        mainshops= MainShop.objects.all()
        mainshows = MainShow.objects.all()

        data = {
            'title':'首页',
            'mainwheel':mainwheel,
            'mainnav':mainnavs,
            'mainbuys':mainbuys,
            'mainshops':mainshops,
            'mainshows':mainshows,
        }
        return render(request,'home/home.html',data)


def market(request):
    if request.method == 'GET':
        return render(request,'market/market.html')
        # return HttpResponseRedirect(reverse('axf:market_parmas',args=('104749','0','0')))


def user_market(request, typeid, cid, sid):
    """
    :param request:
    :param typeid: 分类id
    :param cid: 子分类id
    :param sid: 排序id
    """
    if request.method == 'GET':
        ticket = request.COOKIES.get('ticket')
        user_ticket = UserTicketModel.objects.filter(ticket=ticket).first()
        if user_ticket:
            user = user_ticket.user
        else:
            user=''
        foodtypes = FoodType.objects.all()
        #获取某分类下的商品
        if cid == '0':
            goods = Goods.objects.all()
        else:
            goods = Goods.objects.filter(categoryid=typeid,
                                         childcid=cid)

        #重新组装全部分类的参数
        #组装结果为[【'全部分类','0'】,['酒类','13550']]
        foodtypes_current = foodtypes.filter(typeid=typeid).first()
        if foodtypes_current:
            childtypes = foodtypes_current.childtypenames
            childtypenames = childtypes.split('#')
            child_list = []
            for childtypename in childtypenames:
                child_type_info = childtypename.split(':')
                child_list.append(child_type_info)
            data ={
                'foodtypes':foodtypes,
                'goods':goods,
                'typeid':typeid,
                'cid':cid,
            }

            return render(request,'market/market.html',data)




# def greetings(fn):
#     def y():
#         b = fn().lower
#         return b
#
#     return y
# fn = 'hi there'
# print(greetings(fn))

