# from django.http import HttpResponseRedirect, JsonResponse
# from django.shortcuts import render
# from django.core.urlresolvers import reverse
# from axfapp.models import MainWheel, MainNav, MainMustBuy, MainShop, MainShow, Goods, FoodType, CartModel, OrderModel, \
#     OrderGoodsModel
# from user.models import UserTicketModel
# # from utils.funtions import get_order_random_id
#
#
# def home(request):
#     """首页"""
#     if request.method =='GET':
#         mainwheel = MainWheel.objects.all()
#         mainnav = MainNav.objects.all()
#         mainmustbuy = MainMustBuy.objects.all()
#         mainshop = MainShop.objects.all()
#         show = MainShow.objects.all()
#
#         data = {
#             'title': '首页',
#             'main': mainwheel,
#             'nav':mainnav,
#             'mustbuy':mainmustbuy,
#             'shop': mainshop,
#             'show': show,
#
#
#
#         }
#         return render(request, 'home/home.html',data)
#
#


from django.http import HttpResponse
from xlwt import *

from user.models import UserModel
import datetime

def excel_export(request):
    """
    导出excel表格
    """
    list_obj = UserModel.objects.all().order_by("-time")
    if list_obj:
        # 创建工作薄
        ws = Workbook(encoding='utf-8')
        w = ws.add_sheet(u"数据报表第一页")
        w.write(0, 0, "id")
        w.write(0, 1, u"用户名")
        w.write(0, 2, u"发布时间")
        w.write(0, 3, u"内容")
        w.write(0, 4, u"来源")
        # 写入数据
        excel_row = 1
        for obj in list_obj:
            data_id = obj.id
            data_user = obj.username
            data_time = obj.time.strftime("%Y-%m-%d")[:10]
            data_content = obj.content
            dada_source = obj.source
            w.write(excel_row, 0, data_id)
            w.write(excel_row, 1, data_user)
            w.write(excel_row, 2, data_time)
            w.write(excel_row, 3, data_content)
            w.write(excel_row, 4, dada_source)
            excel_row += 1
        # 检测文件是够存在
        # 方框中代码是保存本地文件使用，如不需要请删除该代码
        ###########################
        exist_file = os.path.exists("test.xls")
        if exist_file:
            os.remove(r"test.xls")
        ws.save("test.xls")
        ############################
        sio = StringIO.StringIO()
        ws.save(sio)
        sio.seek(0)
        response = HttpResponse(sio.getvalue(), content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=test.xls'
        response.write(sio.getvalue())
        return response

#
# def mine(request):
#     """个人中心"""
#     if request.method == 'GET':
#         return render(request, 'mine/mine.html')
#
#
# def market(request):
#     if request.method == 'GET':
#         return HttpResponseRedirect(reverse('axf:user_market', args=('104749','0','0')))
#
# def user_market(request, typeid, cid, sid):
#     if request.method == 'GET':
#         ticket = request.COOKIES.get('ticket')
#         user_ticket = UserTicketModel.objects.filter(ticket=ticket).first()
#         if user_ticket:
#             user = user_ticket.user
#         else:
#             user = ''
#         if user:
#             user_cart = CartModel.objects.filter(user=user)
#         else:
#             user_cart = ''
#         foodtypes = FoodType.objects.all()
#         goods = Goods.objects.filter(categoryid=typeid)
#
#         foodtypes_current = foodtypes.filter(typeid=typeid).first()
#         chlid_list = []
#         if foodtypes_current:
#             childtypes = foodtypes_current.childtypenames
#             childtypenames = childtypes.split('#')
#
#             for childtypename in childtypenames:
#                 child_type_info = childtypename.split(':')
#                 chlid_list.append(child_type_info)
#
#
#         data = {
#             'foodtypes': foodtypes,
#             'goods':goods,
#             'typeid':typeid,
#             'chlid_list': chlid_list,
#             'user_cart':user_cart,
#         }
#         return render(request,'market/market.html',data)
#
#
# # def addcart(request):
# #     if request.method =='POST':
# #         user = request.user
# #         goods_id = request.POST.get('goods_id')
# #         data = {
# #             'code':200,
# #             'msg':'请求成功',
# #         }
# #         if user.id:
# #             user_carts = CartModel.objects.filter(user=user, goods_id=goods_id).first()
# #             if user_carts:
# #                 user_carts.c_num += 1
# #                 user_carts.save()
# #                 data['c_num'] = user_carts.c_num
# #             else:
# #                 CartModel.objects.create(user=user, goods_id=goods_id)
# #                 data['c_num'] = 1
# #
# #             return JsonResponse(data)
# #         data['code'] = 403
# #         data['msg'] = '当前用户满意登录，请登录'
# #         return JsonResponse(data)
#
#
#
# #
#
#
#
#
# def addcart(request):
#     if request.method == 'POST':
#
#         user = request.user
#         goods_id = request.POST.get('goods_id')
#         data = {
#             'code': 200,
#             'msg':'正确'
#         }
#         if user.id:
#             user_carts = CartModel.objects.filter(user=user,
#                                                   goods_id=goods_id).first()
#             if user_carts:
#                 user_carts.c_num += 1
#                 user_carts.save()
#                 data['c_num'] = user_carts.c_num
#             else:
#                 CartModel.objects.create(user=user,
#                                          goods_id=goods_id)
#                 data['c_num'] = 1
#
#             return JsonResponse(data)
#         else:
#             data['code'] = 403
#             return JsonResponse(data)
#
#
# def subcart(request):
#     if request.method == 'POST':
#         user = request.user
#         goods_id = request.POST.get('goods_id')
#         data = {
#             'code': 200,
#             'msg': '请求成功',
#         }
#         if user.id:
#             user_carts = CartModel.objects.filter(user=user, goods_id=goods_id).first()
#
#             if user_carts:
#                 if user_carts.c_num == 1:
#                     user_carts.delete()
#
#                     data['c_num'] = 0
#                 else:
#                     user_carts.c_num -= 1
#                     user_carts.save()
#                     data['c_num'] = user_carts.c_num
#
#                 return JsonResponse(data)
#             data['code'] = 403
#             data['msg'] = '失败'
#             return JsonResponse(data)
#         else:
#             data['msg'] = '请去登录'
#             return JsonResponse(data)
#
#
#
#
# # def subcart(request):
# #     if request.method == 'POST':
# #         data = {
# #             'code':200,
# #             'msg':'请求成功',
# #         }
# #         user = request.user
# #         goods_id = request.POST.get('goods_id')
# #
# #         if user.id:
# #             user_carts = CartModel.objects.filter(user=user,
# #                                                  goods_id=goods_id).first()
# #
# #             if user_carts:
# #                 if user_carts.c_num ==1 :
# #                     user_carts.delete()
# #                     data['c_num'] = 0
# #                 else:
# #                     user_carts.c_num -=1
# #                     user_carts.save()
# #                     data['c_num'] = user_carts.c_num
# #                 return JsonResponse(data)
# #             data['c_num'] = 0
# #             return JsonResponse(data)
# #
# #         data['msg'] = '请去登录'
# #         data['code'] = 403
# #         return JsonResponse(data)
#
#
#
#
# def cart(request):
#     if request.method =='GET':
#         user = request.user
#         user_carts = CartModel.objects.filter(user=user)
#         data = {
#             'user_carts':user_carts
#         }
#         return render(request, 'cart/cart.html', data)
#
# def change_select_status(request):
#     if request.method=='POST':
#         cart_id = request.POST.get('cart_id')
#         cart = CartModel.objects.filter(id=cart_id).first()
#         if cart.is_select:
#             cart.is_select = False
#         else:
#             cart.is_select = True
#         cart.save()
#         data = {
#             'code': 200,
#             'msg': '请求成功',
#             'is_select':cart.is_select
#         }
#         return JsonResponse(data)
# def generate_order(request):
#     if request.method == 'GET':
#         user = request.user
#         #下单
#         o_num = get_order_random_id()
#         order = OrderModel.objects.create(user=user,o_num=o_num)
#         user_carts = CartModel.objects.filter(user=user, is_select=True)
#         for cart in user_carts:
#             OrderGoodsModel.objects.create(goods=cart.goods,
#                                            order=order,goods_num=cart.c_num)
#         user_carts.delete()
#         return render(request, 'order/order_info.html', {'order':order})
#
#
#
# def wait_pay(request):
#     if request.method == 'GET':
#         user = request.user
#         usergoods = OrderGoodsModel.objects.filter(user=user)
#         data = {
#             'usergoods': usergoods
#         }
#         return render(request, 'order/order_list_wait_pay.html', data)
#
#
# def changepaystatus(request):
#     if request.method == 'GET':
#         user = request.user
#         goods_id = request.GET.get('id')
#         usergoods = OrderModel.objects.filter(user=user,id=goods_id )
#
#
#
