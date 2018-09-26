from datetime import datetime

from django.db.models import Q
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.deprecation import MiddlewareMixin

from user.models import UserTicketModel


class UserMiddle(MiddlewareMixin):
    def process_request(self, request):
        #需要登录验证，个人中心和购物车和商品的增删
        need_login = [
            '/axf/mine','axf/adddCart',
            '/axf/subCart',
        ]
        if request.path in need_login:
            #现获取cookies中的ticket参数
            ticket= request.COOKIES.get('ticket')
            user_ticket = UserTicketModel.objects.filter(ticket=ticket).first()
            if not ticket:
                #获取认证相关的信息
                #验证当前认证的信息是否过期，如果没有，requ.user赋值
                #如果过期看，跳转到登录并删除认证信息
                if datetime.utcnow() > user_ticket.out_time.replace(tzinfo=None):
                    #过期
                    UserTicketModel.objects.filter(user=user_ticket.user).delete()
                    return HttpResponseRedirect(reverse('user:login'))
                else:
                    #没有过期，赋值request.user，并且删除多余的认证信息
                    request.user = user_ticket.user
                    #删除多余的认证信息
                    #从UserTicketModel中查询当前的user，并且ticket
                    UserTicketModel.objects.filter(Q(user=user_ticket.user)&
                                                   ~Q(ticket=ticket)).delete()
                    return None

            else:
                return HttpResponseRedirect(reverse('user:login'))
        else:
            return None
